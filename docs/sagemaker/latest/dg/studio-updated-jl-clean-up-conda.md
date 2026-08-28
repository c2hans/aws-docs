---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-clean-up-conda.html
---

# Clean up a conda environment
<a name="studio-updated-jl-clean-up-conda"></a>

Cleaning up conda environments that you’re not using can help free up disk space and improve performance. Use the following template to clean up a conda environment:

```
# list your environments to select an environment to clean
conda info --envs # or conda info -e

# once you've selected your environment to purge
conda remove --name test-env --all

# run conda environment list to ensure the target environment is purged
conda info --envs # or conda info -e
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
