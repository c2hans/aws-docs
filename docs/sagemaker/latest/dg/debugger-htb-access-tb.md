---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-htb-access-tb.html
---

# Accessing the TensorBoard application on SageMaker AI
<a name="debugger-htb-access-tb"></a>

You can access TensorBoard by two methods: programmatically using the `sagemaker.interactive_apps.tensorboard` module that generates an unsigned or a presigned URL, or using the TensorBoard landing page in the SageMaker AI console. After you open TensorBoard, SageMaker AI runs the TensorBoard plugin and automatically finds all training job output data in a TensorBoard-compatible file format.

**Topics**
+ [Open TensorBoard using the `sagemaker.interactive_apps.tensorboard` module](debugger-htb-access-tb-url.md)
+ [Open TensorBoard using the `get_app_url` function as an `ModelTrainer` class method](debugger-htb-access-tb-get-app-url-estimator-method.md)
+ [Open TensorBoard through the SageMaker AI console](debugger-htb-access-tb-console.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
