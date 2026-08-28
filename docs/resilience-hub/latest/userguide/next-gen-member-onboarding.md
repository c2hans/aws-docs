---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-member-onboarding.html
---

# Managing member account onboarding
<a name="next-gen-member-onboarding"></a>

Member account onboarding is handled automatically through SLRs:
+ **New accounts** – When a new account joins the organization, an SLR is automatically created in the new account, the account appears in the DA's organization view, and services created in the new account are visible to the DA.
+ **Removed accounts** – When an account leaves the organization, data for that account is no longer visible to the DA, and services in the removed account continue to function independently.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
