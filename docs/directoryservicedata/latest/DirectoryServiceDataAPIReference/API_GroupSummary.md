---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_GroupSummary.html
---

# GroupSummary
<a name="API_GroupSummary"></a>

A structure containing a subset of fields of a group object from a directory.

## Contents
<a name="API_GroupSummary_Contents"></a>

 ** GroupScope **   <a name="directoryservicedata-Type-GroupSummary-GroupScope"></a>
The scope of the AD group. For details, see [Active Directory security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope).
Type: String
Valid Values: `DomainLocal | Global | Universal | BuiltinLocal`
Required: Yes

 ** GroupType **   <a name="directoryservicedata-Type-GroupSummary-GroupType"></a>
The AD group type. For details, see [Active Directory security group type](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work).
Type: String
Valid Values: `Distribution | Security`
Required: Yes

 ** SAMAccountName **   <a name="directoryservicedata-Type-GroupSummary-SAMAccountName"></a>
The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^:;|=+"*?<>/\\,\[\]@]+`
Required: Yes

 ** SID **   <a name="directoryservicedata-Type-GroupSummary-SID"></a>
The unique security identifier (SID) of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_GroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/GroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/GroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/GroupSummary)
