---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/aft-triggers-configuring.html
---

# Configuring customization triggers
<a name="aft-triggers-configuring"></a>

To enable customization triggers, set the `aft_customization_triggers` variable in your AFT deployment module:

```
module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"

  aft_customization_triggers = ["account_move"]

  # ... other variables
}
```

The only valid value is `"account_move"`. To disable customization triggers, set the variable to an empty list (`[]`). The feature is disabled by default.

To exclude a specific account from automatic trigger processing, set the `account_skip_customization_triggers` attribute to `"true"` for the target account in the account request Terraform file. When this attribute is set, AFT skips customization invocation for that account even when it detects an OU change. This is useful for accounts undergoing planned migrations where automatic re-customization is not desired.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
