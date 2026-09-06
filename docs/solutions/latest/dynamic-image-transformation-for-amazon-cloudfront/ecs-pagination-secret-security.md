---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-pagination-secret-security.html
---

# Pagination token secret (ECS architecture)
<a name="ecs-pagination-secret-security"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

The management API paginates its list endpoints (origins, mappings, and transformation policies) and returns each page’s continuation cursor as an encrypted, tamper-evident `nextToken`. To encrypt these tokens, the ECS template provisions a secret in AWS Secrets Manager and grants the management API read-only access to it. The tokens are bound to the deployment’s AWS account and expire after 24 hours, so a token cannot be reused across deployments or tampered with by a client. No customer action is required to configure this secret.
