---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-job-progression.html
---

# Develop a job bundle through four stages on Deadline Cloud
<a name="examples-jb-job-progression"></a>

The [job\_dev\_progression](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_dev_progression) directory contains a sequence of four job bundle development stages. As you add more options and split a workload into smaller parallel pieces, the complexity of the job grows. The four stages start with a single self-contained template and end at a Python package bundled with script entry points and unit tests. The sample is built around Python, but the ideas are not Python-specific.

Submit the first stage to your farm:

```
deadline bundle submit stage_1_self_contained_template
```

You can also run jobs locally for development with the [Open Job Description CLI](https://github.com/OpenJobDescription/openjd-cli):

```
openjd run stage_1_self_contained_template/template.yaml
```

To use a queue environment locally to provide conda packages, pass the `--environment` option:

```
openjd run --environment ../../queue_environments/conda_queue_env_from_console.yaml \
    stage_1_self_contained_template/template.yaml
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
