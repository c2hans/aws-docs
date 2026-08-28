---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/updating-registered-hook.html
---

# Updating a custom Hook
<a name="updating-registered-hook"></a>

Updating a custom Hook allows revisions in the Hook to be made available in the CloudFormation registry.

To update a custom Hook, submit your revisions to the CloudFormation registry through the CloudFormation CLI [submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html) operation.

```
$ cfn submit
```

To specify the default version of your Hook in your account, use the [set-type-default-version](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/set-type-default-version.html) command and specify the type, type name, and version ID.

```
$ aws cloudformation set-type-default-version \
    --type HOOK \
    --type-name {{MyCompany::Testing::MyTestHook}} \
    --version-id {{00000003}}
```

To retrieve information about the versions of a Hook, use [list-type-versions](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-type-versions.html).

```
$ aws cloudformation list-type-versions \
  --type HOOK \
  --type-name "{{MyCompany::Testing::MyTestHook}}"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
