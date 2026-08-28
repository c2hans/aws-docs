---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_FailedRequest.html
---

# FailedRequest
<a name="API_FailedRequest"></a>

Request for which contact failed to be generated.

## Contents
<a name="API_FailedRequest_Contents"></a>

 ** FailureReasonCode **   <a name="connect-Type-FailedRequest-FailureReasonCode"></a>
Reason code for the failure.
Type: String
Valid Values: `INVALID_ATTRIBUTE_KEY | INVALID_CUSTOMER_ENDPOINT | INVALID_SYSTEM_ENDPOINT | INVALID_QUEUE | INVALID_OUTBOUND_STRATEGY | MISSING_CAMPAIGN | MISSING_CUSTOMER_ENDPOINT | MISSING_QUEUE_ID_AND_SYSTEM_ENDPOINT | REQUEST_THROTTLED | IDEMPOTENCY_EXCEPTION | INTERNAL_ERROR`
Required: No

 ** FailureReasonMessage **   <a name="connect-Type-FailedRequest-FailureReasonMessage"></a>
Why the request to create a contact failed.
Type: String
Required: No

 ** RequestIdentifier **   <a name="connect-Type-FailedRequest-RequestIdentifier"></a>
Request identifier provided in the API call in the ContactDataRequest to create a contact.
Type: String
Length Constraints: Maximum length of 80.
Required: No

## See Also
<a name="API_FailedRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/FailedRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/FailedRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/FailedRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
