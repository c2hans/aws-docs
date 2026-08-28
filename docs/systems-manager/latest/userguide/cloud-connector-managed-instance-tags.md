---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/cloud-connector-managed-instance-tags.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Tags applied to managed instances
<a name="cloud-connector-managed-instance-tags"></a>

When Systems Manager onboards an Azure virtual machine through a Cloud Connector, it automatically applies the following tag to the resulting managed instance. This tag identifies which Cloud Connector was used to onboard the VM and can be used to filter, organize, and apply policies to managed instances based on their originating connector.

| Tag key | Tag value | Description |
| --- | --- | --- |
| CloudConnector | The Cloud Connector ID as a GUID (for example, a1b2c3d4-5678-90ab-cdef-EXAMPLE11111) | Identifies the Systems Manager Cloud Connector that was used to onboard the Azure VM as a managed instance. This tag is applied automatically during the onboarding process. You can use this tag to filter managed instances by connector in the Systems Manager console, AWS CLI, or API operations that support tag-based filtering. |

For example, to list all managed instances onboarded through a specific Cloud Connector, use the following AWS CLI command:

```
aws ssm describe-instance-information \
    --filters "Key=tag:CloudConnector,Values={{CLOUD_CONNECTOR_ID}}"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
