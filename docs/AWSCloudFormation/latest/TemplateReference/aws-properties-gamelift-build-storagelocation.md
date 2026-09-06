---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-build-storagelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Build StorageLocation
<a name="aws-properties-gamelift-build-storagelocation"></a>

The location in Amazon S3 where build or script files are stored for access by Amazon GameLift.

## Syntax
<a name="aws-properties-gamelift-build-storagelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-build-storagelocation-syntax.json"></a>

```
{
  "[Bucket](#cfn-gamelift-build-storagelocation-bucket)" : {{String}},
  "[Key](#cfn-gamelift-build-storagelocation-key)" : {{String}},
  "[ObjectVersion](#cfn-gamelift-build-storagelocation-objectversion)" : {{String}},
  "[RoleArn](#cfn-gamelift-build-storagelocation-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-build-storagelocation-syntax.yaml"></a>

```
  [Bucket](#cfn-gamelift-build-storagelocation-bucket): {{String}}
  [Key](#cfn-gamelift-build-storagelocation-key): {{String}}
  [ObjectVersion](#cfn-gamelift-build-storagelocation-objectversion): {{String}}
  [RoleArn](#cfn-gamelift-build-storagelocation-rolearn): {{String}}
```

## Properties
<a name="aws-properties-gamelift-build-storagelocation-properties"></a>

`Bucket`  <a name="cfn-gamelift-build-storagelocation-bucket"></a>
An Amazon S3 bucket identifier. The name of the S3 bucket.
Amazon GameLift doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Key`  <a name="cfn-gamelift-build-storagelocation-key"></a>
The name of the zip file that contains the build files or script files.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ObjectVersion`  <a name="cfn-gamelift-build-storagelocation-objectversion"></a>
A version of a stored file to retrieve, if the object versioning feature is turned on for the S3 bucket. Use this parameter to specify a specific version. If this parameter isn't set, Amazon GameLift Servers retrieves the latest version of the file.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-gamelift-build-storagelocation-rolearn"></a>
The ARNfor an IAM role that allows Amazon GameLift to access the S3 bucket.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-gamelift-build-storagelocation--seealso"></a>
+ [ Create GameLift resources using Amazon CloudFront](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Developer Guide*
+ [ Create a build with files in Amazon S3](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build) in the *Amazon GameLift Developer Guide*
+ [ Upload script files in Amazon S3](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-script-uploading.html#realtime-script-uploading-s3) in the *Amazon GameLift Developer Guide*
+ [S3Location](https://docs.aws.amazon.com/gamelift/latest/apireference/API_S3Location.html) in the *Amazon GameLift API Reference*
