---
source_url: https://docs.aws.amazon.com/enclaves/latest/user/uninstall-cli.html
---

# Uninstall the Nitro Enclaves CLI on Linux
<a name="uninstall-cli"></a>

If you no longer want to use AWS Nitro Enclaves on your Linux instance, use the following command to uninstall the AWS Nitro Enclaves CLI.

------
#### [ Amazon Linux 2023 ]

```
$ sudo dnf remove aws-nitro-enclaves-cli
```

------
#### [ Amazon Linux 2 ]

```
$ sudo yum remove aws-nitro-enclaves-cli
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query enclaves` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
