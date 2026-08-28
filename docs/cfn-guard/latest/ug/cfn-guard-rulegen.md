---
source_url: https://docs.aws.amazon.com/cfn-guard/latest/ug/cfn-guard-rulegen.html
---

# rulegen
<a name="cfn-guard-rulegen"></a>

Takes a JSON- or YAML-formatted AWS CloudFormation template file and autogenerates a set of AWS CloudFormation Guard rules that match the properties of the template resources. This command is a useful way to get started with rule writing or to create ready-to-use rules from known good templates.

## Syntax
<a name="cfn-guard-rulgen-synopsis"></a>

```
cfn-guard rulegen
--output <value>
--template <value>
```

## Parameters
<a name="cfn-guard-rulegen-flags"></a>

`-h`, `--help`

Prints help information.

`-V`, `--version`

Prints version information.

## Options
<a name="cfn-guard-rulegen-options"></a>

`-o`, `--output`

Writes the generated rules to an output file. Given the potential for hundreds or even thousands of rules to emerge, we recommend using this option.

`-t`, `--template`

Provides the path to a CloudFormation template file in JSON or YAML format.

## Examples
<a name="cfn-guard-rulegen-examples"></a>

```
cfn-guard rulegen --output {{rules.guard}} --template {{template.json}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation Guard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cfn-guard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
