---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/eks_example_eks_UpdateClusterConfig_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateClusterConfig` with a CLI
<a name="eks_example_eks_UpdateClusterConfig_section"></a>

The following code examples show how to use `UpdateClusterConfig`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To update cluster endpoint access**
The following `update-cluster-config` example updates a cluster to disable endpoint public access and enable private endpoint access.

```
aws eks update-cluster-config \
    --name {{example}} \
    --resources-vpc-config {{endpointPublicAccess=false,endpointPrivateAccess=true}}
```
Output:

```
{
    "update": {
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "status": "InProgress",
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
        "createdAt": 1565806986.506,
        "errors": []
    }
}
```
For more information, see [Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the *Amazon EKS User Guide*.
**Example 2: To enable logging for a cluster**
The following `update-cluster-config` example enables all cluster control plane logging types for a cluster named `example`.

```
aws eks update-cluster-config \
    --name {{example}} \
    --logging '{{{"clusterLogging":[{"types":["api","audit","authenticator","controllerManager","scheduler"],"enabled":true}]}}}'
```
Output:

```
{
    "update": {
        "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "status": "InProgress",
        "type": "LoggingUpdate",
        "params": [
            {
                "type": "ClusterLogging",
                "value": "{\"clusterLogging\":[{\"types\":[\"api\",\"audit\",\"authenticator\",\"controllerManager\",\"scheduler\"],\"enabled\":true}]}"
            }
        ],
        "createdAt": 1565807210.37,
        "errors": []
    }
}
```
For more information, see [Send control plane logs to CloudWatch Logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the *Amazon EKS User Guide*.
+  For API details, see [UpdateClusterConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-cluster-config.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [UpdateClusterConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
