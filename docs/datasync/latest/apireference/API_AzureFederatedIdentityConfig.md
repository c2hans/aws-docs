---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_AzureFederatedIdentityConfig.html
---

# AzureFederatedIdentityConfig
<a name="API_AzureFederatedIdentityConfig"></a>

Specifies federated identity parameters that allow AWS DataSync to obtain an OpenID Connect token for access to customer Azure Blob Storage. The token allows for temporary, short-term access to the storage. DataSync automatically refreshes the token to assure uninterrupted access to the storage.

**Note**
Federated identity parameters are an alternative to the `SasConfiguration` credentials that are expected to be valid long-term (e.g. at least for the duration of DataSync task execution). Do not specify federated identity and the SAS configuration for the same Azure Blob location.

## Contents
<a name="API_AzureFederatedIdentityConfig_Contents"></a>

 ** AwsIamRole **   <a name="DataSync-Type-AzureFederatedIdentityConfig-AwsIamRole"></a>
Specifies the ARN for an AWS role that allows DataSync to invoke STS GetWebIdentityToken API on behalf of the customer account and to obtain AWS STS JWT (web token).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`
Required: No

 ** AzureOidc **   <a name="DataSync-Type-AzureFederatedIdentityConfig-AzureOidc"></a>
External identity parameters for Azure Blob Storage.
Type: [AzureOidcConfig](API_AzureOidcConfig.md) object
Required: No

## See Also
<a name="API_AzureFederatedIdentityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/AzureFederatedIdentityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/AzureFederatedIdentityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/AzureFederatedIdentityConfig)
