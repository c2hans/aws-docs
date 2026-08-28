---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## AWS KMS
<a name="aws-kms"></a>

The solution creates an AWS managed Customer managed key, which is used to configure server-side encryption for the SNS topic and the DynamoDB tables.

## Amazon IAM
<a name="amazon-iam"></a>

The solution’s Lambda functions require permissions to access hub account resources and access to get/put Systems Manager parameters, access to CloudWatch log groups, AWS KMS key encryption/decryption, and publish messages to SNS. In addition, Instance Scheduler will also create Scheduling Roles in all managed accounts that will provide access to start/stop EC2, RDS, Autoscaling resurces, DB instances, modify instance attributes, and update tags for those resources. All the necessary permissions are provided by the solution to Lambda service role created as part of the solution template.

On deployment Instance Scheduler will deploy scoped down IAM roles for each of its Lambda functions along with Scheduler Roles that can be assumed only by specific scheduling Lambdas in the deployed hub template. These schedule roles will have names following the pattern `{namespace}-Scheduler-Role`, and `{namespace}-ASG-Scheduling-Role`.

For detailed information about the permission provided to each service role, refer to the [CloudFormation templates](aws-cloudformation-templates.md).

## Encrypted EC2 EBS Volumes
<a name="encrypted-ec2-ebs-volumes"></a>

When scheduling EC2 instances attached to EBS volumes encrypted by AWS KMS, you must grant Instance Scheduler permission to use the associated AWS KMS key(s). This allows Amazon EC2 to decrypt the attached EBS volumes during the started function. This permission must be granted to the scheduling role in the same account as the EC2 instance(s) using the key.

To grant permission to use an AWS KMS key with Instance Scheduler, add the AWS KMS key’s ARN to the Instance Scheduler stack (hub or spoke) in the same account as the EC2 instance(s) using the key(s):

 **KMS Key Arns for EC2**

![image3](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/image3.png)

This will automatically generate the following policy and add it to the scheduling role for that account:

```
 {

   "Version": "2012-10-17",
   "Statement": [
      {
        "Condition": {
            "StringLike": {
               "kms:ViaService": "ec2.*.amazonaws.com"
         },
        "Null": {
              "kms:EncryptionContextKeys": "false",
              "kms:GrantOperations": "false"
         },
        "ForAllValues:StringEquals": {
            "kms:EncryptionContextKeys": [
                 "aws:ebs:id"
              ],
              "kms:GrantOperations": [
                 "Decrypt"
              ]
        },
        "Bool": {
                 "kms:GrantIsForAWSResource": "true"
              }
        },
        "Action": "kms:CreateGrant",
        "Resource": [
             "Your-KMS-ARNs-Here"
        ],
        "Effect": "Allow"
      }
   ]
 }
```

## EC2 License Manager
<a name="ec2-license-manager"></a>

When scheduling EC2 instances that are managed in AWS License Manager, you must grant Instance Scheduler permission to use the associated license configurations. This allows the solution to properly start and stop instances while maintaining license compliance. This permission must be granted to the scheduling role in the same account as the EC2 instance(s) using License Manager.

To grant permission to use AWS License Manager with Instance Scheduler, add the License Manager configuration ARNs to the Instance Scheduler stack (hub or spoke) in the same account as the EC2 instance(s) using License Manager:

 **License Manager Configuration ARNs for EC2**

![license manager cfn param](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/license-manager-cfn-param.png)

This will automatically generate the following policy and add it to the scheduling role for that account:

```
 {

   "Version": "2012-10-17",
   "Statement": [
      {
        "Action": "ec2:StartInstances",
        "Resource": [
             "Your-License-Manager-ARNs-Here"
        ],
        "Effect": "Allow"
      }
   ]
 }
```

For more information about License Manager permissions, refer to [Identity and access management for AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager-iam.html) in the *AWS License Manager User Guide*.

```
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Instance Scheduler on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
