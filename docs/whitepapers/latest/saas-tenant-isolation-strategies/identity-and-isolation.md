---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/identity-and-isolation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Identity and isolation
<a name="identity-and-isolation"></a>

 While the scope of your discussion is limited to isolation, it’s important to look at how identity connects to the isolation model. The reality is, if you are planning to isolate tenants, you must have some way to represent and identify the tenant that is currently accessing the resources of our SaaS environment. In many cases, identity will be used in combination with other constructs to acquire the policies and scoping rules that are at the core of an isolation scheme. How these policies are defined and applied will vary for each of the isolation models and services you’re consuming. Still, the basics of the approach usually follow a pattern similar to what is shown in Figure 5.

![Diagram showing the connection between identity and isolation.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/connecting-identity-and-isolation.png)

 This diagram represents a generalization of how identity gets connected to the broader isolation story. Here you’ll notice that, as a user is authenticated, the system will return tenant context back to your application that includes the user’s binding to a tenant as well as the policies that will be used to enforce isolation for that tenant. This context then flows through all of our interactions and is used by the downstream elements of the SaaS environment to scope access to resource (in this case a database).

 How that scope is acquired and applied will vary based on the isolation model and resources you’re consuming, but this model provides a view of the core concepts. One key area of variation is in how the tenant scoping is determined. This scoping context could be attached to a service when it is deployed or it could be acquired at run-time. We’ll look at both of those models as we get into the specific isolation traits for different architecture models.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
