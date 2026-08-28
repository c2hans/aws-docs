---
source_url: https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html
---

# Integrate IPAM with accounts outside of your organization
<a name="enable-integ-ipam-outside-org"></a>

This section describes how to integrate your IPAM with AWS accounts outside of your organization. To complete steps in this section, you must have already completed the steps in [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md) and delegated an IPAM account.

Integrating IPAM with AWS accounts outside of your organization enables you to do the following:
+ Manage IP addresses outside of your organization from a single IPAM account.
+ Share IPAM pools with third-party services hosted by other AWS accounts in other AWS Organizations.

After you integrate IPAM with AWS accounts outside of your organization, you can share an IPAM pool directly with the desired accounts of other organizations.

**Topics**
+ [Considerations and limitations](enable-integ-ipam-outside-org-considerations.md)
+ [Process overview](enable-integ-ipam-outside-org-process.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
