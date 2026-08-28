---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.dt.2-enhance-understanding-of-data-through-data-profiling.html
---

# [QA.DT.2] Enhance understanding of data through data profiling
<a name="qa.dt.2-enhance-understanding-of-data-through-data-profiling"></a>

 **Category:** OPTIONAL

 Use data profiling tools to examine, analyze, and understand the data including its content, structure, and relationships to identify issues such as inconsistencies, outliers, and missing values. By performing data profiling, teams can gain deeper insights into the characteristics and quality of their data, enabling them to make informed decisions about data management, data governance, and data integration strategies. This data is often used to enable or improve other types of data testing.

 To integrate data profiling into a DevOps environment, consider automating the process using data profiling tools such as [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/), open-source tools, or custom scripts that analyze data regularly. Incorporate the profiling results into your data management, governance, and integration strategies, allowing your team to proactively address data quality issues and maintain consistent data standards throughout the development lifecycle.

**Related information:**
+  [Build an automatic data profiling and reporting solution with Amazon EMR, AWS Glue, and Quick](https://aws.amazon.com/blogs/big-data/build-an-automatic-data-profiling-and-reporting-solution-with-amazon-emr-aws-glue-and-amazon-quicksight/)
+  [Test data quality at scale with Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/)
+  [Deequ single column profiling](https://github.com/awslabs/deequ/blob/master/src/main/scala/com/amazon/deequ/examples/data_profiling_example.md)
+  [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
