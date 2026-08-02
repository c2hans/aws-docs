---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_Member.html
---

# Member
<a name="API_Member"></a>

A member object that contains identifying information for a specified member.

## Contents
<a name="API_Member_Contents"></a>

 ** MemberType **   <a name="directoryservicedata-Type-Member-MemberType"></a>
 The AD type of the member object.
Type: String
Valid Values: `USER | GROUP | COMPUTER`
Required: Yes

 ** SAMAccountName **   <a name="directoryservicedata-Type-Member-SAMAccountName"></a>
 The name of the group member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[^:;|=+"*?<>/\\,\[\]@]+`
Required: Yes

 ** SID **   <a name="directoryservicedata-Type-Member-SID"></a>
 The unique security identifier (SID) of the group member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Member_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/Member)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/Member)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/Member)
