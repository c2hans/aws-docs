---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-debug-training-jobs.html
---

# Debugging training jobs using Amazon SageMaker Debugger
<a name="debugger-debug-training-jobs"></a>

**Note**
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md).

To prepare your training script and run training jobs with SageMaker Debugger to debug model training progress, you follow the typical two-step process: modify your training script using the `sagemaker-debugger` Python SDK, and construct a SageMaker AI ModelTrainer using the SageMaker Python SDK. Go through the following topics to learn how to use SageMaker Debugger's debugging functionality.

**Topics**
+ [Adapting your training script to register a hook](debugger-modify-script.md)
+ [Launch training jobs with Debugger using the SageMaker Python SDK](debugger-configuration-for-debugging.md)
+ [SageMaker Debugger interactive report for XGBoost](debugger-report-xgboost.md)
+ [Action on Amazon SageMaker Debugger rules](debugger-action-on-rules.md)
+ [Visualize Amazon SageMaker Debugger output tensors in TensorBoard](debugger-enable-tensorboard-summaries.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
