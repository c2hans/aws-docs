---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-template-copyrdstos3.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Full copy of Amazon RDS MySQL Table to Amazon S3
<a name="dp-template-copyrdstos3"></a>

The **Full Copy of RDS MySQL Table to S3** template copies an entire Amazon RDS MySQL table and stores the output in an Amazon S3 location. The output is stored as a CSV file in a timestamped subfolder under the specified Amazon S3 location.

The template uses the following pipeline objects:
+ [CopyActivity](dp-object-copyactivity.md)
+ [Ec2Resource](dp-object-ec2resource.md)
+ [SqlDataNode](dp-object-sqldatanode.md)
+ [S3DataNode](dp-object-s3datanode.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
