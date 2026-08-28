---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DynamicPartitioningConfiguration.html
---

# DynamicPartitioningConfiguration
<a name="API_DynamicPartitioningConfiguration"></a>

The configuration of the dynamic partitioning mechanism that creates smaller data sets from the streaming data by partitioning it based on partition keys. Currently, dynamic partitioning is only supported for Amazon S3 destinations.

## Contents
<a name="API_DynamicPartitioningConfiguration_Contents"></a>

 ** Enabled **   <a name="Firehose-Type-DynamicPartitioningConfiguration-Enabled"></a>
Specifies that the dynamic partitioning is enabled for this Firehose stream.
Type: Boolean
Required: No

 ** RetryOptions **   <a name="Firehose-Type-DynamicPartitioningConfiguration-RetryOptions"></a>
The retry behavior in case Firehose is unable to deliver data to an Amazon S3 prefix.
Type: [RetryOptions](API_RetryOptions.md) object
Required: No

## See Also
<a name="API_DynamicPartitioningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DynamicPartitioningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DynamicPartitioningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DynamicPartitioningConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
