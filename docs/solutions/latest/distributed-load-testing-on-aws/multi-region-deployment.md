---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/multi-region-deployment.html
---

# Multi-Region deployment
<a name="multi-region-deployment"></a>

 **Time to deploy:** Approximately 5 minutes per Region

You can run tests across multiple Regions.

When you deploy the Distributed Load Testing solution, it creates a regional CloudFormation template in the scenarios S3 bucket. The URL for this template is listed in the CloudFormation outputs of your main stack under the key "RegionalCFTemplate".

To run a multi-Region test, you must deploy the regional CloudFormation template in each Region where you want to run the test.

**Note**
Each AWS account can use only one regional stack per Region. Also, the regional stack cannot be used in the same Region as the main stack.

You can install the regional template as follows:

1. In the solution’s web console, navigate to **Dashboard** in the left menu.

1. Use the clipboard icon to copy the CloudFormation template link in Amazon S3.

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home) and select the correct Region.

1. On the **Create stack** page, verify that the correct template URL shows in the **Amazon S3 URL** text box and choose **Next**.

1. On the **Specify stack details** page, assign a name to your solution stack.

1. Under **Parameters**, review the parameters for the template and modify them as necessary. This solution uses the following default values.

<table>
<thead>
  <tr><th>Parameter</th><th>Default</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td> <b>Existing VPC ID</b> </td><td>&lt;Optional input&gt;</td><td>If you have a VPC that you want to use and is already created, enter the ID of an existing VPC in the same Region where the stack was deployed. For example, vpc-1a2b3c4d5e6f.</td></tr>
  <tr><td> <b>First existing subnet</b> </td><td>&lt;Optional input&gt;</td><td>The ID of the first subnet within your existing VPC. This subnet needs a route to the internet to pull the container image for running tests. For example, subnet-7h8i9j0k.</td></tr>
  <tr><td> <b>Second existing subnet</b> </td><td>&lt;Optional input&gt;</td><td>The ID of the second subnet within the existing VPC. This subnet needs a route to the internet to pull the container image for running tests. For example, subnet-1x2y3z.</td></tr>
  <tr><td> <b>Provide valid CIDR block for the solution to create VPC</b> </td><td>192.168.0.0/16</td><td>If you do not provide values for an existing VPC, the CIDR block for the solution-created Amazon VPC contains the IP address for AWS Fargate.</td></tr>
  <tr><td> <b>Provide CIDR block for allowing outbound traffic of Fargate tasks</b> </td><td>0.0.0.0/0</td><td>CIDR block that restricts Amazon ECS container outbound access.</td></tr>
</tbody>
</table>

1. Choose **Next**.

1. On the **Configure stack options** page, choose **Next**.

1. On the **Review** page, review and confirm the settings. Be sure to select the box acknowledging that the template will create AWS Identity and Access Management (IAM) resources.

1. Choose **Create stack** to deploy the stack.

   You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a **CREATE\_COMPLETE** status in approximately five minutes.

When the Regions have been successfully deployed, they appear in the web console. When you create a test, all available Regions are listed on the **Dashboard** and in **Scenario Creation**. You can add a Region to a test in the **Traffic Shape** step of Scenario Creation.

The solution creates a DynamoDB item for each deployed Region in the scenarios table, which contains the necessary information about the testing resources in that Region. You can sort test results in the web console by Region. To view aggregate results across all Regions in a multi-Region test, use Amazon CloudWatch metrics. You can find the source code for the graph in the test results after the test completes.

**Note**
You can launch the regional stack without the web console. Obtain a link to the regional template in the Amazon S3 scenarios bucket and provide it as the source when launching the regional stack in the required Region. Alternatively, you can download the template and upload it as the source for the Region you want.
