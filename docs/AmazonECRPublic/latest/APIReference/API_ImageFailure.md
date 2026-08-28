---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_ImageFailure.html
---

# ImageFailure
<a name="API_ImageFailure"></a>

An object that represents an Amazon ECR image failure.

## Contents
<a name="API_ImageFailure_Contents"></a>

 ** failureCode **   <a name="ecrpublic-Type-ImageFailure-failureCode"></a>
The code that's associated with the failure.
Type: String
Valid Values: `InvalidImageDigest | InvalidImageTag | ImageTagDoesNotMatchDigest | ImageNotFound | MissingDigestAndTag | ImageReferencedByManifestList | KmsError`
Required: No

 ** failureReason **   <a name="ecrpublic-Type-ImageFailure-failureReason"></a>
The reason for the failure.
Type: String
Required: No

 ** imageId **   <a name="ecrpublic-Type-ImageFailure-imageId"></a>
The image ID that's associated with the failure.
Type: [ImageIdentifier](API_ImageIdentifier.md) object
Required: No

## See Also
<a name="API_ImageFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/ImageFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/ImageFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/ImageFailure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
