---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_GetNamedQuery_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetNamedQuery` with an AWS SDK or CLI
<a name="athena_example_athena_GetNamedQuery_section"></a>

The following code examples show how to use `GetNamedQuery`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Getting started with query analytics](athena_example_athena_GettingStarted_061_section.md)
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To return a named query**
The following `get-named-query` example returns information about the query that has the specified ID.

```
aws athena get-named-query \
    --named-query-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "NamedQuery": {
        "Name": "CloudFront Logs - SFO",
        "Description": "Shows successful GET request data for SFO",
        "Database": "default",
        "QueryString": "select date, location, browser, uri, status from cloudfront_logs where method = 'GET' and status = 200 and location like 'SFO%' limit 10",
        "NamedQueryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "WorkGroup": "AthenaAdmin"
    }
}
```
For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.
+  For API details, see [GetNamedQuery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-named-query.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def get_named_query(self, named_query_id: str) -> Dict[str, Any]:
        """
        Returns the details of a single named (saved) query, including its
        SQL query string.

        :param named_query_id: The unique ID of the named query.
        :return: A dictionary containing the named query details.
        :raises ClientError: If the named query could not be retrieved.
        """
        try:
            response = self.athena_client.get_named_query(NamedQueryId=named_query_id)
            named_query = response["NamedQuery"]
            logger.info("Retrieved named query '%s'.", named_query_id)
            return named_query
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request retrieving named query '%s'. "
                    "The named query ID was not found or is invalid. %s: %s",
                    named_query_id,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetNamedQuery](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetNamedQuery) in *AWS SDK for Python (Boto3) API Reference*.

------
