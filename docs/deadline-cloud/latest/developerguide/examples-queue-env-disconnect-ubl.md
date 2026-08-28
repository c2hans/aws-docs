---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-queue-env-disconnect-ubl.html
---

# Disconnect Deadline Cloud usage-based licensing with a queue environment
<a name="examples-queue-env-disconnect-ubl"></a>

The [disconnect\_ubl\_queue\_env.yaml](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/disconnect_ubl_queue_env.yaml) queue environment unsets Deadline Cloud usage-based license (UBL) environment variables. Use this queue environment when you want to turn off all connections to Deadline Cloud UBL for your queue and force the use of a custom license server. For more information about bring your own license, see [Connect service-managed fleets to a custom license server](smf-byol.md).

Set the priority of this queue environment to `0` so that it runs before any other queue environments. Otherwise, connections to your custom floating licenses (such as RLM) in other queue environments can be unset accidentally.

**Note**
This queue environment is a sample. Additional UBL environment variables can be added in the future.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
