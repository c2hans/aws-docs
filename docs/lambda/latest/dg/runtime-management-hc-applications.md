---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/runtime-management-hc-applications.html
---

# Controlling Lambda runtime update permissions for high-compliance applications
<a name="runtime-management-hc-applications"></a>

To meet patching requirements, Lambda customers typically rely on automatic runtime updates. If your application is subject to strict patching freshness requirements, you might want to limit use of earlier runtime versions. You can restrict Lambda's runtime management controls by using AWS Identity and Access Management (IAM) to deny users in your AWS account access to the [PutRuntimeManagementConfig](https://docs.aws.amazon.com/lambda/latest/api/API_PutRuntimeManagementConfig.html) API operation. This operation is used to choose the runtime update mode for a function.

Denying access to this operation causes all functions to default to the **Auto** mode. You can apply this restriction across your organization by using a [service control policies (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html). If you must roll back a function to an earlier runtime version, you can grant a policy exception on a case-by-case basis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
