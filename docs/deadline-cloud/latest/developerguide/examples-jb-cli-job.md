---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-cli-job.html
---

# Run a bash script on Deadline Cloud
<a name="examples-jb-cli-job"></a>

The [cli\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/cli_job) job bundle submits a multi-line bash script to Deadline Cloud. The script job parameter uses a multi-line edit control, and a data directory job parameter lets you select a directory of data for the script to read from and write to.

Submit the bundle with a data directory:

```
deadline bundle submit job_bundles/cli_job -p DataDir={{~/data_dir}}
```

For a minimal starter that supplements the developer guide farm setup walkthrough, see the [simple\_job](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/simple_job) bundle.
