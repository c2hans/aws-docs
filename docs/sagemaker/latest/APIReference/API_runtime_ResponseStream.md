---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_ResponseStream.html
---

# ResponseStream
<a name="API_runtime_ResponseStream"></a>

A stream of payload parts. Each part contains a portion of the response for a streaming inference request.

## Contents
<a name="API_runtime_ResponseStream_Contents"></a>

 ** InternalStreamFailure **   <a name="sagemaker-Type-runtime_ResponseStream-InternalStreamFailure"></a>
The stream processing failed because of an unknown error, exception or failure. Try your request again.
Type: Exception
HTTP Status Code:
Required: No

 ** ModelStreamError **   <a name="sagemaker-Type-runtime_ResponseStream-ModelStreamError"></a>
 An error occurred while streaming the response body. This error can have the following error codes:
ModelInvocationTimeExceeded
The model failed to finish sending the response within the timeout period allowed by Amazon SageMaker AI.
StreamBroken
The Transmission Control Protocol (TCP) connection between the client and the model was reset or closed.
Type: Exception
HTTP Status Code:
Required: No

 ** PayloadPart **   <a name="sagemaker-Type-runtime_ResponseStream-PayloadPart"></a>
A wrapper for pieces of the payload that's returned in response to a streaming inference request. A streaming inference response consists of one or more payload parts.
Type: [PayloadPart](API_runtime_PayloadPart.md) object
Required: No

## See Also
<a name="API_runtime_ResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/runtime.sagemaker-2017-05-13/ResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.sagemaker-2017-05-13/ResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.sagemaker-2017-05-13/ResponseStream)
