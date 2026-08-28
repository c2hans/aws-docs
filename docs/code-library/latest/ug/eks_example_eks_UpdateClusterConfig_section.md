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
**To update cluster endpoint access**
This example command updates a cluster to disable endpoint public access and enable private endpoint access.
Command:

```
aws eks update-cluster-config --name {{example}} \
--resources-vpc-config {{endpointPublicAccess=false,endpointPrivateAccess=true}}
```
Output:

```
{
    "update": {
        "id": "ec883c93-2e9e-407c-a22f-8f6fa6e67d4f",
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
**To enable logging for a cluster**
This example command enables all cluster control plane logging types for a cluster named `example`.
Command:

```
aws eks update-cluster-config --name {{example}} \
--logging '{{{"clusterLogging":[{"types":["api","audit","authenticator","controllerManager","scheduler"],"enabled":true}]}}}'
```
Output:

```
{
    "update": {
        "id": "7551c64b-1d27-4b1e-9f8e-c45f056eb6fd",
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
