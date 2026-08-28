---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/security.html
---

# Security
<a name="security"></a>

 When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

 AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users in the AWS Cloud. This solution creates the following IAM roles that grant AWS Lambda functions access to create regional resources.

 **LambdaExecutionRoles**: Each Lambda function has a dedicated role to allow it to interact with Amazon DynamoDB, AWS Config, and AWS Network Firewall in a least privilege manner.

 **ObjectExtensionSecOpsAdminRole:** Assumed by the customer to interact with this solution.

## Network configuration
<a name="network-configuration"></a>

 The solution is deployed in Amazon Virtual Private Cloud (Amazon VPC) with the Lambda functions in a private subnet. Traffic in and out of the private subnet is controlled by security groups. By default, the security group rules only allow inbound traffic from the private subnet to prevent unauthorized access to the data storage layer.

 By default, the solution creates a new Amazon VPC with two subnets each in two availability zones. Each availability zone includes:
+  One public subnet to install a NAT gateway, so that certain AWS services can be reached, for example, AWS Network Firewall.
+  One private subnet to install ECS cluster (if `enableOpa` is set to `true`) and all Lambda functions, so that no data leaves the Amazon VPC (exclude the communication to and from AWS Network Firewall)
+  Eight network interfaces are created to ensure the data is within the Amazon VPC.

## Security groups
<a name="security-groups"></a>

 The security groups created in this solution are designed to control and isolate network traffic between the Lambda functions, Certificate Signing Request (CSR) instances, and remote virtual private network (VPN) endpoints. Once the deployment is up and running, we recommend that you review the security groups and further restrict access as needed.

## Data protection
<a name="data-protection"></a>

 All data committed to the solution is encrypted at rest. This includes the data stored in Amazon S3 and DynamoDB.

 Communication between the solution’s different components is over HTTPS to ensure data is encrypted in transit, and within the VPC boundary.

By default, all S3 buckets for this solution come with the following configuration:
+  All public access blocked
+  Versioning activated
+  Access log activated
+  Encryption at rest by a key management service (KMS)-based customer managed key (CMK)

 Additionally, S3 buckets are also configured with a default resource policy that deny all non-HTTPS requests to ensure data-in-transit encryption.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Object and Rule Extensions for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
