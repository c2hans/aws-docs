---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/tenant-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Tenant isolation
<a name="tenant-isolation"></a>

 The more you move customers into a multi-tenant model, the more they will be concerned about the potential for one tenant to access the resources of another tenant. SaaS systems include explicit mechanisms that ensure that each tenant’s resources—even if they run on shared infrastructure—are isolated.

 This is what we refer to as *tenant isolation*. The idea behind tenant isolation is that your SaaS architecture introduces constructs that tightly control access to resources, and block any attempt to access resources of another tenant.

 Note that tenant isolation is separate from general security mechanisms. Your system will support authentication and authorization; however, the fact that a tenant user is authenticated does not mean that your system has achieved isolation. Isolation is applied separately from the basic authentication and authorization that may be part of your application.

 To better understand this, imagine you’ve used an identity provider to authenticate access to your SaaS system. The token from this authentication experience may also include information about a user’s role which could be used to control that user’s access to a specific application functionality. These constructs provide security, but not isolation. In fact, a user could be authenticated and authorized, and still access the resources of another tenant. Nothing about authentication and authorization will necessarily block this access.

 Tenant isolation focuses exclusively on using tenant context to limit access to resources. It evaluates the context of the current tenant, and uses that context to determine which resources are accessible for that tenant. It applies this isolation for all users within that tenant.

 This gets more challenging as we look at how tenant isolation is realized across all the different SaaS architecture patterns. In some cases, isolation may be achieved by having entire stacks of resources dedicated to a tenant where network (or more coarse-grained) policies prevent cross-tenant access. In other scenarios, you may have pooled resources (items in an [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table) that require more fine-grained policies to control access to the resources.

 Any attempt to access a tenant resource should be scoped to just those resources that belong to that tenant. It’s the job of SaaS developers and architects to determine which combination of tools and technologies will support the isolation requirements of your specific application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
