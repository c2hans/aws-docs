---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_DescribeUpdate_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeUpdate` with a CLI
<a name="eks_example_eks_DescribeUpdate_section"></a>

The following code examples show how to use `DescribeUpdate`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To describe an update for a cluster**
The following `describe-update` example describes an update for a cluster named.

```
aws eks describe-update \
    --name {{my-eks-cluster}} \
    --update-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "update": {
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "status": "Successful",
        "type": "EndpointAccessUpdate",
        "params": [
            {
                "type": "EndpointPublicAccess",
                "value": "false"
            },
            {
                "type": "EndpointPrivateAccess",
                "value": "true"
            }
        ],
        "createdAt": "2024-03-14T10:01:26.297000-04:00",
        "errors": []
    }
}
```
For more information, see [Updating an Amazon EKS cluster Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html) in the *Amazon EKS User Guide*.
**Example 2: To describe an update for a cluster**
The following `describe-update` example describes an update for a cluster named.

```
aws eks describe-update \
    --name {{my-eks-cluster}} \
    --update-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}
```
Output:

```
{
    "update": {
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "status": "Successful",
        "type": "AssociateEncryptionConfig",
        "params": [
            {
                "type": "EncryptionConfig",
                "value": "[{\"resources\":[\"secrets\"],\"provider\":{\"keyArn\":\"arn:aws:kms:region-code:account:key/key\"}}]"
            }
        ],
        "createdAt": "2024-03-14T11:01:26.297000-04:00",
        "errors": []
    }
}
```
For more information, see [Updating an Amazon EKS cluster Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html) in the *Amazon EKS User Guide*.
**Example 3: To describe an update for a cluster**
The following `describe-update` example describes an update for a cluster named.

```
aws eks describe-update \
    --name {{my-eks-cluster}} \
    --update-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}}
```
Output:

```
{
    "update": {
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
        "status": "Successful",
        "type": "VersionUpdate",
        "params": [
            {
                "type": "Version",
                "value": "1.29"
            },
            {
                "type": "PlatformVersion",
                "value": "eks.1"
            }
        ],
        "createdAt": "2024-03-14T12:05:26.297000-04:00",
        "errors": []
    }
}
```
For more information, see [Updating an Amazon EKS cluster Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html) in the *Amazon EKS User Guide*.
+  For API details, see [DescribeUpdate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-update.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [DescribeUpdate](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
