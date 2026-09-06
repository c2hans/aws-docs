---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BlackFramesConfiguration.html
---

# BlackFramesConfiguration
<a name="API_BlackFramesConfiguration"></a>

Detects black frames in the router input's source content and reports them through a CloudWatch metric, an EventBridge event, and a router input message.

## Contents
<a name="API_BlackFramesConfiguration_Contents"></a>

 ** state **   <a name="mediaconnect-Type-BlackFramesConfiguration-state"></a>
Indicates whether black frames detection is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** thresholdSeconds **   <a name="mediaconnect-Type-BlackFramesConfiguration-thresholdSeconds"></a>
The number of consecutive seconds of black frames that MediaConnect must detect before it reports an issue.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 60.
Required: Yes

## See Also
<a name="API_BlackFramesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BlackFramesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BlackFramesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BlackFramesConfiguration)
