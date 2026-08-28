---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ContextDetails.html
---

# ContextDetails
<a name="API_ContextDetails"></a>

Details about a durable execution context.

## Contents
<a name="API_ContextDetails_Contents"></a>

 ** Error **   <a name="lambda-Type-ContextDetails-Error"></a>
Details about the context failure.
Type: [ErrorObject](API_ErrorObject.md) object
Required: No

 ** ReplayChildren **   <a name="lambda-Type-ContextDetails-ReplayChildren"></a>
Whether the state data of child operations of this completed context should be included in the invoke payload and `GetDurableExecutionState` response.
Type: Boolean
Required: No

 ** Result **   <a name="lambda-Type-ContextDetails-Result"></a>
The response payload from the context.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6291456.
Required: No

## See Also
<a name="API_ContextDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ContextDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ContextDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ContextDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
