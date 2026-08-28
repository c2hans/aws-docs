---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-tool-syntax.html
---

# AWS CloudHSM Client SDK 3 configuration syntax
<a name="configure-tool-syntax"></a>

The following table illustrates the syntax for AWS CloudHSM configuration files for Client SDK 3.

```
configure -h | --help
          -a {{<ENI IP address>}}
          -m [-i {{<daemon_id>}}]
          --ssl --pkey {{<private key file>}} --cert {{<certificate file>}}
          --cmu {{<ENI IP address>}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
