---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/check-aft-version.html
---

# Check the AFT version
<a name="check-aft-version"></a>

You can check your deployed AFT version by querying the AWS SSM Parameter Store key:

```
/aft/config/aft/version
```

If you use the registry method, you can pin the version.

```
module "control_tower_account_factory" {
  source  = "aws-ia/control_tower_account_factory/aws"
  version = "1.3.2"
  # insert the 6 required variables here
}
```

You can view more information about AFT versions in the [AFT repository](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
