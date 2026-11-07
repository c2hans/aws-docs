---
source_url: https://docs.aws.amazon.com/account-access-runtime/latest/APIReference/API_CredentialsDetails.html
---

# CredentialsDetails
<a name="API_CredentialsDetails"></a>

The temporary credentials returned for a role. Only one member is set, depending on the type of access that you requested.

## Contents
<a name="API_CredentialsDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** programmaticAccess **   <a name="accountaccessruntime-Type-CredentialsDetails-programmaticAccess"></a>
The access key credentials returned for programmatic access with the AWS CLI or an AWS SDK.
Type: [ProgrammaticAccessDetails](API_ProgrammaticAccessDetails.md) object
Required: No

## See Also
<a name="API_CredentialsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-runtime-2018-05-10/CredentialsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-runtime-2018-05-10/CredentialsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-runtime-2018-05-10/CredentialsDetails)
