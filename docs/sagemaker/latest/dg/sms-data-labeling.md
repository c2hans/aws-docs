---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-labeling.html
---

# Enhanced data labeling
<a name="sms-data-labeling"></a>

**Note**
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

Amazon SageMaker Ground Truth manages sending your data objects to workers to be labeled. Labeling each data object is a *task*. Workers complete each task until the entire labeling job is complete. Ground Truth divides the total number of tasks into smaller *batches* that are sent to workers. A new batch is sent to workers when the previous one is finished.

Ground Truth provides two features that help improve the accuracy of your data labels and reduce the total cost of labeling your data:
+ *Annotation consolidation* helps to improve the accuracy of your data object labels. It combines the results of multiple workers' annotation tasks into one high-fidelity label.
+ *Automated data labeling* uses machine learning to label portions of your data automatically without having to send them to human workers.

**Topics**
+ [Control the flow of data objects sent to workers](sms-batching.md)
+ [Annotation consolidation](sms-annotation-consolidation.md)
+ [Automate data labeling](sms-automated-labeling.md)
+ [Chaining labeling jobs](sms-reusing-data.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
