---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-runtime-env.html
---

# Managing dependencies with runtime\_env
<a name="sagemaker-hyperpod-ray-runtime-env"></a>

Ray `runtime_env` installs pip packages and ships a working directory to the cluster at run time. You add a dependency without rebuilding a container image, which keeps interactive development fast.

## Inject dependencies interactively
<a name="sagemaker-hyperpod-ray-runtime-env-interactive"></a>

Pass `runtime_env` to `ray.init()`. Ray installs the packages and uploads the working directory to the cluster before your code runs.

```
import ray

ray.init(runtime_env={
    "pip": ["pandas==2.2.2", "scikit-learn"],
    "working_dir": "{{./src}}",
})
```

## Inject dependencies for a submitted job
<a name="sagemaker-hyperpod-ray-runtime-env-job"></a>

For a job you submit from the command line, pass the same environment with `--working-dir` and `--runtime-env-json`.

```
ray job submit \
    --address sagemaker_ray://{{my-cluster}}/{{my-namespace}} \
    --working-dir {{./src}} \
    --runtime-env-json '{"pip": ["pandas==2.2.2", "scikit-learn"]}' \
    -- python {{my-script.py}}
```

For the full set of `runtime_env` fields, including conda environments and environment variables, see [Ray runtime environments](https://docs.ray.io/en/latest/ray-core/handling-dependencies.html) in the Ray documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
