---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-contains3resource.html
---

# `AWSSupport-ContainS3Resource`

 **Description**

 The `AWSSupport-ContainS3Resource` runbook provides an automated solution for the procedure outlined in the article [Support Automation Workflow (SAW) Runbook: Contain a compromised AWS Amazon S3 Bucket](https://repost.aws/articles/ARhGc0hDqKRIKAVCbmF1GmuQ)

**Important**
This runbook performs various operations that require elevated privileges, such as modifying Amazon S3 bucket policies, tags, and public access configurations. These actions could potentially lead to privilege escalation or impact other workloads that depend on the targeted Amazon S3 bucket. You should review the permissions granted to the role specified by the `AutomationAssumeRole` parameter and ensure they are appropriate for the intended use case. You can refer to the following AWS documentation for more information on IAM permissions: [`Identity and Access Management (IAM) Permissions`](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html) [`AWS AWS Systems Manager Automation Permissions`](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup-iam.html).
This runbook performs mutative actions that could potentially cause unavailability or disruption to your workloads. Specifically, the `Contain` action blocks all access to the specified Amazon S3 bucket, except for the IAM users or roles specified in the `BucketRestrictAccess` parameter. This could impact any applications or services that rely on the targeted Amazon S3 bucket.
During the `Contain` action, this runbook may create an additional Amazon S3 bucket (specified by the `BackupS3BucketName` parameter) to store the backup of the original bucket's configuration, if it does not already exist.
Ensure that both the target and backup Amazon S3 buckets exist and are owned by the current AWS account. The Amazon S3 operations perform ownership verification and will fail if either bucket is missing or belongs to a different account.
Always verify that the associated backup Amazon S3 bucket policy and ACLs do not grant unnecessary read or write permissions to principals that don't require access.
We recommend using Amazon S3 server-side encryption, enabling Amazon S3 server access logging, and Amazon S3 Versioning for both the target and backup buckets to enhance security and maintain an audit trail.
If the `Action` parameter is set to `Restore`, this runbook attempts to restore the Amazon S3 bucket's configuration to its original state based on the backup stored in the `BackupS3BucketName` bucket. Restoration to the exact previous state is not guaranteed, as changes in the account or associated Amazon S3 resources might have occurred between the time of containment and restoration. There is also a risk that the restoration process may fail, leaving the Amazon S3 bucket in an inconsistent state. The runbook provides instructions for manual restoration in case of such failures, but you should be prepared to handle potential issues during the restoration process.
It is recommended to review the runbook thoroughly, understand its potential impacts, and test it in a non-production environment before executing it in your production environment.

 **How does it work?**

This runbook operates differently based on the resource type and action:
+ For Amazon S3 General Purpose Bucket `Containment`: The automation blocks public access to the bucket, disables ACL configuration, enforces Bucket Owner Object ownership, and puts a restrictive bucket policy denying all Amazon S3 actions to the bucket except for allow listed IAM Roles.
+ For Amazon S3 General Purpose Object `Containment`: The automation blocks Public Access to bucket, disables ACL configuration, enforces Bucket Owner Object ownership, and puts a restrictive bucket policy denying all Amazon S3 actions on the object except for allow listed IAM Roles.
+ For Amazon S3 Directory Bucket `Containment`: The automation puts a restrictive bucket policy denying all Amazon S3 actions to the bucket except for allow listed IAM Roles.
+ For Amazon S3 General Purpose Bucket `Restore`: The automation restores the Block Public Access configuration, Bucket ACL configuration, Bucket Owner Object ownership and Bucket Policy to the initial configuration prior to containment.
+ For Amazon S3 General Purpose Object `Restore`: The automation restores the Block Public Access configuration, Bucket ACL configuration, Object ACL Configuration, Bucket Owner Object ownership and Bucket Policy to the initial configuration prior to containment.
+ For Amazon S3 Directory Bucket `Restore`: The automation restores the bucket policy to the initial configuration prior to containment.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ContainS3Resource)

 **Document Type**

 Automation

 **Owner**

 Amazon

 **Platform**

 /

 **Required IAM Permissions**

 The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ s3:CreateBucket
+ s3:DeleteBucketPolicy
+ s3:DeleteObjectTagging
+ s3:GetAccountPublicAccessBlock
+ s3:GetBucketAcl
+ s3:GetBucketLocation
+ s3:GetBucketOwnershipControls
+ s3:GetBucketPolicy
+ s3:GetBucketPolicyStatus
+ s3:GetBucketTagging
+ s3:GetEncryptionConfiguration
+ s3:GetObject
+ s3:GetObjectAcl
+ s3:GetObjectTagging
+ s3:GetReplicationConfiguration
+ s3:ListBucket
+ s3:PutAccountPublicAccessBlock
+ s3:PutBucketACL
+ s3:PutBucketOwnershipControls
+ s3:PutBucketPolicy
+ s3:PutBucketPublicAccessBlock
+ s3:PutBucketTagging
+ s3:PutBucketVersioning
+ s3:PutObject
+ s3:PutObjectAcl
+ s3express:CreateSession
+ s3express:DeleteBucketPolicy
+ s3express:GetBucketPolicy
+ s3express:PutBucketPolicy
+ ssm:DescribeAutomationExecutions

 Here is an example of an IAM policy that grants the necessary permissions for the `AutomationAssumeRole`:

------
#### [ JSON ]

****

```json
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "S3Permissions",
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucketPolicy",
                "s3:DeleteObjectTagging",
                "s3:GetAccountPublicAccessBlock",
                "s3:GetBucketAcl",
                "s3:GetBucketLocation",
                "s3:GetBucketOwnershipControls",
                "s3:GetBucketPolicy",
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketTagging",
                "s3:GetEncryptionConfiguration",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:GetObjectTagging",
                "s3:GetReplicationConfiguration",
                "s3:ListBucket",
                "s3:PutAccountPublicAccessBlock",
                "s3:PutBucketACL",
                "s3:PutBucketOwnershipControls",
                "s3:PutBucketPolicy",
                "s3:PutBucketPublicAccessBlock",
                "s3:PutBucketTagging",
                "s3:PutBucketVersioning",
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Resource": "*"
        },
        {
            "Sid": "S3ExpressPermissions",
            "Effect": "Allow",
            "Action": [
                "s3express:CreateSession",
                "s3express:DeleteBucketPolicy",
                "s3express:GetBucketPolicy",
                "s3express:PutBucketPolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "SSMPermissions",
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeAutomationExecutions"
            ],
            "Resource": "*"
        }
    ]
}
```

------

 **Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-ContainS3Resource`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ContainS3Resource/description) in Systems Manager under Documents.

1. Select Execute automation.

1. For the input parameters, enter the following:
   + **BucketName (Required):**
     + Description: (Required) The Amazon S3 bucket name.
     + Type: `AWS::S3::Bucket::Name`
   + **Action (Required):**
     + Description: (Required) Select `Contain` to isolate the target Amazon S3 bucket or object or `Restore` to try to restore the target resource to its original configuration from a previous backup.
     + Type: String
     + Allowed Values: `Contain|Restore`
   + **DryRun (Optional):**
     + Description: (Optional) When set to `true`, the automation will not make any changes to the target resource, instead it will output on what it would have attempted to change, detailing out on each step. Default value: `true`.
     + Type: Boolean
     + Allowed Values: `true|false`
   + **BucketKeyName (Optional):**
     + Description: (Optional) The key of the Amazon S3 object you want to contain or restore workflow. Used during object level containment.
     + Type: String
     + Allowed Pattern: `^[a-zA-Z0-9\\.\\-_\\\\!*'()/]{0,1024}$`
   + **BucketRestrictAccess (Optional):**
     + Description: (Optional) The ARN of the IAM users or roles that will be allowed access to the target Amazon S3 resource after running the containment actions. If not provided when Action is `Contain`, only the `AutomationAssumeRole` will be allowed access to the resource. Note: Either this parameter or `AutomationAssumeRole` must be provided when Action is `Contain`. The `AutomationAssumeRole`, or in its absence the user under whose context the automation is running is automatically added to the list.
     + Type: StringList
     + Allowed Pattern: `^$|^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):iam::[0-9]{12}:(role|user)\\/[\\w+\\/=,.@-]+$`
   + **TagIdentifier (Optional):**
     + Description: (Optional) Tag the Amazon S3 bucket principal with a tag of your choice using the following format: `Key=<EXAMPLE_KEY>,Value=<EXAMPLE_VALUE>`. This option allows you to track the Amazon S3 buckets that have been targeted by this runbook. Note: Tag keys and values are case-sensitive.
     + Type: String
     + Allowed Pattern: `^$|^[Kk][Ee][Yy]=[\\+\\-\\=\\.\\_\\:\\/@a-zA-Z0-9]{1,128},[Vv][Aa][Ll][Uu][Ee]=[\\+\\-\\=\\.\\_\\:\\/@a-zA-Z0-9]{0,128}$`
   + **BackupS3BucketName (Conditional):**
     + Description: (Conditional) The Amazon S3 bucket to backup the target resource configuration when the **Action** is set to `Contain` or to restore the configuration from when the **Action** is `Restore`. Note that if the specified **Action** is `Contain` and the runbook is not able to access the bucket or a value is not provided, a new bucket is created in your account with the name `awssupport-contains3resource-<random-string>`.
     + Type: `AWS::S3::Bucket::Name`
   + **BackupS3KeyName (Conditional):**
     + Description: (Conditional) If **Action** is set to `Restore`, this specifies the Amazon S3 key the automation will use to try to restore the target resource configuration. The Amazon S3 key typically follows this format: `{year}/{month}/{day}/{hour}/{minute}/{automation_execution_id}.json`. The key can be obtained from the output of a previous containment automation execution.
     + Type: String
     + Allowed Pattern: `^[a-zA-Z0-9\\.\\-_\\\\!*'()/]{0,1024}$`
   + **BackupS3BucketAccess (Conditional):**
     + Description: (Conditional) The ARN of the IAM users or roles that will be allowed access to the backup Amazon S3 bucket after running the containment actions. This parameter is required when Action is `Contain`. The `AutomationAssumeRole`, or in its absence the user under whose context the automation is running is automatically added to the list.
     + Type: StringList
     + Allowed Pattern: `^$|^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):iam::[0-9]{12}:(role|user)\\/[\\w+\\/=,.@-]+$`
   + **AutomationAssumeRole (Optional):**
     + Description: (Optional) The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     + Type: `AWS::IAM::Role::Arn`

1. Select Execute.

1. The automation initiates.

1. The document performs the following steps:
   + **ValidateRequiredInputs**

     Validates the required automation input parameters based on the **Action** specified.
   + **BranchOnTargetType**

     Branches the automation based on the target Amazon S3 resource: bucket or object.
   + **AssertObjectExists**

     Asserts if the target Amazon S3 object exists and it is accessible by calling the `HeadObject` API.
   + **AssertBucketExists**

     Asserts if the target Amazon S3 bucket exists and it is accessible by calling the `HeadBucket` API.
   + **CheckBackupS3BucketName**

     Checks if the backup Amazon S3 bucket potentially grants **read** or **write** public access to its objects. In case of containment workflow, a new Amazon S3 bucket is created if the `BackupS3BucketName` bucket doesn't exist.
   + **BranchOnActionAndDryRun**

     Branches the automation based on the value of the specified `Action` and if it is running in `DryRun` mode.
   + **ContainS3ResourceDryRun**

     Outputs dry run details for the containment actions.
   + **BackupTargetS3ResourceMetadata**

     Gets and stores the current configuration of the target Amazon S3 resource.
   + **ContainS3Resource**

     Performs the containment actions on the target Amazon S3 resource.
   + **RestoreS3ResourceDryRun**

     Outputs dry run details for the restoring actions.
   + **RestoreS3Resource**

     Restores the target Amazon S3 resource configuration from the backup.
   + **ReportContainmentFailure**

     Provides instructions to restore the target Amazon S3 resource original configuration during a containment workflow failure scenario.
   + **ReportRestoreFailure**

     Provides instructions to restore the target Amazon S3 resource original configuration during a restore workflow failure scenario.
   + **ContainFinalOutput**

     Outputs the details of the containment actions.
   + **RestoreFinalOutput**

     Outputs the details of the restoring actions.

1. After the execution completes, review the Outputs section for the detailed results of the execution:
   + **ContainFinalOutput.Output**

     Outputs the details of the containment actions performed by this runbook when `DryRun` is set to False.
   + **RestoreFinalOutput.Output**

     Outputs the details of the restore actions performed by this runbook when `DryRun` is set to False.
   + **ContainS3ResourceDryRun.Output**

     Outputs the details of the containment actions performed by this runbook when `DryRun` is set to True.
   + **RestoreS3ResourceDryRun.Output**

     Outputs the details of the restore actions performed by this runbook when `DryRun` is set to True.
   + **ReportContainmentFailure.Output**

     Provides instructions to restore the target Amazon S3 resource original configuration during a containment workflow failure scenario.
   + **ReportRestoreFailure.Output**

     Provides instructions to restore the target Amazon S3 resource original configuration during a restore workflow failure scenario.

**References**

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ContainS3Resource/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/)
