---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_NodeSignal.html
---

# NodeSignal
<a name="API_NodeSignal"></a>

A signal to a camera node to start or stop processing video.

## Contents
<a name="API_NodeSignal_Contents"></a>

 ** NodeInstanceId **   <a name="panorama-Type-NodeSignal-NodeInstanceId"></a>
The camera node's name, from the application manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** Signal **   <a name="panorama-Type-NodeSignal-Signal"></a>
The signal value.
Type: String
Valid Values: `PAUSE | RESUME`
Required: Yes

## See Also
<a name="API_NodeSignal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/NodeSignal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/NodeSignal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/NodeSignal)
