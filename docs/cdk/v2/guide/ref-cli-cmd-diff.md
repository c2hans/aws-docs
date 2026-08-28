---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-diff.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk diff`
<a name="ref-cli-cmd-diff"></a>

Perform a diff to see infrastructure changes between AWS CDK stacks.

This command is typically used to compare differences between the current state of stacks in your local CDK app against deployed stacks. However, you can also compare a deployed stack with any local AWS CloudFormation template.

## Usage
<a name="ref-cli-cmd-diff-usage"></a>

```
$ cdk diff <arguments> <options>
```

## Arguments
<a name="ref-cli-cmd-diff-args"></a><a name="ref-cli-cmd-diff-args-stack-name"></a>

 **CDK stack ID**
The construct ID of the CDK stack from your app to perform a diff.
 *Type*: String
 *Required*: No

## Options
<a name="ref-cli-cmd-diff-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-diff-options-method"></a>

 `--method, -m <STRING>`
Specifies how to compute the diff.
+  `auto` – Default. Creates an AWS CloudFormation change set to display accurate replacement information. If the change set can’t be created (for example, due to missing permissions), falls back to a template-only diff. Uses the deploy role.
+  `change-set` – Always creates a change set and fails if it can’t be created. Use this when you need guaranteed accuracy. Uses the deploy role.
+  `template` – Compares CloudFormation templates directly. Faster, but less accurate. Any change detected to properties that require resource replacement is displayed as a resource replacement, even if the change is purely cosmetic. Uses the lookup role.

   *Default value*: `auto` <a name="ref-cli-cmd-diff-options-change-set"></a>

 `--change-set <BOOLEAN>` *(deprecated)*
Specifies whether to create a change set to analyze resource replacements. Use `--method` instead.
 `--change-set` maps to `--method=auto`. `--no-change-set` maps to `--method=template`.<a name="ref-cli-cmd-diff-options-context-lines"></a>

 `--context-lines <NUMBER>`
Number of context lines to include in arbitrary JSON diff rendering.
 *Default value*: `3` <a name="ref-cli-cmd-diff-options-exclusively"></a>

 `--exclusively, -e <BOOLEAN>`
Only diff requested stacks and don’t include dependencies.<a name="ref-cli-cmd-diff-options-fail"></a>

 `--fail <BOOLEAN>`
Fail and exit with a code of `1` if differences are detected.<a name="ref-cli-cmd-diff-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the `cdk diff` command.<a name="ref-cli-cmd-diff-options-processed"></a>

 `--processed <BOOLEAN>`
Specify whether to compare against the template with CloudFormation transforms already processed.
 *Default value*: `false` <a name="ref-cli-cmd-diff-options-quiet"></a>

 `--quiet, -q <BOOLEAN>`
Do not print the CDK stack name and default `cdk diff` message to `stdout` when no changes are detected.
 *Default value*: `false` <a name="ref-cli-cmd-diff-options-security-only"></a>

 `--security-only <BOOLEAN>`
Only diff for broadened security changes.
 *Default value*: `false` <a name="ref-cli-cmd-diff-options-strict"></a>

 `--strict <BOOLEAN>`
Modify `cdk diff` behavior to be more precise or stringent. When true, the CDK CLI will not filter out ` AWS::CDK::Metadata` resources or unreadable non-ASCII characters.
 *Default value*: `false` <a name="ref-cli-cmd-diff-options-template"></a>

 `--template <STRING>`
The path to the CloudFormation template to compare a CDK stack with. Implies `--method=template`.

## Examples
<a name="ref-cli-cmd-diff-examples"></a>

### Diff against the currently deployed stack named MyStackName
<a name="ref-cli-cmd-diff-examples-1"></a>

The CDK CLI uses the following symbols in the diff output:
+  `[+]` – Identifies code or resources that will be added if you deploy your changes.
+  `[-]` – Identifies code or resources that will be removed if you deploy your changes.
+  `[~]` – Identifies a resource or property that will be modified if you deploy your changes.

The following is an example that shows a diff of local changes to a Lambda function:

```
$ cdk diff MyStackName
start: Building <asset-hash>:<account:Region>
success: Built <asset-hash>:<account:Region>
start: Publishing <asset-hash>:<account:Region>
success: Published <asset-hash>:<account:Region>
Hold on while we create a read-only change set to get a diff with accurate replacement information (use --method=template to use a less accurate but faster template-only diff)
Stack MyStackName
Resources
[~] AWS::Lambda::Function HelloWorldFunction <resource-logical-ID>
 └─ [~] Code
     └─ [~] .ZipFile:
         ├─ [-]
        exports.handler = async function(event) {
          return {
            statusCode: 200,
            body: JSON.stringify('Hello World!'),
          };
        };

         └─ [+]
        exports.handler = async function(event) {
          return {
            statusCode: 200,
            body: JSON.stringify('Hello from CDK!'),
          };
        };

✨  Number of stacks with differences: 1
```

A `[~]` indicator for resources that will be modified does not always mean a full resource replacement:
+ Some resource properties, like `Code`, will update the resource.
+ Some resource properties, like `FunctionName`, may cause a full resource replacement.

### Diff against a specific CloudFormation template
<a name="ref-cli-cmd-diff-examples-2"></a>

```
$ cdk diff MyStackName --app='node bin/main.js' --template-path='./MyStackNameTemplate.yaml'
```

### Diff a local stack with its deployed stack. don’t print to stdout if no changes are detected
<a name="ref-cli-cmd-diff-examples-3"></a>

```
$ cdk diff MyStackName --app='node bin/main.js' --quiet
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
