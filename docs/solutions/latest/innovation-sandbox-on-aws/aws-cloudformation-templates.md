---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/aws-cloudformation-templates.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-templates"></a>

This solution uses AWS CloudFormation to automate the deployment of Innovation Sandbox on AWS in the AWS Cloud. It includes the following CloudFormation templates, which you can download before deployment.

## AccountPool stack
<a name="account-pool-stack"></a>

 [![View Template](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-AccountPool.template)

 **InnovationSandbox-AccountPool.template** - Use this template to deploy the resources required to set up Organizational Units (OUs), Service Control Policies (SCPs), roles, and Regions.

## IDC stack
<a name="idc-stack"></a>

 [![View Template](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-IDC.template)

 **InnovationSandbox-IDC.template** - Use this template to deploy the resources required to set up IDC, including mappings, roles, policies, and other configuration.

## Data stack
<a name="data-stack"></a>

 [![View Template](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-Data.template)

 **InnovationSandbox-Data.template** - Use this template to deploy the data resources required for the application. These resources include the Amazon DynamoDB table that stores the solution’s global configuration settings. You manage these settings on the **Settings** page of the web UI after deployment. This stack also contains the AWS AppConfig hosted configurations for the solution’s account cleanup process. These include the AWS Nuke configuration and the cleanup validator exclusion configuration.

## Compute stack
<a name="compute-stack"></a>

 [![View Template](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-Compute.template)

 **InnovationSandbox-Compute.template** - Use this template to deploy the compute resources required for the ISB application. This stack contains all of the stateless (compute) resources used by the solution, including the web application and the event infrastructure.

**Important**
The **SandboxAccount** stack is automatically configured as a service-managed StackSet resource in the **AccountPool** stack using the **AccountPool OU** as deployment target. The stack contains a single **Spoke** role that is assumed into by compute resources in the compute stack to run the account cleanup job.

These AWS CloudFormation templates deploy the Innovation Sandbox on AWS solution in the AWS Cloud.
