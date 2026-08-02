---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-publish-assets.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# `cdk publish-assets`
<a name="ref-cli-cmd-publish-assets"></a>

**Important**
The `cdk publish-assets` command is in development for the AWS CDK. The current features of this command are subject to change. Therefore, you must opt in by providing the `--unstable=publish-assets` option to use this command.

Publish assets such as Docker images and file assets for the specified AWS Cloud Development Kit (AWS CDK) stack to their respective destinations, such as Amazon Elastic Container Registry (Amazon ECR) repositories and Amazon Simple Storage Service (Amazon S3) buckets, without performing a deployment.

This command is useful in CI/CD pipelines where you want to separate the asset publishing phase from the deployment phase. By publishing assets independently, you can validate that all assets are built and available before you start the deployment process.

## Usage
<a name="ref-cli-cmd-publish-assets-usage"></a>

```
$ cdk publish-assets <arguments> <options>
```

## Arguments
<a name="ref-cli-cmd-publish-assets-args"></a><a name="ref-cli-cmd-publish-assets-args-stack-name"></a>

 **CDK stack ID**
The construct ID of the CDK stack from your app to publish assets for.
 *Type*: String
 *Required*: No

## Options
<a name="ref-cli-cmd-publish-assets-options"></a>

For a list of global options that work with all CDK CLI commands, see [Global options](ref-cli-cmd.md#ref-cli-cmd-options).<a name="ref-cli-cmd-publish-assets-options-all"></a>

 `--all <BOOLEAN>`
Publish assets for all stacks in your CDK app.
 *Default value*: `false` <a name="ref-cli-cmd-publish-assets-options-concurrency"></a>

 `--concurrency <NUMBER>`
Specify the maximum number of simultaneous asset publishing operations to perform.
 *Default value*: `4` <a name="ref-cli-cmd-publish-assets-options-exclusively"></a>

 `--exclusively, -e <BOOLEAN>`
Only publish assets for requested stacks and don’t include dependencies.<a name="ref-cli-cmd-publish-assets-options-force"></a>

 `--force <BOOLEAN>`
Re-publish all assets, even if they already exist at the destination.
 *Default value*: `false` <a name="ref-cli-cmd-publish-assets-options-help"></a>

 `--help, -h <BOOLEAN>`
Show command reference information for the `cdk publish-assets` command.

## Examples
<a name="ref-cli-cmd-publish-assets-examples"></a>

### Publish assets for a specific stack
<a name="ref-cli-cmd-publish-assets-examples-1"></a>

```
$ cdk publish-assets MyStack --unstable=publish-assets
```

### Publish assets for all stacks
<a name="ref-cli-cmd-publish-assets-examples-2"></a>

```
$ cdk publish-assets --all --unstable=publish-assets
```

### Force re-publish assets that already exist
<a name="ref-cli-cmd-publish-assets-examples-3"></a>

```
$ cdk publish-assets MyStack --unstable=publish-assets --force
```

### Publish assets then deploy separately
<a name="ref-cli-cmd-publish-assets-examples-4"></a>

First, publish assets for your stack:

```
$ cdk publish-assets MyStack --unstable=publish-assets
```

Then, deploy the stack:

```
$ cdk deploy MyStack
```
