---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation templates specify the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the templates.

## Deployment process overview
<a name="deployment-process-overview"></a>

Before you launch the CloudFormation template, review the architectural and configuration considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 15 minutes.

**Note**
If you have previously deployed this solution, see [Update the solution](update-the-solution.md) for update instructions.

 [Prerequisites](prerequisites.md)
+ Configure a CloudFront distribution
+ Configure an ALB

 [Step 1. Launch the stack](step-1.-launch-the-stack.md)
+ Launch the CloudFormation template into your AWS account.
+ Enter values for the required parameters: **Stack Name** and **Application Access Log Bucket Name**.
+ Review the other template parameters, and adjust if necessary.

 [Step 2. Associate the web ACL with your web application](step-2.-associate-the-web-acl-with-your-web-application.md)
+ Associate your CloudFront web distribution(s) or ALB(s) with the web ACL that this solution generates. You can associate as many distributions or load balancers as you want.

 [Step 3. Configure web access logging](step-3.-configure-web-access-logging.md)
+ Turn on web access logging for your CloudFront web distribution(s) or ALB(s), and send log files to the appropriate Amazon S3 bucket. Save logs in a folder matching the user-defined prefix. If no user-defined prefix is used, save logs to AWSLogs (default log prefix `AWSLogs/`). See the **Application Access Log Bucket Prefix** parameter in [Step 1. Launch the stack](step-1.-launch-the-stack.md) for more information.
