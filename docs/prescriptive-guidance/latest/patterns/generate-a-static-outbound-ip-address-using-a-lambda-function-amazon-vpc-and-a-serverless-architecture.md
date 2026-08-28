---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html
---

# Generate a static outbound IP address using a Lambda function, Amazon VPC, and a serverless architecture
<a name="generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture"></a>

*Thomas Scott, Amazon Web Services*

## Summary
<a name="generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture-summary"></a>

This pattern describes how to generate a static outbound IP address in the Amazon Web Services (AWS) Cloud by using a serverless architecture. Your organization can benefit from this approach if it wants to send files to a separate business entity by using Secure File Transfer Protocol (SFTP). This means that the business entity must have access to an IP address that allows files through its firewall.

The pattern’s approach helps you create an AWS Lambda function that uses an [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) as the outbound IP address. By following the steps in this pattern, you can create a Lambda function and a virtual private cloud (VPC) that routes outbound traffic through an internet gateway with a static IP address. To use the static IP address, you attach the Lambda function to the VPC and its subnets.

## Prerequisites and limitations
<a name="generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ AWS Identity and Access Management (IAM) permissions to create and deploy a Lambda function, and to create a VPC and its subnets. For more information about this, see [Execution role and user permissions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#vpc-permissions) in the AWS Lambda documentation.
+ If you plan to use infrastructure as code (IaC) to implement this pattern’s approach, you need an integrated development environment (IDE) such as AWS Cloud9. For more information about this, see [What is AWS Cloud9?](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html) in the AWS Cloud9 documentation.

## Architecture
<a name="generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture-architecture"></a>

The following diagram shows the serverless architecture for this pattern.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/eb1d0b05-df33-45ae-b27e-36090055b300/images/c15cc6da-ce4e-4ea0-9feb-de1c845d3ce8.png)

The diagram shows the following workflow:

1. Outbound traffic leaves `NAT gateway 1` in `Public subnet 1`.

1. Outbound traffic leaves `NAT gateway 2` in `Public subnet 2`.

1. The Lambda function can run in `Private subnet 1` or `Private subnet 2`.

1. `Private subnet 1` and `Private subnet 2` route traffic to the NAT gateways in the public subnets.

1. The NAT gateways send outbound traffic to the internet gateway from the public subnets.

1. Outbound data is transferred from the internet gateway to the external server.

**Technology stack  **
+ Lambda
+ Amazon Virtual Private Cloud (Amazon VPC)

**Automation and scale**

You can ensure high availability (HA) by using two public and two private subnets in different Availability Zones. Even if one Availability Zone becomes unavailable, the pattern’s solution continues to work.

## Tools
<a name="generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture-tools"></a>
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second. You pay only for the compute time that you consume—there is no charge when your code is not running.
+ [Amazon VPC](https://docs.aws.amazon.com/vpc/) – Amazon Virtual Private Cloud (Amazon VPC) provisions a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

## Epics
<a name="generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture-epics"></a>

### Create a new VPC
<a name="create-a-new-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new VPC. | Sign in to the AWS Management Console, open the Amazon VPC console, and then create a VPC named `Lambda VPC` that has `10.0.0.0/25`** **as the IPv4 CIDR range.<br />For more information about creating a VPC, see [Getting started with Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html#getting-started-create-vpc) in the Amazon VPC documentation.  | AWS administrator |

### Create two public subnets
<a name="create-two-public-subnets"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the first public subnet. | 1. On the Amazon VPC console, choose **Subnets **and then choose **Create Subnet**. <br />2. For **Name tag**, enter `public-one`.<br />3. For **VPC**, choose `Lambda VPC`.<br />4. Choose an Availability Zone and record it. <br />5. For **IPv4 CIDR block**, enter `10.0.0.0/28`** **and then choose **Create subnet**. | AWS administrator |
| Create the second public subnet. | 1. On the Amazon VPC console, choose **Subnets **and then choose **Create Subnet**. <br />2. For **Name tag**, enter `public-two`.<br />3. For **VPC**, choose `Lambda VPC`.<br />4. Choose an Availability Zone and record it. : You cannot use the Availability Zone that contains the `public-one` subnet. <br />5. For **IPv4 CIDR block**, enter `10.0.0.16/28`** **and then choose **Create subnet**. | AWS administrator |

### Create two private subnets
<a name="create-two-private-subnets"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the first private subnet. | 1. On the Amazon VPC console, choose **Subnets **and then choose **Create Subnet**. <br />2. For **Name tag**, enter `private-one`.<br />3. For **VPC**, choose `Lambda VPC`.<br />4. Choose the Availability Zone that contains the `public-one` subnet that you created earlier. <br />5. For **IPv4 CIDR block**, enter `10.0.0.32/28`** **and then choose **Create subnet**. | AWS administrator |
| Create the second private subnet. | 1. On the Amazon VPC console, choose **Subnets **and then choose **Create Subnet**. <br />2. For **Name tag**, enter `private-two`.<br />3. For **VPC**, choose `Lambda VPC`.<br />4. Choose the same Availability Zone that contains the `public-two` subnet that you created earlier. <br />5. For **IPv4 CIDR block**, enter `10.0.0.64/28`** **and then choose **Create subnet**. | AWS administrator |

### Create two Elastic IP addresses for your NAT gateways
<a name="create-two-elastic-ip-addresses-for-your-nat-gateways"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Create the first Elastic IP address. | 1. On the Amazon VPC console, choose **Elastic IPs** and then choose **Allocate new address**.** **<br />2. Choose** Allocate **and record the **Allocation ID **for your newly created Elastic IP address.** **This Elastic IP address is used for your first NAT gateway.  | AWS administrator |
| Create the second Elastic IP address. | 1. On the Amazon VPC console, choose **Elastic IPs** and then choose **Allocate new address**.** **<br />2. Choose** Allocate **and record the **Allocation ID **for this second Elastic IP address.This Elastic IP address is used for your second NAT gateway. | AWS administrator |

### Create an internet gateway
<a name="create-an-internet-gateway"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an internet gateway. | 1. On the Amazon VPC console, choose **Internet Gateways** and then choose **Create internet gateway**.<br />2. Enter `Lambda internet gateway` as the name and then choose **Create internet gateway**. Make sure that you record the internet gateway ID.  | AWS administrator |
| Attach the internet gateway to the VPC. | Select the internet gateway that you just created, and then choose **Actions, Attach to VPC**. | AWS administrator |

### Create two NAT gateways
<a name="create-two-nat-gateways"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the first NAT gateway. | 1. On the Amazon VPC console, choose **NAT Gateways **and then choose** Create NAT Gateway**.<br />2. Enter `nat-one`** **as the NAT gateway name.** **<br />3. Choose `public-one`** **as the subnet to create the NAT gateway in.** **<br />4. For **Connectivity type**, choose **Public**.<br />5. For **Elastic IP allocation ID**, choose the first Elastic IP address that you created earlier and associate it with the NAT gateway.<br />6. Choose** Create NAT gateway**. | AWS administrator |
| Create the second NAT gateway. | 1. On the Amazon VPC console, choose **NAT Gateways **and then choose** Create NAT Gateway**.<br />2. Enter `nat-two`** **as the NAT gateway name.** **<br />3. Choose `public-two`** **as the subnet to create the NAT gateway in.<br />4. For **Connectivity type**, choose **Public**.<br />5. For **Elastic IP allocation ID**, choose the second Elastic IP address that you created earlier and associate it with the NAT gateway.<br />6. Choose** Create NAT gateway**. | AWS administrator |

### Create route tables for your public and private subnets
<a name="create-route-tables-for-your-public-and-private-subnets"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the route table for the public-one subnet. | 1. On the Amazon VPC console, choose **Route Tables** and then choose **Create route table**.<br />2. Enter `public-one-subnet`** **as the route table name and then choose **Create route table**.<br />3. Choose the `public-one-subnet` route table, choose **Edit routes**, and then choose **Add route**.<br />4. Specify `0.0.0.0`** **in the **Destination** box and then choose the internet gateway ID in the **Target** list.<br />5. On the **Subnet associations** tab, choose **Edit subnet associations**, choose the `public-one` subnet** **with the `10.0.0.0/28`** **CIDR range, and then choose **Save associations**.<br />6. Choose** Save Changes**. | AWS administrator |
| Create the route table for the public-two subnet. | 1. On the Amazon VPC console, choose **Route Tables** and then choose **Create route table**.<br />2. Enter `public-two-subnet`** **as the route table name and then choose **Create route table**.<br />3. Choose the `public-two-subnet`** **route table, choose **Edit routes**, and then choose **Add route**.<br />4. Specify `0.0.0.0`** **in the **Destination** box and then choose the internet gateway ID in the **Target** list.<br />5. On the **Subnet associations** tab, choose **Edit subnet associations**, choose the `public-two`** **subnet with the `10.0.0.16/28`** **CIDR range, and then choose **Save associations**.<br />6. Choose** Save Changes**. | AWS administrator |
| Create the route table for the private-one subnet. | 1. On the Amazon VPC console, choose **Route Tables** and then choose **Create route table**.<br />2. Enter `private-one-subnet`** **as the route table name and then choose **Create route table**.<br />3. Choose the `private-one-subnet`** **route table, choose **Edit routes**, and then choose **Add route**.<br />4. Specify `0.0.0.0`** **in the **Destination** box and then choose the NAT gateway in the `public-one` subnet in the **Target** list.<br />5. On the **Subnet associations** tab, choose **Edit subnet associations**, choose the `private-one`subnet with the `10.0.0.32/28`** **CIDR range, and then choose **Save associations**.<br />6. Choose** Save Changes**. | AWS administrator |
| Create the route table for the private-two subnet. | 1. On the Amazon VPC console, choose **Route Tables** and then choose **Create route table**.<br />2. Enter `private-two-subnet`** **as the route table name and then choose **Create route table**.<br />3. Choose the `private-two-subnet`** **route table, choose **Edit routes**, and then choose **Add route**.<br />4. Specify `0.0.0.0`** **in the **Destination** box and then choose the NAT gateway in the `public-two` subnet in the **Target** list.<br />5. On the **Subnet associations** tab, choose **Edit subnet associations**, choose the `private-two`** **subnet with the `10.0.0.64/28` CIDR range, and then choose **Save associations**.<br />6. Choose** Save Changes**. | AWS administrator |

### Create the Lambda function, add it to the VPC, and test the solution
<a name="create-the-lambda-function-add-it-to-the-vpc-and-test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new Lambda function. | 1. Open the AWS Lambda console and choose **Create function**.** **<br />2. Under **Basic information**, enter `Lambda test` under **Function name** and then choose the language of your choice under **Runtime**.**  **<br />3. Choose **Create function**. | AWS administrator |
| Add the Lambda function to your VPC. | 1. On the AWS Lambda console, choose **Functions** and then choose the function that you created earlier. <br />2. Choose **Configuration** and then choose **VPC**.<br />3. Choose **Edit **and then choose `Lambda VPC`** **and both private subnets.<br />4. Choose **Default security group **for testing purposes and then choose **Save**. | AWS administrator |
| Write code to call an external service. | 1. In the programming language of your choice, write code to call an external service that returns your IP address.<br />2. Verify that the returned IP address matches one of your Elastic IP addresses. | AWS administrator |

## Related resources
<a name="generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture-resources"></a>
+ [Configuring a Lambda function to access resources in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
