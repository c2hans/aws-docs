---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ActiveDirectoryConfig.html
---

# ActiveDirectoryConfig
<a name="API_ActiveDirectoryConfig"></a>

Information about the Active Directory config.

## Contents
<a name="API_ActiveDirectoryConfig_Contents"></a>

 ** DomainName **   <a name="WorkSpaces-Type-ActiveDirectoryConfig-DomainName"></a>
The name of the domain.
Type: String
Pattern: `^([a-zA-Z0-9]+[.-])+([a-zA-Z0-9])+$`
Required: Yes

 ** ServiceAccountSecretArn **   <a name="WorkSpaces-Type-ActiveDirectoryConfig-ServiceAccountSecretArn"></a>
Indicates the secret ARN on the service account.
Type: String
Pattern: `^arn:aws[a-z-]{0,7}:secretsmanager:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:secret:[A-Za-z0-9][A-za-z0-9_/.-]{8,519}$`
Required: Yes

## See Also
<a name="API_ActiveDirectoryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ActiveDirectoryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ActiveDirectoryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ActiveDirectoryConfig)
