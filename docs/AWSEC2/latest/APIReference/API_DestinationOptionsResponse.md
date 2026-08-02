---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DestinationOptionsResponse.html
---

# DestinationOptionsResponse
<a name="API_DestinationOptionsResponse"></a>

Describes the destination options for a flow log.

## Contents
<a name="API_DestinationOptionsResponse_Contents"></a>

 ** fileFormat **
The format for the flow log.
Type: String
Valid Values: `plain-text | parquet`
Required: No

 ** hiveCompatiblePartitions **
Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3.
Type: Boolean
Required: No

 ** perHourPartition **
Indicates whether to partition the flow log per hour.
Type: Boolean
Required: No

## See Also
<a name="API_DestinationOptionsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DestinationOptionsResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DestinationOptionsResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DestinationOptionsResponse)
