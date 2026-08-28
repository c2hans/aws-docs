---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/access.html
---

# Controlling database access during decomposition
<a name="access"></a>

Many organizations face a common scenario: a central database that has grown organically over many years and is accessed directly by multiple services and teams. This creates several critical problems:
+ **Uncontrolled growth** – As teams continuously add new features and modify schemas, the database becomes increasingly complex and difficult to manage.
+ **Performance concerns** – Even with hardware improvements, the growing load eventually threatens to exceed the database's capabilities. Impossibility to tune queries due to schema complexity or lack of skills. Unable to predict or explain system performance.
+ **Decomposition paralysis** – It becomes nearly impossible to split or refactor the database while it's actively being modified by multiple teams.

**Note**
Monolithic database systems often reuse the same credentials for applications or services or for administration. This leads to poor database traceability. Setting [dedicated roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) and adopting the [principle of least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) can help you increase security and availability.

When dealing with a monolithic database that has become unwieldy, one of the most effective patterns to control access is called a *database wrapper service*. It provides a strategic first step in managing complex database systems. It establishes controlled database access and enables gradual modernization, while reducing risk. This approach creates a foundation for incremental improvements by providing clear visibility into data usage patterns and dependencies. It's a transitional architecture that serves as a step toward full database decomposition. The wrapper service provides the stability and control needed to make that journey successfully.

**This section contains the following topics:**
+ [Controlling access with the database wrapper service pattern](access-about-dbws.md)
+ [Controlling access with the CQRS pattern](access-about-cqrs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
