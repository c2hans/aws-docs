---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/using-query-output.html
---

# Using query output in other AWS services
<a name="using-query-output"></a>

SQL query output can be used for the seed data for a Clean Rooms ML model. For more information, see [AWS Clean Rooms ML](machine-learning.md).

Query output from AWS Clean Rooms is available on the console (if the console is used to run queries) and downloaded in a specified Amazon S3 bucket. From there, you can use the query output in other AWS services, such as Amazon Quick and Amazon SageMaker AI, depending on how those services use data from Amazon S3.

For more information about Amazon Quick, see the [Amazon Quick Documentation](https://docs.aws.amazon.com/quicksight/?icmpid=docs_homepage_analytics).

For more information about Amazon SageMaker AI, see the [Amazon SageMaker AI Documentation](https://docs.aws.amazon.com/sagemaker/?icmpid=docs_homepage_featuredsvcs).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
