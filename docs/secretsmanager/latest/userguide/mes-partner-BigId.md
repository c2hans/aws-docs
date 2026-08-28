---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partner-BigId.html
---

# Big ID Refresh Token
<a name="mes-partner-BigId"></a>

## Secret Value Fields
<a name="w2aac27c11c13b3"></a>

The following are the fields that must be contained in the Secrets Manager secret:

```
{
  "hostname": "{{Host Name}}",
  "refreshToken": "{{Refresh Token}}"
}
```

hostname
This is the hostname where your BigID instance is hosted. You must enter the fully qualified domain name of your instance.

refreshToken
The JWT user refresh token generated in the BigID Console via Administration → Access Management → Select User → Generate Token → Save

## Usage Flow
<a name="w2aac27c11c13b5"></a>

You can create your secret using the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) call with the secret value containing the fields mentioned above and secret type as BigIDClientSecret. The rotation configurations can be set using a [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call. You must also provide a role ARN in the [RotateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html) call which grants the service the required permissions to rotate the secret. For example of a permissions policy see [Security and Permissions](mes-security.md). Note that the rotation metadata field can be left empty for this partner.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
