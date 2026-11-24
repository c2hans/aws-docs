---
source_url: https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonFSxConsoleFullAccess.html
---

# AmazonFSxConsoleFullAccess

**Description**: Provides full access to Amazon FSx and access to related AWS services via the AWS Management Console.

`AmazonFSxConsoleFullAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonFSxConsoleFullAccess-how-to-use"></a>

You can attach `AmazonFSxConsoleFullAccess` to your users, groups, and roles.

## Policy details
<a name="AmazonFSxConsoleFullAccess-details"></a>
+ **Type**: AWS managed policy
+ **Creation time**: November 28, 2018, 16:36 UTC
+ **Edited time:** November 21, 2026, 20:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AmazonFSxConsoleFullAccess`

## Policy version
<a name="AmazonFSxConsoleFullAccess-version"></a>

**Policy version:** v21 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request.

## JSON policy document
<a name="AmazonFSxConsoleFullAccess-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ListResourcesAssociatedWithFSxFileSystem",
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:DescribeAlarms",
        "cloudwatch:GetMetricData",
        "ds:DescribeDirectories",
        "ec2:DescribeNetworkInterfaceAttribute",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeRouteTables",
        "ec2:DescribeSecurityGroups",
        "ec2:GetSecurityGroupsForVpc",
        "ec2:DescribeSubnets",
        "ec2:DescribeVpcs",
        "firehose:ListDeliveryStreams",
        "kms:ListAliases",
        "logs:DescribeLogGroups",
        "s3:ListBucket",
        "secretsmanager:ListSecrets"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "FullAccessToFSx",
      "Effect" : "Allow",
      "Action" : [
        "fsx:AssociateFileGateway",
        "fsx:AssociateFileSystemAliases",
        "fsx:CancelDataRepositoryTask",
        "fsx:CopyBackup",
        "fsx:CopySnapshotAndUpdateVolume",
        "fsx:CreateAndAttachS3AccessPoint",
        "fsx:CreateBackup",
        "fsx:CreateClusterPeer",
        "fsx:CreateDataRepositoryAssociation",
        "fsx:CreateDataRepositoryTask",
        "fsx:CreateFileCache",
        "fsx:CreateFileSystem",
        "fsx:CreateFileSystemFromBackup",
        "fsx:CreateSnapmirrorPolicy",
        "fsx:CreateSnapmirrorRelationship",
        "fsx:CreateSnapshot",
        "fsx:CreateSnapshotPolicy",
        "fsx:CreateStorageVirtualMachine",
        "fsx:CreateStorageVirtualMachinePeer",
        "fsx:CreateVolume",
        "fsx:CreateVolumeFromBackup",
        "fsx:DeleteBackup",
        "fsx:DeleteClusterPeer",
        "fsx:DeleteDataRepositoryAssociation",
        "fsx:DeleteFileCache",
        "fsx:DeleteFileSystem",
        "fsx:DeleteSnapmirrorPolicy",
        "fsx:DeleteSnapmirrorRelationship",
        "fsx:DeleteSnapshot",
        "fsx:DeleteSnapshotPolicy",
        "fsx:DeleteStorageVirtualMachine",
        "fsx:DeleteStorageVirtualMachinePeer",
        "fsx:DeleteVolume",
        "fsx:DescribeAssociatedFileGateways",
        "fsx:DescribeBackups",
        "fsx:DescribeClusterPeers",
        "fsx:DescribeDataRepositoryAssociations",
        "fsx:DescribeDataRepositoryTasks",
        "fsx:DescribeFileCaches",
        "fsx:DescribeFileSystemAliases",
        "fsx:DescribeFileSystems",
        "fsx:DescribeS3AccessPointAttachments",
        "fsx:DescribeSharedVpcConfiguration",
        "fsx:DescribeSnapmirrorPolicies",
        "fsx:DescribeSnapmirrorRelationships",
        "fsx:DescribeSnapshotPolicies",
        "fsx:DescribeSnapshots",
        "fsx:DescribeStorageVirtualMachinePeers",
        "fsx:DescribeStorageVirtualMachines",
        "fsx:DescribeVolumes",
        "fsx:DetachAndDeleteS3AccessPoint",
        "fsx:DisassociateFileGateway",
        "fsx:DisassociateFileSystemAliases",
        "fsx:ListTagsForResource",
        "fsx:ManageBackupPrincipalAssociations",
        "fsx:ReleaseFileSystemNfsV3Locks",
        "fsx:RestoreVolumeFromSnapshot",
        "fsx:TagResource",
        "fsx:UntagResource",
        "fsx:UpdateClusterPeer",
        "fsx:UpdateDataRepositoryAssociation",
        "fsx:UpdateFileCache",
        "fsx:UpdateFileSystem",
        "fsx:UpdateSharedVpcConfiguration",
        "fsx:UpdateSnapmirrorPolicy",
        "fsx:UpdateSnapmirrorRelationship",
        "fsx:UpdateSnapshot",
        "fsx:UpdateSnapshotPolicy",
        "fsx:UpdateStorageVirtualMachine",
        "fsx:UpdateStorageVirtualMachinePeer",
        "fsx:UpdateVolume"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "CreateFSxSLR",
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : [
            "fsx.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid" : "CreateSLRForLustreS3Integration",
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : [
            "s3.data-source.lustre.fsx.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid" : "CreateTags",
      "Effect" : "Allow",
      "Action" : [
        "ec2:CreateTags"
      ],
      "Resource" : [
        "arn:aws:ec2:*:*:route-table/*"
      ],
      "Condition" : {
        "StringEquals" : {
          "aws:RequestTag/AmazonFSx" : "ManagedByAmazonFSx"
        },
        "ForAnyValue:StringEquals" : {
          "aws:CalledVia" : [
            "fsx.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid" : "ManageCrossAccountDataReplication",
      "Effect" : "Allow",
      "Action" : [
        "fsx:PutResourcePolicy",
        "fsx:GetResourcePolicy",
        "fsx:DeleteResourcePolicy"
      ],
      "Resource" : "*",
      "Condition" : {
        "ForAnyValue:StringEquals" : {
          "aws:CalledVia" : [
            "ram.amazonaws.com"
          ]
        }
      }
    }
  ]
}
```

## Learn more
<a name="AmazonFSxConsoleFullAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html)
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)
