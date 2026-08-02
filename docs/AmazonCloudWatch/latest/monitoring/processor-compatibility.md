---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-compatibility.html
---

# Processor compatibility and restrictions
<a name="processor-compatibility"></a>General processor rules

Maximum count
A pipeline can have at most 20 processors.

Parser placement
Parser processors (OCSF, CSV, Grok, etc.), if used, must be the first processor in a pipeline.

Unique processors
The following processors can appear only once per pipeline:
+ `add_entries`
+ `copy_values`

| Processor Type | CloudWatch Logs Source | S3 Source | API-based Sources |
| --- | --- | --- | --- |
| OCSF | Must be first processor | Must be first processor | Must be first processor |
| parse\_vpc | Must be first processor | Not applicable | Not applicable |
| parse\_route53 | Must be first processor | Not applicable | Not applicable |
| parse\_rds | Must be first processor | Not applicable | Not applicable |
| parse\_json | Must be first processor | Must be first processor | Must be first processor |
| grok | Must be first processor | Must be first processor | Must be first processor |
| csv | Must be first processor | Not compatible | Not compatible |
| key\_value | Must be first processor | Must be first processor | Must be first processor |
| add\_entries | Must be first processor | Must be first processor | Must be first processor |
| copy\_values | Must be first processor | Must be first processor | Must be first processor |
| String processors (lowercase, uppercase, trim) | Must be first processor | Must be first processor | Must be first processor |
| Field processors (move\_keys, rename\_keys) | Must be first processor | Must be first processor | Must be first processor |
| Data transformation (date, flatten) | Must be first processor | Must be first processor | Must be first processor |

**Compatibility definitions**

Must be first processor
When used, must be the first processor in the pipeline configuration

Not compatible
Cannot be used with this source type

Not applicable
Processor is not relevant for this source type

## Processor-specific restrictions
<a name="processor-specific-restrictions"></a>

**Processor restrictions by source type**

| Processor | Source Type | Restrictions |
| --- | --- | --- |
| OCSF | CloudWatch Logs with CloudTrail |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-compatibility.html)  |
| OCSF | API-based Sources |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-compatibility.html)  |
| parse\_vpc | CloudWatch Logs |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-compatibility.html)  |
| parse\_route53 | CloudWatch Logs |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-compatibility.html)  |
| parse\_rds | CloudWatch Logs |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-compatibility.html)  |
| add\_entries | All Sources |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-compatibility.html)  |
| copy\_values | All Sources |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/processor-compatibility.html)  |

**Important**
When using processors with restrictions:
Always validate your pipeline configuration using the `ValidateTelemetryPipelineConfiguration` API before deployment
Test the pipeline with sample data using the `TestTelemetryPipeline` API to ensure proper processing
Monitor pipeline metrics after deployment to ensure events are being processed as expected
