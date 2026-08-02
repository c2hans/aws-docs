---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypeItem.html
---

# ListProfileObjectTypeItem
<a name="API_connect-customer-profiles_ListProfileObjectTypeItem"></a>

A ProfileObjectType instance.

## Contents
<a name="API_connect-customer-profiles_ListProfileObjectTypeItem_Contents"></a>

 ** Description **   <a name="connect-Type-connect-customer-profiles_ListProfileObjectTypeItem-Description"></a>
Description of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** ObjectTypeName **   <a name="connect-Type-connect-customer-profiles_ListProfileObjectTypeItem-ObjectTypeName"></a>
The name of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_ListProfileObjectTypeItem-CreatedAt"></a>
The timestamp of when the domain was created.
Type: Timestamp
Required: No

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_ListProfileObjectTypeItem-LastUpdatedAt"></a>
The timestamp of when the profile object type was most recently edited.
Type: Timestamp
Required: No

 ** MaxAvailableProfileObjectCount **   <a name="connect-Type-connect-customer-profiles_ListProfileObjectTypeItem-MaxAvailableProfileObjectCount"></a>
The amount of provisioned profile object max count available.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MaxProfileObjectCount **   <a name="connect-Type-connect-customer-profiles_ListProfileObjectTypeItem-MaxProfileObjectCount"></a>
The amount of profile object max count assigned to the object type.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** SourcePriority **   <a name="connect-Type-connect-customer-profiles_ListProfileObjectTypeItem-SourcePriority"></a>
An integer that determines the priority of this object type when data from multiple sources is ingested. Lower values take priority. Object types without a specified source priority default to the lowest priority.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_ListProfileObjectTypeItem-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-customer-profiles_ListProfileObjectTypeItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListProfileObjectTypeItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListProfileObjectTypeItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListProfileObjectTypeItem)
