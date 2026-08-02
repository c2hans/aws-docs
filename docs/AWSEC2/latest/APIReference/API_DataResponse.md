---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DataResponse.html
---

# DataResponse
<a name="API_DataResponse"></a>

The response to a `DataQuery`.

## Contents
<a name="API_DataResponse_Contents"></a>

 ** destination **
The Region or Availability Zone that's the destination for the data query. For example, `eu-west-1`.
Type: String
Required: No

 ** id **
The ID passed in the `DataQuery`.
Type: String
Required: No

 ** metric **
The metric used for the network performance request.
Type: String
Valid Values: `aggregate-latency`
Required: No

 ** MetricPointSet.N **
A list of `MetricPoint` objects.
Type: Array of [MetricPoint](API_MetricPoint.md) objects
Required: No

 ** period **
The period used for the network performance request.
Type: String
Valid Values: `five-minutes | fifteen-minutes | one-hour | three-hours | one-day | one-week`
Required: No

 ** source **
The Region or Availability Zone that's the source for the data query. For example, `us-east-1`.
Type: String
Required: No

 ** statistic **
The statistic used for the network performance request.
Type: String
Valid Values: `p50`
Required: No

## See Also
<a name="API_DataResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DataResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DataResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DataResponse)
