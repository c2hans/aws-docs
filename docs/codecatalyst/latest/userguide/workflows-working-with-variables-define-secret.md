---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-define-secret.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Defining a secret
<a name="workflows-working-with-variables-define-secret"></a>

You define a secret on the **Secrets** page of the CodeCatalyst console. For more information, see [Masking data using secrets](workflows-secrets.md).

For example, you might define a secret that looks like this:
+ Name (key): **my-password**
+ Value: **^\*H3\#\!b9**

After the secret is defined, you can specify the secret's key (**my-password**) in the workflow definition file. For an example of how to do this, see [Example: Referencing a secret](workflows-working-with-variables-ex.md#workflows-working-with-variables-ex-refer-secret).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
