---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption.html
---

# Create an AWS Cloud9 IDE that uses Amazon EBS volumes with default encryption
<a name="create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption"></a>

*Janardhan Malyala and Dhrubajyoti Mukherjee, Amazon Web Services*

## Summary
<a name="create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption-summary"></a>

**Notice**: AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

You can use [encryption by default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) to enforce the encryption of your Amazon Elastic Block Store (Amazon EBS) volumes and snapshot copies on the Amazon Web Services (AWS) Cloud.

You can create an AWS Cloud9 integrated development environment (IDE) that uses EBS volumes encrypted by default. However, the AWS Identity and Access Management (IAM) [service-linked role](https://docs.aws.amazon.com/cloud9/latest/user-guide/using-service-linked-roles.html) for AWS Cloud9 requires access to the AWS Key Management Service (AWS KMS) key for these EBS volumes. If access is not provided, the AWS Cloud9 IDE might fail to launch and debugging might be difficult.

This pattern provides the steps to add the service-linked role for AWS Cloud9 to the AWS KMS key that is used by your EBS volumes. The setup described by this pattern helps you successfully create and launch an IDE that uses EBS volumes with encryption by default.

## Prerequisites and limitations
<a name="create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption-prereqs"></a>

**Prerequisites  **
+ An active AWS account.
+ Default encryption turned on for EBS volumes. For more information about encryption by default, see [Amazon EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) in the Amazon Elastic Compute Cloud (Amazon EC2) documentation.
+ An existing [customer managed KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) for encrypting your EBS volumes.

**Note**
You don't need to create the service-linked role for AWS Cloud9. When you create an AWS Cloud9 development environment, AWS Cloud9 creates the service-linked role for you.

## Architecture
<a name="create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption-architecture"></a>

![Using an AWS Cloud9 IDE to enforce the encryption of EBS volumes and snapshots.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/dd98fbb4-0949-4299-b701-bc857e13049c/images/6b22b8d1-75d9-4f06-b5d6-5fff7397f22d.png)

**Technology stack**
+ AWS Cloud9
+ IAM
+ AWS KMS

## Tools
<a name="create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption-tools"></a>
+ [AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html) is an integrated development environment (IDE) that helps you code, build, run, test, and debug software. It also helps you release software to the AWS Cloud.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block-level storage volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.

## Epics
<a name="create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption-epics"></a>

### Find the default encryption key value
<a name="find-the-default-encryption-key-value"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Record the default encryption key value for the EBS volumes.  | Sign in to the AWS Management Console and open the Amazon EC2 console. Choose **EC2 dashboard**, and then choose **Data protection and security** in **Account attributes**. In **EBS encryption **section, copy and record the value in **Default encryption key**. | Cloud architect, DevOps engineer |

### Provide access to the AWS KMS key
<a name="provide-access-to-the-aws-kms-key"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provide AWS Cloud9 with access to the KMS key for EBS volumes. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption.html)For more information about updating a key policy, see [How to change a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html#key-policy-modifying-how-to) (AWS KMS documentation).The service-linked role for AWS Cloud9 is automatically created when you launch your first IDE. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/cloud9/latest/user-guide/using-service-linked-roles.html#create-service-linked-role) in the AWS Cloud9 documentation.  | Cloud architect, DevOps engineer |

### Create and launch the IDE
<a name="create-and-launch-the-ide"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and launch the AWS Cloud9 IDE. | Open the AWS Cloud9 console and choose **Create environment**.** **Configure IDE according to your requirements by following the steps from [Creating an EC2 environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html) in the AWS Cloud9 documentation.  | Cloud architect, DevOps engineer |

## Related resources
<a name="create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption-resources"></a>
+ [Encrypt EBS volumes used by AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/move-environment.html#encrypting-volumes)
+ [Create a service-linked role for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/using-service-linked-roles.html#create-service-linked-role)
+ [Create an EC2 environment in AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html)

## Additional information
<a name="create-an-aws-cloud9-ide-that-uses-amazon-ebs-volumes-with-default-encryption-additional"></a>

**AWS KMS key policy updates**

Replace `<aws_accountid>` with your AWS account ID.

```
{
            "Sid": "Allow use of the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<aws_accountid>:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Allow attachment of persistent resources",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<aws_accountid>:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9"
            },
            "Action": [
                "kms:CreateGrant",
                "kms:ListGrants",
                "kms:RevokeGrant"
            ],
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                }
            }
        }
```

**Using a cross-account key**

If you want to use a cross-account KMS key, you must use a grant in combination with the KMS key policy. This enables cross-account access to the key. In the same account that you used to create the Cloud9 environment, run the following command in the terminal.

```
aws kms create-grant \
 --region <Region where Cloud9 environment is created> \
 --key-id <The cross-account KMS key ARN> \
 --grantee-principal arn:aws:iam::<The account where Cloud9 environment is created>:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9 \
 --operations "Encrypt" "Decrypt" "ReEncryptFrom" "ReEncryptTo" "GenerateDataKey" "GenerateDataKeyWithoutPlaintext" "DescribeKey" "CreateGrant"
```

After you run this command, you can create Cloud9 environments by using EBS encryption with a key in a different account.
