---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/service-linked-role-limitations.html
---

# Service-linked role limitations
<a name="service-linked-role-limitations"></a>

 A service-linked role is a special type of IAM role that's linked directly to AWS Lake Formation. This role has pre-defined permissions that allow Lake Formation to perform actions on your behalf across AWS services.

The following limitations apply when using a service-linked role (SLR) to register data locations with Lake Formation.
+ You can't modify service-linked role policies once created.
+ A service linked role doesn't support encrypted catalog resources sharing across accounts. Encrypted resources require specific AWS KMS key permissions. Service-linked roles have pre-defined permissions that don't include the ability to work with encrypted catalog resources across accounts.
+ When registering multiple Amazon S3 locations, using service-linked role may cause you to exceed your IAM policy limits quickly. This happens because with service-linked roles, AWS writes the policy for you, and it increments as one large block that includes all your registrations. You can write customer-managed policies more efficiently, distribute permissions across multiple policies, or use different roles for different Regions.
+ Amazon EMR on EC2 can't access data you register data locations with service-linked roles.
+ Service-linked role operations bypass your AWS service control policies.
+ When you register data locations with a service-linked role, it updates IAM policies with eventual consistency. For more information, see the the [Troubleshoot IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html#troubleshoot_general_eventual-consistency) documentation in the IAM User Guide.
+  You can't set `SET_CONTEXT = TRUE` in Lake Formation data lake settings when using service-linked roles, and you are using IAM Identity Center. The reason is that service-linked roles have immutable trust policies that are incompatible with the trusted identity propagation needed for `SetContext` auditing with IAM Identity Center principals.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
