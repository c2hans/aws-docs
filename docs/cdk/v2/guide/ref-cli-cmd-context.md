---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-context.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk context`
<a name="ref-cli-cmd-context"></a>

Manage cached context values for your AWS CDK application.

 *Context* represents the configuration and environment information that can influence how your stacks are synthesized and deployed. Use `cdk context` to do the following:
+ View your configured context values.
+ Set and manage context values.
+ Remove context values.

## Usage
<a name="ref-cli-cmd-context-usage"></a>

```
$ cdk context <options>
```

## Options
<a name="ref-cli-cmd-context-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-context-options-clear"></a>

 `--clear <BOOLEAN>`
Clear all context.<a name="ref-cli-cmd-context-options-force"></a>

 `--force, -f <BOOLEAN>`
Ignore missing key error.
 *Default value*: `false` <a name="ref-cli-cmd-context-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the `cdk context` command.<a name="ref-cli-cmd-context-options-reset"></a>

 `--reset, -e <STRING>`
The context key, or its index, to reset.
