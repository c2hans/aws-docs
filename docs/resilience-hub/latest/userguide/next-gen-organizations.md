---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-organizations.html
---

# AWS Organizations integration
<a name="next-gen-organizations"></a>

Next generation Resilience Hub integrates with AWS Organizations to enable organization-wide resilience management from a single delegated administrator (DA) account. This eliminates the need to log into individual accounts to assess resilience posture across your enterprise. You get organization-wide visibility into resilience posture and aggregated dashboards without logging into individual accounts.

| Metric | Value |
| --- | --- |
| Accounts per organization | 50,000\+ |
| Services across organization | 10,000 |
| Dashboard query latency | Independent of organization size |
| Data aggregation latency | Less than 5 minutes |

**Topics**
+ [Overview of multi-account governance in the next generation of Resilience Hub](next-gen-orgs-overview.md)
+ [Setting up Organizations integration](next-gen-delegated-admin-setup.md)
+ [Service-Linked Roles](next-gen-org-slrs.md)
+ [Applying resilience policies across accounts](next-gen-org-policies.md)
+ [Viewing organization-wide resilience posture](next-gen-org-posture.md)
+ [Managing member account onboarding](next-gen-member-onboarding.md)
+ [Required IAM permissions for delegated administrator setup](next-gen-org-permissions.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
