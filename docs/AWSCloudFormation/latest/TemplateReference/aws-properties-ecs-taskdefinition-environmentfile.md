---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-environmentfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition EnvironmentFile
<a name="aws-properties-ecs-taskdefinition-environmentfile"></a>

A list of files containing the environment variables to pass to a container. You can specify up to ten environment files. The file must have a `.env` file extension. Each line in an environment file should contain an environment variable in `VARIABLE=VALUE` format. Lines beginning with `#` are treated as comments and are ignored.

If there are environment variables specified using the `environment` parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, they're processed from the top down. We recommend that you use unique variable names. For more information, see [Use a file to pass environment variables to a container](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/use-environment-file.html) in the *Amazon Elastic Container Service Developer Guide*.

Environment variable files are objects in Amazon S3 and all Amazon S3 security considerations apply.

You must use the following platforms for the Fargate launch type:
+ Linux platform version `1.4.0` or later.
+ Windows platform version `1.0.0` or later.

Consider the following when using the Fargate launch type:
+ The file is handled like a native Docker env-file.
+ There is no support for shell escape handling.
+ The container entry point interperts the `VARIABLE` values.

## Syntax
<a name="aws-properties-ecs-taskdefinition-environmentfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-environmentfile-syntax.json"></a>

```
{
  "[Type](#cfn-ecs-taskdefinition-environmentfile-type)" : {{String}},
  "[Value](#cfn-ecs-taskdefinition-environmentfile-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-environmentfile-syntax.yaml"></a>

```
  [Type](#cfn-ecs-taskdefinition-environmentfile-type): {{String}}
  [Value](#cfn-ecs-taskdefinition-environmentfile-value): {{String}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-environmentfile-properties"></a>

`Type`  <a name="cfn-ecs-taskdefinition-environmentfile-type"></a>
The file type to use. Environment files are objects in Amazon S3. The only supported value is `s3`.
*Required*: No
*Type*: String
*Allowed values*: `s3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-ecs-taskdefinition-environmentfile-value"></a>
The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
