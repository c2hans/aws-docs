---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BatchGetSourceEndpointError.html
---

# BatchGetSourceEndpointError
<a name="API_BatchGetSourceEndpointError"></a>

An error for a source endpoint that MediaConnect couldn't retrieve in a `BatchGetSourceEndpoint` request.

## Contents
<a name="API_BatchGetSourceEndpointError_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-BatchGetSourceEndpointError-arn"></a>
The Amazon Resource Name (ARN) of the source endpoint that MediaConnect couldn't retrieve.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:sourceEndpoint:[a-z0-9]{12}`
Required: Yes

 ** code **   <a name="mediaconnect-Type-BatchGetSourceEndpointError-code"></a>
The error code.
Type: String
Required: Yes

 ** message **   <a name="mediaconnect-Type-BatchGetSourceEndpointError-message"></a>
A description of the error.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetSourceEndpointError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BatchGetSourceEndpointError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BatchGetSourceEndpointError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BatchGetSourceEndpointError)
