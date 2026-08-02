---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DomainObjectTypeField.html
---

# DomainObjectTypeField
<a name="API_connect-customer-profiles_DomainObjectTypeField"></a>

The standard domain object type.

## Contents
<a name="API_connect-customer-profiles_DomainObjectTypeField_Contents"></a>

 ** Source **   <a name="connect-Type-connect-customer-profiles_DomainObjectTypeField-Source"></a>
The expression that defines how to extract the field value from the source object.>
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** Target **   <a name="connect-Type-connect-customer-profiles_DomainObjectTypeField-Target"></a>
The expression that defines where the field value should be placed in the standard domain object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** ContentType **   <a name="connect-Type-connect-customer-profiles_DomainObjectTypeField-ContentType"></a>
The content type of the field.
Type: String
Valid Values: `STRING | NUMBER`
Required: No

 ** FeatureType **   <a name="connect-Type-connect-customer-profiles_DomainObjectTypeField-FeatureType"></a>
The semantic meaning of the field.
Type: String
Valid Values: `TEXTUAL | CATEGORICAL`
Required: No

## See Also
<a name="API_connect-customer-profiles_DomainObjectTypeField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DomainObjectTypeField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DomainObjectTypeField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DomainObjectTypeField)
