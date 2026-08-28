---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-service-linked-roles.html
---

# Using service-linked roles for Elastic Beanstalk
<a name="using-service-linked-roles"></a>

AWS Elastic Beanstalk uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Elastic Beanstalk. Service-linked roles are predefined by Elastic Beanstalk and include all the permissions that the service requires to call other AWS services on your behalf.

Elastic Beanstalk defines a few types of service-linked roles:
+ *Monitoring service-linked role* – Allows Elastic Beanstalk to monitor the health of running environments and publish health event notifications.
+ *Maintenance service-linked role* – Allows Elastic Beanstalk to perform regular maintenance activities for your running environments.
+ *Managed-updates service-linked role* – Allows Elastic Beanstalk to perform scheduled platform updates of your running environments.

**Topics**
+ [The monitoring service-linked role](using-service-linked-roles-monitoring.md)
+ [The maintenance service-linked role](using-service-linked-roles-maintenance.md)
+ [The managed-updates service-linked role](using-service-linked-roles-managedupdates.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
