---
source_url: https://docs.aws.amazon.com/glue/latest/dg/okta-connector-limitations.html
---

# Limitations
<a name="okta-connector-limitations"></a>

The following are limitations for the Okta connector:
+  For ‘Applications’ entity only one filter can be applied. If more than 1 filter is applied then 400 Bad Request is return with error summary –‘Invalid Search criteria’.
+  Order by can be supported with search queries only. For example, ` http://dev-15940405.okta.com/api/v1/groups?search=type e.q. "OKTA_GROUP"&sortBy=lastUpdated&sortOrder=asc `

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
