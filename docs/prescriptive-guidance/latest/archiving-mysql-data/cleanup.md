---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/cleanup.html
---

# Archive table cleanup
<a name="cleanup"></a>

The final stage in the archive process is to clean up the tables in your archive schema. You can do this after you confirm that your archive data is safely archived in Amazon S3. To avoid any impact to your application, we recommend dropping the archive schema tables during a scheduled downtime or maintenance window or during a very low traffic window in your application. These tables are not actively queried by your application and shouldn't be cause for alarm for their impact to ongoing transactions. Still, it is a best practice to run DDLs during a downtime.

After the storage for large archive schema tables is freed up, Amazon Aurora uses [dynamic resizing ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Performance.html)to help you save on storage costs.
