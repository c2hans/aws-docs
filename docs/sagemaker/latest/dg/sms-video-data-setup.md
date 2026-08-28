---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-data-setup.html
---

# Input Data Setup
<a name="sms-video-data-setup"></a>

**Note**
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

When you create a video frame labeling job, you need to let Ground Truth know where to look for your input data. You can do this in one of two ways:
+ You can store your input data in Amazon S3 and have Ground Truth automatically detect the input dataset used for your labeling job. See [Set up Automated Video Frame Input Data](sms-video-automated-data-setup.md) to learn more about this option.
+ You can create an input manifest file and sequence files and upload them to Amazon S3. See [Set up Video Frame Input Data Manually](sms-video-manual-data-setup.md) to learn more about this option.

**Topics**
+ [Set up Automated Video Frame Input Data](sms-video-automated-data-setup.md)
+ [Set up Video Frame Input Data Manually](sms-video-manual-data-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
