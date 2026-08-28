---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/cloudtrail-events-in-model-evaluations.html
---

# CloudTrail management events in model evaluation jobs
<a name="cloudtrail-events-in-model-evaluations"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about the resource operations performed on or in a resource (for example, reading or writing to an Amazon S3 object). These are also known as data plane operations. Data events are often high-volume activities that CloudTrail doesn’t log by default.

Model evaluation jobs log events for multiple AWS services

**CloudTrail data events by AWS service in model evaluation jobs**
+ **Amazon Bedrock**: Data events for all model inference run during the model evaluation job.
+ **Amazon SageMaker AI**: Data events for all human-based model evaluation jobs.
+ **Amazon S3**: Data events for reading and writing data to the Amazon S3 bucket specified when the model evaluation job was created.
+ **AWS Key Management Service**: Data events related to using customer managed AWS KMS keys.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
