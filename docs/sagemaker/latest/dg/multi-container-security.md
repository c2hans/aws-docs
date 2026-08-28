---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-security.html
---

# Security with multi-container endpoints with direct invocation
<a name="multi-container-security"></a>

 For multi-container endpoints with direct invocation, there are multiple containers hosted in a single instance by sharing memory and a storage volume. It's your responsibility to use secure containers, maintain the correct mapping of requests to target containers, and provide users with the correct access to target containers. SageMaker AI uses IAM roles to provide IAM identity-based policies that you use to specify whether access to a resource is allowed or denied to that role, and under what conditions. For information about IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *AWS Identity and Access Management User Guide*. For information about identity-based policies, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html).

By default, an IAM principal with `InvokeEndpoint` permissions on a multi-container endpoint with direct invocation can invoke any container inside the endpoint with the endpoint name that you specify when you call `invoke_endpoint`. If you need to restrict `invoke_endpoint` access to a limited set of containers inside a multi-container endpoint, use the `sagemaker:TargetContainerHostname` IAM condition key. The following policies show how to limit calls to specific containers within an endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
