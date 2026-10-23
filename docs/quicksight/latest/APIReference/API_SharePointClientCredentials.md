---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SharePointClientCredentials.html
---

# SharePointClientCredentials
<a name="API_SharePointClientCredentials"></a>

The client credentials for connecting to a Microsoft SharePoint data source using two-legged OAuth (2LO) certificate-based authentication. SharePoint connections access documents stored in SharePoint sites and libraries. The tenant ID and client ID are supplied through `SharePointParameters`.

## Contents
<a name="API_SharePointClientCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CertThumbprint **   <a name="QS-Type-SharePointClientCredentials-CertThumbprint"></a>
The thumbprint of the certificate used for two-legged OAuth (2LO) authentication to SharePoint. This field is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** KmsKeyArn **   <a name="QS-Type-SharePointClientCredentials-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used to encrypt the SharePoint certificate credentials. This field is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+`
Required: Yes

## See Also
<a name="API_SharePointClientCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SharePointClientCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SharePointClientCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SharePointClientCredentials)
