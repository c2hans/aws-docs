---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-experimentation-archiving-or-deleting.html
---

# Cleaning up an experiment
<a name="appconfig-experimentation-archiving-or-deleting"></a>

After an experiment completes, you can archive or permanently delete the experiment definition.
+ **Archive** – The experiment definition is hidden from the active list but can be restored later. The experiment feature flag remains deployed and continues serving its current configuration. To stop serving the flag, disable it separately in your feature flag configuration.
+ **Delete permanently** – The experiment definition and all associated run history are permanently deleted. This action cannot be undone.

**To archive or delete an experiment**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Experiments**, and then choose an experiment. The experiment dashboard opens.

1. Choose **Actions**, and then choose **Delete experiment definition**.

1. In the **Choose an action** section, choose either **Archive** or **Delete permanently**.

1. In the **Confirmation** section, type **confirm**.

1. Choose the **Archive** or **Delete** button.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
