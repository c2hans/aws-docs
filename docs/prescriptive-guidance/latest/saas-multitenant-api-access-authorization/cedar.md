---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/cedar.html
---

# Cedar overview
<a name="cedar"></a>

Cedar is a flexible, extensible, and scalable policy-based access control language that helps developers express application permissions as policies. Administrators and developers can define policies that permit or forbid users to act on application resources. Multiple policies can be attached to a single resource. When a user of your application tries to perform an action on a resource, your application requests authorization from the Cedar policy engine. Cedar evaluates the applicable policies and returns an `ALLOW` or `DENY` decision. Cedar supports authorization rules for any type of principal and resource, allows for role-based access control (RBAC) and attribute-based access control (ABAC), and supports analysis through automated reasoning tools.

Cedar lets you separate your business logic from the authorization logic. When you make requests from your application's code, you call Cedar's authorization engine to determine whether the request is authorized. If it's authorized (the decision is `ALLOW`), your application can perform the requested operation. If it isn't authorized (the decision is `DENY`), your application can return an error message. Major features of Cedar include:
+ **Expressiveness** – Cedar is purpose-built to support authorization use cases and was developed with human readability in mind.
+ **Performance** – Cedar supports indexing policies for quick retrieval, and provides fast and scalable real-time evaluation with bounded latency.
+ **Analysis** – Cedar supports analysis tools that can optimize your policies and verify your security model.

For more information, see the [Cedar website](https://www.cedarpolicy.com/).
