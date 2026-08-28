---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ValidationError.html
---

# ValidationError
<a name="API_account_ValidationError"></a>

Contains information about a validation error, which can be either a field-level or business rule validation error.

## Contents
<a name="API_account_ValidationError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BusinessValidationError **   <a name="AWSPartnerCentral-Type-account_ValidationError-BusinessValidationError"></a>
Details about a business rule validation error, if applicable.
Type: [BusinessValidationError](API_account_BusinessValidationError.md) object
Required: No

 ** FieldValidationError **   <a name="AWSPartnerCentral-Type-account_ValidationError-FieldValidationError"></a>
Details about a field-level validation error, if applicable.
Type: [FieldValidationError](API_account_FieldValidationError.md) object
Required: No

## See Also
<a name="API_account_ValidationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/ValidationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/ValidationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/ValidationError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
