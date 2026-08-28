---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/establish-mechanisms-changes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Establish mechanisms to access, review, and monitor changes
<a name="establish-mechanisms-changes"></a>

 All changes within the scope of your change management should be monitored and tracked for approved and out-of-band changes within the environment. Every change that is approved and implemented should have a positive impact to the overall service such as, a security gain or performance gain within the environment. Changes that are tracked and have adverse effects to the environment should be rolled back immediately which will restore the baseline to its previous state. The goal of continuously monitoring your baseline and alerting on configuration items changes is that all change introduced into the environment is controlled. Changes that happen outside of the management process need to be tracked down and reverted back to its previous baseline or documented in your change management system.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
