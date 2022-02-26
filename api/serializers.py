from rest_framework import serializers

import debt_sale


class DebtSalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = debt_sale
