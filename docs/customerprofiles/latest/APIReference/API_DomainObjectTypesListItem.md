---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DomainObjectTypesListItem.html
---

# DomainObjectTypesListItem
<a name="API_connect-customer-profiles_DomainObjectTypesListItem"></a>

Represents an item in the list of domain object types, containing basic information about a specific object type within a domain.

## Contents
<a name="API_connect-customer-profiles_DomainObjectTypesListItem_Contents"></a>

 ** ObjectTypeName **   <a name="connect-Type-connect-customer-profiles_DomainObjectTypesListItem-ObjectTypeName"></a>
The name that identifies the object type within the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_DomainObjectTypesListItem-CreatedAt"></a>
The timestamp of when the domain object type was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-connect-customer-profiles_DomainObjectTypesListItem-Description"></a>
A description explaining the purpose and characteristics of this object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_DomainObjectTypesListItem-LastUpdatedAt"></a>
The timestamp of when the domain object type was most recently edited.
Type: Timestamp
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_DomainObjectTypesListItem-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-customer-profiles_DomainObjectTypesListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DomainObjectTypesListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DomainObjectTypesListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DomainObjectTypesListItem)
