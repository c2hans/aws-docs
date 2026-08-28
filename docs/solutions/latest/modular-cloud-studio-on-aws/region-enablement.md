---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/region-enablement.html
---

# Region enablement
<a name="region-enablement"></a>

This section is optional and only required if you want to set up a multi-Region deployment. The solution initially deploys in a single hub Region. All additional AWS Regions enabled through this workflow become spoke Regions that can connect back to the hub Region for centralized management.

## Enable a Region
<a name="enable-a-region"></a>

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **AWS Regions** from the left navigation pane.

1. Choose **Add Region** in the top right corner.

1. Choose the spoke Region that you want to enable from the dropdown menu.

1. Choose **Enable**.

1. The Region appears in **AWS Regions Enabled** with an `ENABLING IN PROGRESS` status.

Enabling the spoke Region takes approximately 5 minutes. After the process completes, the Region status changes to `ENABLED`.

**Note**
Spoke Regions inherit the same tags as the main Solution stack.

After enabling a spoke Region, you can deploy modules to it by following the detailed steps in [Module enablement](module-enablement.md) and choosing the spoke Region during module deployment.

The Enable Region API does the following:

1. Checks if the Region exists in the [Regions DynamoDB table](dynamodb-tables.md#regions-table).

1. Updates Region status to `ENABLING IN PROGRESS` in the [Regions DynamoDB table](dynamodb-tables.md#regions-table).

1. Provisions the spoke Region infrastructure Service Catalog product.

1. If the previous step is successful, updates the Region `provisioned_product_id` attribute and status to `ENABLED` in the [Regions DynamoDB table](dynamodb-tables.md#regions-table). Otherwise, sets the status to `ENABLE FAILED`.

## Disable a Region
<a name="disable-a-region"></a>

### Prerequisites
<a name="prerequisites"></a>

Before disabling a spoke Region, you must first disable all modules deployed in that Region. The system will prevent Region disabling if any modules are still enabled.

To disable modules, see [Disable a module](module-enablement.md#disable-a-module) for detailed instructions on how to disable each module in the Region.

### Steps to disable a Region
<a name="steps-to-disable-a-region"></a>

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **AWS Regions** from the left navigation pane.

1. Choose an enabled spoke Region to disable, and choose **Disable Region**.

1. Choose **Confirm**.

1. The Region appears in **AWS Regions Enabled** with a `DISABLING IN PROGRESS` status.

Disabling the spoke Region takes approximately 5 minutes. After the process completes, the Region becomes available for re-enablement if needed.

The Disable Region API does the following:

1. Checks if the Region exists in the [Regions DynamoDB table](dynamodb-tables.md#regions-table).

1. Checks if there are modules enabled in the Region in the [Enabled Modules DynamoDB table](dynamodb-tables.md#enabled-modules). If so, an error is thrown.

1. Updates Region status to `DISABLING IN PROGRESS` in the [Regions DynamoDB table](dynamodb-tables.md#regions-table).

1. Terminates the provisioned Service Catalog product.

1. If the previous step is successful, updates the Region `provisioned_product_id` attribute to be empty and status to `DISABLED` in the [Regions DynamoDB table](dynamodb-tables.md#regions-table). Otherwise, sets the status to `DISABLE FAILED`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
