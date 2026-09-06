---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuthInfo.html
---

# AuthInfo
<a name="API_AuthInfo"></a>

A collection of authorization information.

## Contents
<a name="API_AuthInfo_Contents"></a>

 ** resources **   <a name="iot-Type-AuthInfo-resources"></a>
The resources for which the principal is being authorized to perform the specified action.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `[\s\S]*`
Required: Yes

 ** actionType **   <a name="iot-Type-AuthInfo-actionType"></a>
The type of action for which the principal is being authorized.
Type: String
Valid Values: `PUBLISH | SUBSCRIBE | RECEIVE | CONNECT`
Required: No

## See Also
<a name="API_AuthInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuthInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuthInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuthInfo)
