---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_ObjectStorageFederatedIdentityConfig.html
---

# ObjectStorageFederatedIdentityConfig
<a name="API_ObjectStorageFederatedIdentityConfig"></a>

Specifies federated identity parameters that allow AWS DataSync to obtain OpenID Connect token for access to customer object storage. The token allows for temporary, short-term access to the storage. DataSync automatically refreshes the token to assure uninterrupted access to the storage.

**Note**
Federated identity parameters are an alternative to the `AccessKey`/`SecretKey` credentials that are expected to be valid long-term (e.g. at least for the duration of DataSync task execution). Do not specify federated identity and the key parameters for the same object storage location.

## Contents
<a name="API_ObjectStorageFederatedIdentityConfig_Contents"></a>

 ** AwsIamRole **   <a name="DataSync-Type-ObjectStorageFederatedIdentityConfig-AwsIamRole"></a>
Specifies the ARN for an AWS role that allows DataSync to invoke STS GetWebIdentityToken API on behalf of the customer account and to obtain AWS STS JWT (web token).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`
Required: No

 ** ExternalIdentity **   <a name="DataSync-Type-ObjectStorageFederatedIdentityConfig-ExternalIdentity"></a>
Specifies cloud-provider-specific external identity parameters used when exchanging the AWS web token for an OpenID Connect token at the object storage provider.
Type: [ObjectStorageExternalIdentityConfig](API_ObjectStorageExternalIdentityConfig.md) object
Required: No

## See Also
<a name="API_ObjectStorageFederatedIdentityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/ObjectStorageFederatedIdentityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/ObjectStorageFederatedIdentityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/ObjectStorageFederatedIdentityConfig)
