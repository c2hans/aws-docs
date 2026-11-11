---
source_url: https://docs.aws.amazon.com/glue/latest/dg/ghost-connection-options.html
---

# Ghost connection options
<a name="ghost-connection-options"></a>

The following are connection options for Ghost:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Ghost object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Server-side (pushed-down) filtering is not supported for Ghost. The connector reads all records of an entity; apply any filtering in your AWS Glue ETL job.
