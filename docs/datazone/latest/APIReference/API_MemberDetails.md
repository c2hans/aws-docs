---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_MemberDetails.html
---

# MemberDetails
<a name="API_MemberDetails"></a>

The details about a project member.

## Contents
<a name="API_MemberDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** group **   <a name="datazone-Type-MemberDetails-group"></a>
The group details of a project member.
Type: [GroupDetails](API_GroupDetails.md) object
Required: No

 ** user **   <a name="datazone-Type-MemberDetails-user"></a>
The user details of a project member.
Type: [UserDetails](API_UserDetails.md) object
Required: No

## See Also
<a name="API_MemberDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/MemberDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/MemberDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/MemberDetails)
