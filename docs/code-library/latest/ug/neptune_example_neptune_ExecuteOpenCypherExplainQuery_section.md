---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/neptune_example_neptune_ExecuteOpenCypherExplainQuery_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ExecuteOpenCypherExplainQuery` with an AWS SDK
<a name="neptune_example_neptune_ExecuteOpenCypherExplainQuery_section"></a>

The following code examples show how to use `ExecuteOpenCypherExplainQuery`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](neptune_example_neptune_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Executes an OpenCypher EXPLAIN query using the provided Neptune data client.
     *
     * @param client The Neptune data client to use for the query execution.
     */
    public static void executeGremlinQuery(NeptunedataClient client) {
        try {
            System.out.println("Executing OpenCypher EXPLAIN query...");
            ExecuteOpenCypherExplainQueryRequest request = ExecuteOpenCypherExplainQueryRequest.builder()
                    .openCypherQuery("MATCH (n {code: 'ANC'}) RETURN n")
                    .explainMode("debug")
                    .build();

            ExecuteOpenCypherExplainQueryResponse response = client.executeOpenCypherExplainQuery(request);

            if (response.results() != null) {
                System.out.println("Explain Results:");
                System.out.println(response.results().asUtf8String());
            } else {
                System.out.println("No explain results returned.");
            }

        } catch (NeptunedataException e) {
            System.err.println("Neptune error: " + e.awsErrorDetails().errorMessage());
        } catch (Exception e) {
            System.err.println("Unexpected error: " + e.getMessage());
        } finally {
            client.close();
        }
    }
```
+  For API details, see [ExecuteOpenCypherExplainQuery](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ExecuteOpenCypherExplainQuery) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
# Replace with your actual Neptune endpoint URL
NEPTUNE_ENDPOINT = "https://<your-neptune-endpoint>:8182"

def main():
    """
    Entry point: Create Neptune client and execute different OpenCypher queries.
    """
    config = Config(connect_timeout=10, read_timeout=30, retries={'max_attempts': 3})

    neptune_client = boto3.client(
        "neptunedata",
        endpoint_url=NEPTUNE_ENDPOINT,
        config=config
    )

    execute_open_cypher_query_without_params(neptune_client)
    execute_open_cypher_query_with_params(neptune_client)
    execute_open_cypher_explain_query(neptune_client)

def execute_open_cypher_query_without_params(client):
    """
    Executes a simple OpenCypher query without parameters.
    """
    try:
        print("\nRunning OpenCypher query without parameters...")
        resp = client.execute_open_cypher_query(
            openCypherQuery="MATCH (n {code: 'ANC'}) RETURN n"
        )
        print("Results:")
        print(resp['results'])

    except Exception as e:
        print(f"Error in simple OpenCypher query: {str(e)}")

def execute_open_cypher_query_with_params(client):
    """
    Executes an OpenCypher query using parameters.
    """
    try:
        print("\nRunning OpenCypher query with parameters...")
        parameters = {'code': 'ANC'}
        resp = client.execute_open_cypher_query(
            openCypherQuery="MATCH (n {code: $code}) RETURN n",
            parameters=json.dumps(parameters)
        )
        print("Results:")
        print(resp['results'])

    except Exception as e:
        print(f"Error in parameterized OpenCypher query: {str(e)}")

def execute_open_cypher_explain_query(client):
    """
    Runs an OpenCypher EXPLAIN query in debug mode.
    """
    try:
        print("\nRunning OpenCypher EXPLAIN query (debug mode)...")
        resp = client.execute_open_cypher_explain_query(
            openCypherQuery="MATCH (n {code: 'ANC'}) RETURN n",
            explainMode="details"
        )
        results = resp.get('results')
        if results is None:
            print("No explain results returned.")
        else:
            try:
                print("Explain Results:")
                print(results.read().decode('UTF-8'))
            except Exception as e:
                print(f"Error in OpenCypher EXPLAIN query: {str(e)}")

    except ClientError as e:
        print(f"Neptune error: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"BotoCore error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
```
+  For API details, see [ExecuteOpenCypherExplainQuery](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ExecuteOpenCypherExplainQuery) in *AWS SDK for Python (Boto3) API Reference*.

------
