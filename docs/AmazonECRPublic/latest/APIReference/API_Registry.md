---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Registry.html
---

# Registry
<a name="API_Registry"></a>

The details of a public registry.

## Contents
<a name="API_Registry_Contents"></a>

 ** aliases **   <a name="ecrpublic-Type-Registry-aliases"></a>
An array of objects that represents the aliases for a public registry.
Type: Array of [RegistryAlias](API_RegistryAlias.md) objects
Required: Yes

 ** registryArn **   <a name="ecrpublic-Type-Registry-registryArn"></a>
The Amazon Resource Name (ARN) of the public registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** registryId **   <a name="ecrpublic-Type-Registry-registryId"></a>
The AWS account ID that's associated with the registry. If you do not specify a registry, the default public registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** registryUri **   <a name="ecrpublic-Type-Registry-registryUri"></a>
The URI of a public registry. The URI contains a universal prefix and the registry alias.
Type: String
Required: Yes

 ** verified **   <a name="ecrpublic-Type-Registry-verified"></a>
Indicates whether the account is a verified AWS Marketplace vendor. If an account is verified, each public repository receives a verified account badge on the Amazon ECR Public Gallery.
Type: Boolean
Required: Yes

## See Also
<a name="API_Registry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/Registry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/Registry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/Registry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
