---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html
---

# Copy a customized or shared model to use in a Region
<a name="copy-model"></a>

By default, models are only available in the Region and account in which they were created. Amazon Bedrock provides you the ability to copy some types of models to other Regions. You can copy the following the types of models to other Regions:
+ [Custom models](custom-models.md)
+ [Shared models](share-model.md)

You can copy models to be used in supported Regions. If a model was shared with you from another account, you must first copy it to a Region to be able to use it. To learn about sharing models to and receiving models from other accounts, see [Share a model for another account to use](share-model.md).

**Topics**
+ [Supported Regions and models for model copy](copy-model-support.md)
+ [Fulfill prerequisites to copy models](copy-model-prereq.md)
+ [Copy a model to a Region](copy-model-copy.md)
+ [View information about model copy jobs](copy-model-job-view.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
