---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_gateway_runtime_ResponseStream.html
---

# ResponseStream

The events in the response stream. The response arrives as `PayloadPart` events. A failure after the stream starts arrives as one `InternalStreamFailure` event, and then the stream ends.

## Contents
<a name="API_gateway_runtime_ResponseStream_Contents"></a>

 ** InternalStreamFailure **   <a name="sagemaker-Type-gateway_runtime_ResponseStream-InternalStreamFailure"></a>
A failure after the stream started. The stream ends after this event.
Type: Exception
HTTP Status Code:
Required: No

 ** ModelStreamError **   <a name="sagemaker-Type-gateway_runtime_ResponseStream-ModelStreamError"></a>
Reserved for a model error during the stream. The Global Inference Gateway doesn't currently send this event. A failure after the stream starts is reported as `InternalStreamFailure`.
Type: Exception
HTTP Status Code:
Required: No

 ** PayloadPart **   <a name="sagemaker-Type-gateway_runtime_ResponseStream-PayloadPart"></a>
A part of the model server's response.
Type: [PayloadPart](API_gateway_runtime_PayloadPart.md) object
Required: No

## See Also
<a name="API_gateway_runtime_ResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-gateway-runtime-2026-10-01/ResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-gateway-runtime-2026-10-01/ResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-gateway-runtime-2026-10-01/ResponseStream)
