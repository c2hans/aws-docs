---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

For a general reference of AWS terms, see the [AWS glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html) in the AWS General Reference.

 **segment**

Apache Druid stores its data and indexes in *segment files* partitioned by time. Druid creates a segment for each segment interval that contains data.

 **quorum**

A replicated group of servers in the same application is called a *quorum*, and in replicated mode, all servers in the quorum have copies of the same configuration file.

**Note**
For a general reference of standard Apache Druid concepts, refer to the [Apache Druid documentation](https://druid.apache.org/docs/latest/design/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
