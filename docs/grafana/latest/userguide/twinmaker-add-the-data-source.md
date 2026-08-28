---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/twinmaker-add-the-data-source.html
---

# Manually adding the AWS IoT TwinMaker data source
<a name="twinmaker-add-the-data-source"></a>

## Prerequisites
<a name="twinmaker-prerequisites"></a>

Before you begin, ensure that you have access to **AWS IoT TwinMaker** from your AWS account.

 To learn how to add permission to your workspace IAM role to access AWS IoT TwinMaker, see [Adding the permission for AWS IoT TwinMaker to your workspace user role](AMG-iot-twinmaker.md#twinmaker-add-permission).

**To add the AWS IoT TwinMaker data source:**

1. Ensure that your user role is admin or editor.

1.  In the Grafana console side menu, hover over the **Configuration** (gear) icon and then choose **Data Sources**.

1. Choose **Add data source**.

1. Choose the **AWS IoT TwinMaker** data source. If necessary, you can start typing **TwinMaker** in the search box to help you find it.

1. This opens the **Connection Details** page. Follow the steps in configuring the [AWS IoT TwinMaker connection details settings](AMG-iot-twinmaker.md#twinmaker-connection-details).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
