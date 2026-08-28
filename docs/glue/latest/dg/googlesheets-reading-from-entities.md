---
source_url: https://docs.aws.amazon.com/glue/latest/dg/googlesheets-reading-from-entities.html
---

# Reading from Google Sheets entities
<a name="googlesheets-reading-from-entities"></a>

 **Prerequisites**
+  A Google SpreadSheet that you would like to read from. You will need the SpreadSheet ID and tabName of the spreadsheet.

 **Google Sheets Entity and Field Details:**

| Entity | Data Type | Supported Operators |
| --- | --- | --- |
| Spreadsheet | String | N/A (filter is not supported) |

 **Example**

```
googleSheets_read = glueContext.create_dynamic_frame.from_options(
    connection_type="googlesheets",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "{SpreadSheetID}#{SheetTabName}",
        "API_VERSION": "v4"
    }
```

 **Partitioning queries**

 For Record Base Partitioning only, `NUM_PARTITIONS` can be provided as additional spark options if you want to utilize concurrency in Spark. With this parameter, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by spark tasks concurrently.

 **Example with `NUM_PARTITIONS`**

```
googlesheets_read = glueContext.create_dynamic_frame.from_options(
    connection_type="googlesheets",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "{SpreadSheetID}#{SheetTabName}",
        "API_VERSION": "v4",
        "NUM_PARTITIONS": "10"
    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
