---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_AuthenticationDescription.html
---

# AuthenticationDescription
<a name="API_AuthenticationDescription"></a>

A structure containing information about the user authentication methods used by the workspace.

## Contents
<a name="API_AuthenticationDescription_Contents"></a>

 ** providers **   <a name="ManagedGrafana-Type-AuthenticationDescription-providers"></a>
Specifies whether this workspace uses IAM Identity Center, SAML, or both methods to authenticate users to use the Grafana console in the Amazon Managed Grafana workspace.
Type: Array of strings
Valid Values: `AWS_SSO | SAML`
Required: Yes

 ** awsSso **   <a name="ManagedGrafana-Type-AuthenticationDescription-awsSso"></a>
A structure containing information about how this workspace works with IAM Identity Center.
Type: [AwsSsoAuthentication](API_AwsSsoAuthentication.md) object
Required: No

 ** saml **   <a name="ManagedGrafana-Type-AuthenticationDescription-saml"></a>
A structure containing information about how this workspace works with SAML, including what attributes within the assertion are to be mapped to user information in the workspace.
Type: [SamlAuthentication](API_SamlAuthentication.md) object
Required: No

## See Also
<a name="API_AuthenticationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/AuthenticationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/AuthenticationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/AuthenticationDescription)
