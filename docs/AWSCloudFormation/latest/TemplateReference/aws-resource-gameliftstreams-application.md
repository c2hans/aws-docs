---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gameliftstreams-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLiftStreams::Application
<a name="aws-resource-gameliftstreams-application"></a>

 The `AWS::GameLiftStreams::Application` resource defines an Amazon GameLift Streams application. An application specifies the content that you want to stream, such as a game or other software, and its runtime environment (Microsoft Windows, Ubuntu, or Proton).

 Before you create an Amazon GameLift Streams application, upload your *uncompressed* game files (do not upload a .zip file) to an Amazon Simple Storage Service (Amazon S3) standard bucket.

## Syntax
<a name="aws-resource-gameliftstreams-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-gameliftstreams-application-syntax.json"></a>

```
{
  "Type" : "AWS::GameLiftStreams::Application",
  "Properties" : {
      "[ApplicationLogOutputUri](#cfn-gameliftstreams-application-applicationlogoutputuri)" : {{String}},
      "[ApplicationLogPaths](#cfn-gameliftstreams-application-applicationlogpaths)" : {{[ String, ... ]}},
      "[ApplicationSourceUri](#cfn-gameliftstreams-application-applicationsourceuri)" : {{String}},
      "[Description](#cfn-gameliftstreams-application-description)" : {{String}},
      "[ExecutablePath](#cfn-gameliftstreams-application-executablepath)" : {{String}},
      "[RuntimeEnvironment](#cfn-gameliftstreams-application-runtimeenvironment)" : {{RuntimeEnvironment}},
      "[Tags](#cfn-gameliftstreams-application-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-gameliftstreams-application-syntax.yaml"></a>

```
Type: AWS::GameLiftStreams::Application
Properties:
  [ApplicationLogOutputUri](#cfn-gameliftstreams-application-applicationlogoutputuri): {{String}}
  [ApplicationLogPaths](#cfn-gameliftstreams-application-applicationlogpaths): {{
    - String}}
  [ApplicationSourceUri](#cfn-gameliftstreams-application-applicationsourceuri): {{String}}
  [Description](#cfn-gameliftstreams-application-description): {{String}}
  [ExecutablePath](#cfn-gameliftstreams-application-executablepath): {{String}}
  [RuntimeEnvironment](#cfn-gameliftstreams-application-runtimeenvironment): {{
    RuntimeEnvironment}}
  [Tags](#cfn-gameliftstreams-application-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-gameliftstreams-application-properties"></a>

`ApplicationLogOutputUri`  <a name="cfn-gameliftstreams-application-applicationlogoutputuri"></a>
An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more `ApplicationLogPaths`.
*Required*: No
*Type*: String
*Pattern*: `^$|^s3://([a-zA-Z0-9][a-zA-Z0-9._-]{1,61}[a-zA-Z0-9])(/[a-zA-Z0-9._-]+)*/?$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationLogPaths`  <a name="cfn-gameliftstreams-application-applicationlogpaths"></a>
Locations of log files that your content generates during a stream session. Enter path values that are relative to the `ApplicationSourceUri` location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.
Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: `.txt`, `.log`, and `.utrace`. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.
The following path variables are recognized when they appear as the first component of a path: `%USERPROFILE%` (Windows and Proton), `$HOME` or `~` (Linux). Use a path variable when your application writes logs outside of the application directory.
Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in `ApplicationLogOutputUri` at the end of a stream session. To retrieve stored log files, call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) and get the `LogFileLocationUri`.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 0`
*Maximum*: `1024 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationSourceUri`  <a name="cfn-gameliftstreams-application-applicationsourceuri"></a>
The location of the content that you want to stream. Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location.
This value is immutable. To designate a different content location, create a new application.
The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same AWS Region.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-gameliftstreams-application-description"></a>
A human-readable label for the application. You can update this value later.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*$`
*Minimum*: `1`
*Maximum*: `80`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutablePath`  <a name="cfn-gameliftstreams-application-executablepath"></a>
The relative path and file name of the executable file that Amazon GameLift Streams will stream. Specify a path relative to the location set in `ApplicationSourceUri`. The file must be contained within the application's root folder. For Windows applications, the file must be a valid Windows executable or batch file with a filename ending in .exe, .cmd, or .bat. For Linux applications, the file must be a valid Linux binary executable or a script that contains an initial interpreter line starting with a shebang ('`#!`').
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuntimeEnvironment`  <a name="cfn-gameliftstreams-application-runtimeenvironment"></a>
 A set of configuration settings to run the application on a stream group. This configures the operating system, and can include compatibility layers and other drivers.
*Required*: Yes
*Type*: [RuntimeEnvironment](aws-properties-gameliftstreams-application-runtimeenvironment.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-gameliftstreams-application-tags"></a>
A list of labels to assign to the new application resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management and cost allocation. See [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-gameliftstreams-application-return-values"></a>

### Ref
<a name="aws-resource-gameliftstreams-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource across all AWS Regions. For example:

 `arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-gameliftstreams-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-gameliftstreams-application-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource across all AWS Regions. For example:
`arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6`.

`Id`  <a name="Id-fn::getatt"></a>
An ID that uniquely identifies the application resource. For example: `a-9ZY8X7Wv6`.

## See also
<a name="aws-resource-gameliftstreams-application--seealso"></a>
+ [Prepare an application in Amazon GameLift Streams](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html) in the *Amazon GameLift Streams Developer Guide*
+ [CreateApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateApplication.html) in the *Amazon GameLift Streams API Reference*
