---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_FieldValidationError.html
---

# FieldValidationError
<a name="API_account_FieldValidationError"></a>

Contains information about a field-level validation error that occurred during an operation.

## Contents
<a name="API_account_FieldValidationError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Code **   <a name="AWSPartnerCentral-Type-account_FieldValidationError-Code"></a>
A code identifying the specific field validation error.
Type: String
Valid Values: `REQUIRED_FIELD_MISSING | DUPLICATE_VALUE | INVALID_VALUE | INVALID_STRING_FORMAT | TOO_MANY_VALUES | ACTION_NOT_PERMITTED | INVALID_ENUM_VALUE`
Required: Yes

 ** Message **   <a name="AWSPartnerCentral-Type-account_FieldValidationError-Message"></a>
A description of the field validation error.
Type: String
Required: Yes

 ** Name **   <a name="AWSPartnerCentral-Type-account_FieldValidationError-Name"></a>
The name of the field that failed validation.
Type: String
Required: Yes

## See Also
<a name="API_account_FieldValidationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/FieldValidationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/FieldValidationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/FieldValidationError)
