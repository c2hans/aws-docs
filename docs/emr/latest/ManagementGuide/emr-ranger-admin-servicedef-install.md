---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-admin-servicedef-install.html
---

# Service definition installation for Ranger integration with Amazon EMR
<a name="emr-ranger-admin-servicedef-install"></a>

A service definition is used by the Ranger Admin server to describe the attributes of policies for an application. The policies are then stored in a policy repository for clients to download.

To be able to configure service definitions, REST calls must be made to the Ranger Admin server. See [Apache Ranger PublicAPIsv2](https://ranger.apache.org/apidocs/resource_PublicAPIsv2.html#resource_PublicAPIsv2_createServiceDef_POST)for APIs required in the following section.

**Installing Apache Spark's Service Definition**

To install Apache Spark's service definition, see [Apache Spark plugin for Ranger integration with Amazon EMR](emr-ranger-spark.md).

**Installing EMRFS Service Definition**

To install the S3 service definition for Amazon EMR, see [EMRFS S3 plugin for Ranger integration with Amazon EMR](emr-ranger-emrfs.md).

**Using Hive Service Definition**

Apache Hive can use the existing Ranger service definition that ships with Apache Ranger 2.0 and later. For more information, see [Apache Hive plugin for Ranger integration with Amazon EMR](emr-ranger-hive.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
