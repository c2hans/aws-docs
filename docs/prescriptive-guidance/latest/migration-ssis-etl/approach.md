---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/approach.html
---

# Determining the migration approach
<a name="approach"></a>

To decide on a migration approach, you use the analysis you performed on existing patterns in the previous phase. Your organization's future data and analytics needs are equally important considerations. Traditional on-premises ETL tools deal with relational data models and structured data. If you have semi-structured and unstructured data to process, you can use AWS services such as AWS Glue or Amazon EMR for the migration. Other factors that can influence the migration approach include:
+ Whether you want to use a graphical interface (such as [AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)) or a custom framework (such as Spark/Python libraries)
+ Whether you have secure access to on-premises sources and AWS targets
+ Skills and training required for the team
+ Audit and compliance requirements

You can select from three migration approaches: big bang, phased, and lift and shift. The following table compares these three approaches.

|
|
| Approach | Description | Use case | Advantages and disadvantages |
| --- |--- |--- |--- |
| Big bang | Migrate all SSIS packages within a specific time period.  | + Complexity, scope, and target architecture are clear.<br />+ Team has the required skills, or the learning curve is shallow. | + High risk.<br />+ Takes less time than the phased approach.<br />+ You can use AWS Glue, Amazon EMR, or custom frameworks.  |
| Phased | Identify one SSIS package for each distinct pattern and complexity. Migrate the package to AWS, test, and compare results with existing architecture. | + Time is not a constraint.<br />+ You want different designs for different ETL patterns. | + Less risky than the big bang approach but takes more time and effort.<br />+ You can use AWS Glue, Amazon EMR, or custom frameworks.  |
| Lift and shift | Migrate the current architecture as is to AWS. | + Your on-premises hardware is no longer supported.<br />+ You don't have the resources to plan a migration immediately.  | + Least amount of migration effort and time required.<br />+ The problems with the existing solution remain on AWS.<br />+ SSIS packages are run as is. No other ETL tools or frameworks are needed. |

A comparison of data on the source and target systems is fundamental for a successful migration. Because the existing production system gets regular updates from source systems, this comparison might become confusing. For this reason, when you're determining your migration approach, we recommend that you also decide on your data validation strategy.
+ Take backups of all applicable databases and files from the production environment on the source system at a specific date and time.
+ Take backups of all databases from the production environment on the target system after all jobs have successfully loaded data from backed up source data.
+ Restore the source data in a testing environment, and run the new jobs.
+ Agree on a percentage of valid differences between the source and target (old and new) databases. For example, you might decide that a difference of less than 1% is acceptable.
+ List all the validation rules to be covered.
+ Automate the comparison as much as possible, and cover all the rules.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
