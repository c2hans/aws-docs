---
source_url: https://docs.aws.amazon.com/ram/latest/userguide/tshoot-shared-org-no-invite.html
---

# The other account in my organization never receives an invitation
<a name="tshoot-shared-org-no-invite"></a>

## Scenario
<a name="tshoot-shared-org-no-invite-scenario"></a>

When you share resources with another account in the same organization managed by AWS Organizations, they don't receive invitations.

## Cause
<a name="tshoot-shared-org-no-invite-cause"></a>

This is **expected behavior** if your account has [sharing within the AWS organization](getting-started-sharing.md#getting-started-sharing-orgs) turned on.

When this option is turned on and you share with another account in your organization, no invitations are sent and no acceptance is required. All organization accounts that you reference as principals in the resource share can immediately begin accessing the resources in the share.

If your account has *not* turned on sharing within the AWS organization, then when you share with other accounts, even if they are in the same AWS organization, they are treated as standalone accounts. Invitations are sent and must be accepted before users can access the resources in the shares.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
