---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth-troubleshooting.html
---

# Troubleshoot MediaPackage CDN authorization errors
<a name="cdn-auth-troubleshooting"></a>

When AWS Elemental MediaPackage CDN authorization fails, you may encounter various error codes and authorization issues. This section helps you identify and resolve common problems with CDN authorization configuration, secret management, and IAM permissions.

**Common Error Scenarios and Resolutions**

| Scenario | Error Type | Resolution |
| --- | --- | --- |
| Secret validation failure | 4XX error | Verify that your secret is stored with the correct key name MediaPackageV2CDNIdentifier and the value is between 8-256 characters. |
| IAM role access denied | 4XX error | Check that the IAM role has the correct permissions and trust relationship as described in [Configure MediaPackage CDN authorization setup](cdn-auth-setup.md). |
| Secret not found | 4XX error | Verify that the secret ARN is correct and the secret exists in the same Region as your MediaPackage endpoint. |
| Header value mismatch | 403 Unauthorized | Ensure that the value in the X-MediaPackageV2-CDNIdentifier header matches the value stored in Secrets Manager. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
