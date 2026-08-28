---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ErrorDetail.html
---

# ErrorDetail
<a name="API_account_ErrorDetail"></a>

Contains detailed information about an error that occurred during an operation.

## Contents
<a name="API_account_ErrorDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Locale **   <a name="AWSPartnerCentral-Type-account_ErrorDetail-Locale"></a>
The locale or language code for the error message.
Type: String
Required: Yes

 ** Message **   <a name="AWSPartnerCentral-Type-account_ErrorDetail-Message"></a>
A human-readable description of the error.
Type: String
Required: Yes

 ** Reason **   <a name="AWSPartnerCentral-Type-account_ErrorDetail-Reason"></a>
A machine-readable code or reason for the error.
Type: String
Valid Values: `INVALID_CONTENT | DUPLICATE_PROFILE | INVALID_LOGO | INVALID_LOGO_URL | INVALID_LOGO_FILE | INVALID_LOGO_SIZE | INVALID_WEBSITE_URL`
Required: Yes

## See Also
<a name="API_account_ErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/ErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/ErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/ErrorDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
