---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ImageDetails.html
---

# ImageDetails
<a name="API_ImageDetails"></a>

Information about the container image used for a task.

## Contents
<a name="API_ImageDetails_Contents"></a>

 ** image **   <a name="omics-Type-ImageDetails-image"></a>
The URI of the container image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** imageDigest **   <a name="omics-Type-ImageDetails-imageDigest"></a>
The container image digest. If the image URI was transformed, this will be the digest of the container image referenced by the transformed URI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `sha[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** sourceImage **   <a name="omics-Type-ImageDetails-sourceImage"></a>
URI of the source registry. If the URI is from a third-party registry, AWS HealthOmics transforms the URI to the corresponding ECR path, using the pull-through cache mapping rules.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_ImageDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ImageDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ImageDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ImageDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
