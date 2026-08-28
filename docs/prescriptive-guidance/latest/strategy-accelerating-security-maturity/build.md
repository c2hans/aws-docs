---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/build.html
---

# Build: Laying the groundwork for a strong cloud security foundation
<a name="build"></a>

Now that you have a plan, the next step is laying the groundwork. This step demonstrates how to build an initial cloud foundation on AWS that is secure, resilient, scalable, and automated across multiple accounts. Laying the groundwork can be specifically designed and customized according to your business goals. You can adapt controls to a new landing zone, or you can include them in an existing landing zone. The automations in [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) can help you lay the security groundwork in the AWS Cloud. The following image shows a landing zone that is set up through AWS Control Tower.

![Build an initial cloud foundation by using AWS Control Tower](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/0a0df765-5dea-41b9-be80-44f4ef98ca43.png)

AWS Control Tower orchestrates multiple AWS services on your behalf, such as AWS Organizations, AWS Service Catalog, and AWS IAM Identity Center. You can set up a new landing zone within an hour, and that landing zone is designed to meet your security and compliance requirements. AWS Control Tower sets up your landing zone according to prescriptive security best practices. AWS Control Tower helps you manage cloud provisioning by enhancing visibility and control over accounts and end users. It helps administrators efficiently allocate and oversee compute resources, implement role-based access control, monitor performance through logging and monitoring tools, effectively manage costs, automate deployment processes, enforce security measures, and ensure compliance to industry standards.

AWS Control Tower is the fastest way to set up and govern a secure, compliant, multi-account AWS environment based on best practices. For more information about the working with AWS Control Tower and the best practices outlined in the AWS multi-account strategy, see [AWS multi-account strategy: Best practices guidance](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html#multi-account-guidance).

Although AWS Control Tower is the fastest approach, it's not the only one. The important part is that you set up a landing zone that, at a minimum, provides the following:
+ Multi-account management
+ Identity and federated access management
+ A centralized archive for logs
+ Cross-account audit access
+ End-user account provisioning
+ Centralized monitoring and notifications

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
