---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageIdentifier.html
---

# ImageIdentifier
<a name="API_ImageIdentifier"></a>

An object with identifying information for an image in an Amazon ECR repository.

## Contents
<a name="API_ImageIdentifier_Contents"></a>

 ** imageDigest **   <a name="ECR-Type-ImageIdentifier-imageDigest"></a>
The `sha256` digest of the image manifest.
Type: String
Required: No

 ** imageTag **   <a name="ECR-Type-ImageIdentifier-imageTag"></a>
The tag used for the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## See Also
<a name="API_ImageIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
