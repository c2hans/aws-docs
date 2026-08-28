---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/cancel-automatic-rotation.html
---

# Cancel automatic rotation in Secrets Manager
<a name="cancel-automatic-rotation"></a>

If you configured [automatic rotation](rotating-secrets.md) for a secret and you want to stop rotating it, you can cancel rotation.

**To cancel automatic rotation**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose your secret.

1. On the secret details page, under **Rotation configuration**, choose **Edit rotation**.

1. In the **Edit rotation configuration** dialog box, turn off **Automatic rotation**, and then choose **Save**.

   Secrets Manager retains the rotation configuration information so that you can use it in the future if you decide to turn rotation back on.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
