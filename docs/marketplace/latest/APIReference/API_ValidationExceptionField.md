---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ValidationExceptionField.html
---

# ValidationExceptionField
<a name="API_ValidationExceptionField"></a>

Detailed information about a single request field that failed validation, including the field's location, the reason it failed, and a human-readable message.

## Contents
<a name="API_ValidationExceptionField_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ChangeType **   <a name="AWSMarketplaceService-Type-ValidationExceptionField-ChangeType"></a>
The change type the failing field applies to, if the field is part of a change request. For example, `AddDeliveryOptions`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[A-Z][\w]*$`
Required: No

 ** EntityId **   <a name="AWSMarketplaceService-Type-ValidationExceptionField-EntityId"></a>
The entity identifier the failing field applies to, if the field is on a specific entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: No

 ** EntityType **   <a name="AWSMarketplaceService-Type-ValidationExceptionField-EntityType"></a>
The entity type the failing field applies to, if the field is on a specific entity. For example, `AmiProduct@1.0`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+$`
Required: No

 ** Field **   <a name="AWSMarketplaceService-Type-ValidationExceptionField-Field"></a>
The name of the request field that failed validation, expressed as a JSON path (for example, `Details.DeliveryOptions[0].Type`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\-_\.\/]+$`
Required: No

 ** Message **   <a name="AWSMarketplaceService-Type-ValidationExceptionField-Message"></a>
A human-readable message describing why the field failed validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(.)+$`
Required: No

 ** Reason **   <a name="AWSMarketplaceService-Type-ValidationExceptionField-Reason"></a>
The reason the field failed validation.
Type: String
Valid Values: `UnknownOperation | CannotParse | FieldValidationFailed | Other`
Required: No

## See Also
<a name="API_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ValidationExceptionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ValidationExceptionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ValidationExceptionField)
