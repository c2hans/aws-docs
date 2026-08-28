---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_InvocationCompletedDetails.html
---

# InvocationCompletedDetails
<a name="API_InvocationCompletedDetails"></a>

Details about a function invocation that completed.

## Contents
<a name="API_InvocationCompletedDetails_Contents"></a>

 ** EndTimestamp **   <a name="lambda-Type-InvocationCompletedDetails-EndTimestamp"></a>
The date and time when the invocation ended, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: Yes

 ** RequestId **   <a name="lambda-Type-InvocationCompletedDetails-RequestId"></a>
The request ID for the invocation.
Type: String
Required: Yes

 ** StartTimestamp **   <a name="lambda-Type-InvocationCompletedDetails-StartTimestamp"></a>
The date and time when the invocation started, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: Yes

 ** Error **   <a name="lambda-Type-InvocationCompletedDetails-Error"></a>
Details about the invocation failure.
Type: [EventError](API_EventError.md) object
Required: No

## See Also
<a name="API_InvocationCompletedDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/InvocationCompletedDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/InvocationCompletedDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/InvocationCompletedDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
