---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/manufacturing_plans.html
---

# Manufacturing Plans
<a name="manufacturing_plans"></a>

Manufacturing Plans helps you to determine production, transfer, and material requirements for multiple levels of sub-assemblies and components in a bill of material (BOM). Manufacturing Plans uses finished goods forecasts, BOMs, sourcing rules, on-hand inventory, on-order inventory, and lead times to determine net material, transfer, and production requirements. Manufacturing Plans propagates finished goods forecasts through the BOMs and applies sourcing rules to determine production, transfer, and material requirements. You can use this capability if you have in-house manufacturing or use outsourced manufacturers to make finished products or sub-assemblies. You can input plans to your purchasing systems to help create purchase orders for components with suppliers, production planning systems for detailed production scheduling and performance, and labor and production capacity planning systems to manage mid- to long-term capacities.

Material plans (also called component forecasts) can also be shared with your contract manufacturers or with component suppliers through N-Tier Visibility. By sharing or publishing the Material Plans, you can provide better demand signals to upstream suppliers so that they can plan their inventory to meet future demand. By using N-Tier Visibility, suppliers can provide commitments on component forecasts back to you. For information on N-Tier Visibility, see [N-Tier Visibility](partner.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
