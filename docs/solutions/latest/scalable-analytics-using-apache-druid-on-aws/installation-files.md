---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/installation-files.html
---

# Installation files
<a name="installation-files"></a>

The guidance sets up an S3 bucket for storing the installation files required by the guidance.

During the build process, the guidance downloads the necessary files, which include Apache Druid, Apache ZooKeeper, and Druid community extensions from the Apache Content Delivery Network (CDN) and then uploads these files into the installation bucket. The guidance performs a signature/hash verification to ensure the binary’s authenticity and integrity prior to deployment.

As part of the EC2 bootstrapping process, these files are retrieved from the installation bucket and installed onto the instances under the `/home/druid-cluster` directory.

**Note**
The installation files are kept in the installation bucket throughout the lifetime of the cluster. When a new EC2 instance starts, it retrieves the installation files from the installation bucket. The installation files may also get updated when configuration is changed, such as upgrading Apache Druid from v26 to v30.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
