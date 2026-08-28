---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-destroy.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk destroy`
<a name="ref-cli-cmd-destroy"></a>

Delete one or more AWS CDK stacks from your AWS environment.

When you delete a stack, resources in the stack will be destroyed, unless they were configured with a `DeletionPolicy` of `Retain`.

During stack deletion, this command will output progress information similar to `cdk deploy` behavior.

## Usage
<a name="ref-cli-cmd-destroy-usage"></a>

```
$ cdk destroy <arguments> <options>
```

## Arguments
<a name="ref-cli-cmd-destroy-args"></a><a name="ref-cli-cmd-destroy-args-stack-name"></a>

 **CDK stack ID**
The construct ID of the CDK stack from your app to delete.
 *Type*: String
 *Required*: No

## Options
<a name="ref-cli-cmd-destroy-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-destroy-options-all"></a>

 `--all <BOOLEAN>`
Destroy all available stacks.
 *Default value*: `false` <a name="ref-cli-cmd-destroy-options-concurrency"></a>

 `--concurrency <NUMBER>`
Destroy multiple stacks in parallel while accounting for inter-stack dependencies. Use this option to speed up destroy operations. You must still factor in AWS CloudFormation and other AWS account rate limiting.
Provide a number to specify the maximum number of simultaneous destroy operations (dependency permitting) to perform.
 *Default value*: `1` <a name="ref-cli-cmd-destroy-options-exclusively"></a>

 `--exclusively, -e <BOOLEAN>`
Only destroy requested stacks and don’t include dependencies.<a name="ref-cli-cmd-destroy-options-express"></a>

 `--express <BOOLEAN>`
Destroy stacks using CloudFormation express mode. Express mode allows for faster deletions through CloudFormation by reporting stack operations as completed as soon as CloudFormation applies the resource configuration. However, CloudFormation reports success without waiting for resources to stabilize. Additionally, express mode does not perform rollback automatically and will leave stacks in a failed state if something goes wrong.
For more information, see [express mode](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-express-mode.html) in the * AWS CloudFormation User Guide*.
Express mode does not wait for stabilization before reporting success and does not perform automatic rollback upon failure. We do not recommend express mode for production stack teardown. Express mode is targeted towards iterative deployments you would perform while developing your application.
 *Default value*: `false` <a name="ref-cli-cmd-destroy-options-force"></a>

 `--force, -f <BOOLEAN>`
Do not ask for confirmation before destroying the stacks.<a name="ref-cli-cmd-destroy-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the `cdk destroy` command.

## Examples
<a name="ref-cli-cmd-destroy-examples"></a>

### Delete a stack named MyStackName
<a name="ref-cli-cmd-destroy-examples-1"></a>

```
$ cdk destroy --app='node bin/main.js' <MyStackName>
```

### Delete multiple stacks in parallel
<a name="ref-cli-cmd-destroy-examples-2"></a>

Use the `--concurrency` option with `--all` to delete all stacks in parallel:

```
$ cdk destroy --all --concurrency 5
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
