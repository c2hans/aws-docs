---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-list-conda-packages.html
---

# List available conda packages on Deadline Cloud
<a name="examples-jb-list-conda-packages"></a>

The [list\_available\_conda\_packages](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/list_available_conda_packages) job bundle lists all conda packages available in the `deadline-cloud` channel using `conda search -c deadline-cloud '*'` and prints the list to the job log.

For a list of available packages with their major and minor versions, and recommendations for pinning, see [Conda queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html#conda-queue-environment).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
