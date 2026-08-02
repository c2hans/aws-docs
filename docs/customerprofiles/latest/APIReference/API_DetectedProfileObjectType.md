---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DetectedProfileObjectType.html
---

# DetectedProfileObjectType
<a name="API_connect-customer-profiles_DetectedProfileObjectType"></a>

Contains `ProfileObjectType` mapping information from the model.

## Contents
<a name="API_connect-customer-profiles_DetectedProfileObjectType_Contents"></a>

 ** Fields **   <a name="connect-Type-connect-customer-profiles_DetectedProfileObjectType-Fields"></a>
A map of the name and the `ObjectType` field.
Type: String to [ObjectTypeField](API_connect-customer-profiles_ObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`
Required: No

 ** Keys **   <a name="connect-Type-connect-customer-profiles_DetectedProfileObjectType-Keys"></a>
A list of unique keys that can be used to map data to a profile.
Type: String to array of [ObjectTypeKey](API_connect-customer-profiles_ObjectTypeKey.md) objects map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** SourceLastUpdatedTimestampFormat **   <a name="connect-Type-connect-customer-profiles_DetectedProfileObjectType-SourceLastUpdatedTimestampFormat"></a>
The format of `sourceLastUpdatedTimestamp` that was detected in fields.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_connect-customer-profiles_DetectedProfileObjectType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DetectedProfileObjectType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DetectedProfileObjectType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DetectedProfileObjectType)
