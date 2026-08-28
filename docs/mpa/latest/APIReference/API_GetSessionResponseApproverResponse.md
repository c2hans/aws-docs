---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_GetSessionResponseApproverResponse.html
---

# GetSessionResponseApproverResponse
<a name="API_GetSessionResponseApproverResponse"></a>

Contains details for an approver response in an approval session.

## Contents
<a name="API_GetSessionResponseApproverResponse_Contents"></a>

 ** ApproverId **   <a name="mpa-Type-GetSessionResponseApproverResponse-ApproverId"></a>
ID for the approver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IdentityId **   <a name="mpa-Type-GetSessionResponseApproverResponse-IdentityId"></a>
ID for the identity source. The identity source manages the user authentication for approvers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IdentitySourceArn **   <a name="mpa-Type-GetSessionResponseApproverResponse-IdentitySourceArn"></a>
Amazon Resource Name (ARN) for the identity source. The identity source manages the user authentication for approvers.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** Response **   <a name="mpa-Type-GetSessionResponseApproverResponse-Response"></a>
Response to the operation request.
Type: String
Valid Values: `APPROVED | REJECTED | NO_RESPONSE`
Required: No

 ** ResponseTime **   <a name="mpa-Type-GetSessionResponseApproverResponse-ResponseTime"></a>
Timestamp when a approver responded to the operation request.
Type: Timestamp
Required: No

## See Also
<a name="API_GetSessionResponseApproverResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/GetSessionResponseApproverResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/GetSessionResponseApproverResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/GetSessionResponseApproverResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
