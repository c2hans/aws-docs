---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/step-1.-launch-the-stack.html
---

# Step 1. Launch the stack
<a name="step-1.-launch-the-stack"></a>

This automated AWS CloudFormation template deploys the solution on the AWS Cloud.

1. Sign into [AWS Management Console](https://aws.amazon.com/console) and select the **Launch Solution** to launch `waf-automation-on-aws.template` CloudFormation template.

    [https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=WAFSecurityAutomations&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fsecurity-automations-for-aws-waf%2Flatest%2Faws-waf-security-automations.template&redirectId=ImplementationGuide](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=WAFSecurityAutomations&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fsecurity-automations-for-aws-waf%2Flatest%2Faws-waf-security-automations.template&redirectId=ImplementationGuide)

1. The template launches in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the Region selector in the console navigation bar. If you choose `CloudFront` as your endpoint, you must deploy the solution in the US East (N. Virginia) (`us-east-1`) Region.
**Note**
Depending on the input parameters values you define, this solution requires different resources. These resources are currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where these services are available. For more information, refer to [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions).

1. On the **Specify template** page, verify that you selected the correct template and choose **Next**.

1. On the **Specify stack details** page, assign a name to your AWS WAF configuration in the **Stack name** field. This is also the name of the web ACL that the template creates.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. To opt out of a particular feature, choose `none` or `no` as applicable. This solution uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/step-1.-launch-the-stack.html)

1. Choose **Next.**

1. On the **Configure stack options** page, you can specify tags (key-value pairs) for resources in your stack and set additional options. Choose **Next**.

1. On the **Review and create** page, review and confirm the settings. Select the boxes acknowledging that the template will create IAM resources and any additional capabilities required.

1. Choose **Submit** to deploy the stack.

   View the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a status of CREATE\_COMPLETE in approximately 15 minutes.
**Note**
In addition to the `Log Parser` and `IP Lists Parser` AWS Lambda functions, this solution includes the `helper` and `custom-resource` Lambda functions, which run only during initial configuration or when resources are updated or deleted.
When using this solution, you will see all functions in the AWS Lambda console, but only the three primary solution functions are regularly active. Don’t delete the other two functions; they are necessary to manage associated resources.

To see details about the stack resources, choose the **Outputs** tab. This includes the **BadBotHoneypotEndpoint** value. Remember this value because you will be used it in [Embed the Honeypot link in your web application](embed-the-honeypot-link-in-your-web-application-optional.md).
