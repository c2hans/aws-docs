---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_MSKSourceConfiguration.html
---

# MSKSourceConfiguration
<a name="API_MSKSourceConfiguration"></a>

The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.

## Contents
<a name="API_MSKSourceConfiguration_Contents"></a>

 ** AuthenticationConfiguration **   <a name="Firehose-Type-MSKSourceConfiguration-AuthenticationConfiguration"></a>
The authentication configuration of the Amazon MSK cluster.
Type: [AuthenticationConfiguration](API_AuthenticationConfiguration.md) object
Required: Yes

 ** MSKClusterARN **   <a name="Firehose-Type-MSKSourceConfiguration-MSKClusterARN"></a>
The ARN of the Amazon MSK cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*`
Required: Yes

 ** TopicName **   <a name="Firehose-Type-MSKSourceConfiguration-TopicName"></a>
The topic name within the Amazon MSK cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\\._\\-]+`
Required: Yes

 ** ReadFromTimestamp **   <a name="Firehose-Type-MSKSourceConfiguration-ReadFromTimestamp"></a>
The start date and time in UTC for the offset position within your MSK topic from where Firehose begins to read. By default, this is set to timestamp when Firehose becomes Active.
If you want to create a Firehose stream with Earliest start position from SDK or CLI, you need to set the `ReadFromTimestamp` parameter to Epoch (1970-01-01T00:00:00Z).
Type: Timestamp
Required: No

## See Also
<a name="API_MSKSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/MSKSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/MSKSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/MSKSourceConfiguration)
