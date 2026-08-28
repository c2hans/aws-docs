---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Image.html
---

# Image
<a name="API_Image"></a>

Contains details about a container image involved in a finding.

## Contents
<a name="API_Image_Contents"></a>

 ** architecture **   <a name="inspector2-Type-Image-architecture"></a>
The architecture of the container image.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** author **   <a name="inspector2-Type-Image-author"></a>
The author of the container image.
Type: String
Required: No

 ** imageDigest **   <a name="inspector2-Type-Image-imageDigest"></a>
The image digest of the container image.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** imageTags **   <a name="inspector2-Type-Image-imageTags"></a>
The image tags attached to the container image.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** inUseCount **   <a name="inspector2-Type-Image-inUseCount"></a>
The number of times the container image is in use.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** lastInUseAt **   <a name="inspector2-Type-Image-lastInUseAt"></a>
The last time the container image was in use.
Type: Timestamp
Required: No

 ** platform **   <a name="inspector2-Type-Image-platform"></a>
The platform of the container image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** pushedAt **   <a name="inspector2-Type-Image-pushedAt"></a>
The date and time the container image was pushed.
Type: Timestamp
Required: No

 ** registry **   <a name="inspector2-Type-Image-registry"></a>
The registry for the container image.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** repositoryName **   <a name="inspector2-Type-Image-repositoryName"></a>
The name of the repository the container image resides in.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_Image_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Image)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Image)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Image)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
