---
source_url: https://docs.aws.amazon.com/glue/latest/dg/intercom-limitations.html
---

# Limitations
<a name="intercom-limitations"></a>

The following are limitations for the Intercom connector:
+  When using the Company entity, there is a limit of 10,000 Companies that can be returned. For more information, see [ List all companies API](https://developers.intercom.com/docs/references/2.5/rest-api/companies/list-companies).
+  While applying order by, filter is mandatory for both **Contact** and **Conversation** entities.
+  MCA is supported by the SaaS provider. However, based on the API rate limits mentioned in the documentation, we will not host MCA on AWS Glue as it may impact other workloads and potentially cause performance issues due to resource contention.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
