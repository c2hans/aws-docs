---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/use-debugger-built-in-rules.html
---

# How to configure Debugger built-in rules
<a name="use-debugger-built-in-rules"></a>

**Note**
Amazon SageMaker Debugger is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md).

In the following topics, you'll learn how to use the SageMaker Debugger built-in rules. Amazon SageMaker Debugger's built-in rules analyze tensors emitted during the training of a model. SageMaker AI Debugger offers the `Rule` API operation that monitors training job progress and errors for the success of training your model. For example, the rules can detect whether gradients are getting too large or too small, whether a model is overfitting or overtraining, and whether a training job does not decrease loss function and improve. To see a full list of available built-in rules, see [List of Debugger built-in rules](debugger-built-in-rules.md).

**Topics**
+ [Use Debugger built-in rules with the default parameter settings](debugger-built-in-rules-configuration.md)
+ [Use Debugger built-in rules with custom parameter values](debugger-built-in-rules-configuration-param-change.md)
+ [Example notebooks and code samples to configure Debugger rules](debugger-built-in-rules-example.md)

For an advanced configuration of the Debugger built-in rules using the `CreateTrainingJob` API, see [Configure Debugger using SageMaker API](debugger-createtrainingjob-api.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
