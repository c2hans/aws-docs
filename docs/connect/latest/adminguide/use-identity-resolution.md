---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/use-identity-resolution.html
---

# Use Identity Resolution to consolidate similar profiles in Connect Customer
<a name="use-identity-resolution"></a>

A *similar profile* is when two or more profiles are determined to be for the same contact. There can be multiple profiles when customer records are captured across multiple channels and applications for the same customer, and do not share a common unique identifier.

Identity Resolution automatically finds similar profiles and helps you consolidate them. It runs an Identity Resolution Job on a weekly basis, which performs the following steps:

1. [Automatic profile matching](how-identity-resolution-works.md#auto-profile-matching)

1. [Automatic merging of similar profiles](how-identity-resolution-works.md#auto-profile-merging) based on your consolidation criteria

Each time an Identity Resolution Job runs, it displays metrics on the **Customer Profiles** page. The metrics show the number of profiles it reviewed, the number of match groups found, and the number of profiles consolidated.

Additional charges might apply for enabling Identity Resolution. For more information, see [Connect Customer pricing](https://aws.amazon.com/connect/pricing/).

![The Connect Customer Customer Profiles page, the Enable Identity Resolution button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-enable-ir.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
