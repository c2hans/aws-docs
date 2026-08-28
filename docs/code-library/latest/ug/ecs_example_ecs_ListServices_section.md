---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ecs_example_ecs_ListServices_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListServices` with an AWS SDK or CLI
<a name="ecs_example_ecs_ListServices_section"></a>

The following code examples show how to use `ListServices`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Creating a container service for virtual machine instances](ecs_example_ecs_GettingStarted_018_section.md)
+  [Get ARN information for clusters, services, and tasks](ecs_example_ecs_Scenario_GetClustersServicesAndTasks_section.md)

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/ECS#code-examples).

```
    /// <summary>
    /// List service ARNs available.
    /// </summary>
    /// <param name="clusterARN">The arn of the ECS cluster.</param>
    /// <returns>The ARN list of services in given cluster.</returns>
    public async Task<List<string>> GetServiceARNSAsync(string clusterARN)
    {
        List<string> serviceArns = new List<string>();

        var request = new ListServicesRequest
        {
            Cluster = clusterARN
        };
        // Call the ListServices API operation and get the list of service ARNs
        var serviceList = _ecsClient.Paginators.ListServices(request);

        await foreach (var serviceARN in serviceList.ServiceArns)
        {
            if (serviceARN is null)
                continue;

            serviceArns.Add(serviceARN);
        }

        if (serviceArns.Count == 0)
        {
            _logger.LogWarning($"No services found in cluster {clusterARN} .");
        }

        return serviceArns;
    }
```
+  For API details, see [ListServices](https://docs.aws.amazon.com/goto/DotNetSDKV3/ecs-2014-11-13/ListServices) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To list the services in a cluster**
The following `list-services` example shows how to list the services running in a cluster.

```
aws ecs list-services --cluster {{MyCluster}}
```
Output:

```
 {
     "serviceArns": [
         "arn:aws:ecs:us-west-2:123456789012:service/MyCluster/MyService"
     ]
}
```
For more information, see [Services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) in the *Amazon ECS Developer Guide*.
+  For API details, see [ListServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-services.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists all services running in your default cluster.**

```
Get-ECSClusterService
```
**Example 2: This example lists all services running in the specified cluster.**

```
Get-ECSClusterService -Cluster myCluster
```
+  For API details, see [ListServices](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
