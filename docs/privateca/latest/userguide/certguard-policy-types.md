---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/certguard-policy-types.html
---

# Supported policy types

You can use X.509 certificate condition keys in the following policy types:
+ **IAM identity-based policies** – Attach to the users, groups, or roles that request certificates. Supports `Allow` and `Deny` statements.
+ **Service control policies (SCPs) and resource control policies (RCPs)** – Apply guardrails across the accounts in an organization in AWS Organizations. Use `Deny` statements.
+ **VPC endpoint policies** – Restrict the certificates that can be requested through an interface VPC endpoint for AWS Private CA. Supports `Allow` and `Deny` statements.
+ **Resource-based policies** – Control cross-account issuance from a shared CA (not available yet; see the following note). AWS Private CA resource-based policies are managed through AWS Resource Access Manager (RAM) and support only `Allow` statements. To restrict the certificates that a cross-account principal can request, add conditions to the `Allow` statement for `acm-pca:IssueCertificate`, for example in a RAM customer managed permission. For more information, see [Customer managed permissions in RAM](pca-cmp.md) and [Resource-based policies](pca-rbp.md).

**Note**
X.509 certificate condition keys (`acm-pca:x509*`) aren't supported yet in the resource-based policy of a private CA. This includes AWS RAM customer managed permissions and policies that you set with [PutPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html). Support is coming soon. Until then, AWS RAM and `PutPolicy` reject a policy that uses these keys with an error such as the following:

```
The condition key acm-pca:x509SAN/DNS does not exist in the service acm-pca. Use a valid condition key.
```
IAM Access Analyzer might also flag these keys in identity-based policies, SCPs, and RCPs, but the keys still take effect in those policies.
To restrict cross-account issuance from a shared CA, use an RCP in the organization that owns the CA. RCPs don't apply to a CA in the organization's management account. Requesting accounts can also use identity-based policies or SCPs.

Most of the examples in this topic use `Deny` statements. Because a resource-based policy can't contain a `Deny` statement, use those examples in identity-based policies, SCPs, RCPs, or VPC endpoint policies.
