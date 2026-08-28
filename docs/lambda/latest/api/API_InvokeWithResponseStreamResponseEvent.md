---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_InvokeWithResponseStreamResponseEvent.html
---

# InvokeWithResponseStreamResponseEvent
<a name="API_InvokeWithResponseStreamResponseEvent"></a>

An object that includes a chunk of the response payload. When the stream has ended, Lambda includes a `InvokeComplete` object.

## Contents
<a name="API_InvokeWithResponseStreamResponseEvent_Contents"></a>

 ** InvokeComplete **   <a name="lambda-Type-InvokeWithResponseStreamResponseEvent-InvokeComplete"></a>
An object that's returned when the stream has ended and all the payload chunks have been returned.
Type: [InvokeWithResponseStreamCompleteEvent](API_InvokeWithResponseStreamCompleteEvent.md) object
Required: No

 ** PayloadChunk **   <a name="lambda-Type-InvokeWithResponseStreamResponseEvent-PayloadChunk"></a>
A chunk of the streamed response payload.
Type: [InvokeResponseStreamUpdate](API_InvokeResponseStreamUpdate.md) object
Required: No

## See Also
<a name="API_InvokeWithResponseStreamResponseEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/InvokeWithResponseStreamResponseEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/InvokeWithResponseStreamResponseEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/InvokeWithResponseStreamResponseEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
