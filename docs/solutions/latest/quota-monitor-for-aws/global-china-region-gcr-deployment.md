---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/global-china-region-gcr-deployment.html
---

# Global China Region (GCR) deployment
<a name="global-china-region-gcr-deployment"></a>

You can deploy the Quota Monitor for AWS solution in AWS China Regions (Beijing and Ningxia) with certain regional limitations and considerations.

Limitations in China Regions:
+ EventBridge does not support cross-region event routing.
+ The Trusted Advisor (TA) stack is not supported in China Regions.

## Deployment strategy for China Regions
<a name="deployment-strategy-for-china-regions"></a>

To accommodate these limitations, follow this deployment strategy for the hybrid/OU model:

1. Hub deployment:
   + Deploy the hub stack separately in `cn-north-1` (Beijing) and `cn-northwest-1` (Ningxia) if you want to monitor services in both Regions.
   + Use the `quota-monitor-hub.template` CloudFormation template for the hub deployment.

1. Spoke deployment:
   + Deploy spoke stacks in the same Region as their corresponding hub.
   + Use the `quota-monitor-spoke.template` CloudFormation template for spoke deployment.

**Important**
All deployments are Region-specific and do not support cross-region monitoring.
The hub and associated spoke stacks must be deployed in the same Region.
To monitor supported services in both China Regions, deploy the solution twice - once in each Region.

 **Deployment models**

1. Account model:
   + Use the `quota-monitor-hub-no-ou.template` CloudFormation template for single account deployments.
   + Use this model when deploying Quota Monitor for individual accounts.
   + Deploy spoke stacks manually in the same Region as the hub using the GCR-specific spoke template.
   + Follow the steps in the [Deploy the solution](deploy-the-solution.md) section for more information.

1. Hybrid/OU model:
   + Use this model when deploying across an AWS Organization or a mix of Organization and individual accounts.
   + In the CloudFormation template, specify the Region where you’re deploying the hub in the Region parameter.
   + If you leave the default value `ALL` for the Regions parameter, the solution will attempt to deploy StackSets in both China Regions. The deployment will succeed in the current hub Region but fail in the other Region. The solution will still function correctly, monitoring services in the current hub Region for all spoke stacks.

**Note**
All monitored accounts must be in the same China Region as the hub.

For detailed steps on deploying hub and spoke stacks, refer to the [Deploy the solution](deploy-the-solution.md) section. Follow those steps for each China Region where you want to deploy, using the GCR-specific templates provided above.

**Note**
Some features available in global Regions might not be supported in China Regions. Always refer to the AWS documentation for the most up-to-date information on service availability in China Regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
