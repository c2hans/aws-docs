---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/entitlements.html
---

# Seller issued license entitlements in License Manager
<a name="entitlements"></a>

License Manager captures seller issued license capabilities as *entitlements* in the license. Entitlements can be characterized with a limited or unlimited quantity. An example of a limited entitlement is ‘40 GB of data transfer’. An example of an unlimited quantity entitlement is ‘Platinum Tier’.

A license captures all the granted entitlements, the activation and expiration dates, and the issuer details. A license is a versioned entity and each version is immutable. License versions are updated whenever the license is changed.

To check out or check in limited entitlements, ISV applications must specify the amount of each limited capacity. For unlimited entitlements, ISV applications can simply specify the relevant entitlement to check out or check in again. Finally, limited capabilities also support an “overage” flag, which indicates if end-users can exceed their usage of the initial entitlements. License Manager tracks and reports usage, along with any overages, to the ISV.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
