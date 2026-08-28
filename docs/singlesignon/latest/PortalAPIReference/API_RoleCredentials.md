---
source_url: https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_RoleCredentials.html
---

# RoleCredentials
<a name="API_RoleCredentials"></a>

Provides information about the role credentials that are assigned to the user.

## Contents
<a name="API_RoleCredentials_Contents"></a>

 ** accessKeyId **   <a name="singlesignon-Type-RoleCredentials-accessKeyId"></a>
The identifier used for the temporary security credentials. For more information, see [Using Temporary Security Credentials to Request Access to AWS Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the * AWS IAM Identity Center User Guide*.
Type: String
Required: No

 ** expiration **   <a name="singlesignon-Type-RoleCredentials-expiration"></a>
The date on which temporary security credentials expire.
Type: Long
Required: No

 ** secretAccessKey **   <a name="singlesignon-Type-RoleCredentials-secretAccessKey"></a>
The key that is used to sign the request. For more information, see [Using Temporary Security Credentials to Request Access to AWS Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the * AWS IAM Identity Center User Guide*.
Type: String
Required: No

 ** sessionToken **   <a name="singlesignon-Type-RoleCredentials-sessionToken"></a>
The token used for temporary credentials. For more information, see [Using Temporary Security Credentials to Request Access to AWS Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the * AWS IAM Identity Center User Guide User Guide*.
Type: String
Required: No

## See Also
<a name="API_RoleCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-2019-06-10/RoleCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-2019-06-10/RoleCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-2019-06-10/RoleCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
