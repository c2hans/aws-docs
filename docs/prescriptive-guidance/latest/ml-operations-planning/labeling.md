---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-operations-planning/labeling.html
---

# Labeling
<a name="labeling"></a>

## Provide clear labeling instructions
<a name="instructions"></a>

A dataset might include ambiguous samples that result in inconsistent labeling across the entire dataset. For example, consider the task of labeling images that contain a dog. Some samples might contain only a glimpse of the animal. Should those be marked with a positive or negative label? This type of problem might be solved by providing clear and objective instructions to labelers.

## Use majority voting
<a name="use-majority-voting"></a>

Now consider the issue of labeling a speech-to-text dataset that contains noisy audio with words that are phonetically similar or identical to others, such as *know* and *go*, *shoe* and *two*, *cry* and *high*, or *right* and *write*. In this case, labelers might label these samples inconsistently.

To maintain a high degree of correctness in labeling, a common approach is to use majority voting, in which the same data sample is given to multiple workers and their results are aggregated. This method and its more sophisticated variations are described in the [blog post](https://aws.amazon.com/blogs/machine-learning/use-the-wisdom-of-crowds-with-amazon-sagemaker-ground-truth-to-annotate-data-more-accurately/) [Use the wisdom of crowds with Amazon SageMaker Ground Truth to annotate data more accurately](https://aws.amazon.com/blogs/machine-learning/use-the-wisdom-of-crowds-with-amazon-sagemaker-ground-truth-to-annotate-data-more-accurately/) on the AWS Machine Learning blog.
