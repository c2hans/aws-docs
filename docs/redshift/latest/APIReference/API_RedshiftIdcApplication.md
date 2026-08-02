---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_RedshiftIdcApplication.html
---

# RedshiftIdcApplication
<a name="API_RedshiftIdcApplication"></a>

Contains properties for the Redshift IDC application.

## Contents
<a name="API_RedshiftIdcApplication_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ApplicationType **
The type of application being created. Valid values are `None` or `Lakehouse`. Use `Lakehouse` to enable Amazon Redshift federated permissions on cluster.
Type: String
Valid Values: `None | Lakehouse`
Required: No

 ** AuthorizedTokenIssuerList.member.N **
The authorized token issuer list for the Amazon Redshift IAM Identity Center application.
Type: Array of [AuthorizedTokenIssuer](API_AuthorizedTokenIssuer.md) objects
Required: No

 ** IamRoleArn **
The ARN for the Amazon Redshift IAM Identity Center application. It has the required permissions to be assumed and invoke the IDC Identity Center API.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** IdcDisplayName **
The display name for the Amazon Redshift IAM Identity Center application. It appears on the console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\w+=,.@-]+`
Required: No

 ** IdcInstanceArn **
The ARN for the IAM Identity Center instance that Redshift integrates with.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** IdcManagedApplicationArn **
The ARN for the Amazon Redshift IAM Identity Center application.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** IdcOnboardStatus **
The onboarding status for the Amazon Redshift IAM Identity Center application.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** IdentityNamespace **
The identity namespace for the Amazon Redshift IAM Identity Center application. It determines which managed application verifies the connection token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[a-zA-Z0-9_+.#@$-]+$`
Required: No

 ** RedshiftIdcApplicationArn **
The ARN for the Redshift application that integrates with IAM Identity Center.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** RedshiftIdcApplicationName **
The name of the Redshift application in IAM Identity Center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: No

 ** ServiceIntegrations.member.N **
A list of service integrations for the Redshift IAM Identity Center application.
Type: Array of [ServiceIntegrationsUnion](API_ServiceIntegrationsUnion.md) objects
Required: No

 ** SsoTagKeys.TagKey.N **
A list of tags keys that Redshift Identity Center applications copy to IAM Identity Center. For each input key, the tag corresponding to the key-value pair is propagated.
Type: Array of strings
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Tags.Tag.N **
A list of tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_RedshiftIdcApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RedshiftIdcApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RedshiftIdcApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RedshiftIdcApplication)
