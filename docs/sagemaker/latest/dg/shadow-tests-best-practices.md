---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests-best-practices.html
---

# Best practices
<a name="shadow-tests-best-practices"></a>

 When creating an inference experiment, keep the following information in mind:
+  **Traffic sampling percentage** – Sampling 100 percent of the inference requests lets you validate that your shadow variant can handle production traffic when promoted. You may start off with a lower traffic sampling percentage and dial up as you gain confidence in your variant, but it is best practice to ensure that you’ve increased the traffic to 100 percent prior to promotion.
+  **Instance type** – Unless you are using shadow variants to evaluate alternate instance types or sizes, we recommend that you use the same instance type, size, and count so that you can be certain that your shadow variant can handle the volume of inference requests after you promote it.
+  **Auto scaling** – To ensure that your shadow variant can respond to spikes in the number of inference requests or changes in inference requests patterns, we highly recommend that you configure autoscaling on your shadow variants. To learn how to configure autoscaling, see [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md). If you have configured autoscaling, you can also validate changes to autoscaling policies without causing impact to users.
+  **Metrics monitoring** – After you initiate a shadow experiment and have sufficient invocations, monitor the metrics dashboard to ensure that the metrics such as latency and error rate are within acceptable bounds. This helps you catch misconfigurations early and take corrective action. For information about how to monitor the metrics of an in-progress inference experiment, see [How to view, monitor, and edit shadow tests](shadow-tests-view-monitor-edit.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
