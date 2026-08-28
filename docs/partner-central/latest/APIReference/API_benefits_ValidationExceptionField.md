---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_ValidationExceptionField.html
---

# ValidationExceptionField
<a name="API_benefits_ValidationExceptionField"></a>

Represents a field-specific validation error with detailed information.

## Contents
<a name="API_benefits_ValidationExceptionField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Message **   <a name="AWSPartnerCentral-Type-benefits_ValidationExceptionField-Message"></a>
A detailed message explaining why the field validation failed.
Type: String
Required: Yes

 ** Name **   <a name="AWSPartnerCentral-Type-benefits_ValidationExceptionField-Name"></a>
The name of the field that failed validation.
Type: String
Required: Yes

 ** Code **   <a name="AWSPartnerCentral-Type-benefits_ValidationExceptionField-Code"></a>
An error code explaining why the field validation failed.
Type: String
Valid Values: `REQUIRED_FIELD_MISSING | INVALID_ENUM_VALUE | INVALID_STRING_FORMAT | INVALID_VALUE | NOT_ENOUGH_VALUES | TOO_MANY_VALUES | INVALID_RESOURCE_STATE | DUPLICATE_KEY_VALUE | VALUE_OUT_OF_RANGE | ACTION_NOT_PERMITTED`
Required: No

## See Also
<a name="API_benefits_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/ValidationExceptionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/ValidationExceptionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/ValidationExceptionField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
