---
source_url: https://docs.aws.amazon.com/glue/latest/dg/googleads-connection-options.html
---

# Google Ads connection options
<a name="googleads-connection-options"></a>

The following are connection options for Google Ads:
+  `ENTITY_NAME`(String) - (Required) Used for Read/Write. The name of your Object in Google Ads.
+  `API_VERSION`(String) - (Required) Used for Read/Write. Google Ads Rest API version you want to use. Example: v16.
+  `DEVELOPER_TOKEN`(String) - (Required) Used for Read/Write. Required to authenticate the developer or application making requests to the API.
+  `MANAGER_ID`(String) - Used for Read/Write. A unique identifier that allows you to manage multiple Google Ads accounts. This is the customer ID of the authorized manager. If your access to the customer account is through a manager account, the `MANAGER_ID` is required. For more information, see [login-customer-id](https://developers.google.com/google-ads/api/docs/concepts/call-structure#cid).
+  `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
+  `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
+  `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
+  `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query.
+  `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field.
+  `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field.
+  `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
