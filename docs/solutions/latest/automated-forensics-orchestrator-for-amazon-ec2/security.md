---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/security.html
---

# Security
<a name="security"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit the [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users in the AWS Cloud. This Guidance creates IAM roles that grant the Guidance’s automated functions access to perform remediation actions within a narrow scope set of permissions specific to each remediation.

## AWS Key Management Service (KMS) Keys
<a name="aws-key-management-service-kms-keys"></a>

The Automated Forensics Orchestrator for Amazon EC2 and EKS Guidance allows you to provide your own AWS KMS keys to encrypt data stored. We recommend referring to [Security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html) to enhance the protection of your encryption keys.

AWS recommends that customers encrypt sensitive data in transit and at rest. This Guidance automatically encrypts file data, and metadata at rest with [Amazon S3 Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html) (SSE) with AES256 algorithm.

Additionally, this Guidance’s Amazon DynamoDB are encrypted at rest using SSE with AWS Key Management Service (AWS KMS).

## Network configuration
<a name="network-configuration"></a>

The Automated Forensics Orchestrator for Amazon EC2 and EKS Guidance is deployed in Amazon VPC, with the Lambda functions in a private subnet. Traffic in and out of the subnet is controlled by security groups. To prevent unauthorized access to the data storage layer, by default, the security group rules only allow inbound traffic from the Lambda function’s private subnet.

## Data protection
<a name="data-protection"></a>

All data committed to Automated Forensics Orchestrator for Amazon EC2 and EKS is encrypted at rest, this includes data stored in Amazon S3 and Amazon DynamoDB.

Communications between the Guidance’s different components are over HTTPS to ensure data encryption in transit.
