---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_AwsEcrContainerImageDetails.html
---

# AwsEcrContainerImageDetails
<a name="API_AwsEcrContainerImageDetails"></a>

The image details of the Amazon ECR container image.

## Contents
<a name="API_AwsEcrContainerImageDetails_Contents"></a>

 ** architecture **   <a name="ECR-Type-AwsEcrContainerImageDetails-architecture"></a>
The architecture of the Amazon ECR container image.
Type: String
Required: No

 ** author **   <a name="ECR-Type-AwsEcrContainerImageDetails-author"></a>
The image author of the Amazon ECR container image.
Type: String
Required: No

 ** imageHash **   <a name="ECR-Type-AwsEcrContainerImageDetails-imageHash"></a>
The image hash of the Amazon ECR container image.
Type: String
Required: No

 ** imageTags **   <a name="ECR-Type-AwsEcrContainerImageDetails-imageTags"></a>
The image tags attached to the Amazon ECR container image.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** inUseCount **   <a name="ECR-Type-AwsEcrContainerImageDetails-inUseCount"></a>
The number of Amazon ECS or Amazon EKS clusters currently running the image.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** lastInUseAt **   <a name="ECR-Type-AwsEcrContainerImageDetails-lastInUseAt"></a>
The most recent date and time a cluster was running the image.
Type: Timestamp
Required: No

 ** platform **   <a name="ECR-Type-AwsEcrContainerImageDetails-platform"></a>
The platform of the Amazon ECR container image.
Type: String
Required: No

 ** pushedAt **   <a name="ECR-Type-AwsEcrContainerImageDetails-pushedAt"></a>
The date and time the Amazon ECR container image was pushed.
Type: Timestamp
Required: No

 ** registry **   <a name="ECR-Type-AwsEcrContainerImageDetails-registry"></a>
The registry the Amazon ECR container image belongs to.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** repositoryName **   <a name="ECR-Type-AwsEcrContainerImageDetails-repositoryName"></a>
The name of the repository the Amazon ECR container image resides in.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: No

## See Also
<a name="API_AwsEcrContainerImageDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/AwsEcrContainerImageDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/AwsEcrContainerImageDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/AwsEcrContainerImageDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
