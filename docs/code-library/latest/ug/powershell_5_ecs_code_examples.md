---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_ecs_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon ECS examples using Tools for PowerShell V5
<a name="powershell_5_ecs_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Amazon ECS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-ECSClusterDetail`
<a name="ecs_DescribeClusters_powershell_5_topic"></a>

The following code example shows how to use `Get-ECSClusterDetail`.

**Tools for PowerShell V5**
**Example 1: This cmdlet describes one or more of your ECS clusters.**

```
Get-ECSClusterDetail -Cluster "LAB-ECS-CL" -Include SETTINGS | Select-Object *
```
**Output:**

```
LoggedAt         : 12/27/2019 9:27:41 PM
Clusters         : {LAB-ECS-CL}
Failures         : {}
ResponseMetadata : Amazon.Runtime.ResponseMetadata
ContentLength    : 396
HttpStatusCode   : OK
```
+  For API details, see [DescribeClusters](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ECSClusterList`
<a name="ecs_ListClusters_powershell_5_topic"></a>

The following code example shows how to use `Get-ECSClusterList`.

**Tools for PowerShell V5**
**Example 1: This cmdlet returns a list of existing ECS clusters.**

```
Get-ECSClusterList
```
**Output:**

```
arn:aws:ecs:us-west-2:012345678912:cluster/LAB-ECS-CL
arn:aws:ecs:us-west-2:012345678912:cluster/LAB-ECS
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ECSClusterService`
<a name="ecs_ListServices_powershell_5_topic"></a>

The following code example shows how to use `Get-ECSClusterService`.

**Tools for PowerShell V5**
**Example 1: This example lists all services running in your default cluster.**

```
Get-ECSClusterService
```
**Example 2: This example lists all services running in the specified cluster.**

```
Get-ECSClusterService -Cluster myCluster
```
+  For API details, see [ListServices](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-ECSService`
<a name="ecs_DescribeServices_powershell_5_topic"></a>

The following code example shows how to use `Get-ECSService`.

**Tools for PowerShell V5**
**Example 1: This example shows how to retrieve details of a specific service from your default cluster.**

```
Get-ECSService -Service my-hhtp-service
```
**Example 2: This example shows how to retrieve details of a specific service running in the named cluster.**

```
Get-ECSService -Cluster myCluster -Service my-hhtp-service
```
+  For API details, see [DescribeServices](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ECSCluster`
<a name="ecs_CreateCluster_powershell_5_topic"></a>

The following code example shows how to use `New-ECSCluster`.

**Tools for PowerShell V5**
**Example 1: This cmdlet creates a new Amazon ECS cluster. **

```
New-ECSCluster -ClusterName "LAB-ECS-CL" -Setting @{Name="containerInsights"; Value="enabled"}
```
**Output:**

```
ActiveServicesCount               : 0
Attachments                       : {}
AttachmentsStatus                 :
CapacityProviders                 : {}
ClusterArn                        : arn:aws:ecs:us-west-2:012345678912:cluster/LAB-ECS-CL
ClusterName                       : LAB-ECS-CL
DefaultCapacityProviderStrategy   : {}
PendingTasksCount                 : 0
RegisteredContainerInstancesCount : 0
RunningTasksCount                 : 0
Settings                          : {containerInsights}
Statistics                        : {}
Status                            : ACTIVE
Tags                              : {}
```
+  For API details, see [CreateCluster](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-ECSService`
<a name="ecs_CreateService_powershell_5_topic"></a>

The following code example shows how to use `New-ECSService`.

**Tools for PowerShell V5**
**Example 1: This example command creates a service in your default cluster called `ecs-simple-service`. The service uses the `ecs-demo` task definition and it maintains 10 instantiations of that task.**

```
New-ECSService -ServiceName ecs-simple-service -TaskDefinition ecs-demo -DesiredCount 10
```
**Example 2: This example command creates a service behind a load balancer in your default cluster called `ecs-simple-service`. The service uses the `ecs-demo` task definition and it maintains 10 instantiations of that task.**

```
$lb = @{
    LoadBalancerName = "EC2Contai-EcsElast-S06278JGSJCM"
    ContainerName = "simple-demo"
    ContainerPort = 80
}
New-ECSService -ServiceName ecs-simple-service -TaskDefinition ecs-demo -DesiredCount 10 -LoadBalancer $lb
```
+  For API details, see [CreateService](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ECSCluster`
<a name="ecs_DeleteCluster_powershell_5_topic"></a>

The following code example shows how to use `Remove-ECSCluster`.

**Tools for PowerShell V5**
**Example 1: This cmdlet deletes the specified ECS cluster. You must deregister all container instances from this cluster before you may delete it. **

```
Remove-ECSCluster -Cluster "LAB-ECS"
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-ECSCluster (DeleteCluster)" on target "LAB-ECS".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteCluster](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-ECSService`
<a name="ecs_DeleteService_powershell_5_topic"></a>

The following code example shows how to use `Remove-ECSService`.

**Tools for PowerShell V5**
**Example 1: Deletes the service named 'my-http-service' in the default cluster. The service must have a desired count and running count of 0 before you can delete it. You are prompted for confirmation before the command proceeds. To bypass the confirmation prompt add the -Force switch.**

```
Remove-ECSService -Service my-http-service
```
**Example 2: Deletes the service named 'my-http-service' in the named cluster.**

```
Remove-ECSService -Cluster myCluster -Service my-http-service
```
+  For API details, see [DeleteService](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-ECSClusterSetting`
<a name="ecs_UpdateClusterSettings_powershell_5_topic"></a>

The following code example shows how to use `Update-ECSClusterSetting`.

**Tools for PowerShell V5**
**Example 1: This cmdlet modifies the settings to use for an ECS cluster.**

```
Update-ECSClusterSetting -Cluster "LAB-ECS-CL" -Setting @{Name="containerInsights"; Value="disabled"}
```
**Output:**

```
ActiveServicesCount               : 0
Attachments                       : {}
AttachmentsStatus                 :
CapacityProviders                 : {}
ClusterArn                        : arn:aws:ecs:us-west-2:012345678912:cluster/LAB-ECS-CL
ClusterName                       : LAB-ECS-CL
DefaultCapacityProviderStrategy   : {}
PendingTasksCount                 : 0
RegisteredContainerInstancesCount : 0
RunningTasksCount                 : 0
Settings                          : {containerInsights}
Statistics                        : {}
Status                            : ACTIVE
Tags                              : {}
```
+  For API details, see [UpdateClusterSettings](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-ECSService`
<a name="ecs_UpdateService_powershell_5_topic"></a>

The following code example shows how to use `Update-ECSService`.

**Tools for PowerShell V5**
**Example 1: This example command updates the `my-http-service` service to use the `amazon-ecs-sample` task definition.**

```
Update-ECSService -Service my-http-service -TaskDefinition amazon-ecs-sample
```
**Example 2: This example command updates the desired count of the `my-http-service` service to 10.**

```
Update-ECSService -Service my-http-service -DesiredCount 10
```
+  For API details, see [UpdateService](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
