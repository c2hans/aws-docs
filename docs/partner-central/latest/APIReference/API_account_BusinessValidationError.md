---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_BusinessValidationError.html
---

# BusinessValidationError
<a name="API_account_BusinessValidationError"></a>

Contains information about a business rule validation error that occurred during an operation.

## Contents
<a name="API_account_BusinessValidationError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Code **   <a name="AWSPartnerCentral-Type-account_BusinessValidationError-Code"></a>
A code identifying the specific business validation error.
Type: String
Valid Values: `INCOMPATIBLE_CONNECTION_INVITATION_REQUEST | INCOMPATIBLE_LEGAL_NAME | INCOMPATIBLE_KNOW_YOUR_BUSINESS_STATUS | INCOMPATIBLE_IDENTITY_VERIFICATION_STATUS | INVALID_ACCOUNT_LINKING_STATUS | INVALID_ACCOUNT_STATE | INCOMPATIBLE_DOMAIN | INELIGIBLE_ACCOUNT_TIER | MISSING_ACTIVE_SUBSIDIARY_CONNECTION | INCOMPATIBLE_SUBSIDIARY_CONNECTION | INCOMPATIBLE_PRIMARY_PARTNER | QUALIFICATIONS_ASSOCIATION_LIMIT_EXCEEDED | QUALIFICATIONS_ASSOCIATION_NOT_FOUND | QUALIFICATIONS_ASSOCIATION_EXISTS`
Required: Yes

 ** Message **   <a name="AWSPartnerCentral-Type-account_BusinessValidationError-Message"></a>
A description of the business validation error.
Type: String
Required: Yes

## See Also
<a name="API_account_BusinessValidationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/BusinessValidationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/BusinessValidationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/BusinessValidationError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
