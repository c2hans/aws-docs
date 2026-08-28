---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/monitoring.html
---

# Monitoring
<a name="monitoring"></a>

 The model monitoring system must capture data, compare that data to the training set, define rules to detect issues, and send alerts. This process repeats on a defined schedule, when initiated by an event, or when initiated by human intervention. The issues detected in the monitoring phase include: data quality, model quality, bias drift, and feature attribution drift.

![Chart displaying model monitoring main components](http://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/images/key-components-monitor-phase.png)

 Figure 17 lists key components of monitoring, including:
+  **Model explainability:** Monitoring system uses *explainability* to evaluate the soundness of the model and if the predictions can be trusted.
+  **Detect drift:** Monitoring system detects data and concept drifts, initiates an alert, and sends it to the alarm manager system. Data drift is significant changes to the data distribution compared to the data used for training. Concept drift is when the properties of the target variables change. Data drift can result in model performance degradation.
+  **Model update pipeline:** If the alarm manager identifies violations, it launches the model update pipeline for a re-train. This can be seen in Figure 18. The *Data prepare*, *CI/CD/CT*, and *Feature* pipelines will also be active during this process.

![ML lifecycle with model update, retrain, and batch or real-time inference pipelines](http://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/images/ml-lifecycle-model-update-inference-pipelines.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
