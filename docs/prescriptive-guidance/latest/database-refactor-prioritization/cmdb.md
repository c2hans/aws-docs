---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/cmdb.html
---

# Step 1. Collect CMDB data
<a name="cmdb"></a>

The first step is to collect data to identify databases that are potential candidates for refactoring on AWS. There are eight data elements that are essential to this phase:
+ Server name
+ Service or instance name
+ Database name
+ Database engine
+ Database port
+ Whether it's a production database
+ Whether it's a critical database
+ Database size (in GB)
+ (Optional) Whether it's part of a commercial off-the-shelf (COTS) application

This data should be readily available, typically in a configuration management database (CMDB), so it can be easily consolidated into another database or spreadsheet, where it will be analyzed.

When the data has been collected and consolidated, filter out the databases that don't meet the following criteria:
+ Production database.
+ Custom database, not a COTS database. (This is because COT databases are vendor-supported, and some vendors don't support refactoring, and rewriting the code is time-consuming.)
+ Non-critical database.
+ Database size less than 800 GB. (You can modify this requirement based on your database estate.)

This filtering reduces your candidate database list significantly (typically more than 50%) by filtering out the non-production databases). Sort the remaining databases by size (in ascending order) in preparation for [step 2](pl-sql.md).

![Criteria for filtering the initial dataset in a CMDB](http://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/images/guide-img/d514dcdf-d1f9-43a2-ac0b-46dc109cf9b2/images/1ccd221c-1cb1-4228-845b-32917db49193.png)

## Best practices
<a name="cmdb-best-practices"></a>
+ Make sure that the CMDB has an accurate and up-to-date inventory of all the databases that are in scope for migration.
+ Gather the database details outlined in this section from your CMDB.
