---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/authorization-for-blueprints.html
---

# Manage blueprint authorization
<a name="authorization-for-blueprints"></a>

You can perform the following procedure to manage the authorization configuration of a blueprint.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and choose the domain’s name from the list. The name is a hyperlink.

1. On the domain's details page, navigate to the **Blueprints** tab.

1. In the **Blueprints** tab, choose the blueprint the authorization configuration of which you'd like to change. The name of the blueprint is a hyperlink.

1. On the bluprint's details page, navigate to the **Authorization** tab.

1. In the Authorization tab, you can use the Add and Remove buttons to add or remove domain units. By adding a domain unit, you're allowing projects that belong to this domain unit to use this blueprint. By removing a domain unit, you're removing the ability to use this blueprint from projects that belong to this domain unit.

   You can use the **Cascade to all child domain units** toggle to apply the authorization setting that you're configuring to all the child domain units of the domain unit that you're adding or removing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
