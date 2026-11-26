---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/security-iam.html
---

# Identity and access management for ELB for Envoy

AWS Identity and Access Management (IAM) controls who in your account can create and manage proxies, and which role each proxy uses to run on your behalf.

To let a user, group, or role manage proxies, attach an identity-based IAM policy that allows the ELB for Envoy API operations. Grant only the operations that the identity needs.

Each proxy also uses an IAM role that you pass in the `roleArn` field when you create the proxy. The role's trust policy allows the `elasticloadbalancing.amazonaws.com` service principal to assume it, so that ELB for Envoy can run the proxy for you. For instructions on creating this role, see [Create a proxy role](setting-up.md#setting-up-proxy-role).
