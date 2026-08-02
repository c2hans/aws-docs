---
source_url: https://docs.aws.amazon.com/glue/latest/dg/release-notes.html
---

# AWS Glue versions
<a name="release-notes"></a>

You can configure the AWS Glue version parameter when you add or update a job. The AWS Glue version determines the versions of Apache Spark and Python that AWS Glue supports. The Python version indicates the version that's supported for jobs of type Spark. The following table lists the available AWS Glue versions, the corresponding Spark and Python versions, and other changes in functionality.

You can use the [Generative AI upgrades for Apache Spark](upgrade-analysis.md) to upgrade your Glue ETL jobs from older Glue versions (≥ 2.0) to the latest Glue version.

## AWS Glue versions
<a name="release-notes-versions"></a>

<a name="table-glue-versions"></a>

- **AWS Glue 5.1**
  - **Supported runtime environment versions:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)
  - **Supported Java version:** Java 17
  - **Changes in functionality:** AWS Glue 5.1 is the default version for jobs created without specifying an AWS Glue version.<br />In addition to the spark engine upgrade, there are optimizations and upgrades built into this AWS Glue release, such as:[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)

- **AWS Glue 5.0**
  - **Supported runtime environment versions:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)
  - **Supported Java version:** Java 17
  - **Changes in functionality:** In addition to the framework updates, there are optimizations and upgrades built into this AWS Glue release, such as:[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html) Limitations The following are limitations with AWS Glue 5.0: [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)<br />For more information about migrating to AWS Glue version 5.0, see [Migrating AWS Glue for Spark jobs to AWS Glue version 5.0](migrating-version-50.md).

- **AWS Glue 4.0**
  - **Supported runtime environment versions:**  Spark environment versions [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)  / **Supported Java version:** Java 8 / **Changes in functionality:** AWS Glue 4.0 has a number of optimizations and upgrades built into this AWS Glue release, such as:[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html) Limitations The following are limitations with AWS Glue 4.0: [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)<br />For more information about migrating to AWS Glue version 4.0, see [Migrating AWS Glue for Spark jobs to AWS Glue version 4.0](migrating-version-40.md).
  - **Supported runtime environment versions:** Ray environment versions [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html) / **Supported Java version:** N/A / **Changes in functionality:** Build and run distributed Python applications with AWS Glue for Ray.[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)<br />**Limitations on Ray jobs in AWS Glue 4.0**[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)

- **AWS Glue 3.0**
  - **Supported runtime environment versions:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)
  - **Supported Java version:** Java 8
  - **Changes in functionality:** In addition to the Spark engine upgrade to 3.0, there are optimizations and upgrades built into this AWS Glue release, such as:[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html) Limitations The following are limitations with AWS Glue 3.0: [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)

- **AWS Glue 2.0 ([end of life on April 1, 2026](https://docs.aws.amazon.com/glue/latest/dg/glue-version-support-policy.html))**
  - **Supported runtime environment versions:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)
  - **Supported Java version:** N/A
  - **Changes in functionality:** In addition to the features provided in AWS Glue version 1.0, AWS Glue version 2.0 also provides:[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html) AWS Glue version 2.0 differs from AWS Glue version 1.0 for some dependencies and versions due to underlying architectural changes. Validate your AWS Glue jobs before migrating across major AWS Glue version releases.

- **AWS Glue 1.0 ([end of life on April 1, 2026](https://docs.aws.amazon.com/glue/latest/dg/glue-version-support-policy.html))**
  - **Supported runtime environment versions:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)
  - **Supported Java version:** N/A
  - **Changes in functionality:** You can maintain job bookmarks for Parquet and ORC formats in AWS Glue ETL jobs (using AWS Glue version 1.0). Previously, you were only able to bookmark common Amazon S3 source formats such as JSON, CSV, Apache Avro, and XML in AWS Glue ETL jobs. <br />When setting format options for ETL inputs and outputs, you can specify to use Apache Avro reader/writer format 1.8 to support Avro logical type reading and writing (using AWS Glue version 1.0). Previously, only the version 1.7 Avro reader/writer format was supported.<br />The DynamoDB connection type supports a writer option (using AWS Glue version 1.0). Limitations The following are limitations with AWS Glue 1.0: [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)

- **AWS Glue 0.9 ([end of life on April 1, 2026](https://docs.aws.amazon.com/glue/latest/dg/glue-version-support-policy.html))**
  - **Supported runtime environment versions:**  [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)
  - **Supported Java version:** N/A
  - **Changes in functionality:**   Limitations The following are limitations with AWS Glue 0.9:  [See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/release-notes.html)

**Note**
The following Glue versions support these versions of PythonShell:
PythonShell v3.6 is supported in Glue version 1.0.
PythonShell v3.9 is supported in Glue version 3.0.
Additionally, dev endpoints are supported only in Glue version 1.0, and 0.9.
