---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-orphan.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk orphan`
<a name="ref-cli-cmd-orphan"></a>

**Important**
The `cdk orphan` command is in preview release and is subject to change.
You must provide the `--unstable=orphan` option when using this command.

Safely detach one or more resources from an AWS CloudFormation stack without deleting them. This is useful when you need to migrate a resource from one construct type to another (for example, migrating a DynamoDB `Table` to `TableV2`) without downtime or data loss.

When you change a construct type in your CDK code, CloudFormation interprets this as a resource replacement, which deletes the existing resource and creates a new one. For stateful resources like databases and storage, this causes data loss. The `cdk orphan` command solves this by detaching the resource from the stack first, so you can re-import it under the new construct type using `cdk import`.

With `cdk orphan`, you can:
+ Detach stateful resources from a stack before changing their construct type.
+ Migrate between construct versions (for example, DynamoDB `Table` to `TableV2`) without data loss.
+ Change the CloudFormation resource type backing a construct without replacing the physical resource.

The orphan command performs three CloudFormation deployments:

1.  **Resolve references**: Resolves cross-resource references (`Ref`, `Fn::GetAtt`, `Fn::Sub`) to the orphaned resources, so that other resources in the stack that depend on them continue to work after the orphaned resources are removed.

1.  **Decouple**: Replaces all cross-resource references with their resolved literal values, sets `DeletionPolicy` to `Retain`, and removes `DependsOn` entries to isolate the resources from the rest of the stack.

1.  **Remove**: Removes the resources from the CloudFormation template. The physical resources continue to exist in your AWS account.

After orphaning, update your CDK code to use the new construct type and use [cdk import](ref-cli-cmd-import.md) to bring the resource back under management.

 **To orphan a resource and re-import it under a new construct type**

1. Deploy your stack and verify the resource exists.

1. Run `cdk orphan` with the construct path of the resource:

   ```
   $ cdk orphan MyStack/MyTable --unstable=orphan
   ```

1. The command outputs a resource mapping. Save this for the import step.

1. Update your CDK code to use the new construct type (for example, change `Table` to `TableV2`).

1. Run `cdk import` with the resource mapping from the orphan output:

   ```
   $ cdk import MyStack --resource-mapping-inline '{"MyTable":{"TableName":"my-table"}}'
   ```

1. After the import completes, `cdk import` detects drift and prompts you to deploy. Accept the prompt to reconcile the stack.

This feature currently has the following limitations:
+ All construct paths must reference the same stack. Orphaning resources across multiple stacks in a single command is not supported.
+ Wildcard patterns are not supported. Paths are matched as exact prefixes.
+ This command requires version 32 of the bootstrap template, which includes the necessary IAM permissions for the deploy role.

## Usage
<a name="ref-cli-cmd-orphan-usage"></a>

```
$ cdk orphan <PATHS> <options>
```

## Arguments
<a name="ref-cli-cmd-orphan-args"></a><a name="ref-cli-cmd-orphan-args-paths"></a>

 **PATHS**
One or more construct paths to orphan, in the format `StackName/ConstructPath`. For example, `MyStack/MyTable`. Multiple paths can be provided to orphan several resources in a single command.
All paths must reference the same stack.
 *Type*: String
 *Required*: Yes

## Options
<a name="ref-cli-cmd-orphan-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-orphan-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the `cdk orphan` command.

## Examples
<a name="ref-cli-cmd-orphan-examples"></a>

### Orphan a single resource
<a name="ref-cli-cmd-orphan-examples-single"></a>

```
$ cdk orphan MyStack/MyTable --unstable=orphan
```

### Orphan multiple resources
<a name="ref-cli-cmd-orphan-examples-multiple"></a>

```
$ cdk orphan MyStack/MyTable MyStack/MyBucket --unstable=orphan
```

### Skip confirmation prompt
<a name="ref-cli-cmd-orphan-examples-yes"></a>

```
$ cdk orphan MyStack/MyTable --unstable=orphan --yes
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
