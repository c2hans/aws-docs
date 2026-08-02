---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_InputConfiguration.html
---

# InputConfiguration
<a name="API_InputConfiguration"></a>

 The transport parameters that are associated with an incoming media stream.

## Contents
<a name="API_InputConfiguration_Contents"></a>

 ** inputIp **   <a name="mediaconnect-Type-InputConfiguration-inputIp"></a>
 The IP address that the flow listens on for incoming content for a media stream.
Type: String
Required: Yes

 ** inputPort **   <a name="mediaconnect-Type-InputConfiguration-inputPort"></a>
 The port that the flow listens on for an incoming media stream.
Type: Integer
Required: Yes

 ** interface **   <a name="mediaconnect-Type-InputConfiguration-interface"></a>
 The VPC interface where the media stream comes in from.
Type: [Interface](API_Interface.md) object
Required: Yes

## See Also
<a name="API_InputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/InputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/InputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/InputConfiguration)
