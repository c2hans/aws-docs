---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-create-wp-stack.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Console Tutorial: Deploying a Tier and Tie WordPress Website
<a name="gui-ex-create-wp-stack"></a>

This section describes how to deploy a high availability (HA) WordPress site into an AMS environment using the AMS console. This set of instructions includes an example of creating the necessary WordPress CodeDeploy-compatible package (e.g. zip) file. The provisioning of the resources follows an order that allows you to tie them together to form "tiers."

**Note**
This deployment walkthrough is designed for use with an AMZN Linux OS.
The essential variable parameters are notated as {{replaceable}}; however, you may want to modify other parameters to suit your situation.

Summary of tasks and required RFCs:

1. Create the infrastructure:

   1. Create a MySQL RDS database cluster

   1. Create a load balancer

   1. Create an Auto scaling group and tie it to the load balancer

   1. Create an S3 bucket for CodeDeploy applications

1. Create a WordPress application bundle (does not require an RFC)

1. Deploy the WordPress application bundle with CodeDeploy:

   1. Create a CodeDeploy application

   1. Create a CodeDeploy deployment group

   1. Upload your WordPress application bundle to the S3 bucket (does not require an RFC)

   1. Deploy the CodeDeploy application

1. Validate the deployment

1. Tear down the deployment

Descriptions for all CT options, including ChangeTypeId can be found in [AMS Change Type Reference](https://docs.aws.amazon.com/managedservices/latest/ctref/index.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
