---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RedshiftCredentialConfiguration.html
---

# RedshiftCredentialConfiguration
<a name="API_RedshiftCredentialConfiguration"></a>

The details of the credentials required to access an Amazon Redshift cluster.

## Contents
<a name="API_RedshiftCredentialConfiguration_Contents"></a>

 ** secretManagerArn **   <a name="datazone-Type-RedshiftCredentialConfiguration-secretManagerArn"></a>
The ARN of a secret manager for an Amazon Redshift cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[^:]*:secretsmanager:[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]:\d{12}:secret:.*`
Required: Yes

## See Also
<a name="API_RedshiftCredentialConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RedshiftCredentialConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RedshiftCredentialConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RedshiftCredentialConfiguration)
