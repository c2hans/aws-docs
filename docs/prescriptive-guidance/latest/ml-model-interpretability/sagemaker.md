---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-model-interpretability/sagemaker.html
---

# Interpretability on AWS
<a name="sagemaker"></a>

You can use Jupyter instances that are managed by Amazon SageMaker to easily install Python modules through Conda and pip.  For information about Python packages for SHAP and integrated gradient-based methods, see the [Resources](resources.md) section.  For smaller jobs and local testing on a SageMaker Jupyter instance, using the methods from these Python packages might be sufficient.  If you are using a SageMaker managed model, SageMaker Clarify provides convenience methods for launching Kernel SHAP on a dedicated instance, and offloading the computation while a model developer continues to work on their Jupyter instance. For more information, see [Create Feature Attribute Baselines and Explainability Reports](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-baselines-reports.html) in the SageMaker documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
