---
source_url: https://docs.aws.amazon.com/vpc/latest/ipam/choose-single-user-or-orgs-ipam.html
---

# Configure integration options for your IPAM
<a name="choose-single-user-or-orgs-ipam"></a>

This section describes your options for how you can integrate IPAM with AWS Organizations, other AWS accounts, or use it with a single AWS account.

Before you begin using IPAM, you must choose one of the options in this section to enable IPAM to monitor CIDRs associated with EC2 networking resources and store metrics:
+ To enable IPAM to integrate with AWS Organizations to enable the Amazon VPC IPAM service to manage and monitor networking resources created by all AWS Organizations member accounts, see [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md).
+ After you integrate with AWS Organizations, to integrate IPAM with accounts outside of your organization, see [Integrate IPAM with accounts outside of your organization](enable-integ-ipam-outside-org.md).
+ To use a single AWS account with IPAM and enable the Amazon VPC IPAM service to manage and monitor the networking resources you create with the single account, see [Use IPAM with a single account](enable-single-user-ipam.md).

If you do not choose one of these options, you can still create IPAM resources, such as pools, but you won't see metrics in your dashboard and you will not be able to monitor the status of resources.

**Topics**
+ [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md)
+ [Integrate IPAM with accounts outside of your organization](enable-integ-ipam-outside-org.md)
+ [Use IPAM with a single account](enable-single-user-ipam.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
