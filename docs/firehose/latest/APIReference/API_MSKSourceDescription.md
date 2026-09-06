---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_MSKSourceDescription.html
---

# MSKSourceDescription
<a name="API_MSKSourceDescription"></a>

Details about the Amazon MSK cluster used as the source for a Firehose stream.

## Contents
<a name="API_MSKSourceDescription_Contents"></a>

 ** AuthenticationConfiguration **   <a name="Firehose-Type-MSKSourceDescription-AuthenticationConfiguration"></a>
The authentication configuration of the Amazon MSK cluster.
Type: [AuthenticationConfiguration](API_AuthenticationConfiguration.md) object
Required: No

 ** DeliveryStartTimestamp **   <a name="Firehose-Type-MSKSourceDescription-DeliveryStartTimestamp"></a>
Firehose starts retrieving records from the topic within the Amazon MSK cluster starting with this timestamp.
Type: Timestamp
Required: No

 ** MSKClusterARN **   <a name="Firehose-Type-MSKSourceDescription-MSKClusterARN"></a>
The ARN of the Amazon MSK cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*`
Required: No

 ** ReadFromTimestamp **   <a name="Firehose-Type-MSKSourceDescription-ReadFromTimestamp"></a>
The start date and time in UTC for the offset position within your MSK topic from where Firehose begins to read. By default, this is set to timestamp when Firehose becomes Active.
If you want to create a Firehose stream with Earliest start position from SDK or CLI, you need to set the `ReadFromTimestampUTC` parameter to Epoch (1970-01-01T00:00:00Z).
Type: Timestamp
Required: No

 ** TopicName **   <a name="Firehose-Type-MSKSourceDescription-TopicName"></a>
The topic name within the Amazon MSK cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\\._\\-]+`
Required: No

## See Also
<a name="API_MSKSourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/MSKSourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/MSKSourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/MSKSourceDescription)
