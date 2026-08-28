---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/definition-1.html
---

# Definition
<a name="definition-1"></a>

 There are five best practice areas for security in the cloud:
+  Identity and access management
+  Detective controls
+  Infrastructure protection
+  Data protection
+  Incident response

 Multi-tenancy adds a layer of additional considerations to your SaaS architecture. With SaaS, you have users that are now accessing a shared environment in the context of a given tenant. This context must be captured and conveyed across all the layers of your application’s architecture and plays a fundamental role in securing the overall footprint of your environment.

 From a security perspective, you need to look at how tenancy is introduced into your environment and how it is used to secure tenant resources. Overall, you need to ensure that each tenant has a carefully constrained experience that prevents them from accessing any other tenant’s resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
