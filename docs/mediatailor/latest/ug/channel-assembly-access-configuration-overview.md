---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-overview.html
---

# How MediaTailor Secrets Manager access token authentication works
<a name="channel-assembly-access-configuration-overview"></a>

After you create or update a source location to use access token authentication, MediaTailor includes the access token in an HTTP header when requesting source content manifests from your origin.

Here's an overview of how MediaTailor uses Secrets Manager access token authentication for source location origin authentication:

1. When you create or update a MediaTailor source location that uses access token authentication, MediaTailor sends a [DescribeSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html#SecretsManager-DescribeSecret-request-SecretId) request to Secrets Manager to determine the AWS KMS key associated with the secret. You include the secret ARN in your source location access configuration.

1. MediaTailor creates a [grant](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) for the customer managed key, so that MediaTailor can use the key to access and decrypt the access token stored in the SecretString. The grant name will be `MediaTailor-SourceLocation-{{your AWS account ID}}-{{source location name}}`.

   You can revoke access to the grant, or remove MediaTailor's access to the customer managed key at any time. For more information, see [RevokeGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html) in the *AWS Key Management Service API Reference*.

1. When a VOD source is created or updated, or used in a program, MediaTailor makes HTTP requests to the source locations to retrieve the source content manifests associated with the VOD sources in the source location. If the VOD source is associated with a source location that has an access token configured, the requests include the access token as an HTTP header value.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
