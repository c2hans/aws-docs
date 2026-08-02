---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# AWS CDK CLI command reference
<a name="ref-cli-cmd"></a>

This section contains command reference information for the AWS Cloud Development Kit (AWS CDK) Command Line Interface (CLI). The CDK CLI is also referred to as the CDK Toolkit.

## Usage
<a name="ref-cli-cmd-usage"></a>

```
$ cdk <command> <arguments> <options>
```

## Commands
<a name="ref-cli-cmd-commands"></a><a name="ref-cli-cmd-commands-acknowledge"></a>

 ` acknowledge ack `
Acknowledge a notice by issue number and hide it from displaying again.<a name="ref-cli-cmd-commands-bootstrap"></a>

 ` bootstrap `
Prepare an AWS environment for CDK deployments by deploying the CDK bootstrap stack, named `CDKToolkit`, into the AWS environment.<a name="ref-cli-cmd-commands-context"></a>

 ` context `
Manage cached context values for your CDK application.<a name="ref-cli-cmd-commands-deploy"></a>

 ` deploy `
Deploy one or more CDK stacks into your AWS environment.<a name="ref-cli-cmd-commands-destroy"></a>

 ` destroy `
Delete one or more CDK stacks from your AWS environment.<a name="ref-cli-cmd-commands-diff"></a>

 ` diff `
Perform a diff to see infrastructure changes between CDK stacks.<a name="ref-cli-cmd-commands-docs"></a>

 ` docs doc `
Open CDK documentation in your browser.<a name="ref-cli-cmd-commands-doctor"></a>

 ` doctor `
Inspect and display useful information about your local CDK project and development environment.<a name="ref-cli-cmd-commands-drift"></a>

 ` drift `
Detect configuration drift for resources that you define, manage, and deploy using CDK.<a name="ref-cli-cmd-commands-flags"></a>

 ` flags `
View and modify your feature flag configurations for the CDK CLI.<a name="ref-cli-cmd-commands-import"></a>

 ` import `
Use AWS CloudFormation resource imports to import existing AWS resources into a CDK stack.<a name="ref-cli-cmd-commands-init"></a>

 ` init `
Create a new CDK project from a template.<a name="ref-cli-cmd-commands-list"></a>

 ` list, ls `
List all CDK stacks and their dependencies from a CDK app.<a name="ref-cli-cmd-commands-metadata"></a>

 ` metadata `
Display metadata associated with a CDK stack.<a name="ref-cli-cmd-commands-migrate"></a>

 ` migrate `
Migrate AWS resources, AWS CloudFormation stacks, and AWS CloudFormation templates into a new CDK project.<a name="ref-cli-cmd-commands-notices"></a>

 ` notices `
Display notices for your CDK application.<a name="ref-cli-cmd-commands-orphan"></a>

 ` orphan `
Safely detach resources from a CloudFormation stack without deleting them.<a name="ref-cli-cmd-commands-publish-assets"></a>

 ` publish-assets `
Publish assets for the specified CDK stack to their respective destinations without performing a deployment.<a name="ref-cli-cmd-commands-refactor"></a>

 ` refactor `
Preserve deployed resources when refactoring code in your CDK application.<a name="ref-cli-cmd-commands-synthesize"></a>

 ` synthesize, synth `
Synthesize a CDK app to produce a cloud assembly, including an AWS CloudFormation template for each stack.<a name="ref-cli-cmd-commands-watch"></a>

 ` watch `
Continuously watch a local CDK project for changes to perform deployments and hotswaps.

## Global options
<a name="ref-cli-cmd-options"></a>

The following options are compatible with all CDK CLI commands.<a name="ref-cli-cmd-options-app"></a>

 `--app, -a <STRING>`
Provide the command for running your app or cloud assembly directory.
 *Required*: Yes<a name="ref-cli-cmd-options-asset-metadata"></a>

 `--asset-metadata <BOOLEAN>`
Include `aws:asset:*` AWS CloudFormation metadata for resources that use assets.
 *Required*: No
 *Default value*: `true` <a name="ref-cli-cmd-options-build"></a>

 `--build <STRING>`
Command for running a pre-synthesis build.
 *Required*: No<a name="ref-cli-cmd-options-ca-bundle-path"></a>

 `--ca-bundle-path <STRING>`
Path to a CA certificate to use when validating HTTPS requests.
If this option is not provided, the CDK CLI will read from the `AWS_CA_BUNDLE` environment variable.
 *Required*: Yes<a name="ref-cli-cmd-options-ci"></a>

 `--ci <BOOLEAN>`
Indicate that CDK CLI commands are being run in a continuous integration (CI) environment.
This option modifies the behavior of the CDK CLI to better suit automated operations that are typical in CI pipelines.
When you provide this option, logs are sent to `stdout` instead of `stderr`.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-context"></a>

 `--context, -c <ARRAY>`
Add contextual string parameters as key-value pairs.<a name="ref-cli-cmd-options-debug"></a>

 `--debug <BOOLEAN>`
Enable detailed debugging information. This option produces a verbose output that includes a lot more detail about what the CDK CLI is doing behind the scenes.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-ec2creds"></a>

 `--ec2creds, -i <BOOLEAN>`
Force the CDK CLI to try and fetch Amazon EC2 instance credentials.
By default, the CDK CLI guesses the Amazon EC2 instance status.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the CDK CLI.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-ignore-errors"></a>

 `--ignore-errors <BOOLEAN>`
Ignore synthesis errors, which will likely produce an output that is not valid.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-json"></a>

 `--json, -j <BOOLEAN>`
Use JSON instead of YAML for AWS CloudFormation templates that are printed to standard output (`stdout`).
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-lookups"></a>

 `--lookups <BOOLEAN>`
Perform context lookups.
Synthesis will fail if this value is `false` and context lookups need to be performed.
 *Required*: No
 *Default value*: `true` <a name="ref-cli-cmd-options-no-color"></a>

 `--no-color <BOOLEAN>`
Remove color and other styling from the console output.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-notices"></a>

 `--notices <BOOLEAN>`
Show relevant notices.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-output"></a>

 `--output, -o <STRING>`
Specify the directory to output the synthesized cloud assembly to.
 *Required*: Yes
 *Default value*: `cdk.out` <a name="ref-cli-cmd-options-path-metadata"></a>

 `--path-metadata <BOOLEAN>`
Include `aws::cdk::path` AWS CloudFormation metadata for each resource.
 *Required*: No
 *Default value*: `true` <a name="ref-cli-cmd-options-plugin"></a>

 `--plugin, -p <ARRAY>`
Name or path of a node package that extends CDK features. This option can be provided multiple times in a single command.
You can configure this option in the project’s `cdk.json` file or at `~/.cdk.json` on your local development machine:

```
{
   // ...
   "plugin": [
      "module_1",
      "module_2"
   ],
   // ...
}
```
 *Required*: No<a name="ref-cli-cmd-options-profile"></a>

 `--profile <STRING>`
Specify the name of the AWS profile, containing your AWS environment information, to use with the CDK CLI.
 *Required*: Yes<a name="ref-cli-cmd-options-proxy"></a>

 `--proxy <STRING>`
Use the indicated proxy.
If this option is not provided, the CDK CLI will read from the `HTTPS_PROXY` environment variable.
 *Required*: Yes
 *Default value*: Read from `HTTPS_PROXY` environment variable.<a name="ref-cli-cmd-options-role-arn"></a>

 `--role-arn, -r <STRING>`
The ARN of the IAM role that the CDK CLI will assume when interacting with AWS CloudFormation.
 *Required*: No<a name="ref-cli-cmd-options-staging"></a>

 `--staging <BOOLEAN>`
Copy assets to the output directory.
Specify `false` to prevent the copying of assets to the output directory. This allows the AWS SAM CLI to reference the original source files when performing local debugging.
 *Required*: No
 *Default value*: `true` <a name="ref-cli-cmd-options-strict"></a>

 `--strict <BOOLEAN>`
Do not construct stacks that contain warnings.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-trace"></a>

 `--trace <BOOLEAN>`
Print trace for stack warnings.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-verbose"></a>

 `--verbose, -v <COUNT>`
Show debug logs. You can specify this option multiple times to increase verbosity.
 *Required*: No<a name="ref-cli-cmd-options-version"></a>

 `--version <BOOLEAN>`
Show the CDK CLI version number.
 *Required*: No
 *Default value*: `false` <a name="ref-cli-cmd-options-version-reporting"></a>

 `--version-reporting <BOOLEAN>`
Include the ` AWS::CDK::Metadata` resource in synthesized AWS CloudFormation templates.
 *Required*: No
 *Default value*: `true`

## Providing and configuring options
<a name="ref-cli-cmd-configure"></a>

You can pass options through command-line arguments. For most options, you can configure them in a `cdk.json` configuration file. When you use multiple configuration sources, the CDK CLI adheres to the following precedence:

1.  **Command-line values** – Any option provided at the command-line overrides options configured in `cdk.json` files.

1.  **Project configuration file** – The `cdk.json` file in your CDK project’s directory.

1.  **User configuration file** – The `cdk.json` file located at `~/.cdk.json` on your local machine.

## Passing options at the command line
<a name="ref-cli-cmd-pass"></a><a name="ref-cli-cmd-pass-bool"></a>

 **Passing boolean values**
For options that accept a boolean value, you can specify them in the following ways:
+ Use `true` and `false` values – Provide the boolean value with the command. The following is an example:

  ```
  $ cdk deploy --watch=true
  $ cdk deploy --watch=false
  ```
+ Provide the option’s counterpart – Modify the option name by adding `no` to specify a `false` value. The following is an example:

  ```
  $ cdk deploy --watch
  $ cdk deploy --no-watch
  ```
+ For options that default to `true` or `false`, you don’t have to provide the option unless you want to change from the default.
