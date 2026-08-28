---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html
---

# Configure the application configuration parameters
<a name="app-config-param"></a>

This section allows you to provide the details of your cross-Region failover support using AWS Elastic Disaster Recovery. AWS Resilience Hub will use this information to provide resiliency recommendations.

For more information about application configuration parameters, see [Application configuration parameters](app-config.md).

**To add application configuration parameters (Optional)**

1. To expand the **Application configuration parameters** section, choose the right arrow.

1. Enter the failover account ID in the **Account ID** box. By default, we have pre-populated this field with your account ID that is used for AWS Resilience Hub, which can be changed.

1. Select a failover Region from the **Region** dropdown list.
**Note**
If you want to disable this feature, select "**–**" from the dropdown list.

## Next
<a name="add-tags-next"></a>

 [Add tags](add-tags.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
