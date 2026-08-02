---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/export-data-by-using-select-into-outfile-s3.html
---

# Export data by using SELECT INTO OUTFILE S3
<a name="export-data-by-using-select-into-outfile-s3"></a>

To copy data from the Aurora MySQL-Compatible DB directly into Amazon S3, you can use the statement `SELECT INTO OUTFILE S3`. This SQL statement can be run on the table, and the required number of rows can be offloaded as comma-separated values (CSV) files with a maximum size of 6 GB. When the 6 GB threshold is crossed, multiple .csv files are created.

For the export to work, configure the following:
+ AWS Identity and Access Management (IAM) roles and policies
+ Database permissions granted to the user to run the command
+ The Amazon S3 location for offloading

For more information, see the [Amazon Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.SaveIntoS3.html).

**Note**
To transition the S3 objects into cost-saving storage tiers, we recommend configuring [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) rules in the S3 bucket where the data is being exported.
