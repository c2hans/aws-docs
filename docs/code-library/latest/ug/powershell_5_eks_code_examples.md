---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_eks_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon EKS examples using Tools for PowerShell V5
<a name="powershell_5_eks_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Amazon EKS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-EKSResourceTag`
<a name="eks_TagResource_powershell_5_topic"></a>

The following code example shows how to use `Add-EKSResourceTag`.

**Tools for PowerShell V5**
**Example 1: This cmdlet associates the specified tags to a resource with the specified resourceArn. **

```
Add-EKSResourceTag -ResourceArn "arn:aws:eks:us-west-2:012345678912:cluster/PROD" -Tag @{Name = "EKSPRODCLUSTER"}
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-EKSCluster`
<a name="eks_DescribeCluster_powershell_5_topic"></a>

The following code example shows how to use `Get-EKSCluster`.

**Tools for PowerShell V5**
**Example 1: This cmdlet returns descriptive information about an Amazon EKS cluster.**

```
Get-EKSCluster -Name "PROD"
```
**Output:**

```
Arn                  : arn:aws:eks:us-west-2:012345678912:cluster/PROD
CertificateAuthority : Amazon.EKS.Model.Certificate
ClientRequestToken   :
CreatedAt            : 12/25/2019 6:46:17 AM
Endpoint             : https://669608765450FBBE54D1D78A3D71B72C.gr8.us-west-2.eks.amazonaws.com
Identity             : Amazon.EKS.Model.Identity
Logging              : Amazon.EKS.Model.Logging
Name                 : PROD
PlatformVersion      : eks.7
ResourcesVpcConfig   : Amazon.EKS.Model.VpcConfigResponse
RoleArn              : arn:aws:iam::012345678912:role/eks-iam-role
Status               : ACTIVE
Tags                 : {}
Version              : 1.14
```
+  For API details, see [DescribeCluster](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-EKSClusterList`
<a name="eks_ListClusters_powershell_5_topic"></a>

The following code example shows how to use `Get-EKSClusterList`.

**Tools for PowerShell V5**
**Example 1: This cmdlet lists the Amazon EKS clusters in your AWS account in the specified Region.**

```
Get-EKSClusterList
```
**Output:**

```
 PROD
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-EKSFargateProfile`
<a name="eks_DescribeFargateProfile_powershell_5_topic"></a>

The following code example shows how to use `Get-EKSFargateProfile`.

**Tools for PowerShell V5**
**Example 1: This cmdlet returns descriptive information about an AWS Fargate profile.**

```
Get-EKSFargateProfile -FargateProfileName "EKSFargate" -ClusterName "TEST"
```
**Output:**

```
ClusterName         : TEST
CreatedAt           : 12/26/2019 12:34:47 PM
FargateProfileArn   : arn:aws:eks:us-east-2:012345678912:fargateprofile/TEST/EKSFargate/42b7a119-e16b-a279-ce97-bdf303adec92
FargateProfileName  : EKSFargate
PodExecutionRoleArn : arn:aws:iam::012345678912:role/AmazonEKSFargatePodExecutionRole
Selectors           : {Amazon.EKS.Model.FargateProfileSelector}
Status              : ACTIVE
Subnets             : {subnet-0cd976f08d5fbfaae, subnet-02f6ff500ff2067a0}
Tags                : {}
```
+  For API details, see [DescribeFargateProfile](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-EKSFargateProfileList`
<a name="eks_ListFargateProfiles_powershell_5_topic"></a>

The following code example shows how to use `Get-EKSFargateProfileList`.

**Tools for PowerShell V5**
**Example 1: This cmdlet lists the AWS Fargate profiles associated with the specified cluster in your AWS account in the specified Region.**

```
Get-EKSFargateProfileList -ClusterName "TEST"
```
**Output:**

```
EKSFargate
EKSFargateProfile
```
+  For API details, see [ListFargateProfiles](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-EKSNodegroup`
<a name="eks_DescribeNodegroup_powershell_5_topic"></a>

The following code example shows how to use `Get-EKSNodegroup`.

**Tools for PowerShell V5**
**Example 1: This cmdlet returns descriptive information about an Amazon EKS node group.**

```
Get-EKSNodegroup -NodegroupName "ProdEKSNodeGroup" -ClusterName "PROD"
```
**Output:**

```
AmiType        : AL2_x86_64
ClusterName    : PROD
CreatedAt      : 12/25/2019 10:16:45 AM
DiskSize       : 40
Health         : Amazon.EKS.Model.NodegroupHealth
InstanceTypes  : {t3.large}
Labels         : {}
ModifiedAt     : 12/25/2019 10:16:45 AM
NodegroupArn   : arn:aws:eks:us-west-2:012345678912:nodegroup/PROD/ProdEKSNodeGroup/7eb79e47-82b6-04d9-e984-95110db6fa85
NodegroupName  : ProdEKSNodeGroup
NodeRole       : arn:aws:iam::012345678912:role/NodeInstanceRole
ReleaseVersion : 1.14.7-20190927
RemoteAccess   :
Resources      :
ScalingConfig  : Amazon.EKS.Model.NodegroupScalingConfig
Status         : CREATING
Subnets        : {subnet-0d1a9fff35efa7691, subnet-0a3f4928edbc224d4}
Tags           : {}
Version        : 1.14
```
+  For API details, see [DescribeNodegroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-EKSNodegroupList`
<a name="eks_ListNodegroups_powershell_5_topic"></a>

The following code example shows how to use `Get-EKSNodegroupList`.

**Tools for PowerShell V5**
**Example 1: This cmdlet lists the Amazon EKS node groups associated with the specified cluster in your AWS account in the specified Region. **

```
Get-EKSNodegroupList -ClusterName PROD
```
**Output:**

```
 ProdEKSNodeGroup
```
+  For API details, see [ListNodegroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-EKSResourceTag`
<a name="eks_ListTagsForResource_powershell_5_topic"></a>

The following code example shows how to use `Get-EKSResourceTag`.

**Tools for PowerShell V5**
**Example 1: This cmdlet list the tags for an Amazon EKS resource. **

```
Get-EKSResourceTag -ResourceArn "arn:aws:eks:us-west-2:012345678912:cluster/PROD"
```
**Output:**

```
Key  Value
---  -----
Name EKSPRODCLUSTER
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-EKSUpdate`
<a name="eks_DescribeUpdate_powershell_5_topic"></a>

The following code example shows how to use `Get-EKSUpdate`.

**Tools for PowerShell V5**
**Example 1: This cmdlet returns descriptive information about an update against your Amazon EKS cluster or associated managed node group. **

```
Get-EKSUpdate -Name "PROD" -UpdateId "ee708232-7d2e-4ed7-9270-d0b5176f0726"
```
**Output:**

```
CreatedAt : 12/25/2019 5:03:07 PM
Errors    : {}
Id        : ee708232-7d2e-4ed7-9270-d0b5176f0726
Params    : {Amazon.EKS.Model.UpdateParam}
Status    : Successful
Type      : LoggingUpdate
```
+  For API details, see [DescribeUpdate](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-EKSUpdateList`
<a name="eks_ListUpdates_powershell_5_topic"></a>

The following code example shows how to use `Get-EKSUpdateList`.

**Tools for PowerShell V5**
**Example 1: This cmdlet lists the updates associated with an Amazon EKS cluster or managed node group in your AWS account, in the specified Region.**

```
Get-EKSUpdateList -Name "PROD"
```
**Output:**

```
ee708232-7d2e-4ed7-9270-d0b5176f0726
```
+  For API details, see [ListUpdates](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-EKSCluster`
<a name="eks_CreateCluster_powershell_5_topic"></a>

The following code example shows how to use `New-EKSCluster`.

**Tools for PowerShell V5**
**Example 1: This example creates a new cluster called 'prod'.**

```
New-EKSCluster -Name prod -ResourcesVpcConfig @{SubnetIds=@("subnet-0a1b2c3d","subnet-3a2b1c0d");SecurityGroupIds="sg-6979fe18"} -RoleArn "arn:aws:iam::012345678901:role/eks-service-role"
```
**Output:**

```
Arn                  : arn:aws:eks:us-west-2:012345678901:cluster/prod
CertificateAuthority : Amazon.EKS.Model.Certificate
ClientRequestToken   :
CreatedAt            : 12/10/2018 9:25:31 PM
Endpoint             :
Name                 : prod
PlatformVersion      : eks.3
ResourcesVpcConfig   : Amazon.EKS.Model.VpcConfigResponse
RoleArn              : arn:aws:iam::012345678901:role/eks-service-role
Status               : CREATING
Version              : 1.10
```
+  For API details, see [CreateCluster](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-EKSFargateProfile`
<a name="eks_CreateFargateProfile_powershell_5_topic"></a>

The following code example shows how to use `New-EKSFargateProfile`.

**Tools for PowerShell V5**
**Example 1: This cmdlet creates an AWS Fargate profile for your Amazon EKS cluster. You must have at least one Fargate profile in a cluster to be able to schedule pods on Fargate infrastructure. **

```
New-EKSFargateProfile -FargateProfileName EKSFargateProfile -ClusterName TEST -Subnet "subnet-02f6ff500ff2067a0", "subnet-0cd976f08d5fbfaae" -PodExecutionRoleArn arn:aws:iam::012345678912:role/AmazonEKSFargatePodExecutionRole -Selector @{Namespace="default"}
```
**Output:**

```
ClusterName         : TEST
CreatedAt           : 12/26/2019 12:38:21 PM
FargateProfileArn   : arn:aws:eks:us-east-2:012345678912:fargateprofile/TEST/EKSFargateProfile/20b7a11b-8292-41c1-bc56-ffa5e60f6224
FargateProfileName  : EKSFargateProfile
PodExecutionRoleArn : arn:aws:iam::012345678912:role/AmazonEKSFargatePodExecutionRole
Selectors           : {Amazon.EKS.Model.FargateProfileSelector}
Status              : CREATING
Subnets             : {subnet-0cd976f08d5fbfaae, subnet-02f6ff500ff2067a0}
Tags                : {}
```
+  For API details, see [CreateFargateProfile](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-EKSNodeGroup`
<a name="eks_CreateNodegroup_powershell_5_topic"></a>

The following code example shows how to use `New-EKSNodeGroup`.

**Tools for PowerShell V5**
**Example 1: This cmdlet creates a managed worker node group for an Amazon EKS cluster. You can only create a node group for your cluster that is equal to the current Kubernetes version for the cluster. All node groups are created with the latest AMI release version for the respective minor Kubernetes version of the cluster. **

```
New-EKSNodeGroup -NodeGroupName "ProdEKSNodeGroup" -AmiType "AL2_x86_64" -DiskSize 40 -ClusterName "PROD" -ScalingConfig_DesiredSize 2 -ScalingConfig_MinSize 2 -ScalingConfig_MaxSize 5 -InstanceType t3.large -NodeRole "arn:aws:iam::012345678912:role/NodeInstanceRole" -Subnet "subnet-0d1a9fff35efa7691","subnet-0a3f4928edbc224d4"
```
**Output:**

```
AmiType        : AL2_x86_64
ClusterName    : PROD
CreatedAt      : 12/25/2019 10:16:45 AM
DiskSize       : 40
Health         : Amazon.EKS.Model.NodegroupHealth
InstanceTypes  : {t3.large}
Labels         : {}
ModifiedAt     : 12/25/2019 10:16:45 AM
NodegroupArn   : arn:aws:eks:us-west-2:012345678912:nodegroup/PROD/ProdEKSNodeGroup/7eb79e47-82b6-04d9-e984-95110db6fa85
NodegroupName  : ProdEKSNodeGroup
NodeRole       : arn:aws:iam::012345678912:role/NodeInstanceRole
ReleaseVersion : 1.14.7-20190927
RemoteAccess   :
Resources      :
ScalingConfig  : Amazon.EKS.Model.NodegroupScalingConfig
Status         : CREATING
Subnets        : {subnet-0d1a9fff35efa7691, subnet-0a3f4928edbc224d4}
Tags           : {}
Version        : 1.14
```
+  For API details, see [CreateNodegroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-EKSCluster`
<a name="eks_DeleteCluster_powershell_5_topic"></a>

The following code example shows how to use `Remove-EKSCluster`.

**Tools for PowerShell V5**
**Example 1: This cmdlet deletes the Amazon EKS cluster control plane.**

```
Remove-EKSCluster -Name "DEV-KUBE-CL"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EKSCluster (DeleteCluster)" on target "DEV-KUBE-CL".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

Arn                  : arn:aws:eks:us-west-2:012345678912:cluster/DEV-KUBE-CL
CertificateAuthority : Amazon.EKS.Model.Certificate
ClientRequestToken   :
CreatedAt            : 12/25/2019 9:33:25 AM
Endpoint             : https://02E6D31E3E4F8C15D7BE7F58D527776A.yl4.us-west-2.eks.amazonaws.com
Identity             : Amazon.EKS.Model.Identity
Logging              : Amazon.EKS.Model.Logging
Name                 : DEV-KUBE-CL
PlatformVersion      : eks.7
ResourcesVpcConfig   : Amazon.EKS.Model.VpcConfigResponse
RoleArn              : arn:aws:iam::012345678912:role/eks-iam-role
Status               : DELETING
Tags                 : {}
Version              : 1.14
```
+  For API details, see [DeleteCluster](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-EKSFargateProfile`
<a name="eks_DeleteFargateProfile_powershell_5_topic"></a>

The following code example shows how to use `Remove-EKSFargateProfile`.

**Tools for PowerShell V5**
**Example 1: This cmdlet deletes an AWS Fargate profile. When you delete a Fargate profile, any pods running on Fargate that were created with the profile are deleted. **

```
Remove-EKSFargateProfile -FargateProfileName "EKSFargate" -ClusterName "TEST"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EKSFargateProfile (DeleteFargateProfile)" on target "EKSFargate".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

ClusterName         : TEST
CreatedAt           : 12/26/2019 12:34:47 PM
FargateProfileArn   : arn:aws:eks:us-east-2:012345678912:fargateprofile/TEST/EKSFargate/42b7a119-e16b-a279-ce97-bdf303adec92
FargateProfileName  : EKSFargate
PodExecutionRoleArn : arn:aws:iam::012345678912:role/AmazonEKSFargatePodExecutionRole
Selectors           : {Amazon.EKS.Model.FargateProfileSelector}
Status              : DELETING
Subnets             : {subnet-0cd976f08d5fbfaae, subnet-02f6ff500ff2067a0}
Tags                : {}
```
+  For API details, see [DeleteFargateProfile](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-EKSNodegroup`
<a name="eks_DeleteNodegroup_powershell_5_topic"></a>

The following code example shows how to use `Remove-EKSNodegroup`.

**Tools for PowerShell V5**
**Example 1: This cmdlet deletes an Amazon EKS node group for a cluster.**

```
Remove-EKSNodegroup -NodegroupName "ProdEKSNodeGroup" -ClusterName "PROD"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EKSNodegroup (DeleteNodegroup)" on target "ProdEKSNodeGroup".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

AmiType        : AL2_x86_64
ClusterName    : PROD
CreatedAt      : 12/25/2019 10:16:45 AM
DiskSize       : 40
Health         : Amazon.EKS.Model.NodegroupHealth
InstanceTypes  : {t3.large}
Labels         : {}
ModifiedAt     : 12/25/2019 11:01:16 AM
NodegroupArn   : arn:aws:eks:us-west-2:012345678912:nodegroup/PROD/ProdEKSNodeGroup/7eb79e47-82b6-04d9-e984-95110db6fa85
NodegroupName  : ProdEKSNodeGroup
NodeRole       : arn:aws:iam::012345678912:role/NodeInstanceRole
ReleaseVersion : 1.14.7-20190927
RemoteAccess   :
Resources      : Amazon.EKS.Model.NodegroupResources
ScalingConfig  : Amazon.EKS.Model.NodegroupScalingConfig
Status         : DELETING
Subnets        : {subnet-0d1a9fff35efa7691, subnet-0a3f4928edbc224d4}
Tags           : {}
Version        : 1.14
```
+  For API details, see [DeleteNodegroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-EKSResourceTag`
<a name="eks_UntagResource_powershell_5_topic"></a>

The following code example shows how to use `Remove-EKSResourceTag`.

**Tools for PowerShell V5**
**Example 1: This cmdlet deletes specified tags from an EKS resource.**

```
Remove-EKSResourceTag -ResourceArn "arn:aws:eks:us-west-2:012345678912:cluster/PROD" -TagKey "Name"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EKSResourceTag (UntagResource)" on target "arn:aws:eks:us-west-2:012345678912:cluster/PROD".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [UntagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-EKSClusterConfig`
<a name="eks_UpdateClusterConfig_powershell_5_topic"></a>

The following code example shows how to use `Update-EKSClusterConfig`.

**Tools for PowerShell V5**
**Example 1: Updates an Amazon EKS cluster configuration. Your cluster continues to function during the update.**

```
Update-EKSClusterConfig -Name "PROD" -Logging_ClusterLogging @{Types="api","audit","authenticator","controllerManager","scheduler",Enabled="True"}
```
**Output:**

```
CreatedAt : 12/25/2019 5:03:07 PM
Errors    : {}
Id        : ee708232-7d2e-4ed7-9270-d0b5176f0726
Params    : {Amazon.EKS.Model.UpdateParam}
Status    : InProgress
Type      : LoggingUpdate
```
+  For API details, see [UpdateClusterConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-EKSClusterVersion`
<a name="eks_UpdateClusterVersion_powershell_5_topic"></a>

The following code example shows how to use `Update-EKSClusterVersion`.

**Tools for PowerShell V5**
**Example 1: This cmdlet updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update.**

```
Update-EKSClusterVersion -Name "PROD-KUBE-CL" -Version 1.14
```
**Output:**

```
CreatedAt : 12/26/2019 9:50:37 AM
Errors    : {}
Id        : ef186eff-3b3a-4c25-bcfc-3dcdf9e898a8
Params    : {Amazon.EKS.Model.UpdateParam, Amazon.EKS.Model.UpdateParam}
Status    : InProgress
Type      : VersionUpdate
```
+  For API details, see [UpdateClusterVersion](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
