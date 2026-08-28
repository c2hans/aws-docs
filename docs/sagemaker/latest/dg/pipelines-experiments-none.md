---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-experiments-none.html
---

# Disable Experiments Integration
<a name="pipelines-experiments-none"></a>

**Create a pipeline**

You can disable your pipeline's integration with SageMaker Experiments by setting the `pipeline_experiment_config` parameter to `None` when you define your pipeline. This way, SageMaker AI will not automatically create an experiment, run groups, or individual runs for tracking metrics and artifacts associated with your pipeline executions. The following example sets the pipeline config parameter to `None`.

```
pipeline_name = f"MyPipeline"
pipeline = Pipeline(
    name=pipeline_name,
    parameters=[...],
    pipeline_experiment_config=None,
    steps=[step_train]
)
```

**Pipeline definition file**

This is the same as the preceding default example, without the `PipelineExperimentConfig`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
