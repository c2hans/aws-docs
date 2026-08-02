---
source_url: https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-line-item.html
---

# Line item columns
<a name="table-dictionary-cur2-line-item"></a>

Line item columns contain data about cost, usage, type of usage, pricing rates, product name, and more.

****

| Column name | Description | Data type |
| --- | --- | --- |
| line\_item\_usage\_account\_name | The name of the account that used this line item. For organizations, this can be either the management account or a member account. You can use this field to track costs or usage by account. | string |
| line\_item\_availability\_zone | The Availability Zone that hosts this line item. For example, us-east-1a or us-east-1b. | string |
| line\_item\_blended\_cost | The `BlendedRate` multiplied by the `UsageAmount`.<br />**BlendedCost** is blank for line items that have a **LineItemType** of **Discount**. Discounts are calculated using only the unblended cost of a member account, aggregated by member account and SKU. As a result, **BlendedCost** is not available for discounts. | double |
| line\_item\_blended\_rate | The `BlendedRate` is the average cost incurred for each SKU across an organization.<br />For example, the Amazon S3 blended rates are the total cost of storage divided by the amount of data stored per month. For accounts with RIs, the blended rates are calculated as the average costs of the RIs and the On-Demand Instances.<br />Blended rates are calculated at the management account level, and used to allocate costs to each member account. For more information, see [Blended Rates and Costs](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/con-bill-blended-rates.html#Blended_CB) in the *AWS Billing User Guide*. | string |
| line\_item\_currency\_code | The currency that this line item is shown in. All AWS customers are billed in US dollars by default. To change your billing currency, see [Changing which currency you use to pay your bill](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-account-payment.html#manage-account-payment-change-currency) in the *AWS Billing User Guide*. | string |
| line\_item\_iam\_principal | The IAM ARN of the principal that performed the Amazon Bedrock model inference. This column is populated when you enable IAM principal data in your CUR 2.0 data export. Currently supported for Amazon Bedrock only. | string |
| line\_item\_legal\_entity | The Seller of Record of a specific product or service. In most cases, the invoicing entity and legal entity are the same. The values might differ for third-party AWS Marketplace transactions. Possible values include:[See the AWS documentation website for more details](http://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-line-item.html) | string |
| line\_item\_line\_item\_description | The description of the line item type. For example, the description of a usage line item summarizes the type of usage incurred during a specific time period.<br />For size-flexible RIs, the description corresponds to the RI the benefit was applied to. For example, if a line item corresponds to a `t2.micro` and a `t2.small` RI was applied to the usage, the **line\_item\_line\_item\_description** displays `t2.small`.<br />The description for a usage line item with an RI discount contains the pricing plan covered by the line item. | string |
| line\_item\_line\_item\_type | The type of charge covered by this line item. The possible types are as follows:[See the AWS documentation website for more details](http://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-line-item.html) | string |
| line\_item\_net\_unblended\_cost | The actual after-discount cost that you're paying for the line item. This column is only included in your report when your account has a discount in the applicable billing period. | double |
| line\_item\_net\_unblended\_rate | The actual after-discount rate that you're paying for the line item. This column is only included in your report when your account has a discount in the applicable billing period. | string |
| line\_item\_normalization\_factor | As long as the instance has shared tenancy, AWS can apply all Regional Linux or Unix Amazon EC2 and Amazon RDS RI discounts to all instance sizes in an instance family and AWS Region. This also applies to RI discounts for member accounts in an organization. All new and existing Amazon EC2 and Amazon RDS size-flexible RIs are sized according to a normalization factor, based on the instance size. | double |
| line\_item\_normalized\_usage\_amount | The amount of usage that you incurred, in normalized units, for size-flexible RIs. The **NormalizedUsageAmount** is equal to **UsageAmount** multiplied by **NormalizationFactor**. | double |
| line\_item\_operation | The specific AWS operation covered by this line item. This describes the specific usage of the line item. For example, a value of RunInstances indicates the operation of an Amazon EC2 instance. | string |
| line\_item\_product\_code | The code of the product measured. For example, Amazon EC2 is the product code for Amazon Elastic Compute Cloud. | string |
| line\_item\_resource\_id | **Table configuration:** Added by: INCLUDE RESOURCES<br />(Optional) If you chose to include individual resource IDs in your report, this column contains the ID of the resource that you provisioned. For example, an Amazon S3 storage bucket, an Amazon EC2 compute instance, or an Amazon RDS database can each have a resource ID. This field is blank for usage types that aren't associated with an instantiated host, such as data transfers and API requests, and line item types such as discounts, credits, and taxes. | string |
| line\_item\_tax\_type | The type of tax that AWS applied to this line item. | string |
| line\_item\_unblended\_cost | The UnblendedCost is the UnblendedRate multiplied by the UsageAmount. | double |
| line\_item\_unblended\_rate | In consolidated billing for accounts using AWS Organizations, the unblended rate is the rate associated with an individual account's service usage.<br />For Amazon EC2 and Amazon RDS line items that have an RI discount applied to them, the `UnblendedRate` is `0`. Line items with an RI discount have a `LineItemType` of `DiscountedUsage`. | string |
| line\_item\_usage\_account\_id | The account ID of the account that used this line item. For organizations, this can be either the management account or a member account. You can use this field to track costs or usage by account. | string |
| line\_item\_usage\_amount | The amount of usage that you incurred during the specified time period. For size-flexible Reserved Instances, use the **reservation/TotalReservedUnits** column instead.<br />Certain subscription charges will have a **UsageAmount** of `0`. | double |
| line\_item\_usage\_end\_date | The end date and time for the corresponding line item in UTC, exclusive. The format is YYYY-MM-DDTHH:mm:ssZ. | timestamp |
| line\_item\_usage\_start\_date | The start date and time for the line item in UTC, inclusive. The format is YYYY-MM-DDTHH:mm:ssZ. | timestamp |
| line\_item\_usage\_type | The usage details of the line item. For example, USW2-BoxUsage:m2.2xlarge describes an M2 High Memory Double Extra Large instance in the US West (Oregon) Region. | string |
| line\_item\_user\_identifier | The Identity Access Management (IAM) Identity Center identifier of a workforce user. The monthly flat-rate subscription and on-demand charges are calculated for the user identified by this identifier. | string |
