---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-service-functions.html
---

# Service functions
<a name="next-gen-service-functions"></a>

**Service functions** are technical subsets of the service topology that represent specific workflows within a service.

For example, an authentication service might have two service functions:
+ **SSO sign-in** – involving the identity provider, session store, and token service.
+ **Registration** – involving the user database, email service, and verification flow.

Service functions help you understand which resources participate in which workflows within a single service. Service functions are identified by the next generation of Resilience Hub during assessment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
