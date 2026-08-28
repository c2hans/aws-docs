---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-cost-allocation-tags-planning.html
---

# Account cost allocation tags
<a name="account-cost-allocation-tags-planning"></a>

Innovation Sandbox on AWS applies AWS Organizations account tags to sandbox accounts throughout the lease lifecycle. It then activates these tags as cost allocation tags in AWS Billing and Cost Management. With these tags, you can analyze sandbox costs by lease, user, cost report group, lease template, and account state in AWS Cost Explorer, AWS Budgets, and Cost and Usage Reports. For an architectural description of this feature, see the [Account cost allocation tagging](account-cost-allocation-tagging.md) section.

Consider the following before you deploy:
+  **Activation delay**: After deployment or update, the ISB tag keys can take up to 24 hours to activate in the billing system, and tagged cost data can take up to 24 hours to appear in AWS Cost Explorer. All cost is still attributed correctly during this delay.
+  **Tags are not retroactive**: The solution attributes cost to a tag only from the time it applies the tag to the account.
+  **Account tag limit**: AWS Organizations allows a maximum of 50 tags per account. The solution reserves 5 tags for its ISB tag keys, so a sandbox account must have 45 or fewer of your own custom tags when a lease is approved. If an account already has more tags than this limit, the solution logs a `TagResourceFailed` event with `reason: "TagSpaceExhausted"` and the lease proceeds using the legacy cost attribution path.
+  **Backward compatibility**: Leases created before you deploy this feature continue to use the solution’s existing AWS Cost Explorer cost attribution until they are terminated. No migration is required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
