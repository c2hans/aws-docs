---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_ListQueryExecutions_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListQueryExecutions` with an AWS SDK or CLI
<a name="athena_example_athena_ListQueryExecutions_section"></a>

The following code examples show how to use `ListQueryExecutions`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To list the query IDs of the queries in a specified workgroup**
The following `list-query-executions` example lists a maximum of ten of the query IDs in the `AthenaAdmin` workgroup.

```
aws athena list-query-executions \
    --work-group {{AthenaAdmin}} \
    --max-items {{10}}
```
Output:

```
{
    "QueryExecutionIds": [
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11110",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11114",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11115",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11116",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11117",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11118",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11119"
    ],
    "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxMH0="
}
```
For more information, see [Working with Query Results, Output Files, and Query History](https://docs.aws.amazon.com/athena/latest/ug/querying.html) in the *Amazon Athena User Guide*.
+  For API details, see [ListQueryExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-query-executions.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def list_query_executions(self, work_group: str) -> List[str]:
        """
        Lists query execution IDs for the specified workgroup using pagination.

        :param work_group: The name of the workgroup.
        :return: A list of query execution IDs.
        :raises ClientError: If the query executions could not be listed.
        """
        try:
            paginator = self.athena_client.get_paginator("list_query_executions")
            page_iterator = paginator.paginate(WorkGroup=work_group)
            execution_ids = list()
            for page in page_iterator:
                execution_ids.extend(page.get("QueryExecutionIds", list()))
            logger.info(
                "Found %d query execution(s) in workgroup '%s'.",
                len(execution_ids),
                work_group,
            )
            return execution_ids
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request listing query executions for workgroup '%s'. "
                    "%s: %s",
                    work_group,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListQueryExecutions](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/ListQueryExecutions) in *AWS SDK for Python (Boto3) API Reference*.

------
