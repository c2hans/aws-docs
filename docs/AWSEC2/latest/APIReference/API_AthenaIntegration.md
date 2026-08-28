---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AthenaIntegration.html
---

# AthenaIntegration
<a name="API_AthenaIntegration"></a>

Describes integration options for Amazon Athena.

## Contents
<a name="API_AthenaIntegration_Contents"></a>

 ** IntegrationResultS3DestinationArn **
The location in Amazon S3 to store the generated CloudFormation template.
Type: String
Required: Yes

 ** PartitionLoadFrequency **
The schedule for adding new partitions to the table.
Type: String
Valid Values: `none | daily | weekly | monthly`
Required: Yes

 ** PartitionEndDate **
The end date for the partition.
Type: Timestamp
Required: No

 ** PartitionStartDate **
The start date for the partition.
Type: Timestamp
Required: No

## See Also
<a name="API_AthenaIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AthenaIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AthenaIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AthenaIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
