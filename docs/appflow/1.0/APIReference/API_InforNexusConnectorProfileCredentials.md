---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_InforNexusConnectorProfileCredentials.html
---

# InforNexusConnectorProfileCredentials
<a name="API_InforNexusConnectorProfileCredentials"></a>

 The connector-specific profile credentials required by Infor Nexus.

## Contents
<a name="API_InforNexusConnectorProfileCredentials_Contents"></a>

 ** accessKeyId **   <a name="appflow-Type-InforNexusConnectorProfileCredentials-accessKeyId"></a>
 The Access Key portion of the credentials.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** datakey **   <a name="appflow-Type-InforNexusConnectorProfileCredentials-datakey"></a>
 The encryption keys used to encrypt data.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** secretAccessKey **   <a name="appflow-Type-InforNexusConnectorProfileCredentials-secretAccessKey"></a>
 The secret key used to sign requests.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** userId **   <a name="appflow-Type-InforNexusConnectorProfileCredentials-userId"></a>
 The identifier for the user.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

## See Also
<a name="API_InforNexusConnectorProfileCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/InforNexusConnectorProfileCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/InforNexusConnectorProfileCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/InforNexusConnectorProfileCredentials)
