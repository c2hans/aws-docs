---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters.html
---

# Automatically remediate unencrypted Amazon RDS DB instances and clusters
<a name="automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters"></a>

*Ajay Rawat and Josh Joy, Amazon Web Services*

## Summary
<a name="automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters-summary"></a>

This pattern describes how to automatically remediate unencrypted Amazon Relational Database Service (Amazon RDS) DB instances and clusters on Amazon Web Services (AWS) by using AWS Config, AWS Systems Manager runbooks, and AWS Key Management Service (AWS KMS) keys.

Encrypted RDS DB instances provide an additional layer of data protection by securing your data from unauthorized access to the underlying storage. You can use Amazon RDS encryption to increase data protection of your applications deployed in the AWS Cloud, and to fulfill compliance requirements for encryption at rest. You can enable encryption for an RDS DB instance when you create it, but not after it's created. However, you can add encryption to an unencrypted RDS DB instance by creating a snapshot of your DB instance, and then creating an encrypted copy of that snapshot. You can then restore a DB instance from the encrypted snapshot to get an encrypted copy of your original DB instance.

This pattern uses AWS Config Rules to evaluate RDS DB instances and clusters. It applies remediation by using AWS Systems Manager runbooks, which define the actions to be performed on noncompliant Amazon RDS resources, and AWS KMS keys to encrypt the DB snapshots. It then enforces service control policies (SCPs) to prevent the creation of new DB instances and clusters without encryption.

The code for this pattern is provided in [GitHub](https://github.com/aws-samples/aws-system-manager-automation-unencrypted-to-encrypted-resources).

## Prerequisites and limitations
<a name="automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Files from the [GitHub source code repository](https://github.com/aws-samples/aws-system-manager-automation-unencrypted-to-encrypted-resources) for this pattern downloaded to your computer
+ An unencrypted RDS DB instance or cluster
+ An existing AWS KMS key for encrypting RDS DB instances and clusters
+ Access to update the KMS key resource policy
+ AWS Config enabled in your AWS account (see [Getting Started with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) in the AWS documentation)

**Limitations**
+ You can enable encryption for an RDS DB instance only when you create it, not after it has been created.
+ You can't have an encrypted read replica of an unencrypted DB instance or an unencrypted read replica of an encrypted DB instance.
+ You can't restore an unencrypted backup or snapshot to an encrypted DB instance.
+ Amazon RDS encryption is available for most DB instance classes. For a list of exceptions, see [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) in the Amazon RDS documentation.
+ To copy an encrypted snapshot from one AWS Region to another, you must specify the KMS key in the destination AWS Region. This is because KMS keys are specific to the AWS Region that they are created in.
+ The source snapshot remains encrypted throughout the copy process. Amazon RDS uses envelope encryption to protect data during the copy process. For more information, see [Envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping) in the AWS KMS documentation.
+ You can't unencrypt an encrypted DB instance. However, you can export data from an encrypted DB instance and import the data into an unencrypted DB instance.
+ You should delete a KMS key only when you are sure that you don't need to use it any longer. If you aren't sure, consider [disabling the KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) instead of deleting it. You can reenable a disabled KMS key if you need to use it again later, but you cannot recover a deleted KMS key.
+ If you don't choose to retain automated backups, your automated backups that are in the same AWS Region as the DB instance are deleted. They can't be recovered after you delete the DB instance.
+ Your automated backups are retained for the retention period that is set on the DB instance at the time you delete it. This set retention period occurs whether or not you choose to create a final DB snapshot.
+ If automatic remediation is enabled, this solution encrypts all databases that have the same KMS key.

## Architecture
<a name="automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters-architecture"></a>

The following diagram illustrates the architecture for the CloudFormation implementation. Note that you can also implement this pattern by using the AWS Cloud Development Kit (AWS CDK).

![AWS CloudFormation implementation for remediating unencrypted Amazon RDS instances.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7f7195e3-98c4-4b18-9192-c0400ac5b891/images/8c1466fa-15b3-44ef-aa7e-7958f80cb699.png)

## Tools
<a name="automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters-tools"></a>

**Tools**
+ [CloudFormation](https://aws.amazon.com/cloudformation/) helps you automatically set up your AWS resources. It enables you to use a template file to create and delete a collection of resources together as a single unit (a stack).
+ [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) is a software development framework for defining your cloud infrastructure in code and provisioning it by using familiar programming languages.

**AWS services and features**
+ [AWS Config](https://aws.amazon.com/config/) keeps track of the configuration of your AWS resources and their relationships to your other resources. It can also evaluate those AWS resources for compliance. This service uses rules that can be configured to evaluate AWS resources against desired configurations. You can use a set of AWS Config managed rules for common compliance scenarios, or you can create your own rules for custom scenarios. When an AWS resource is found to be noncompliant, you can specify a remediation action through an AWS Systems Manager runbook and optionally send an alert through an Amazon Simple Notification Service (Amazon SNS) topic. In other words, you can associate remediation actions with AWS Config Rules and choose to run them automatically to address noncompliant resources without manual intervention. If a resource is still noncompliant after automatic remediation, you can set the rule to try automatic remediation again.
+ [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) makes it easier to set up, operate, and scale a relational database in the cloud. The basic building block of Amazon RDS is the DB instance, which is an isolated database environment in the AWS Cloud. Amazon RDS provides a [selection of instance types](https://aws.amazon.com/rds/instance-types/) that are optimized to fit different relational database use cases. Instance types comprise various combinations of CPU, memory, storage, and networking capacity and give you the flexibility to choose the appropriate mix of resources for your database. Each instance type includes several instance sizes, allowing you to scale your database to the requirements of your target workload.
+ [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) is a managed service that makes it easy for you to create and control AWS KMS keys, which encrypt your data. A KMS key is a logical representation of a root key. The KMS key includes metadata, such as the key ID, creation date, description, and key state.
+ [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) offer central control over the maximum available permissions for all accounts in your organization. SCPs help you ensure that your accounts stay within your organization’s access control guidelines. SCPs don't affect users or roles in the management account. They affect only the member accounts in your organization. We strongly recommend that you don't attach SCPs to the root of your organization without thoroughly testing the impact that the policy has on accounts. Instead, create an organizational unit (OU) that you can move your accounts into one at a time, or at least in small numbers, to ensure that you don't inadvertently lock users out of key services.

**Code**

The source code and templates for this pattern are available in a [GitHub repository](https://github.com/aws-samples/aws-system-manager-automation-unencrypted-to-encrypted-resources/). The pattern provides two implementation options: You can deploy an CloudFormation template to create the remediation role that encrypts RDS DB instances and clusters, or use the AWS CDK. The repository has separate folders for these two options.

The [Epics](#automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters-epics) section provides step-by-step instructions for deploying the CloudFormation template. If you want to use the AWS CDK, follow the instructions in the `README.md` file in the GitHub repository.

## Best practices
<a name="automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters-best-practices"></a>
+ Enable data encryption both at rest and in transit.
+ Enable AWS Config in all accounts and AWS Regions.
+ Record configuration changes to all resource types.
+ Rotate your IAM credentials regularly.
+ Leverage tagging for AWS Config, which makes is easier to manage, search for, and filter resources.

## Epics
<a name="automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters-epics"></a>

### Create the IAM remediation role and Systems Manager runbook
<a name="create-the-iam-remediation-role-and-sys-runbook"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the CloudFormation template. | Download the `unencrypted-to-encrypted-rds.template.json` file from the [GitHub repository](https://github.com/aws-samples/aws-system-manager-automation-unencrypted-to-encrypted-resources/tree/main/rds/CloudFormation). | DevOps engineer |
| Create the CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters.html)For more information about deploying templates, see the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html). | DevOps engineer |
| Review CloudFormation parameters and values. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters.html) | DevOps engineer |
| Review the resources. | When the stack has been created, its status changes to **CREATE\_COMPLETE**. Review the created resources (IAM role, Systems Manager runbook) in the CloudFormation console. | DevOps engineer |

### Update the AWS KMS key policy
<a name="update-the-kms-key-policy"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update your KMS key policy. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters.html)<pre>{<br />    "Sid": "Allow access through RDS for all principals in the account that are authorized to use RDS",<br />    "Effect": "Allow",<br />    "Principal": {<br />        "AWS": "arn:aws:iam:: <your-AWS-account-ID>":role/<your-IAM-remediation-role>"<br />    },<br />    "Action": [<br />        "kms:Encrypt",<br />        "kms:Decrypt",<br />        "kms:ReEncrypt*",<br />        "kms:GenerateDataKey*",<br />        "kms:CreateGrant",<br />        "kms:ListGrants",<br />        "kms:DescribeKey"<br />    ],<br />    "Resource": "*",<br />    "Condition": {<br />        "StringEquals": {<br />            "kms:ViaService": "rds.us-east-1.amazonaws.com",<br />            "kms:CallerAccount": "<your-AWS-account-ID>"<br />        }<br />    }<br />}</pre> | DevOps engineer |

### Find and remediate noncompliant resources
<a name="find-and-remediate-noncompliant-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| View noncompliant resources. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters.html)The noncompliant resources listed in the AWS Config console will be instances, not clusters. The remediation automation encrypts instances and clusters, and creates either a newly encrypted instance or a newly created cluster. However, be sure not to simultaneously remediate multiple instances that belong to the same cluster.<br />Before you remediate any RDS DB instances or volumes, make sure that the RDS DB instance is not in use. Confirm that there are no write operations occurring while the snapshot is being created, to ensure that the snapshot contains the original data. Consider enforcing a maintenance window during which the remediation will run. | DevOps engineer |
| Remediate noncompliant resources. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters.html) | DevOps engineer |
| Verify that the RDS DB instance is available. | After the automation completes, the newly encrypted RDS DB instance will become available. The encrypted RDS DB instance will have the prefix `encrypted` followed by the original name. For example, if the unencrypted RDS DB instance name was `database-1`, the newly encrypted RDS DB instance would be `encrypted-database-1`. | DevOps engineer |
| Terminate the unencrypted instance. | After remediation is complete and the newly encrypted resource has been validated, you can terminate the unencrypted instance. Make sure to confirm that the newly encrypted resource matches the unencrypted resource before you terminate any resources. | DevOps engineer |

### Enforce SCPs
<a name="enforce-scps"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enforce SCPs. | Enforce SCPs to prevent DB instances and clusters from being created without encryption in the future. Use the `rds_encrypted.json` file that’s provided in the [GitHub repository](https://github.com/aws-samples/aws-system-manager-automation-unencrypted-to-encrypted-resources/tree/main/rds/SCP) for this purpose, and follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_create.html).  | Security engineer |

## Related resources
<a name="automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters-resources"></a>

**References**
+ [Setting up AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)
+ [AWS Config custom rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html)
+ [AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
+ [AWS Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html)
+ [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Tools**
+ [CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/)

**Guides and patterns**
+ [Automatically re-enable AWS CloudTrail by using a custom remediation rule in AWS Config](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-re-enable-aws-cloudtrail-by-using-a-custom-remediation-rule-in-aws-config.html)

## Additional information
<a name="automatically-remediate-unencrypted-amazon-rds-db-instances-and-clusters-additional"></a>

**How does AWS Config work?**

When you use AWS Config, it first discovers the supported AWS resources that exist in your account and generates a [configuration item](https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-items) for each resource. AWS Config also generates configuration items when the configuration of a resource changes, and it maintains historical records of the configuration items of your resources from the time you start the configuration recorder. By default, AWS Config creates configuration items for every supported resource in the AWS Region. If you don't want AWS Config to create configuration items for all supported resources, you can specify the resource types that you want it to track.

**How are AWS Config and AWS Config Rules related to AWS Security Hub CSPM?**

AWS Security Hub CSPM is a security and compliance service that provides security and compliance posture management as a service. It uses AWS Config and AWS Config Rules as its primary mechanism to evaluate the configuration of AWS resources. AWS Config Rules can also be used to evaluate resource configuration directly. Other AWS services, such AWS Control Tower and AWS Firewall Manager, also use AWS Config Rules.
