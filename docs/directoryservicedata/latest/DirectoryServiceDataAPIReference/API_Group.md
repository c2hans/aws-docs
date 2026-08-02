---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_Group.html
---

# Group
<a name="API_Group"></a>

 A group object that contains identifying information and attributes for a specified group.

## Contents
<a name="API_Group_Contents"></a>

 ** SAMAccountName **   <a name="directoryservicedata-Type-Group-SAMAccountName"></a>
 The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^:;|=+"*?<>/\\,\[\]@]+`
Required: Yes

 ** DistinguishedName **   <a name="directoryservicedata-Type-Group-DistinguishedName"></a>
The [distinguished name](https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name) of the object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** GroupScope **   <a name="directoryservicedata-Type-Group-GroupScope"></a>
 The scope of the AD group. For details, see [Active Directory security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope)
Type: String
Valid Values: `DomainLocal | Global | Universal | BuiltinLocal`
Required: No

 ** GroupType **   <a name="directoryservicedata-Type-Group-GroupType"></a>
 The AD group type. For details, see [Active Directory security group type](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work).
Type: String
Valid Values: `Distribution | Security`
Required: No

 ** OtherAttributes **   <a name="directoryservicedata-Type-Group-OtherAttributes"></a>
 An expression of one or more attributes, data types, and the values of a group.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Map Entries: Maximum number of 25 items.
Key Length Constraints: Minimum length of 1. Maximum length of 63.
Key Pattern: `[A-Za-z*][A-Za-z-*]*`
Required: No

 ** SID **   <a name="directoryservicedata-Type-Group-SID"></a>
 The unique security identifier (SID) of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Group_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/Group)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/Group)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/Group)
