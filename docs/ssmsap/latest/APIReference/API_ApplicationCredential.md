---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ApplicationCredential.html
---

# ApplicationCredential
<a name="API_ApplicationCredential"></a>

The credentials of your SAP application.

## Contents
<a name="API_ApplicationCredential_Contents"></a>

 ** CredentialType **   <a name="ssmsap-Type-ApplicationCredential-CredentialType"></a>
The type of the application credentials.
Type: String
Valid Values: `ADMIN`
Required: Yes

 ** DatabaseName **   <a name="ssmsap-Type-ApplicationCredential-DatabaseName"></a>
The name of the SAP HANA database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** SecretId **   <a name="ssmsap-Type-ApplicationCredential-SecretId"></a>
The secret ID created in AWS Secrets Manager to store the credentials of the SAP application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## See Also
<a name="API_ApplicationCredential_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ApplicationCredential)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ApplicationCredential)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ApplicationCredential)
