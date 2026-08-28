---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DestinationOptionsRequest.html
---

# DestinationOptionsRequest
<a name="API_DestinationOptionsRequest"></a>

Describes the destination options for a flow log.

## Contents
<a name="API_DestinationOptionsRequest_Contents"></a>

 ** FileFormat **
The format for the flow log. The default is `plain-text`.
Type: String
Valid Values: `plain-text | parquet`
Required: No

 ** HiveCompatiblePartitions **
Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3. The default is `false`.
Type: Boolean
Required: No

 ** PerHourPartition **
Indicates whether to partition the flow log per hour. This reduces the cost and response time for queries. The default is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_DestinationOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DestinationOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DestinationOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DestinationOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
