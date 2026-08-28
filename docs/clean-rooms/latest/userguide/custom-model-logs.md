---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/custom-model-logs.html
---

# Receiving model logs and metrics
<a name="custom-model-logs"></a>

To receive logs and metrics from custom model training or inference, members must have [created an ML Configuration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-custom-ml-collaboration.html) with a valid role that provides the necessary CloudWatch permissions (see [Create a service role for custom ML modeling - ML Configuration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-roles.html#ml-roles-custom-configure)).

**System metric**

System metrics for both training and inference, such as CPU and memory utilization, are published to all members in the collaboration with valid ML Configurations. These metrics can be viewed as the job progresses via CloudWatch Metrics in the `/aws/cleanroomsml/TrainedModels` or `/aws/cleanroomsml/TrainedModelInferenceJobs` namespaces, respectively.

**Model logs**

Access to the model logs is provided by the privacy configuration policy of each configured model algorithm. The model author sets the privacy configuration policy when associating a configured model algorithm (either via the console or the `CreateConfiguredModelAlgorithmAssociation` API) to a collaboration. Setting the privacy configuration policy controls which members can receive the model logs.

Additionally, the model author can set a filter pattern in the privacy configuration policy to filter log events. All logs that a model container sends to `stdout` or `stderr` and that match the filter pattern (if set), are sent to Amazon CloudWatch Logs. Model logs are available in CloudWatch log groups `/aws/cleanroomsml/TrainedModels` or `/aws/cleanroomsml/TrainedModelInferenceJobs`, respectively.

**Custom defined metrics**

When you configure a model algorithm (either via the console or the `CreateConfiguredModelAlgorithm` API), the model author can provide specific metric names and regex statements to search for in the output logs. These can be viewed as the job progresses via CloudWatch Metrics in the `/aws/cleanroomsml/TrainedModels` namespace. When associating a configured model algorithm, the model author can set an optional noise level in the metrics privacy configuration to avoid outputting raw data while still providing visibility into custom metric trends. If a noise level is set, the metrics are published at the end of the job rather than in real time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
