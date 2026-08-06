---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/cost.html
---

# Cost
<a name="cost"></a>

 You are responsible for the cost of the AWS services used while running this Guidance. As of this revision, the cost for running this Guidance with the default settings in the US East (Ohio) Region is approximately **$153.57** for 100,000 Amazon Glacier vault archives (1GB each) and **$1,229.21** for 10,000,000 Amazon Glacier vault archives (10MB each). These costs assume that the destination bucket is also in US East (Ohio) Region. Refer to Sample cost tables for more details.

**Note**
If the destination bucket is not in the same region as the Glacier vault, a "Data Transfer OUT From Amazon S3 Glacier" fee will be added. See [Data transfer pricing](https://aws.amazon.com/s3/glacier/pricing/#Data_transfer_pricing) for more information. This cost should be considered when planning your data storage and transfer strategies to avoid unexpected charges.

See the pricing webpage for each AWS service used in this Guidance. Estimated costs vary based on the number of archives processed and the total volume of data to copy from an Amazon Glacier vault.

 We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through AWS Cost Explorer to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each [AWS service used in this Guidance](architecture-details.md#aws-services-in-this-guidance).

## Cost table calculation
<a name="cost-table-calculation"></a>

The following table shows how the sample cost tables were calculated.

|  Guidance component  |  Type  |  [A] - Unit cost  |  [B] - Value  |  [C] - Estimated cost  |
| --- | --- | --- | --- | --- |
|  Additional services  |  Per 1,000 requests  |  $0.01  | `{{<# of S3 Glacier vault archives>}}` | *[A] × [B] / 1,000* |
|  Amazon S3 multipart upload create requests  |  Per 1,000 requests  |  $0.005  | `{{<# of S3 Glacier vault archives>}}` | *[A] × [B] / 1,000* |
|  Amazon S3 multipart upload complete requests  |  Per 1,000 requests  |  $0.03  | `{{<# of S3 Glacier vault archives>}}` | *[A] × [B] / 1,000* |
|  Guidance runtime (Lambda and Step Functions)  |  Per GB  |  $0.00143  | `{{<Size of S3 Glacier vault in GBs>}}` | *[A] × [B]* |
|  Guidance runtime (Lambda and Step Functions)  |  Per 1,000 requests  |  $0.0447  | `{{<# of S3 Glacier vault archives>}}` | *[A] × [B] / 1,000* |
|  DynamoDB writes/reads for transfer metadata  |  Per 1,000 requests  |  $0.02  | `{{<# of S3 Glacier vault archives>}}` | *[A] × [B] / 1,000* |
| Data Transfer OUT from S3 Glacier | Per GB  | $0.02 *if destination bucket is in a different region than S3 Glacier vault.*<br />$0.00 <br />*if destination bucket is in the same region as S3 Glacier vault.* | {{<Size of S3 Glacier vault in GBs>}} | *[A] × [B]* |

## Sample cost tables
<a name="sample-cost-tables"></a>

 The following tables provide two sample cost breakdowns for deploying this Guidance with the default parameters in the US East (Ohio) Region, with an Amazon Glacier vault size of 100 TB. These cost breakdowns are based on the destination bucket is also being in the US East (Ohio) Region, the same region as the S3 Glacier vault.

**Note**
 Costs associated with storing data in the Amazon S3 service are nearly continuous and aren't included in these estimates.

### Scenario 1: 100,000 Amazon Glacier vault archives
<a name="scenario-1-100000-s3-glacier-vault-archives"></a>

|  AWS service  |  Dimensions  |  Cost [USD]  |
| --- | --- | --- |
|  Step Functions  |   |  $0.07  |
|  Lambda  |   |  $140.00  |
|  DynamoDB  |   |  $2.00  |
|  Amazon S3  |  Transfer cost  |  $5.00  |
|  Additional services: +   Amazon SQS  <br />+   Amazon SNS  <br />+   AWS Glue  <br />+   CloudWatch   |   |  $6.50  |
|   |  Total:  |  $153.57 [USD]  |

If the destination bucket is in a different region than US East (Ohio), an additional price of $2048 ($0.02 x size of S3 Glacier vault in GBs) should be added to the total.

### Scenario 2: 10,000,000 Amazon Glacier vault archives
<a name="scenario-2-10000000-s3-glacier-vault-archives"></a>

|  AWS service  |  Dimensions  |  Cost [USD]  |
| --- | --- | --- |
|  Step Functions  |   |  $3.21  |
|  Lambda  |   |  $411.00  |
|  DynamoDB  |   |  $221.00  |
|  Amazon S3  |  Transfer cost  |  $465.00  |
|  Additional services: +   Amazon SQS  <br />+   Amazon SNS  <br />+   AWS Glue  <br />+   CloudWatch   |   |  $129.00  |
|   |  Total:  |  $1,229.21 [USD]  |

If the destination bucket is in a different region than US East (Ohio), an additional price of $2048 ($0.02 x size of S3 Glacier vault in GBs) should be added to the total.

## AWS CloudTrail cost
<a name="aws-cloudtrail-cost"></a>

You can use [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. When you create additional trails—for example, to capture data or insight on generated events—AWS CloudTrail charges apply. See [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/) for more information.

## Potential cost savings
<a name="potential-cost-savings"></a>

 As of this revision, you can save $0.00261 per GB per month by storing your archives in the Amazon S3 service with the S3 Glacier Deep Archive storage class applied. For example, if you have 100 TB stored in your Amazon Glacier vault, you can save $261.00 per month by storing that data in the Amazon S3 service with the S3 Glacier Deep Archive storage class applied.

 The cost to run the Guidance scales with the size of the Amazon Glacier vault and the number of archives. Cost savings only scale with the Amazon Glacier vault size.
