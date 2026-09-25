---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ecs_example_ecs_Hello_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Hello Amazon ECS
<a name="ecs_example_ecs_Hello_section"></a>

The following code examples show how to get started using Amazon ECS.

------
#### [ .NET ]

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/ECS#code-examples).

```
using Amazon.ECS;
using Amazon.ECS.Model;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Logging.Console;
using Microsoft.Extensions.Logging.Debug;

namespace ECSActions;

/// <summary>
/// A class that introduces the Amazon ECS Client by listing the
/// cluster ARNs for the account.
/// </summary>
public class HelloECS
{
    static async System.Threading.Tasks.Task Main(string[] args)
    {
        // Use the AWS .NET Core Setup package to set up dependency injection for the Amazon ECS client.
        // Use your AWS profile name, or leave it blank to use the default profile.
        using var host = Host.CreateDefaultBuilder(args)
            .ConfigureLogging(logging =>
                logging.AddFilter("System", LogLevel.Debug)
                    .AddFilter<DebugLoggerProvider>("Microsoft", LogLevel.Information)
                    .AddFilter<ConsoleLoggerProvider>("Microsoft", LogLevel.Trace))
            .ConfigureServices((_, services) =>
                services.AddAWSService<IAmazonECS>()
            )
            .Build();

        var amazonECSClient = host.Services.GetRequiredService<IAmazonECS>();

        Console.WriteLine($"Hello Amazon ECS! Following are some cluster ARNS available in the your account");
        Console.WriteLine();

        var clusters = new List<string>();

        var clustersPaginator = amazonECSClient.Paginators.ListClusters(new ListClustersRequest());

        await foreach (var response in clustersPaginator.Responses)
        {
            clusters.AddRange(response.ClusterArns);
        }

        if (clusters.Count > 0)
        {
            clusters.ForEach(cluster =>
            {
                Console.WriteLine($"\tARN: {cluster}");
                Console.WriteLine($"Cluster Name: {cluster.Split("/").Last()}");
                Console.WriteLine();
            });
        }
        else
        {
            Console.WriteLine("No clusters were found.");
        }

    }
}
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListClusters) in *AWS SDK for .NET API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ecs#code-examples).

```
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def hello_ecs():
    """
    Lists the Amazon ECS clusters in the current AWS region.
    Uses a paginator to handle large numbers of clusters.
    """
    ecs_client = boto3.client("ecs")
    try:
        paginator = ecs_client.get_paginator("list_clusters")
        cluster_arns = list()
        for page in paginator.paginate():
            cluster_arns.extend(page.get("clusterArns", list()))
        if cluster_arns:
            print(f"Found {len(cluster_arns)} ECS cluster(s):")
            for arn in cluster_arns:
                print(f"  - {arn}")
        else:
            print("No ECS clusters found in the current region.")
    except ClientError as err:
        logger.error(
            "Error listing ECS clusters: %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise

if __name__ == "__main__":
    hello_ecs()
```
+  For API details, see [ListClusters](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListClusters) in *AWS SDK for Python (Boto3) API Reference*.

------
