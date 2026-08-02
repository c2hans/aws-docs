---
source_url: https://docs.aws.amazon.com/glue/latest/dg/salesforce-connector-limitations.html
---

# Limitations for the Salesforce connector
<a name="salesforce-connector-limitations"></a>

The following are limitations for the Salesforce connector:
+ We only support Spark SQL and Salesforce SOQL is not supported.
+ Job bookmarks are not supported.
+ Salesforce field names are case sensitive. When writing to Salesforce, data must match the casing of the fields defined within Salesforce.
