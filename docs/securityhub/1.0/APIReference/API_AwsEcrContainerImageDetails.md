---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcrContainerImageDetails.html
---

# AwsEcrContainerImageDetails
<a name="API_AwsEcrContainerImageDetails"></a>

Information about an Amazon ECR image.

## Contents
<a name="API_AwsEcrContainerImageDetails_Contents"></a>

 ** Architecture **   <a name="securityhub-Type-AwsEcrContainerImageDetails-Architecture"></a>
The architecture of the image. Valid values are as follows:
+  `arm64`
+  `i386`
+  `x86_64`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ImageDigest **   <a name="securityhub-Type-AwsEcrContainerImageDetails-ImageDigest"></a>
The sha256 digest of the image manifest.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ImagePublishedAt **   <a name="securityhub-Type-AwsEcrContainerImageDetails-ImagePublishedAt"></a>
The date and time when the image was pushed to the repository.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** ImageTags **   <a name="securityhub-Type-AwsEcrContainerImageDetails-ImageTags"></a>
The list of tags that are associated with the image.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** RegistryId **   <a name="securityhub-Type-AwsEcrContainerImageDetails-RegistryId"></a>
The AWS account identifier that is associated with the registry that the image belongs to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RepositoryName **   <a name="securityhub-Type-AwsEcrContainerImageDetails-RepositoryName"></a>
The name of the repository that the image belongs to.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcrContainerImageDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcrContainerImageDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcrContainerImageDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcrContainerImageDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
