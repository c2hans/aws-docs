---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_EventResumeReason.html
---

# EventResumeReason

The reason for resuming a durable execution, as recorded in the execution history.

## Contents
<a name="API_EventResumeReason_Contents"></a>

 ** Payload **   <a name="lambda-Type-EventResumeReason-Payload"></a>
The reason that you provided when you resumed the execution. This field is only present if you set `IncludeExecutionData` to `true` in the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Truncated **   <a name="lambda-Type-EventResumeReason-Truncated"></a>
Specifies whether Lambda omitted the reason from the response because `IncludeExecutionData` is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_EventResumeReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/EventResumeReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/EventResumeReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/EventResumeReason)
