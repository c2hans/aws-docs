---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_TerminateCustomerAgreementSummary.html
---

# TerminateCustomerAgreementSummary
<a name="API_TerminateCustomerAgreementSummary"></a>

Summary returned when terminating an agreement.

## Contents
<a name="API_TerminateCustomerAgreementSummary_Contents"></a>

 ** agreementArn **   <a name="artifact-Type-TerminateCustomerAgreementSummary-agreementArn"></a>
ARN of the agreement resource the customer-agreement resource represents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** arn **   <a name="artifact-Type-TerminateCustomerAgreementSummary-arn"></a>
Arn of the customer-agreement resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** effectiveEnd **   <a name="artifact-Type-TerminateCustomerAgreementSummary-effectiveEnd"></a>
Timestamp indicating when the agreement was terminated.
Type: Timestamp
Required: No

 ** effectiveStart **   <a name="artifact-Type-TerminateCustomerAgreementSummary-effectiveStart"></a>
Timestamp indicating when the agreement became effective.
Type: Timestamp
Required: No

 ** id **   <a name="artifact-Type-TerminateCustomerAgreementSummary-id"></a>
Identifier of the customer-agreement resource.
Type: String
Pattern: `customer-agreement-[a-zA-Z0-9]{16}`
Required: No

 ** name **   <a name="artifact-Type-TerminateCustomerAgreementSummary-name"></a>
Name of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** state **   <a name="artifact-Type-TerminateCustomerAgreementSummary-state"></a>
State of the resource.
Type: String
Valid Values: `ACTIVE | CUSTOMER_TERMINATED | AWS_TERMINATED`
Required: No

## See Also
<a name="API_TerminateCustomerAgreementSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/TerminateCustomerAgreementSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/TerminateCustomerAgreementSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/TerminateCustomerAgreementSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Artifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query artifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
