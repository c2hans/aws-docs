---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/deployment-summary.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Deployment summary
<a name="deployment-summary"></a>

A description of the deployment. For example:
+ This account is for a Line-of-Business application deployment (as opposed to a Product application deployment).
+ The deployment involves an auto-scaled ARP (authenticated reverse proxy) within the account’s public or DMZ subnet.
+ Web and application servers will be deployed within the account's private subnet.
+ An RDS (Amazon Relational Database Service) instance will also be deployed within the account’s private Subnet.
+ The servers (ARP, web, application, database, load balancer, etc.) are separated into distinct security groups.
+ The account requires an HA (high availability) design spread across availability zones (AZs) i.e. "Multi-AZ".

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
