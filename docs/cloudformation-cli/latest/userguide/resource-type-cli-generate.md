---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-generate.html
---

# generate

## Description
<a name="resource-type-cli-generate-description"></a>

The `generate` command generates code based on the project and appropriate extension type schema.

## Synopsis
<a name="resource-type-cli-generate-synopsis"></a>

```sh
$ cfn generate
```

## Examples
<a name="resource-type-cli-generate-examples"></a>

The following command submits the resource to the registry in your CloudFormation account.

```sh
$ cfn generate && cfn submit --set-default --region us-east-1
```

## Output
<a name="resource-type-cli-generate-output"></a>

```
Generated files for <{{type_name}}>
```
