---
source_url: https://docs.aws.amazon.com/lookout-for-equipment/latest/userguide/create-model.html
---

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/).

# Training your model
<a name="create-model"></a>

**Note**
You can also train your model [with the SDK](SDK-examples.md#create-model-sdk).

You've ingested your dataset, and you've reviewed any issues with the job, the files, or the sensors. You've also decided which sensors are providing the data that will be used to train your model. Now it's time to move forward with creating the model.

First, you'll specify the details of your model, such as its name, encryption settings, and tags.

Then, you'll configure your input data. During that process, you'll make decisions about the balance between your training dataset and your evaluation dataset, and whether or not to use data labels.

**Topics**
+ [Specifying model details](specifying-model-details.md)
+ [Configuring your input data](configuring-input-data.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lookout for Equipment. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lookout-for-equipment` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
