---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DomainJoinInfo.html
---

# DomainJoinInfo
<a name="API_DomainJoinInfo"></a>

Describes the configuration information required to join fleets and image builders to Microsoft Active Directory domains.

## Contents
<a name="API_DomainJoinInfo_Contents"></a>

 ** DirectoryName **   <a name="WorkSpacesApplications-Type-DomainJoinInfo-DirectoryName"></a>
The fully qualified name of the directory (for example, corp.example.com).
Type: String
Required: No

 ** OrganizationalUnitDistinguishedName **   <a name="WorkSpacesApplications-Type-DomainJoinInfo-OrganizationalUnitDistinguishedName"></a>
The distinguished name of the organizational unit for computer accounts.
Type: String
Length Constraints: Maximum length of 2000.
Required: No

## See Also
<a name="API_DomainJoinInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DomainJoinInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DomainJoinInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DomainJoinInfo)
