---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/launch-the-stack.html
---

# Launch the stack (default, CloudFront \+ S3 hosted web console)
<a name="launch-the-stack"></a>

Follow these steps to deploy the Distributed Load Testing on AWS solution into your account. This automated AWS CloudFormation template deploys Distributed Load Testing on AWS.

1. Sign in to the AWS Management Console and choose the button to launch the CloudFormation template.

    [![Launch solution with the CloudFront + S3 default template](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/launch-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template&redirectId=ImplementationGuide)

   Alternatively, you can [download the template](https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template) as a starting point for your own implementation.

1. The template is launched in the US East (N. Virginia) Region by default. To launch this solution in a different AWS Region, use the Region selector in the console navigation bar.
**Note**
This solution uses Amazon Cognito, which is currently available in specific AWS Regions only. Therefore, you must launch this solution in an AWS Region where Amazon Cognito is available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Administrator Name</b> </td><td> <i>&lt;Requires input&gt;</i> </td><td>User name for the initial solution administrator.</td></tr>
  <tr><td> <b>Administrator Email</b> </td><td> {{ <i>&lt;Requires input&gt;</i> }} </td><td>Email address of the administrator user. After launch, an email will be sent to this address with console login instructions.</td></tr>
  <tr><td> <b>Existing VPC ID</b> </td><td>&lt;Optional input&gt;</td><td>If you have a VPC that you want to use and is already created, enter the ID of an existing VPC in the same Region where the stack was deployed. For example, vpc-1a2b3c4d5e6f.</td></tr>
  <tr><td> <b>First existing subnet</b> </td><td>&lt;Optional input&gt;</td><td>The ID of the first subnet within your existing VPC. This subnet needs a route to the internet to pull the container image for running tests. For example, subnet-7h8i9j0k.</td></tr>
  <tr><td> <b>Second existing subnet</b> </td><td>&lt;Optional input&gt;</td><td>The ID of the second subnet within the existing VPC. This subnet needs a route to the internet to pull the container image for running tests. For example, subnet-1x2y3z.</td></tr>
  <tr><td> <b>Provide valid CIDR block for the solution to create VPC</b> </td><td>192.168.0.0/16</td><td>You may leave this parameter blank if you are using existing VPC</td></tr>
  <tr><td> <b>Provide valid CIDR block for subnet A for the solution to create VPC</b> </td><td>192.168.0.0/20</td><td>CIDR block for subnet A of the AWS Fargate VPC</td></tr>
  <tr><td> <b>Provide valid CIDR block for subnet B for the solution to create VPC</b> </td><td>192.168.16.0/20</td><td>CIDR block for subnet B of the AWS Fargate VPC</td></tr>
  <tr><td> <b>Provide CIDR block for allowing outbound traffic of Fargate tasks</b> </td><td>0.0.0.0/0</td><td>CIDR block that restricts Amazon ECS container outbound access.</td></tr>
  <tr><td> <b>Auto-update Container Image</b> </td><td> <code>No</code> </td><td>Automatically use the most up to date and secure image up until the next minor release. Selecting <code>No</code> will pull the image as originally released, without any security updates.</td></tr>
  <tr><td> <b>Deploy Optional MCP Server</b> </td><td> <code>No</code> </td><td>Deploy the optional remote MCP Server, using AgentCore Gateway to connect AI applications to Distributed Load Testing on AWS.</td></tr>
  <tr><td> <b>Load Tester Image URI</b> </td><td>&lt;Optional input&gt;</td><td>URI of a custom load tester container image from Amazon Elastic Container Registry (Amazon ECR) private registry (for example, <code>123456789012.dkr.ecr.us-gov-west-1.amazonaws.com/dlt-load-tester:v4.0.0</code>). Required for AWS GovCloud (US) deployments where ECS tasks cannot access <code>public.ecr.aws</code>. If empty, the default public image is used. For more information, see <a href="container-image.md#load-tester-image-uri">Load tester image URI</a>.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately 15 minutes.

**Note**
In addition to the primary AWS Lambda function, this solution includes the custom-resource Lambda function, which runs only during initial configuration or when resources are updated or deleted.

When running this solution, the custom-resource Lambda function is inactive. However, do not delete this function as it is necessary to manage associated resources.
