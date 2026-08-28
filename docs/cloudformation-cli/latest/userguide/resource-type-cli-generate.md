---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-generate.html
---

# generate
<a name="resource-type-cli-generate"></a>

## Description
<a name="resource-type-cli-generate-description"></a>

The `generate` command generates code based on the project and appropriate extension type schema.

## Synopsis
<a name="resource-type-cli-generate-synopsis"></a>

```
$ cfn generate
```

## Examples
<a name="resource-type-cli-generate-examples"></a>

The following command submits the resource to the registry in your CloudFormation account.

```
$ cfn generate && cfn submit --set-default --region us-east-1
```

## Output
<a name="resource-type-cli-generate-output"></a>

```
Generated files for <{{type_name}}>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudformation-cli` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
