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
