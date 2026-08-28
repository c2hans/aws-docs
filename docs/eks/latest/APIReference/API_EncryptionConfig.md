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
Specifies the resources to be encrypted. The only supported value is `secrets`.
Type: Array of strings
Required: No

## See Also
<a name="API_EncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/EncryptionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/EncryptionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/EncryptionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
