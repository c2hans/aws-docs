---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/restart-node.html
---

# Rebooting a data node in Amazon OpenSearch Service
<a name="restart-node"></a>

**To reboot a data node**

1. Navigate to the OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, choose **Domains**. Choose the name of the domain that you want to work with.

1. After the domain details page opens, navigate to the **Instance health** tab.

1. Under **Data nodes**, select the button next to the node that you want to restart the process on.

1. Select the **Actions** dropdown and choose **Reboot node**.

1. Choose **Confirm** on the modal.

1. To see the status of the action that you initiated, select the name of the node. After the node details page opens, choose the **Events** tab under the name of the node to see a list of events associated with that node.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
