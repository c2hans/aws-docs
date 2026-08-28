---
source_url: https://docs.aws.amazon.com/glue/latest/dg/microsoft-dynamics-365-connection-options.html
---

# Microsoft Dynamics 365 CRM connection option reference
<a name="microsoft-dynamics-365-connection-options"></a>

The following are connection options for Microsoft Dynamics 365 CRM:
+  `ENTITY_NAME`(String) - (Required) Used for Read. The name of your object in Microsoft Dynamics 365 CRM.
+  `API_VERSION`(String) - (Required) Used for Read. Microsoft Dynamics 365 CRM Rest API version you want to use.
+  `SELECTED_FIELDS`(List<String>) - Default: empty(SELECT \*). Used for Read. Columns you want to select for the object.
+  `FILTER_PREDICATE`(String) - Default: empty. Used for Read. It should be in the Spark SQL format.
+  `QUERY`(String) - Default: empty. Used for Read. Full Spark SQL query.
+  `INSTANCE_URL`(String) - (Required) A valid Microsoft Dynamics 365 CRM Instance URL with the format: `https://{tenantID}.api.crm.dynamics.com`
+  `NUM_PARTITIONS`(Integer) - Default: 1. Used for Read. Number of partitions for read.
+  `PARTITION_FIELD`(String) - Used for Read. Field to be used to partition query.
+  `LOWER_BOUND`(String)- Used for Read. An inclusive lower bound value of the chosen partition field. Example: `2024-01-30T06:47:51.000Z`.
+  `UPPER_BOUND`(String) - Used for Read. An exclusive upper bound value of the chosen partition field. Example: `2024-06-30T06:47:51.000Z`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
