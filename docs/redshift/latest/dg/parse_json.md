---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/parse_json.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Using JSON\_PARSE to insert data into SUPER columns
<a name="parse_json"></a>

You can insert or update JSON data into a SUPER column using the [JSON\_PARSE function](JSON_PARSE.md). The function parses data in JSON format and converts it into the SUPER data type, which you can use in INSERT or UPDATE statements.

The following example inserts JSON data into a SUPER column. If the JSON\_PARSE function is missing in the query, Amazon Redshift treats the value as a single string instead of a JSON-formatted string that must be parsed.

```
--Drop the table if it exists.
DROP TABLE IF EXISTS test_json;

--Create the table.
CREATE TABLE test_json (all_data SUPER);

--Populate the table.
INSERT INTO test_json VALUES (JSON_PARSE('
{
    "name": {
        "first_name": "Jake",
        "last_name": "Smith"
    },
    "age": 30,
    "hobby": "Biking"
}'
) );

SELECT * FROM test_json;

 all_data
---------
{"name":{"first_name":"Jake","last_name":"Smith"},"age":30,"hobby":"Biking"}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
