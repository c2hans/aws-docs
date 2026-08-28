---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-canary-code.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary Code
<a name="aws-properties-synthetics-canary-code"></a>

Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of `Script`.

## Syntax
<a name="aws-properties-synthetics-canary-code-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-canary-code-syntax.json"></a>

```
{
  "[BlueprintTypes](#cfn-synthetics-canary-code-blueprinttypes)" : {{[ String, ... ]}},
  "[Dependencies](#cfn-synthetics-canary-code-dependencies)" : {{[ Dependency, ... ]}},
  "[Handler](#cfn-synthetics-canary-code-handler)" : {{String}},
  "[S3Bucket](#cfn-synthetics-canary-code-s3bucket)" : {{String}},
  "[S3Key](#cfn-synthetics-canary-code-s3key)" : {{String}},
  "[S3ObjectVersion](#cfn-synthetics-canary-code-s3objectversion)" : {{String}},
  "[Script](#cfn-synthetics-canary-code-script)" : {{String}},
  "[SourceLocationArn](#cfn-synthetics-canary-code-sourcelocationarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-synthetics-canary-code-syntax.yaml"></a>

```
  [BlueprintTypes](#cfn-synthetics-canary-code-blueprinttypes): {{
    - String}}
  [Dependencies](#cfn-synthetics-canary-code-dependencies): {{
    - Dependency}}
  [Handler](#cfn-synthetics-canary-code-handler): {{String}}
  [S3Bucket](#cfn-synthetics-canary-code-s3bucket): {{String}}
  [S3Key](#cfn-synthetics-canary-code-s3key): {{String}}
  [S3ObjectVersion](#cfn-synthetics-canary-code-s3objectversion): {{String}}
  [Script](#cfn-synthetics-canary-code-script): {{String}}
  [SourceLocationArn](#cfn-synthetics-canary-code-sourcelocationarn): {{String}}
```

## Properties
<a name="aws-properties-synthetics-canary-code-properties"></a>

`BlueprintTypes`  <a name="cfn-synthetics-canary-code-blueprinttypes"></a>
`BlueprintTypes` are a list of templates that enable simplified canary creation. You can create canaries for common monitoring scenarios by providing only a JSON configuration file instead of writing custom scripts. `multi-checks` is the only supported value.
When you specify `BlueprintTypes`, the `Handler` field cannot be specified since the blueprint provides a pre-defined entry point.
*Required*: No
*Type*: Array of String
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dependencies`  <a name="cfn-synthetics-canary-code-dependencies"></a>
Property description not available.
*Required*: No
*Type*: Array of [Dependency](aws-properties-synthetics-canary-dependency.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Handler`  <a name="cfn-synthetics-canary-code-handler"></a>
The entry point to use for the source code when running the canary. For canaries that use the `syn-python-selenium-1.0` runtime or a `syn-nodejs.puppeteer` runtime earlier than `syn-nodejs.puppeteer-3.4`, the handler must be specified as `fileName.handler`. For `syn-python-selenium-1.1`, `syn-nodejs.puppeteer-3.4`, and later runtimes, the handler can be specified as `fileName.functionName`, or you can specify a folder where canary scripts reside as `folder/fileName.functionName`.
This field is required when you don't specify `BlueprintTypes` and is not allowed when you specify `BlueprintTypes`.
*Required*: Conditional
*Type*: String
*Pattern*: `^(([0-9a-zA-Z_-]+(\/|\.))*[0-9A-Za-z_\\-]+(\.|::)[A-Za-z_][A-Za-z0-9_]*)?$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Bucket`  <a name="cfn-synthetics-canary-code-s3bucket"></a>
If your canary script is located in S3, specify the bucket name here. The bucket must already exist.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Key`  <a name="cfn-synthetics-canary-code-s3key"></a>
The Amazon S3 key of your script. For more information, see [Working with Amazon S3 Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html).
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3ObjectVersion`  <a name="cfn-synthetics-canary-code-s3objectversion"></a>
The Amazon S3 version ID of your script.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Script`  <a name="cfn-synthetics-canary-code-script"></a>
If you input your canary script directly into the canary instead of referring to an S3 location, the value of this parameter is the script in plain text. It can be up to 5 MB.
*Required*: Conditional
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceLocationArn`  <a name="cfn-synthetics-canary-code-sourcelocationarn"></a>
The ARN of the Lambda layer where Synthetics stores the canary script code.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
