from django.conf import settings
from django.db import models

# 出金元テーブルモデル
class Wallet(models.Model):
    wallet_id = models.BigAutoField(primary_key=True)
    wallet_name = models.CharField('出金元名', max_length=128)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = "wallets"

    def __str__(self):
        return f'{self.wallet_name}'

# 残高確認テーブルモデル
class Balance(models.Model):
    balance_id = models.BigAutoField(primary_key=True)
    balance_amount = models.DecimalField(verbose_name="残高金額",max_digits=10,decimal_places=2)
    receipt_date = models.DateTimeField(verbose_name="記帳日")

    wallet_id = models.ForeignKey(Wallet, verbose_name="出金元",
                                     on_delete=models.CASCADE)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = "balances"

    def __str__(self):
        return f'{self.receipt_date} {self.receipt_date}'

# 大項目テーブルモデル
class PrimaryItem(models.Model):
    primary_item_id = models.BigAutoField(primary_key=True)
    primary_item_name = models.CharField('大項目名', max_length=128)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = "primary_items"

    def __str__(self):
        return f'{self.primary_item_id} {self.primary_item_name}'

# 中項目テーブルモデル
class SecondaryItem(models.Model):
    secondary_item_id = models.BigAutoField(primary_key=True)
    secondary_item_name = models.CharField('中項目名', max_length=128)
    primary_item_id = models.ForeignKey(PrimaryItem, verbose_name="大項目名",
                                     on_delete=models.CASCADE)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = "secondary_items"

    def __str__(self):
        return f'{self.secondary_item_id} {self.secondary_item_name}'

# 小項目テーブルモデル
class TertiaryItem(models.Model):
    tertiary_item_id = models.BigAutoField(primary_key=True)
    tertiary_item_name = models.CharField('中項目名', max_length=128)
    secondary_item_id = models.ForeignKey(SecondaryItem, verbose_name="中項目名",
                                     on_delete=models.CASCADE)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = "tertiary_items"

    def __str__(self):
        return f'{self.tertiary_item_id} {self.tertiary_item_name}'

# 取引種別テーブルモデル
class TransactionType(models.Model):
    transaction_type_id = models.BigAutoField(primary_key=True)
    transaction_type_name = models.CharField('取引種別名', max_length=128)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = "transaction_types"

    def __str__(self):
        return f'{self.tertiary_item_id} {self.tertiary_item_name}'



class Transaction(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    # 外部テーブルより読み込み
    wallet_id = models.ForeignKey(Wallet, verbose_name="出金元",
                                     on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, verbose_name="取引種別名",
                                     on_delete=models.CASCADE)
    primary_item_id = models.ForeignKey(PrimaryItem, verbose_name="大項目名",
                                     on_delete=models.CASCADE)
    secondary_item_id = models.ForeignKey(SecondaryItem, verbose_name="中項目名",
                                     on_delete=models.CASCADE)
    tertiary_item_id = models.ForeignKey(TertiaryItem, verbose_name="小項目名",
                                     on_delete=models.CASCADE)

    # 取引情報
    transaction_at = models.DateTimeField(verbose_name="取引日")
    transaction_amount = models.DecimalField(verbose_name="取引金額",max_digits=10,decimal_places=2)
    note = models.CharField('備考', blank=True, max_length=128)
    quantity = models.DecimalField(verbose_name="数量", blank=True,max_digits=10,decimal_places=2)
    quantity_unit = models.CharField('数量単位', blank=True, max_length=128)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = "transactions"

    def __str__(self):
        return f'{self.transaction_at} {self.note}'


class Budgets(models.Model):
    budget_id = models.BigAutoField(primary_key=True)
    # 外部テーブルより読み込み
    primary_item_id = models.ForeignKey(PrimaryItem, verbose_name="大項目名",
                                     on_delete=models.CASCADE)
    secondary_item_id = models.ForeignKey(SecondaryItem, verbose_name="中項目名",
                                     on_delete=models.CASCADE)
    tertiary_item_id = models.ForeignKey(TertiaryItem, verbose_name="小項目名",
                                     on_delete=models.CASCADE)

    # 予算情報
    budget_period_start_at = models.DateField(verbose_name="予算開始日")
    budget_period_end_at = models.DateField(verbose_name="予算終了日")
    budget_amount = models.DecimalField(verbose_name="予算金額",max_digits=10,decimal_places=2)
    note = models.CharField('備考', blank=True, max_length=128)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = "budgets"

    def __str__(self):
        return f'{self.transaction_at} {self.note}'

