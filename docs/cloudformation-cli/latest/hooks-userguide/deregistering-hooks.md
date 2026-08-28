---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/deregistering-hooks.html
---

# Deregistering a custom Hook from the CloudFormation registry
<a name="deregistering-hooks"></a>

Deregistering a custom Hook marks the extension or extension version as `DEPRECATED` in the CloudFormation registry, which removes it from active use. Once deprecated, the custom Hook can't be used in a CloudFormation operation.

**Note**
Before deregistering the Hook, you must individually deregister all previous active versions of that extension. For more information, see [DeregisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html).

To deregister a Hook, use the [deregister-type](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deregister-type.html) operation and specify your Hook ARN.

```
$ aws cloudformation deregister-type \
    --arn {{HOOK_TYPE_ARN}}
```

This command doesn't produce an output.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
