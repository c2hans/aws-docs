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
| Create the first public subnet. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |
| Create the second public subnet. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |

### Create two private subnets
<a name="create-two-private-subnets"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the first private subnet. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |
| Create the second private subnet. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |

### Create two Elastic IP addresses for your NAT gateways
<a name="create-two-elastic-ip-addresses-for-your-nat-gateways"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Create the first Elastic IP address. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html)This Elastic IP address is used for your first NAT gateway.  | AWS administrator |
| Create the second Elastic IP address. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html)This Elastic IP address is used for your second NAT gateway. | AWS administrator |

### Create an internet gateway
<a name="create-an-internet-gateway"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an internet gateway. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |
| Attach the internet gateway to the VPC. | Select the internet gateway that you just created, and then choose **Actions, Attach to VPC**. | AWS administrator |

### Create two NAT gateways
<a name="create-two-nat-gateways"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the first NAT gateway. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |
| Create the second NAT gateway. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |

### Create route tables for your public and private subnets
<a name="create-route-tables-for-your-public-and-private-subnets"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the route table for the public-one subnet. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |
| Create the route table for the public-two subnet. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |
| Create the route table for the private-one subnet. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |
| Create the route table for the private-two subnet. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |

### Create the Lambda function, add it to the VPC, and test the solution
<a name="create-the-lambda-function-add-it-to-the-vpc-and-test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new Lambda function. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |
| Add the Lambda function to your VPC. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |
| Write code to call an external service. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture.html) | AWS administrator |

## Related resources
<a name="generate-a-static-outbound-ip-address-using-a-lambda-function-amazon-vpc-and-a-serverless-architecture-resources"></a>
+ [Configuring a Lambda function to access resources in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)
