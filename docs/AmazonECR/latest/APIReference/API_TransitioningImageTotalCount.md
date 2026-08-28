---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_TransitioningImageTotalCount.html
---

# TransitioningImageTotalCount
<a name="API_TransitioningImageTotalCount"></a>

The total count of images transitioning to a storage class.

## Contents
<a name="API_TransitioningImageTotalCount_Contents"></a>

 ** imageTotalCount **   <a name="ECR-Type-TransitioningImageTotalCount-imageTotalCount"></a>
The total number of images transitioning to the storage class.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** targetStorageClass **   <a name="ECR-Type-TransitioningImageTotalCount-targetStorageClass"></a>
The target storage class.
Type: String
Valid Values: `ARCHIVE`
Required: No

## See Also
<a name="API_TransitioningImageTotalCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/TransitioningImageTotalCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/TransitioningImageTotalCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/TransitioningImageTotalCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
