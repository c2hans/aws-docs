---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-10-end-user-identity-and-authentication.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 10: End user identity and authentication
<a name="principle-10-end-user-identity-and-authentication"></a>

 *All access to service interfaces should be constrained to authenticated and authorised [end user] individuals.*

 **Applicable risk classes:** III-V
+  **Two factor authentication** — If required, the customer may configure identities to authenticate using additional factors.
+  **Identity federation with your existing identity provider** — If configuring federation between an existing identity provider and IAM, the identity provider’s two-factor authentication will operate independently of AWS, so the only AWS-specific task the customer is required to undertake is the federation itself.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
