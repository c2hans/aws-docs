---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_CustomerAgreementSummary.html
---

# CustomerAgreementSummary
<a name="API_CustomerAgreementSummary"></a>

Summary for customer-agreement resource.

## Contents
<a name="API_CustomerAgreementSummary_Contents"></a>

 ** acceptanceTerms **   <a name="artifact-Type-CustomerAgreementSummary-acceptanceTerms"></a>
Terms required to accept the agreement resource.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** agreementArn **   <a name="artifact-Type-CustomerAgreementSummary-agreementArn"></a>
ARN of the agreement resource the customer-agreement resource represents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** arn **   <a name="artifact-Type-CustomerAgreementSummary-arn"></a>
ARN of the customer-agreement resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** awsAccountId **   <a name="artifact-Type-CustomerAgreementSummary-awsAccountId"></a>
AWS account Id that owns the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** description **   <a name="artifact-Type-CustomerAgreementSummary-description"></a>
Description of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** effectiveEnd **   <a name="artifact-Type-CustomerAgreementSummary-effectiveEnd"></a>
Timestamp indicating when the agreement was terminated.
Type: Timestamp
Required: No

 ** effectiveStart **   <a name="artifact-Type-CustomerAgreementSummary-effectiveStart"></a>
Timestamp indicating when the agreement became effective.
Type: Timestamp
Required: No

 ** id **   <a name="artifact-Type-CustomerAgreementSummary-id"></a>
Identifier of the customer-agreement resource.
Type: String
Pattern: `customer-agreement-[a-zA-Z0-9]{16}`
Required: No

 ** name **   <a name="artifact-Type-CustomerAgreementSummary-name"></a>
Name of the customer-agreement resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** organizationArn **   <a name="artifact-Type-CustomerAgreementSummary-organizationArn"></a>
ARN of the organization that owns the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** state **   <a name="artifact-Type-CustomerAgreementSummary-state"></a>
State of the resource.
Type: String
Valid Values: `ACTIVE | CUSTOMER_TERMINATED | AWS_TERMINATED`
Required: No

 ** terminateTerms **   <a name="artifact-Type-CustomerAgreementSummary-terminateTerms"></a>
Terms required to terminate the customer-agreement resource.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** type **   <a name="artifact-Type-CustomerAgreementSummary-type"></a>
Type of the customer-agreement resource.
Type: String
Valid Values: `CUSTOM | DEFAULT | MODIFIED`
Required: No

## See Also
<a name="API_CustomerAgreementSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/CustomerAgreementSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/CustomerAgreementSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/CustomerAgreementSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Artifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query artifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
