---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AuthenticationMethod.html
---

# AuthenticationMethod
<a name="API_AuthenticationMethod"></a>

A structure that describes an authentication method that can be used by an application.

## Contents
<a name="API_AuthenticationMethod_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Iam **   <a name="singlesignon-Type-AuthenticationMethod-Iam"></a>
A structure that describes details for IAM authentication.
Type: [IamAuthenticationMethod](API_IamAuthenticationMethod.md) object
Required: No

## See Also
<a name="API_AuthenticationMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AuthenticationMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AuthenticationMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AuthenticationMethod)
