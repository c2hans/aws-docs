---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_CreateNodegroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateNodegroup` with a CLI
<a name="eks_example_eks_CreateNodegroup_section"></a>

The following code examples show how to use `CreateNodegroup`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Getting started with managed kubernetes clusters](eks_example_eks_GettingStarted_034_section.md)

------
#### [ CLI ]

**AWS CLI**
**Example 1: Creates a managed node group for an Amazon EKS cluster**
The following `create-nodegroup` example creates a managed node group for an Amazon EKS cluster.

```
aws eks create-nodegroup \
    --cluster-name {{my-eks-cluster}} \
    --nodegroup-name {{my-eks-nodegroup}} \
    --node-role {{arn:aws:iam::111122223333:role/role-name}} \
    --subnets {{"subnet-0e2907431c9988b72"}} {{"subnet-04ad87f71c6e5ab4d"}} {{"subnet-09d912bb63ef21b9a"}} \
    --scaling-config {{minSize=1,maxSize=3,desiredSize=1}} \
    --region {{us-east-2}}
```
Output:

```
{
    "nodegroup": {
        "nodegroupName": "my-eks-nodegroup",
        "nodegroupArn": "arn:aws:eks:us-east-2:111122223333:nodegroup/my-eks-cluster/my-eks-nodegroup/bac7550f-b8b8-5fbb-4f3e-7502a931119e",
        "clusterName": "my-eks-cluster",
        "version": "1.26",
        "releaseVersion": "1.26.12-20240329",
        "createdAt": "2024-04-04T13:19:32.260000-04:00",
        "modifiedAt": "2024-04-04T13:19:32.260000-04:00",
        "status": "CREATING",
        "capacityType": "ON_DEMAND",
        "scalingConfig": {
            "minSize": 1,
            "maxSize": 3,
            "desiredSize": 1
        },
        "instanceTypes": [
            "t3.medium"
        ],
        "subnets": [
            "subnet-0e2907431c9988b72, subnet-04ad87f71c6e5ab4d, subnet-09d912bb63ef21b9a"
        ],
        "amiType": "AL2_x86_64",
        "nodeRole": "arn:aws:iam::111122223333:role/role-name",
        "diskSize": 20,
        "health": {
            "issues": []
        },
        "updateConfig": {
            "maxUnavailable": 1
        },
        "tags": {}
    }
}
```
For more information, see [Creating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/create-managed-node-group.html) in the *Amazon EKS User Guide*.
**Example 2: Creates a managed node group for an Amazon EKS cluster with custom instance-types and disk-size**
The following `create-nodegroup` example creates a managed node group for an Amazon EKS cluster with custom instance-types and disk-size.

```
aws eks create-nodegroup \
    --cluster-name {{my-eks-cluster}} \
    --nodegroup-name {{my-eks-nodegroup}} \
    --node-role {{arn:aws:iam::111122223333:role/role-name}} \
    --subnets {{"subnet-0e2907431c9988b72"}} {{"subnet-04ad87f71c6e5ab4d"}} {{"subnet-09d912bb63ef21b9a"}} \
    --scaling-config {{minSize=1,maxSize=3,desiredSize=1}} \
    --capacity-type {{ON_DEMAND}} \
    --instance-types '{{m5.large}}' \
    --disk-size {{50}} \
    --region {{us-east-2}}
```
Output:

```
{
    "nodegroup": {
        "nodegroupName": "my-eks-nodegroup",
        "nodegroupArn": "arn:aws:eks:us-east-2:111122223333:nodegroup/my-eks-cluster/my-eks-nodegroup/c0c7551b-e4f9-73d9-992c-a450fdb82322",
        "clusterName": "my-eks-cluster",
        "version": "1.26",
        "releaseVersion": "1.26.12-20240329",
        "createdAt": "2024-04-04T13:46:07.595000-04:00",
        "modifiedAt": "2024-04-04T13:46:07.595000-04:00",
        "status": "CREATING",
        "capacityType": "ON_DEMAND",
        "scalingConfig": {
            "minSize": 1,
            "maxSize": 3,
            "desiredSize": 1
        },
        "instanceTypes": [
            "m5.large"
        ],
        "subnets": [
            "subnet-0e2907431c9988b72",
            "subnet-04ad87f71c6e5ab4d",
            "subnet-09d912bb63ef21b9a"
        ],
        "amiType": "AL2_x86_64",
        "nodeRole": "arn:aws:iam::111122223333:role/role-name",
        "diskSize": 50,
        "health": {
            "issues": []
        },
        "updateConfig": {
            "maxUnavailable": 1
        },
        "tags": {}
    }
}
```
For more information, see [Creating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/create-managed-node-group.html) in the *Amazon EKS User Guide*.
**Example 3: Creates a managed node group for an Amazon EKS cluster with custom instance-types, disk-size, ami-type, capacity-type, update-config, labels, taints and tags.**
The following `create-nodegroup` example creates a managed node group for an Amazon EKS cluster with custom instance-types, disk-size, ami-type, capacity-type, update-config, labels, taints and tags.

```
aws eks create-nodegroup  \
    --cluster-name {{my-eks-cluster}} \
    --nodegroup-name {{my-eks-nodegroup}} \
    --node-role {{arn:aws:iam::111122223333:role/role-name}} \
    --subnets {{"subnet-0e2907431c9988b72"}} {{"subnet-04ad87f71c6e5ab4d"}} {{"subnet-09d912bb63ef21b9a"}} \
    --scaling-config {{minSize=1,maxSize=5,desiredSize=4}} \
    --instance-types '{{t3.large}}' \
    --disk-size {{50}} \
    --ami-type {{AL2_x86_64}} \
    --capacity-type {{SPOT}} \
    --update-config {{maxUnavailable=2}} \
    --labels '{{{"my-eks-nodegroup-label-1": "value-1" , "my-eks-nodegroup-label-2": "value-2"}}}' \
    --taints '{{{"key": "taint-key-1" , "value": "taint-value-1", "effect": "NO_EXECUTE"}}}' \
    --tags '{{{"my-eks-nodegroup-key-1": "value-1" , "my-eks-nodegroup-key-2": "value-2"}}}'
```
Output:

```
{
    "nodegroup": {
        "nodegroupName": "my-eks-nodegroup",
        "nodegroupArn": "arn:aws:eks:us-east-2:111122223333:nodegroup/my-eks-cluster/my-eks-nodegroup/88c75524-97af-0cb9-a9c5-7c0423ab5314",
        "clusterName": "my-eks-cluster",
        "version": "1.26",
        "releaseVersion": "1.26.12-20240329",
        "createdAt": "2024-04-04T14:05:07.940000-04:00",
        "modifiedAt": "2024-04-04T14:05:07.940000-04:00",
        "status": "CREATING",
        "capacityType": "SPOT",
        "scalingConfig": {
            "minSize": 1,
            "maxSize": 5,
            "desiredSize": 4
        },
        "instanceTypes": [
            "t3.large"
        ],
        "subnets": [
            "subnet-0e2907431c9988b72",
            "subnet-04ad87f71c6e5ab4d",
            "subnet-09d912bb63ef21b9a"
        ],
        "amiType": "AL2_x86_64",
        "nodeRole": "arn:aws:iam::111122223333:role/role-name",
        "labels": {
            "my-eks-nodegroup-label-2": "value-2",
            "my-eks-nodegroup-label-1": "value-1"
        },
        "taints": [
            {
                "key": "taint-key-1",
                "value": "taint-value-1",
                "effect": "NO_EXECUTE"
            }
        ],
        "diskSize": 50,
        "health": {
            "issues": []
        },
        "updateConfig": {
            "maxUnavailable": 2
        },
        "tags": {
            "my-eks-nodegroup-key-1": "value-1",
            "my-eks-nodegroup-key-2": "value-2"
        }
    }
}
```
For more information, see [Creating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/create-managed-node-group.html) in the *Amazon EKS User Guide*.
+  For API details, see [CreateNodegroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-nodegroup.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [CreateNodegroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
