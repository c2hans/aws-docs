---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-overview.html
---

# Apache Ranger with Amazon EMR
<a name="emr-ranger-overview"></a>

Apache Ranger is a framework to enable, monitor, and manage comprehensive data security across the Hadoop platform.

Apache Ranger has the following features:
+ Centralized security administration to manage all security related tasks in a central UI or using REST APIs.
+ Fine-grained authorization to do a specific action or operation with a Hadoop component or tool, managed through a central administration tool.
+ A standardized authorization method across all Hadoop components.
+ Enhanced support for various authorization methods.
+ Centralized auditing of user access and administrative actions (security related) within all the components of Hadoop.

Apache Ranger uses two key components for authorization:
+ **Apache Ranger policy admin server** - This server allows you to define the authorization policies for Hadoop applications. When integrating with Amazon EMR, you are able to define and enforce policies for Apache Spark and Hive to access Hive Metastore, and accessing Amazon S3 data [EMR File System (EMRFS)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-fs). You can set up a new or use an existing Apache Ranger policy admin server to integrate with Amazon EMR.
+ **Apache Ranger plugin** - This plugin validates the access of a user against the authorization policies defined in the Apache Ranger policy admin server. Amazon EMR installs and configures the Apache Ranger plugin automatically for each Hadoop application selected in the Apache Ranger configuration.

**Topics**
+ [Architecture of Amazon EMR integration with Apache Ranger](emr-ranger-architecture.md)
+ [Amazon EMR components for use with Apache Ranger](emr-ranger-components.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
