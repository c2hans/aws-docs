---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac-permissions-ref.html
---

# Amazon OpenSearch Service API permissions reference
<a name="ac-permissions-ref"></a>

When you set up [access control](ac.md), you write permission policies that you can attach to an IAM identity (identity-based policies). For detailed reference information, see the following topics in the *Service Authorization Reference*:
+ [Actions, resources, and condition keys for OpenSearch Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonopensearchservice.html).
+ [Actions, resources, and condition keys for OpenSearch Ingestion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_opensearchingestionservice.html).

This reference contains information about which API operations can be used in an IAM policy. It also includes the AWS resource for which you can grant the permissions, and condition keys that you can include for fine-grained access control.

You specify the actions in the policy's `Action` field, the resource value in the policy's `Resource` field, and conditions in the policy's `Condition` field. To specify an action for OpenSearch Service, use the `es:` prefix followed by the API operation name (for example, `es:CreateDomain`). To specify an action for OpenSearch Ingestion, use the `osis:` prefix followed by the API operation (for example, `osis:CreatePipeline`).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
