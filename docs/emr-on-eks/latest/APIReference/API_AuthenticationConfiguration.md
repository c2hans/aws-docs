---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_AuthenticationConfiguration.html
---

# AuthenticationConfiguration
<a name="API_AuthenticationConfiguration"></a>

Contains the authentication settings for a security configuration, including Identity Center and IAM configuration options.

## Contents
<a name="API_AuthenticationConfiguration_Contents"></a>

 ** iamConfiguration **   <a name="emroneks-Type-AuthenticationConfiguration-iamConfiguration"></a>
The IAM configuration to use for authentication.
Type: [IAMConfiguration](API_IAMConfiguration.md) object
Required: No

 ** identityCenterConfiguration **   <a name="emroneks-Type-AuthenticationConfiguration-identityCenterConfiguration"></a>
The IAM Identity Center configuration to use for authentication.
Type: [IdentityCenterConfiguration](API_IdentityCenterConfiguration.md) object
Required: No

## See Also
<a name="API_AuthenticationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/AuthenticationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/AuthenticationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/AuthenticationConfiguration)
