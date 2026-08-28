---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete_key_using_keytool_5.html
---

# Delete an AWS CloudHSM key using keytool
<a name="delete_key_using_keytool_5"></a>

The AWS CloudHSM key store doesn't support deleting keys. You can delete keys using the destroy method of the [Destroyable interface](https://devdocs.io/openjdk%7E8/javax/security/auth/destroyable#destroy--).

```
((Destroyable) key).destroy();
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
