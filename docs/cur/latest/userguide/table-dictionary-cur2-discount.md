---
source_url: https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-discount.html
---

# Discount columns
<a name="table-dictionary-cur2-discount"></a>

Discount columns contain data about any discounts you are receiving.

****

| Column name | Description | Data type |
| --- | --- | --- |
| discount | **Table configuration:** Removed by: INCLUDE MANUAL DISCOUNT COMPATIBILITY<br />A "struct" column containing key-value pairs of any specific discounts that apply to this line item. The keys correspond to a discount type and the values correspond to either the discount value or other information. The values in this column are either data type "numeric" or "string" depending on the specific key.<br />The keys of this column can be queried as individual columns by using the dot operator. For more information, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-data-query.html).<br />This column is not available when "Manual discount compatibility" is enabled. When it's enabled, discounts are populated as separate line items and not in this column. | map <string, double> |
| discount\_bundled\_discount | The bundled discount applied to the line item. A bundled discount is a usage-based discount that provides free or discounted usage of a service or feature based on the usage of another service or feature.<br />As of August 2025, bundled discounts are applied using an "Owner-first approach" where discounts are first applied to the account that generates the source usage. Within the source account, discounts are applied based on the following sequence:[See the AWS documentation website for more details](http://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-discount.html)<br />Any remaining discounts are distributed across other accounts in the Consolidated Billing Family (CBF) based on the following sequence:[See the AWS documentation website for more details](http://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-discount.html)<br />Examples of bundled discounts include:[See the AWS documentation website for more details](http://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-discount.html) | double |
| discount\_total\_discount | **Table configuration:** Removed by: `INCLUDE MANUAL DISCOUNT COMPATIBILITY`<br />The sum of all the discount columns for the corresponding line item.<br />This column is not available when "Manual discount compatibility" is enabled. When it's enabled, discounts are populated as separate line items and not in this column. | double |
