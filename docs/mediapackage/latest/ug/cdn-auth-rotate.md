---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/cdn-auth-rotate.html
---

# Rotating the CDN header value
<a name="cdn-auth-rotate"></a>

If you change the CDN custom origin HTTP header value, you need to rotate the stored secret value in Secrets Manager. The following procedure describes how to rotate your value in Secrets Manager to make sure that your CDN's HTTP header value and the Secrets Manager stored secret value are in sync.

**To rotate the value**

1. Update the stored secret value in Secrets Manager as described in [Modifying a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret.html) in the *AWS Secrets Manager User Guide*.

   To ensure continued playback for active streams, MediaPackage authorizes requests that use either the current value in Secrets Manager or one version back.

1. Wait 10 minutes for MediaPackage to recognize that the value has changed in Secrets Manager.

1. In your CDN, update the value in `X-MediaPackage-CDNIdentifier` to the new authorization code.

1. Wait for your CDN to update fully with the new value before you send any requests through it to MediaPackage.

   To disable the previous secret value, save the new secret value two times. This way, both the current and previous secret versions have the same value.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
