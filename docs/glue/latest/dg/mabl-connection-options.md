---
source_url: https://docs.aws.amazon.com/glue/latest/dg/mabl-connection-options.html
---

# mabl connection options
<a name="mabl-connection-options"></a>

The following are connection options for mabl:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the mabl object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Server-side (pushed-down) filtering is not supported for mabl. The connector reads all records of an entity; apply any filtering in your AWS Glue ETL job.
