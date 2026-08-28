---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/change-management-for-the-nitro-system.html
---

# Change management for the Nitro System
<a name="change-management-for-the-nitro-system"></a>

 The software and firmware underlying the Nitro System is developed by diverse and globally distributed teams of engineers. All Nitro System related configurations and code changes are subject to multi-party review and approval, and staged rollouts in both testing and production environments. The software development starts with design documents and reviews, and moves through code reviews. A security review will be conducted by both the independent AWS Security team as well as the Amazon EC2 engineering team for significant changes or features.

 All changes are reviewed by at least one additional engineering team member or stakeholder, as well as by an engineer with substantial EC2 tenure serving as a member of our Change Management Bar Raiser program. In addition to expert human review, all code check-ins must pass a battery of automated quality and security checks that cannot be by-passed and that run automatically under the control of a central build service which ensures deployment best practices are followed, including proper monitoring and rollback.

 Once code reviews and approvals are complete, and all automated checks are passed, our automated package deployment process takes over. As part of this automated deployment pipeline, binary artifacts are built and teams run end-to-end, validation, and security-specific tests. If any type of validation fails, the deployment process is halted until the issue is remediated.

 Software and firmware binaries are cryptographically signed using an asymmetric private key which is only accessible through the automated pipeline, which logs all key signing activity.

 Signed software and firmware are deployed to the EC2 fleet by a dedicated EC2 deployment system, which is configured to follow a defined deployment policy and schedule. Changes roll out in waves across Availability Zones and Regions. Deployments are monitored to ensure that only software versions that function as intended remain deployed and that any anomalous behavior triggers automatic rollbacks.

**Note**
 Refer to the [Amazon Builder’s Library](https://aws.amazon.com/builders-library) for more on how Amazon builds and operates software. Specifically, [Automating safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/) by Clare Liguori, Sr. Principal Engineer at AWS, [Going faster with continuous delivery](https://aws.amazon.com/builders-library/going-faster-with-continuous-delivery) by Mark Mansour, Senior Manager of Software Development at AWS, and [Ensuring rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/) by Sandeep Pokkunuri, Senior Principal Engineer at AWS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
