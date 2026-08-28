---
source_url: https://docs.aws.amazon.com/machine-learning/latest/dg/training-process.html
---

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Training Process
<a name="training-process"></a>

 To train an ML model, you need to specify the following:
+  Input training datasource
+  Name of the data attribute that contains the target to be predicted
+  Required data transformation instructions
+  Training parameters to control the learning algorithm

 During the training process, Amazon ML automatically selects the correct learning algorithm for you, based on the type of target that you specified in the training datasource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Machine Learning. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query machine-learning` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
