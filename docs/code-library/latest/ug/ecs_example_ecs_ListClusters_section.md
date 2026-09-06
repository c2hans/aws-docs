---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ecs_example_ecs_ListClusters_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListClusters` with an AWS SDK or CLI
<a name="ecs_example_ecs_ListClusters_section"></a>

The following code examples show how to use `ListClusters`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Get ARN information for clusters, services, and tasks](ecs_example_ecs_Scenario_GetClustersServicesAndTasks_section.md)

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/ECS#code-examples).

```
    /// <summary>
    /// List cluster ARNs available.
    /// </summary>
    /// <returns>The ARN list of clusters.</returns>
    public async Task<List<string>> GetClusterARNSAsync()
    {

        Console.WriteLine("Getting a list of all the clusters in your AWS account...");
        List<string> clusterArnList = new List<string>();
        // Get a list of all the clusters in your AWS account
        try
        {

            var listClustersResponse = _ecsClient.Paginators.ListClusters(new ListClustersRequest
            {
            });

            var clusterArns = listClustersResponse.ClusterArns;

            // Print the ARNs of the clusters
            await foreach (var clusterArn in clusterArns)
            {
                clusterArnList.Add(clusterArn);
            }

            if (clusterArnList.Count == 0)
            {
                _logger.LogWarning("No clusters found in your AWS account.");
            }
            return clusterArnList;
        }
        catch (Exception e)
        {
            _logger.LogError($"An error occurred while getting a list of all the clusters in your AWS account. {e.InnerException}");
            throw new Exception($"An error occurred while getting a list of all the clusters in your AWS account. {e.InnerException}");
        }
    }
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/goto/DotNetSDKV3/ecs-2014-11-13/ListClusters) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To list your available clusters**
The following `list-clusters` example lists all of the available clusters.

```
aws ecs list-clusters
```
Output:

```
{
    "clusterArns": [
        "arn:aws:ecs:us-west-2:123456789012:cluster/MyECSCluster1",
        "arn:aws:ecs:us-west-2:123456789012:cluster/AnotherECSCluster"
    ]
}
```
For more information, see [Amazon ECS Clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_clusters.html) in the *Amazon ECS Developer Guide*.
+  For API details, see [ListClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-clusters.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ecs#code-examples).

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ecs.EcsClient;
import software.amazon.awssdk.services.ecs.model.ListClustersResponse;
import software.amazon.awssdk.services.ecs.model.EcsException;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class ListClusters {
    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        EcsClient ecsClient = EcsClient.builder()
                .region(region)
                .build();

        listAllClusters(ecsClient);
        ecsClient.close();
    }

    public static void listAllClusters(EcsClient ecsClient) {
        try {
            ListClustersResponse response = ecsClient.listClusters();
            List<String> clusters = response.clusterArns();
            for (String cluster : clusters) {
                System.out.println("The cluster arn is " + cluster);
            }

        } catch (EcsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListClusters) in *AWS SDK for Java 2.x API Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This cmdlet returns a list of existing ECS clusters.**

```
Get-ECSClusterList
```
**Output:**

```
arn:aws:ecs:us-west-2:012345678912:cluster/LAB-ECS-CL
arn:aws:ecs:us-west-2:012345678912:cluster/LAB-ECS
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
