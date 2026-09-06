---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_EncryptionConfig.html
---

# EncryptionConfig
<a name="API_EncryptionConfig"></a>

The encryption configuration for the cluster.

## Contents
<a name="API_EncryptionConfig_Contents"></a>

 ** provider **   <a name="AmazonEKS-Type-EncryptionConfig-provider"></a>
 AWS Key Management Service (AWS KMS) key. Either the ARN or the alias can be used.
Type: [Provider](API_Provider.md) object
Required: No

 ** resources **   <a name="AmazonEKS-Type-EncryptionConfig-resources"></a>
 *This member has been deprecated.*
Amazon EKS encrypts all Kubernetes API data with envelope encryption by default for clusters running Kubernetes version 1.28 or higher, so this field no longer affects which resources are encrypted.
Specifies the resources to be encrypted. The only supported value is `secrets`.
Type: Array of strings
Required: No

## See Also
<a name="API_EncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/EncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/EncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/EncryptionConfig)
