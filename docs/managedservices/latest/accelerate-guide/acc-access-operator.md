---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-access-operator.html
---

# How AMS accesses your account
<a name="acc-access-operator"></a>

AMS Accelerate operators can access your account console and instances, in certain circumstances.

![AMS Accelerate console access method.](http://docs.aws.amazon.com/managedservices/latest/accelerate-guide/images/acc-op-console-access-method2.png)

AMS operators use the internal AMS Accelerate access service to access your accounts in a secured and audited manner. To access your instances, AMS operators use the same internal AMS access service as the broker and, after access is granted, AMS Accelerate operators use SSM session manager to gain access by using session credentials. RDP access for Windows instances is provided by establishing port forwarding to the instance and creating a local user using SSM. The local user credentials are used for RDP access and removed at the end of the session.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
