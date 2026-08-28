---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/monitoring-ad-trust.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Single-Account Landing Zone proactive monitoring of Active Directory Trust in AMS
<a name="monitoring-ad-trust"></a>

AMS single-account landing zone (SALZ) monitors the status of the one-way trust(s) between the Managed Active Directory (AD) in your AMS managed account and your company domain. The one-way trust with Managed AD is critical for access requests and instance logon requests. With this new monitoring, AMS now proactively responds to trust related issues, and reduces the mean time to detect access related incidents.

This feature is automatically enabled in your AWS Managed Services (AMS) accounts.

There is a small cost impact. The feature uses four AWS CloudWatch metrics, and two AWS CloudWatch alarms for one trust.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
