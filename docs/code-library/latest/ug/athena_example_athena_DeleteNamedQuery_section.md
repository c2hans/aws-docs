---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_DeleteNamedQuery_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteNamedQuery` with an AWS SDK or CLI
<a name="athena_example_athena_DeleteNamedQuery_section"></a>

The following code examples show how to use `DeleteNamedQuery`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Getting started with query analytics](athena_example_athena_GettingStarted_061_section.md)
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete a named query**
The following `delete-named-query` example deletes the named query that has the specified ID.

```
aws athena delete-named-query \
    --named-query-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
This command produces no output.
For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.
+  For API details, see [DeleteNamedQuery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-named-query.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def delete_named_query(self, named_query_id: str) -> None:
        """
        Deletes a named query by its ID.

        :param named_query_id: The unique ID of the named query to delete.
        :raises ClientError: If the named query could not be deleted.
        """
        try:
            self.athena_client.delete_named_query(NamedQueryId=named_query_id)
            logger.info("Deleted named query '%s'.", named_query_id)
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request deleting named query '%s'. "
                    "The named query ID was not found or is invalid. %s: %s",
                    named_query_id,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteNamedQuery](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/DeleteNamedQuery) in *AWS SDK for Python (Boto3) API Reference*.

------
