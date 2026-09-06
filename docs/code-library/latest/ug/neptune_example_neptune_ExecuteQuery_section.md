---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/neptune_example_neptune_ExecuteQuery_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ExecuteQuery` with an AWS SDK
<a name="neptune_example_neptune_ExecuteQuery_section"></a>

The following code examples show how to use `ExecuteQuery`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](neptune_example_neptune_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Executes a Gremlin profile query on the Neptune Analytics graph.
     *
     * @param client       the {@link NeptuneGraphClient} instance to use for the query
     * @param graphId      the identifier of the graph to execute the query on
     *
     * @throws NeptuneGraphException if an error occurs while executing the query on the Neptune Graph
     * @throws Exception if an unexpected error occurs
     */
    public static void executeGremlinProfileQuery(NeptuneGraphClient client, String graphId) {

        try {
            System.out.println("Running openCypher query on Neptune Analytics...");

            ExecuteQueryRequest request = ExecuteQueryRequest.builder()
                    .graphIdentifier(graphId)
                    .queryString("MATCH (n {code: 'ANC'}) RETURN n")
                    .language("OPEN_CYPHER")
                    .build();

            ResponseInputStream<ExecuteQueryResponse> response = client.executeQuery(request);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(response, StandardCharsets.UTF_8))) {
                String result = reader.lines().collect(Collectors.joining("\n"));
                System.out.println("Query Result:");
                System.out.println(result);
            } catch (Exception e) {
                System.err.println("Error reading response: " + e.getMessage());
            }

        } catch (NeptuneGraphException e) {
            System.err.println("NeptuneGraph error: " + e.awsErrorDetails().errorMessage());
        } catch (Exception e) {
            System.err.println("Unexpected error: " + e.getMessage());
        } finally {
            client.close();
        }
    }
```
+  For API details, see [ExecuteQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteQuery) in *AWS SDK for Java 2.x API Reference*.

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

GRAPH_ID = "<your-graph-id>"

def main():
    config = Config(retries={"total_max_attempts": 1, "mode": "standard"}, read_timeout=None)
    client = boto3.client("neptune-graph", config=config)

    try:
        print("\n--- Running OpenCypher query without parameters ---")
        run_open_cypher_query(client, GRAPH_ID)

        print("\n--- Running OpenCypher query with parameters ---")
        run_open_cypher_query_with_params(client, GRAPH_ID)

        print("\n--- Running OpenCypher explain query ---")
        run_open_cypher_explain_query(client, GRAPH_ID)

    except Exception as e:
        print(f"Unexpected error in main: {e}")

def run_open_cypher_query(client, graph_id):
    """
    Run an OpenCypher query without parameters.
    """
    try:
        resp = client.execute_query(
            graphIdentifier=graph_id,
            queryString="MATCH (n {code: 'ANC'}) RETURN n",
            language='OPEN_CYPHER'
        )
        print(resp['payload'].read().decode('UTF-8'))

    except client.exceptions.InternalServerException as e:
        print(f"InternalServerException: {e.response['Error']['Message']}")
    except ClientError as e:
        print(f"ClientError: {e.response['Error']['Message']}")
    except Exception as e:  # <--- ADD THIS BLOCK
        print(f"Unexpected error: {e}")

def run_open_cypher_query_with_params(client, graph_id):
    """
    Run an OpenCypher query with parameters.
    """
    try:
        parameters = {'code': 'ANC'}
        resp = client.execute_query(
            graphIdentifier=graph_id,
            queryString="MATCH (n {code: $code}) RETURN n",
            language='OPEN_CYPHER',
            parameters=parameters
        )
        print(resp['payload'].read().decode('UTF-8'))

    except client.exceptions.InternalServerException as e:
        print(f"InternalServerException: {e.response['Error']['Message']}")
    except ClientError as e:
        print(f"ClientError: {e.response['Error']['Message']}")
    except Exception as e:  # <--- ADD THIS BLOCK
        print(f"Unexpected error: {e}")

def run_open_cypher_explain_query(client, graph_id):
    """
    Run an OpenCypher explain query (explainMode = "debug").
    """
    try:
        resp = client.execute_query(
            graphIdentifier=graph_id,
            queryString="MATCH (n {code: 'ANC'}) RETURN n",
            language='OPEN_CYPHER',
            explainMode='DETAILS'
        )
        print(resp['payload'].read().decode('UTF-8'))

    except ClientError as e:
        print(f"Neptune error: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"Unexpected Boto3 error: {str(e)}")
    except Exception as e:  # <-- Add this generic catch
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
+  For API details, see [ExecuteQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteQuery) in *AWS SDK for Python (Boto3) API Reference*.

------
