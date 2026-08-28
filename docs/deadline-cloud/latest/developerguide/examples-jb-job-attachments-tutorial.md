---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-job-attachments-tutorial.html
---

# Job attachment tutorial bundles for Deadline Cloud
<a name="examples-jb-job-attachments-tutorial"></a>

The [job\_attachments\_devguide](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_attachments_devguide) and [job\_attachments\_devguide\_output](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_attachments_devguide_output) job bundles supplement the [Use job attachments to share files](build-job-attachments.md) section in the developer guide. The bundles demonstrate how data flow metadata on path job parameters and the job bundle `asset_references.yaml` file work together to describe the files a job needs as input and produces as output.

When a job bundle specifies this metadata, it can work with either job attachments or shared file systems without changes to the template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
