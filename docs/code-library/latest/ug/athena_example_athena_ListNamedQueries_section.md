---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_ListNamedQueries_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListNamedQueries` with an AWS SDK or CLI
<a name="athena_example_athena_ListNamedQueries_section"></a>

The following code examples show how to use `ListNamedQueries`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Getting started with query analytics](athena_example_athena_GettingStarted_061_section.md)
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To list the named queries for a workgroup**
The following `list-named-queries` example lists the named queries for the `AthenaAdmin` workgroup.

```
aws athena list-named-queries \
    --work-group {{AthenaAdmin}}
```
Output:

```
{
    "NamedQueryIds": [
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
    ]
}
```
For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.
+  For API details, see [ListNamedQueries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-named-queries.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def list_named_queries(self, work_group: str) -> List[str]:
        """
        Lists named query IDs in the specified workgroup using pagination.

        :param work_group: The name of the workgroup.
        :return: A list of named query IDs.
        :raises ClientError: If the named queries could not be listed.
        """
        try:
            paginator = self.athena_client.get_paginator("list_named_queries")
            page_iterator = paginator.paginate(WorkGroup=work_group)
            named_query_ids = list()
            for page in page_iterator:
                named_query_ids.extend(page.get("NamedQueryIds", list()))
            logger.info(
                "Found %d named query ID(s) in workgroup '%s'.",
                len(named_query_ids),
                work_group,
            )
            return named_query_ids
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request listing named queries for workgroup '%s'. "
                    "%s: %s",
                    work_group,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListNamedQueries](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/ListNamedQueries) in *AWS SDK for Python (Boto3) API Reference*.

------
