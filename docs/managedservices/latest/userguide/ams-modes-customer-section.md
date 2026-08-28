---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/ams-modes-customer-section.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Customer Managed mode
<a name="ams-modes-customer-section"></a>

AWS Managed Services (AMS) Customer Managed mode provides a governance model that is flexible and can be adapted to your requirements. This can be considered a fallback option for services and applications that AMS is unable to operate for you. AMS does not operate infrastructure hosted in accounts created under this mode. However, you can leverage centralized multi-account management in this mode. The following Multi-Account Landing Zone features can be leveraged in this mode:
+ Automated Account deployment
+ Connectivity through Transit Gateway in networking account
+ AMS Config Rules library
+ Store copies of logs in logging account
+ Aggregation of customer managed Guard Duty alerts to Security account
+ Consolidated Billing
+ Enablement of custom Service Control Policies.

For example: If you want to run workloads on Ubuntu Pro, which is not an Operating System managed by AMS, you could use a customer managed account for hosting it. You can also consolidate workloads through customer managed accounts, to take advantage of the bulk discount on Reserved Instances/Sharing Plans available through sharing across an AWS organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
