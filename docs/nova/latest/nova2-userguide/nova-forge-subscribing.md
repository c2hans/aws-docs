---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-subscribing.html
---

# Subscribe to Amazon Nova Forge
<a name="nova-forge-subscribing"></a>

To access Amazon Nova Forge features, complete the following steps:

1. Verify administrator access to the AWS account.

1. Navigate to the SageMaker AI console and [ request access to Amazon Nova Forge](nova-forge.md).

1. Wait for the Amazon Nova team to email a confirmation after the subscription request is approved.

1. Tag your SageMaker HyperPod execution role with the `forge-subscription` tag. This tag is required for accessing Amazon Nova Forge features and checkpoints. Add the following tag to your execution role:
   + Key: `forge-subscription`
   + Value: `true`

**Note**
Standard Amazon Nova features remain available without a Forge subscription. Amazon Nova Forge is designed for building custom frontier models with control and flexibility across all model training phases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
