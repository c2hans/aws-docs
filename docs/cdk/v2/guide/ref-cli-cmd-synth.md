---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-synth.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk synthesize`
<a name="ref-cli-cmd-synth"></a>

Synthesize a CDK app to produce a cloud assembly, including an AWS CloudFormation template for each stack.

Cloud assemblies are files that include everything needed to deploy your app to your AWS environment. For example, it includes a CloudFormation template for each stack in your app, and a copy of the file assets or Docker images that you reference in your app.

If your app contains a single stack or if a single stack is provided as an argument, the CloudFormation template will also be displayed in the standard output (`stdout`) in YAML format.

If your app contains multiple stacks, `cdk synth` will synthesize the cloud assembly to `cdk.out`.

## Usage
<a name="ref-cli-cmd-synth-usage"></a>

```
cdk synthesize <arguments> <options>
```

## Arguments
<a name="ref-cli-cmd-synth-args"></a><a name="ref-cli-cmd-synth-args-stack-name"></a>

 **CDK stack ID**
The construct ID of the CDK stack from your app to synthesize.
 *Type*: String
 *Required*: No

## Options
<a name="ref-cli-cmd-synth-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-synth-options-exclusively"></a>

 `--exclusively, -e <BOOLEAN>`
Only synthesize requested stacks, don’t include dependencies.<a name="ref-cli-cmd-synth-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the `cdk synthesize` command.<a name="ref-cli-cmd-synth-options-quiet"></a>

 `--quiet, -q <BOOLEAN>`
Do not output the CloudFormation template to `stdout`.
This option can be configured in the CDK project’s `cdk.json` file. The following is an example:

```
{
   "quiet": true
}
```
 *Default value*: `false` <a name="ref-cli-cmd-synth-options-validation"></a>

 `--validation <BOOLEAN>`
Validate the generated CloudFormation templates after synthesis by performing additional checks.
You can also configure this option through the `validateOnSynth` attribute or `CDK_VALIDATION` environment variable.
 *Default value*: `true`

## Examples
<a name="ref-cli-cmd-synth-examples"></a>

### Synthesize the cloud assembly for a CDK stack with logical ID MyStackName and output the CloudFormation template to stdout
<a name="ref-cli-cmd-synth-examples-1"></a>

```
$ cdk synth MyStackName
```

### Synthesize the cloud assembly for all stacks in a CDK app and save them into cdk.out
<a name="ref-cli-cmd-synth-examples-2"></a>

```
$ cdk synth
```

### Synthesize the cloud assembly for MyStackName, but don’t include dependencies
<a name="ref-cli-cmd-synth-examples-3"></a>

```
$ cdk synth MyStackName --exclusively
```

### Synthesize the cloud assembly for MyStackName, but don’t output the CloudFormation template to stdout
<a name="ref-cli-cmd-synth-examples-4"></a>

```
$ cdk synth MyStackName --quiet
```
