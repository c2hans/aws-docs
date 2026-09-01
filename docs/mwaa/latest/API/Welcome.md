---
source_url: https://docs.aws.amazon.com/mwaa/latest/API/Welcome.html
---

# Welcome
<a name="Welcome"></a>

This section contains the Amazon Managed Workflows for Apache Airflow (MWAA) API reference documentation. For more information, see [What is Amazon MWAA?](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html).

 **Endpoints**
+  `api.airflow.{region}.amazonaws.com` (use `api.airflow.{region}.api.aws` for IPv6) - This endpoint is used for environment management.
  +  [CreateEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateEnvironment.html)
  +  [DeleteEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_DeleteEnvironment.html)
  +  [GetEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_GetEnvironment.html)
  +  [ListEnvironments](https://docs.aws.amazon.com/mwaa/latest/API/API_ListEnvironments.html)
  +  [ListTagsForResource](https://docs.aws.amazon.com/mwaa/latest/API/API_ListTagsForResource.html)
  +  [TagResource](https://docs.aws.amazon.com/mwaa/latest/API/API_TagResource.html)
  +  [UntagResource](https://docs.aws.amazon.com/mwaa/latest/API/API_UntagResource.html)
  +  [UpdateEnvironment](https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateEnvironment.html)
+  `env.airflow.{region}.amazonaws.com` (use `env.airflow.{region}.api.aws` for IPv6) - This endpoint is used to operate the Airflow environment.
  +  [CreateCliToken](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateCliToken.html )
  +  [CreateWebLoginToken](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateWebLoginToken.html)
  +  [InvokeRestApi](https://docs.aws.amazon.com/mwaa/latest/API/API_InvokeRestApi.html)

 **Regions**

For a list of supported regions, see [Amazon MWAA endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/mwaa.html) in the * AWS General Reference*.

This document was last published on September 1, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MWAA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
