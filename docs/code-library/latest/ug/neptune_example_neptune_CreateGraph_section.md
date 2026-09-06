---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/neptune_example_neptune_CreateGraph_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateGraph` with an AWS SDK
<a name="neptune_example_neptune_CreateGraph_section"></a>

The following code examples show how to use `CreateGraph`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](neptune_example_neptune_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Executes the process of creating a new Neptune graph.
     *
     * @param client        the Neptune graph client used to interact with the Neptune service
     * @param graphName     the name of the graph to be created
     * @throws NeptuneGraphException if an error occurs while creating the graph
     */
    public static void executeCreateGraph(NeptuneGraphClient client, String graphName) {
        try {
            // Create the graph request
            CreateGraphRequest request = CreateGraphRequest.builder()
                    .graphName(graphName)
                    .provisionedMemory(16)
                    .build();

            // Create the graph
            CreateGraphResponse response = client.createGraph(request);

            // Extract the graph name and ARN
            String createdGraphName = response.name();
            String graphArn = response.arn();
            String graphEndpoint = response.endpoint();

            System.out.println("Graph created successfully!");
            System.out.println("Graph Name: " + createdGraphName);
            System.out.println("Graph ARN: " + graphArn);
            System.out.println("Graph Endpoint: " +graphEndpoint );

        } catch (NeptuneGraphException e) {
            System.err.println("Failed to create graph: " + e.awsErrorDetails().errorMessage());
        } finally {
            client.close();
        }
   }
```
+  For API details, see [CreateGraph](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/CreateGraph) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
"""
Running this example.

----------------------------------------------------------------------------------
VPC Networking Requirement:
----------------------------------------------------------------------------------
Amazon Neptune must be accessed from **within the same VPC** as the Neptune cluster.
It does not expose a public endpoint, so this code must be executed from:

  - An **AWS Lambda function** configured to run inside the same VPC
  - An **EC2 instance** or **ECS task** running in the same VPC
  - A connected environment such as a **VPN**, **AWS Direct Connect**, or a **peered VPC**

"""

GRAPH_NAME = "sample-analytics-graph"

def main():
    config = Config(retries={"total_max_attempts": 1, "mode": "standard"}, read_timeout=None)
    client = boto3.client("neptune-graph", config=config)
    execute_create_graph(client, GRAPH_NAME)

def execute_create_graph(client, graph_name):
    try:
        print("Creating Neptune graph...")
        response = client.create_graph(
            graphName=graph_name,
            provisionedMemory = 16
        )

        created_graph_name = response.get("name")
        graph_arn = response.get("arn")
        graph_endpoint = response.get("endpoint")

        print("Graph created successfully!")
        print(f"Graph Name: {created_graph_name}")
        print(f"Graph ARN: {graph_arn}")
        print(f"Graph Endpoint: {graph_endpoint}")

    except ClientError as e:
        print(f"Failed to create graph: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"Failed to create graph: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
+  For API details, see [CreateGraph](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/CreateGraph) in *AWS SDK for Python (Boto3) API Reference*.

------
