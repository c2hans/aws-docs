---
source_url: https://docs.aws.amazon.com/glue/latest/dg/teamwork-connection-options.html
---

# Teamwork connection options
<a name="teamwork-connection-options"></a>

The following are connection options for Teamwork:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the Teamwork object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.

Server-side (pushed-down) filtering is not supported for Teamwork. Apply any filtering in your AWS Glue ETL job.
