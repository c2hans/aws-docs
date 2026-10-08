---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_StartQueryExecution_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `StartQueryExecution` with an AWS SDK or CLI
<a name="athena_example_athena_StartQueryExecution_section"></a>

The following code examples show how to use `StartQueryExecution`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Getting started with query analytics](athena_example_athena_GettingStarted_061_section.md)
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**Example 1: To run a query in a workgroup on the specified table in the specified database and data catalog**
The following `start-query-execution` example uses the `AthenaAdmin` workgroup to run a query on the `cloudfront_logs` table in the `cflogsdatabase` in the `AwsDataCatalog` data catalog.

```
aws athena start-query-execution \
    --query-string {{"select date, location, browser, uri, status from cloudfront_logs where method = 'GET' and status = 200 and location like 'SFO%' limit 10"}} \
    --work-group {{"AthenaAdmin"}} \
    --query-execution-context {{Database=cflogsdatabase,Catalog=AwsDataCatalog}}
```
Output:

```
{
"QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.
**Example 2: To run a query that uses a specified workgroup to create a database in the specified data catalog**
The following `start-query-execution` example uses the `AthenaAdmin` workgroup to create the database `newdb` in the default data catalog `AwsDataCatalog`.

```
aws athena start-query-execution \
    --query-string {{"create database if not exists newdb"}} \
    --work-group {{"AthenaAdmin"}}
```
Output:

```
{
"QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11112"
}
```
For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.
**Example 3: To run a query that creates a view on a table in the specified database and data catalog**
The following `start-query-execution` example uses a `SELECT` statement on the `cloudfront_logs` table in the `cflogsdatabase` to create the view `cf10`.

```
aws athena start-query-execution \
    --query-string  {{"CREATE OR REPLACE VIEW cf10 AS SELECT * FROM cloudfront_logs limit 10"}} \
    --query-execution-context {{Database=cflogsdatabase}}
```
Output:

```
{
"QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11113"
}
```
For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.
+  For API details, see [StartQueryExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-query-execution.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def start_query_execution(
        self,
        query_string: str,
        work_group: str,
        database: Optional[str] = None,
    ) -> str:
        """
        Runs a SQL query using Amazon Athena.

        :param query_string: The SQL query to execute.
        :param work_group: The workgroup in which to run the query.
        :param database: The database context for the query (optional).
        :return: The query execution ID.
        :raises ClientError: If the query could not be started.
        """
        try:
            params: Dict[str, Any] = dict()
            params["QueryString"] = query_string
            params["WorkGroup"] = work_group
            if database is not None:
                params["QueryExecutionContext"] = {"Database": database}
            response = self.athena_client.start_query_execution(**params)
            query_execution_id = response["QueryExecutionId"]
            logger.info("Started query execution. ID: %s", query_execution_id)
            return query_execution_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request starting query execution. The query string, "
                    "database, or workgroup is invalid. %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [StartQueryExecution](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/StartQueryExecution) in *AWS SDK for Python (Boto3) API Reference*.

------
