---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/sct.html
---

# Step 3. Run AWS SCT reports
<a name="sct"></a>

In this step, you use the output from [step 2](pl-sql.md) (formatted as a CSV file) as input for running the [AWS SCT multiserver assessor](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Multiserver.html). You must add login credentials (user ID and password), database names, and database descriptions to the CSV file before you provide it as input to the AWS SCT multiserver assessor. Follow the AWS SCT format provided in the [example](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Multiserver.html#CHAP_AssessmentReport.Multiserver.Input) in the AWS documentation.

The multiserver assessor runs AWS SCT against each database schema listed in the CSV file. It produces a detailed report that reflects the conversion complexity for each schema. This calculation is based on the percentage of code objects, storage objects, and syntax elements that AWS SCT can convert automatically, and the code that you need to fix manually during migration. The complexity values range from 1 (least complex) to 10 (most complex).

![Criteria for filtering databases based on the AWS SCT report](http://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/images/guide-img/d514dcdf-d1f9-43a2-ac0b-46dc109cf9b2/images/96d5cb40-0a7d-4a2b-9c86-e405ab710aee.png)

AWS SCT specifies the conversion complexity level based on the effort of code conversion and migration.  The number 1 represents the lowest level of complexity, and the number 10 represents the highest level of complexity. Sorting on the conversion complexity level and filtering on values that are less than 2 produces a list of databases that are candidates to migrate to the target database engine. You can include other properties, such as database size and total number of objects, to fine-tune your list of candidates, as discussed in the following examples.

## Multiserver assessor examples
<a name="multiserver-assessor-examples"></a>

The following examples use AWS SCT multiserver assessor to evaluate Oracle and SQL Server database schemas. The assessment is performed against PostgreSQL and MySQL as the target database engines.

The AWS SCT multiserver assessor produces a summary aggregated report that shows the estimated complexity for each migration target. You can sort this report on the column *Conversion complexity* column for the Amazon Relational Database Service (Amazon RDS) for PostgreSQL or Amazon RDS for MySQL target engines. This provides a list of databases that are easy to migrate to open-source database engines like PostgreSQL or MySQL with minimal or no effort, based on code conversion requirements, storage complexity, and syntax complexity.

The following table shows a sample list of SQL Server databases that are early candidates to migrate to open-source database engines such as PostgreSQL and MySQL. The table also includes the *Total objects* and *Size in GB* columns from the output of [step 2](pl-sql.md).

![Sample AWS SCT report for SQL Server databases that are early candidates to migrate to open-source database engines](http://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/images/guide-img/d514dcdf-d1f9-43a2-ac0b-46dc109cf9b2/images/4ab8e8b8-ba14-4750-b405-810daec90fa0.png)

The data is sorted on the *Conversion complexity* columns (for Amazon RDS for PostgreSQL or MySQL) in ascending order. You can also further sort the table by *Size in GB* and *Total objects*, in ascending order based on your requirements. This results in a list of database schemas that are smaller in size, have fewer objects, and have the least conversion complexity. The table shows the list of SQL Server database schemas that have a conversion complexity of 1 (least complex), for Amazon RDS for PostgreSQL and Amazon RDS for MySQL. These results show that it will take minimal effort to migrate these schemas to open-source database engines on AWS.

The following table shows a similar list of Oracle databases that are early candidates to migrate to open-source PostgreSQL and MySQL databases.

![Sample AWS SCT report for Oracle databases that are early candidates to migrate to open-source database engines](http://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/images/guide-img/d514dcdf-d1f9-43a2-ac0b-46dc109cf9b2/images/0755a4a4-e948-48b5-863a-57c58f2b9ad7.png)

The Oracle and SQL Server tables also provide vital information such as the schema name, the database version, the total number of objects, the size of the schema, and its conversion complexity. You can use this data to review and plan the migration based on your requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
