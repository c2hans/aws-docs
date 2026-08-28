---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-provider-managed-instances-best-practices.html
---

# Best practices for updating capacity providers for Amazon ECS Managed Instances
<a name="capacity-provider-managed-instances-best-practices"></a>

For the highest level of safety and rollback support, we recommend treating capacity providers as immutable resources. When you need to update a capacity provider configuration, follow this recommended workflow:

1. **Create a new capacity provider** with your updated configuration instead of modifying the existing one.

1. **Update each service** to use the new capacity provider and allow the deployments to complete.

1. **Delete the old capacity provider** after confirming the new configuration works as expected.

This approach provides several benefits:
+ **Controlled rollout** - You can update services one at a time and monitor the impact.
+ **Easy rollback** - If issues occur, you can quickly revert services to use the previous capacity provider.
+ **Reduced blast radius** - Problems with the new configuration don't immediately affect all workloads.

**Note**
If you're using CloudFormation, consider keeping the old capacity provider until a later deployment to preserve the ability to roll back your stack changes.

While you can update capacity providers in place, this approach creates a larger uncontrolled blast radius. In-place updates apply new settings to all new capacity provisioned going forward, but don't trigger service deployments. This means you might not discover configuration issues until much later when your services need to scale.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
