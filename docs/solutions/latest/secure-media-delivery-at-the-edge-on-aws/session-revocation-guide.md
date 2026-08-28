---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/session-revocation-guide.html
---

# Session revocation guide
<a name="session-revocation-guide"></a>

 For improving video streams protection, this solution relies on restricting the usage of the token by scoping down viewer specific attributes and video assets path by the relevant token claims. In an ideal situation, the generated token would work with a single video asset and more importantly grant access to a single individual the token was created for. To accomplish this type of strong uniqueness in token to viewer mapping requires selecting a right set of viewer attributes when creating the token, which in aggregation create a unique attributes combination not easily replicable. The weaker the level of viewer attributes uniqueness used in the token, the easier is to reuse the token by other viewers which would give them unauthorized access. Therefore, while it is recommended to include a number of attributes that increase uniqueness of resulting their sum it can also come at the price of false positives as explained in the [Using viewer’s source IP in the token](access-tokens-management-guide.md#using-viewers-source-ip-in-the-token) section as an example. To better manage that tradeoff, this solution also provides an option to revoke playback sessions that were identified as compromised ones – meaning, shared with other viewers through unauthorized channels. If you decide to complement token-based protection with session revocation, think about what type of logic you can employ to discover and block suspicious traffic pattern.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
