---
source_url: https://docs.aws.amazon.com/ses/latest/dg/identity-authorization-policies.html
---

# Using identity authorization in Amazon SES
<a name="identity-authorization-policies"></a>

Identity authorization policies define how individual verified identities can use Amazon SES by specifying which SES API actions are allowed or denied for the identity and under what conditions.

Through the use of these authorization polices, you can maintain control over your identities by changing or revoking permissions at any time. You can even authorize other users to use the identities that you own (domains or email addresses) with their own SES accounts.

**Topics**
+ [Amazon SES policy anatomy](policy-anatomy.md)
+ [Creating an identity authorization policy in Amazon SES](identity-authorization-policies-creating.md)
+ [Identity policy examples in Amazon SES](identity-authorization-policy-examples.md)
+ [Managing your identity authorization policies in Amazon SES](managing-policies.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
