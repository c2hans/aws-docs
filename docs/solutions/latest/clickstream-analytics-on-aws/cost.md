---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/cost.html
---

# Cost
<a name="cost"></a>

**Important**
 The following cost estimations are examples and may vary depending on your environment.

 You are responsible for the cost of AWS services used when running this guidance. Deploying this guidance will only create a guidance web console in your AWS account, which is completely serverless and typically can be covered within free tier.

The cost for this guidance is mostly incurred by the data pipeline. As of this revision, the main factors affecting the guidance cost include:
+  **Ingestion module**, the cost depends on the size of the ingestion server and the type of the data sink you choose.
+  **Data processing and modeling module** (optional), the cost depends on whether you choose to enabled this module and its relevant configurations
+  **Enabled Dashboards** (optional), the cost depends on whether you choose to enabled this module and its relevant configurations
+  **Additional features**

 The following are cost estimations for data volumes of 10/100/1000/10000 RPS (request per second) with different data pipeline configurations. Cost estimation are provided by modules. To get a total cost for your use case, sum the cost by modules based on your actual configuration.

**Important**
 As of this revision, the following cost is calculated with `On-Demand` prices in the `us-east-1` Region and measured in USD.

## Ingestion module
<a name="ingestion-module-2"></a>

 Ingestion module includes the following cost components:
+  Application load balancer
+  EC2 for ECS
+  Data sink (Kinesis \| Kafka \| Direct to S3)
+  S3 storage

 Key assumptions include:
+  Compressed request payload: 2KB (10 events per request)
+  MSK configurations (m5.large \* 2)
+  KDS configuration (on-demand, provision)
+  10/100/1000 request per second (RPS)

- ** 10 RPS (49GB per month)**
  - ****ALB cost**:** $28.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  Kinesis (On-Demand)  / ****Buffer cost**:**  $38.00 / ****S3 cost**:** $3.00 / ****Total (USD per month)**:**  $191.80
  - ****ALB cost**:** $28.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  Kinesis (Provisioned 2 shard)  / ****Buffer cost**:**  $22.00 / ****S3 cost**:** $3.00 / ****Total (USD per month)**:**  $175.80
  - ****ALB cost**:** $28.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  Amazon MSK (m5.large \* 2, connector MCU \* 1)  / ****Buffer cost**:**  $417.00 / ****S3 cost**:** $3.00 / ****Total (USD per month)**:**  $570.80
  - ****ALB cost**:** $28.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  None / ****Buffer cost**:** None / ****S3 cost**:** $3.00 / ****Total (USD per month)**:**  $153.80

- ** 100 PRS (490GB per month)**
  - ****ALB cost**:** $53.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  Kinesis(On-demand)  / ****Buffer cost**:**  $115.00 / ****S3 cost**:** $4.00 / ****Total (USD per month)**:**  $294.80
  - ****ALB cost**:** $53.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  Kinesis (Provisioned 2 shard) / ****Buffer cost**:**  $26.00 / ****S3 cost**:** $4.00 / ****Total (USD per month)**:**  $205.80
  - ****ALB cost**:** $53.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  Amazon MSK (m5.large \* 2, connector MCU \* 1)  / ****Buffer cost**:**  $417.00 / ****S3 cost**:** $4.00 / ****Total (USD per month)**:**  $596.80
  - ****ALB cost**:** $53.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  None / ****Buffer cost**:** None / ****S3 cost**:** $4.00 / ****Total (USD per month)**:**  $179.80

- ** 1,000 RPS (4,900 GB per month)**
  - ****ALB cost**:** $262.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  Kinesis(On-demand)  / ****Buffer cost**:**  $1,051.00 / ****S3 cost**:** $14.00 / ****Total (USD per month)**:**  $1,449.80
  - ****ALB cost**:** $262.80  / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  Kinesis (Provisioned 10 shard) / ****Buffer cost**:**  $180.00 / ****S3 cost**:** $14.00 / ****Total (USD per month)**:**  $578.80
  - ****ALB cost**:** $262.80 / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  Amazon MSK (m5.large \* 2, connector MCU \* 2\~3) / ****Buffer cost**:**  $590.00 / ****S3 cost**:** $14.00 / ****Total (USD per month)**:**  $988.80
  - ****ALB cost**:** $262.80  / ****EC2 cost**:**  $122.00 / ****Buffer type**:**  None / ****Buffer cost**:** None / ****S3 cost**:** $14.00 / ****Total (USD per month)**:**  $398.80

### Data transfer
<a name="data-transfer"></a>

There are associated costs for data transfer from EC2 to the downstream data sink. Below is an example of data transfer costs based on 1000 RPS and a 1KB request payload.
+  EC2 Network In: This does not incur any costs.
+  EC2 Network Out: There are three data sink types (Amazon S3, Amazon MSK, and Amazon Kinesis Data Streams).

|  **Data sink type**  |  **Way to access data sink**  |  **Dimensions**  |  **Total (USD)**  |
| --- | --- | --- | --- |
|  Amazon S3 | Amazon S3 gateway endpoints  | The Amazon S3 gateway endpoints do not incur any costs.  |  $0  |
|  Amazon MSK | N/A |  Data processed cost ($0.010 per GB in/out/between EC2 Availability Zones)  |  $210 |
|  Amazon Kinesis Data Streams | NAT | NAT fixed cost: $64 (2 Availability Zones and a NAT per Availability Zone, $0.045 per NAT Gateway Hour).<br />Data processed cost: $1201 ($0.045 per GB Data Processed by NAT gateways).  |  $1266  |
| Amazon Kinesis Data Streams | VPC endpoint | VPC endpoint fixed cost: $14.62 (Availability Zones $0.01 per AZ Hour).<br />Data processed cost: $267 ($0.01 per GB Data Processed by Interface endpoints). |  $281.62 |

You are recommended to use a VPC endpoint for the Amazon Kinesis Data Streams data sink. For more information, refer to the [VPC endpoint](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html) documentation.

## Data processing & modeling modules
<a name="data-processing-modeling-modules"></a>

 Data processing & modeling module include the following cost components if you enable:
+  EMR Serverless
+  Redshift

 Key assumptions include:
+  10/100/1000 RPS
+  Data processing interval: hourly/6-hourly/daily
+  EMR running three built-in plugins to process data

- ** 10 RPS**
  - ****EMR schedule interval**:**  Hourly  / ****EMR cost**:**  $65.50 ($1.35/GB)  / ****Redshift type**:**  Serverless (8 based RPU)  / ****Redshift load cost**:**  $172.00 / **Redshift storage cost:** $3.40 / **S3 cost:** $0.36 / ****Total (USD/Month)**:**  $242.26
  - ****EMR schedule interval**:**  6-hourly / ****EMR cost**:**  $22.20 ($0.45/GB) / ****Redshift type**:**  Serverless (8 based RPU)  / ****Redshift load cost**:**  $70.00 / **Redshift storage cost:** $3.40 / **S3 cost:** $0.36 / ****Total (USD/Month)**:**  $95.96
  - ****EMR schedule interval**:**  Daily / ****EMR cost**:**  $39.00 ($0.80/GB) / ****Redshift type**:**  Serverless (8 based RPU)  / ****Redshift load cost**:**  $31.00 / **Redshift storage cost:** $3.40 / **S3 cost:** $0.36 / ****Total (USD/Month)**:**  $73.76

- ** 100 RPS**
  - ****EMR schedule interval**:**  Hourly  / ****EMR cost**:**  $353.00 ($0.72/GB) / ****Redshift type**:**  Serverless (8 based RPU)  / ****Redshift load cost**:**  $385.00 / **Redshift storage cost:** $34.00 / **S3 cost:** $3.60 / ****Total (USD/Month)**:**  $775.60
  - ****EMR schedule interval**:**  6-hourly / ****EMR cost**:**  $179.00 ($0.37/GB) / ****Redshift type**:**  Serverless (8 based RPU)  / ****Redshift load cost**:**  $282.00 / **Redshift storage cost:** $34.00 / **S3 cost:** $3.60 / ****Total (USD/Month)**:**  $498.60
  - ****EMR schedule interval**:**  Daily / ****EMR cost**:**  $247.00 ($0.50/GB) / ****Redshift type**:**  Serverless (8 based RPU)  / ****Redshift load cost**:**  $160.00 / **Redshift storage cost:** $34.00 / **S3 cost:** $3.60 / ****Total (USD/Month)**:**  $444.60

- ** 1,000 RPS**
  - ****EMR schedule interval**:**  Hourly
  - ****EMR cost**:**  $1,260.00 ($0.26/GB)
  - ****Redshift type**:**  Serverless (16 based RPU)
  - ****Redshift load cost**:**  $2,325.00
  - **Redshift storage cost:** $340
  - **S3 cost:** $36
  - ****Total (USD/Month)**:**  $3,961.00

**Note**
The term **Redshift storage cost **refers to the cost of Redshift storage incurred for one month based on the corresponding RPS. If the data is stored for more than one month, please refer to the [Redshift pricing](https://aws.amazon.com/redshift/pricing/?nc1=h_ls).

## Reporting module
<a name="reporting-module"></a>

 Reporting module includes the following cost components if you choose to enable:
+  QuickSight

 Key assumptions include
+  QuickSight Enterprise subscription
+  Exclude Q cost
+ Analytics Studio
+ 10GB SPICE capacity

|  **Daily data volume/RPS**  |  **Cost for authors **  | **Cost for SPICE** |  **Total cost (USD/Month)**  |
| --- | --- | --- | --- |
|  All size  | $24 | 0 |  $24 |

**Note**
The QuickSight cost applies to all your data pipelines, including the visualization managed outside the guidance.

## Logging and monitoring
<a name="logging-and-monitoring"></a>

The guidance utilizes CloudWatch Logs, CloudWatch Metrics and CloudWatch Dashboard to implement logging, monitoring and visualizating features. The total cost is around $14 per month and may vary based on the volume of logs and the number of metrics being monitored.

## Additional features
<a name="additional-features"></a>

You will be charged with additional cost only if you choose to enable the following features.

### Secrets Manager
<a name="secrets-manager"></a>
+ If you enable reporting, the guidance creates a secret in Secrets Manager to store the Redshift credentials used by QuickSight visualization. **Cost**: 0.40 USD/month.
+ If you enable the authentication feature of the ingestion module, you need to create a secret in Secrets Manager to store the information for OIDC. **Cost**: 0.40 USD/month.

### AWS Global Accelerator
<a name="global-accelerator"></a>

It incurs a fixed hourly charge and a per-day volume data transfer cost.

Key assumptions: Ingestion deployment in `us-east-1`

|  **RPS**  |  **Fixed hourly cost**  |  **Data transfer cost**  |  **Total cost (USD/Month)**  |
| --- | --- | --- | --- |
| 10 RPS | $18 | $0.60 | $18.60 |
| 100 RPS | $18 | $6 | $24 |
| 1000 RPS | $18 | $60 | $78 |

### Application Load Balancer access logs
<a name="alb-access-log"></a>

The charged cost includes the storage cost for Amazon S3, but not for the bandwidth used by Elastic Load Balancing to send log files to Amazon S3. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

|  **RPS**  |  **Log size (GB)**  |  **S3 cost (USD/Month)**  |
| --- | --- | --- |
| 10 RPS | 16.50 | $0.38 |
| 100 RPS | 165 | $3.80 |
| 1000 RPS | 1650 | $38 |
