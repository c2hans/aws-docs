---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_prm_ValidationExceptionField.html
---

# ValidationExceptionField
<a name="API_prm_ValidationExceptionField"></a>

Details about a specific field that failed validation.

## Contents
<a name="API_prm_ValidationExceptionField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Code **   <a name="AWSPartnerCentral-Type-prm_ValidationExceptionField-Code"></a>
The specific validation error code indicating the type of validation failure.
Type: String
Valid Values: `REQUIRED_FIELD_MISSING | DUPLICATE_VALUE | INVALID_VALUE | INVALID_STRING_FORMAT | TOO_MANY_VALUES | ACTION_NOT_PERMITTED | INVALID_ENUM_VALUE | INVALID_NUMBER_FORMAT | INVALID_STRING_LENGTH`
Required: Yes

 ** Message **   <a name="AWSPartnerCentral-Type-prm_ValidationExceptionField-Message"></a>
A human-readable message describing why the field validation failed.
Type: String
Required: Yes

 ** Name **   <a name="AWSPartnerCentral-Type-prm_ValidationExceptionField-Name"></a>
The name of the field that failed validation.
Type: String
Required: Yes

## See Also
<a name="API_prm_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-revenue-measurement-2022-07-26/ValidationExceptionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-revenue-measurement-2022-07-26/ValidationExceptionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-revenue-measurement-2022-07-26/ValidationExceptionField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
