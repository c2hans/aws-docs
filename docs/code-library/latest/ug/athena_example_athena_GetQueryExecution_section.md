---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_GetQueryExecution_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetQueryExecution` with an AWS SDK or CLI
<a name="athena_example_athena_GetQueryExecution_section"></a>

The following code examples show how to use `GetQueryExecution`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Getting started with query analytics](athena_example_athena_GettingStarted_061_section.md)
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To return information about a query execution**
The following `get-query-execution` example returns information about the query that has the specified query ID.

```
aws athena get-query-execution \
    --query-execution-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "QueryExecution": {
        "QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "Query": "select date, location, browser, uri, status from cloudfront_logs where method = 'GET
' and status = 200 and location like 'SFO%' limit 10",
        "StatementType": "DML",
        "ResultConfiguration": {
            "OutputLocation": "s3://amzn-s3-demo-bucket/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111.csv"
        },
        "QueryExecutionContext": {
            "Database": "mydatabase",
            "Catalog": "awsdatacatalog"
        },
        "Status": {
            "State": "SUCCEEDED",
            "SubmissionDateTime": 1593469842.665,
            "CompletionDateTime": 1593469846.486
        },
        "Statistics": {
            "EngineExecutionTimeInMillis": 3600,
            "DataScannedInBytes": 203089,
            "TotalExecutionTimeInMillis": 3821,
            "QueryQueueTimeInMillis": 267,
            "QueryPlanningTimeInMillis": 1175
        },
        "WorkGroup": "AthenaAdmin"
    }
}
```
For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.
+  For API details, see [GetQueryExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-execution.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def get_query_execution(self, query_execution_id: str) -> Dict[str, Any]:
        """
        Returns information about a single query execution.

        :param query_execution_id: The unique ID of the query execution.
        :return: A dictionary containing the query execution details.
        :raises ClientError: If the query execution information could not be retrieved.
        """
        try:
            response = self.athena_client.get_query_execution(
                QueryExecutionId=query_execution_id
            )
            query_execution = response["QueryExecution"]
            logger.info(
                "Retrieved query execution '%s'. State: %s",
                query_execution_id,
                query_execution["Status"]["State"],
            )
            return query_execution
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request retrieving query execution '%s'. "
                    "The execution ID is invalid or not found. %s: %s",
                    query_execution_id,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetQueryExecution](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetQueryExecution) in *AWS SDK for Python (Boto3) API Reference*.

------
