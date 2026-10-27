---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BatchGetDestinationEndpointError.html
---

# BatchGetDestinationEndpointError
<a name="API_BatchGetDestinationEndpointError"></a>

An error for a destination endpoint that MediaConnect couldn't retrieve in a `BatchGetDestinationEndpoint` request.

## Contents
<a name="API_BatchGetDestinationEndpointError_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-BatchGetDestinationEndpointError-arn"></a>
The Amazon Resource Name (ARN) of the destination endpoint that MediaConnect couldn't retrieve.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:destinationEndpoint:[a-z0-9]{12}`
Required: Yes

 ** code **   <a name="mediaconnect-Type-BatchGetDestinationEndpointError-code"></a>
The error code.
Type: String
Required: Yes

 ** message **   <a name="mediaconnect-Type-BatchGetDestinationEndpointError-message"></a>
A description of the error.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetDestinationEndpointError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BatchGetDestinationEndpointError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BatchGetDestinationEndpointError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BatchGetDestinationEndpointError)
