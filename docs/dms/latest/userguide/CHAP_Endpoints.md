---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html
---

# Working with AWS DMS endpoints
<a name="CHAP_Endpoints"></a>

An endpoint provides connection, data store type, and location information about your data store. AWS Database Migration Service uses this information to connect to a data store and migrate data from a source endpoint to a target endpoint. You can specify additional connection attributes for an endpoint by using endpoint settings. These settings can control logging, file size, and other parameters; for more information about endpoint settings, see the documentation section for your data store.

Following, you can find out more details about endpoints.

**Topics**
+ [Creating source and target endpoints](CHAP_Endpoints.Creating.md)
+ [Sources for data migration](CHAP_Source.md)
+ [Targets for data migration](CHAP_Target.md)
+ [Configuring VPC endpoints for AWS DMS](CHAP_VPC_Endpoints.md)
+ [DDL statements supported by AWS DMS](CHAP_Introduction.SupportedDDL.md)
+ [Advanced endpoint configuration](CHAP_Advanced.Endpoints.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
