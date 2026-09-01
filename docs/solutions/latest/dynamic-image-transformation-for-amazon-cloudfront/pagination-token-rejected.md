---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/pagination-token-rejected.html
---

# List endpoint returns the first page instead of the next page
<a name="pagination-token-rejected"></a>

 **Symptoms:**
+ Paging through `GET /policies`, `GET /origins`, or `GET /mappings` with a `nextToken` returns the first page again, or a list request fails immediately after the ECS tasks restart.

 **Cause:**

Pagination tokens are encrypted, account-bound, and expire 24 hours after they are issued. An expired, tampered, or cross-deployment token is treated as invalid, and the API returns the first page rather than failing. Separately, generating a token requires reading the pagination secret from AWS Secrets Manager; on a cold start, before the key is cached, a transient Secrets Manager error can cause a list request to fail.

 **Solutions:**
+ Don’t store or reuse `nextToken` values for longer than 24 hours, and don’t share them across deployments. Restart pagination from the first request to obtain a fresh token.
+ If a list request fails right after a deployment or scaling event, retry; the encryption key is cached after the first successful read, so the condition is transient.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
