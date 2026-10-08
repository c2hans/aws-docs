---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_CreateNamedQuery_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateNamedQuery` with an AWS SDK or CLI
<a name="athena_example_athena_CreateNamedQuery_section"></a>

The following code examples show how to use `CreateNamedQuery`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Getting started with query analytics](athena_example_athena_GettingStarted_061_section.md)
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To create a named query**
The following `create-named-query` example creates a saved query in the `AthenaAdmin` workgroup that queries the `flights_parquet` table for flights from Seattle to New York in January, 2016 whose departure and arrival were both delayed by more than ten minutes. Because the airport code values in the table are strings that include double quotes (for example, "SEA"), they are escaped by backslashes and surrounded by single quotes.

```
aws athena create-named-query \
    --name {{"SEA to JFK delayed flights Jan 2016"}} \
    --description {{"Both arrival and departure delayed more than 10 minutes."}} \
    --database {{sampledb}} \
    --query-string "SELECT flightdate, carrier, flightnum, origin, dest, depdelayminutes, arrdelayminutes FROM sampledb.flights_parquet WHERE yr = 2016 AND month = 1 AND origin = '\"SEA\"' AND dest = '\"JFK\"' AND depdelayminutes > 10 AND arrdelayminutes > 10" \
    --work-group {{AthenaAdmin}}
```
Output:

```
{
    "NamedQueryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.
+  For API details, see [CreateNamedQuery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-named-query.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def create_named_query(
        self,
        name: str,
        description: str,
        database: str,
        query_string: str,
        work_group: str,
    ) -> str:
        """
        Creates a named (saved) query in the specified workgroup.

        :param name: The name for the query.
        :param description: A description of the query.
        :param database: The database to which the query belongs.
        :param query_string: The SQL query string.
        :param work_group: The workgroup in which to save the query.
        :return: The named query ID.
        :raises ClientError: If the named query could not be created.
        """
        try:
            response = self.athena_client.create_named_query(
                Name=name,
                Description=description,
                Database=database,
                QueryString=query_string,
                WorkGroup=work_group,
            )
            named_query_id = response["NamedQueryId"]
            logger.info("Created named query '%s'. ID: %s", name, named_query_id)
            return named_query_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request creating named query '%s'. "
                    "The query name, database, or query string is invalid. "
                    "%s: %s",
                    name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CreateNamedQuery](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateNamedQuery) in *AWS SDK for Python (Boto3) API Reference*.

------
