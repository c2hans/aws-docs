---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-script.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Script
<a name="aws-resource-gamelift-script"></a>

The `AWS::GameLift::Script` resource creates a new script record for your Realtime Servers script. Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Realtime Servers fleet to host your game sessions. Script logic is executed during an active game session.

## Syntax
<a name="aws-resource-gamelift-script-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-gamelift-script-syntax.json"></a>

```
{
  "Type" : "AWS::GameLift::Script",
  "Properties" : {
      "[Name](#cfn-gamelift-script-name)" : {{String}},
      "[NodeJsVersion](#cfn-gamelift-script-nodejsversion)" : {{String}},
      "[StorageLocation](#cfn-gamelift-script-storagelocation)" : {{S3Location}},
      "[Tags](#cfn-gamelift-script-tags)" : {{[ Tag, ... ]}},
      "[Version](#cfn-gamelift-script-version)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-gamelift-script-syntax.yaml"></a>

```
Type: AWS::GameLift::Script
Properties:
  [Name](#cfn-gamelift-script-name): {{String}}
  [NodeJsVersion](#cfn-gamelift-script-nodejsversion): {{String}}
  [StorageLocation](#cfn-gamelift-script-storagelocation): {{
    S3Location}}
  [Tags](#cfn-gamelift-script-tags): {{
    - Tag}}
  [Version](#cfn-gamelift-script-version): {{String}}
```

## Properties
<a name="aws-resource-gamelift-script-properties"></a>

`Name`  <a name="cfn-gamelift-script-name"></a>
A descriptive label that is associated with a script. Script names do not need to be unique.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeJsVersion`  <a name="cfn-gamelift-script-nodejsversion"></a>
The Node.js version used for execution of your Realtime script. The valid values are `10.x | 24.x`. By default, `NodeJsVersion` is `10.x`. This value cannot be updated later.
Node.js 10 will reach end of support on September 30, 2026. See more details in the [Node.js 10 FAQs](https://aws.amazon.com/gamelift/faq/nodejs10/). For migration guidance, see [ Migrating from Node.js 10 to 24](https://docs.aws.amazon.com/gamelift/latest/realtimeguide/realtime-script.html#realtime-script-nodejs-migration).
*Required*: No
*Type*: String
*Pattern*: `^\d+\.[x0-9]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageLocation`  <a name="cfn-gamelift-script-storagelocation"></a>
The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the `ObjectVersion` parameter to specify an earlier version.
*Required*: Yes
*Type*: [S3Location](aws-properties-gamelift-script-s3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-gamelift-script-tags"></a>
A list of labels to assign to the new script resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*. Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
*Required*: No
*Type*: Array of [Tag](aws-properties-gamelift-script-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-gamelift-script-version"></a>
The version that is associated with a build or script. Version strings do not need to be unique.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-gamelift-script-return-values"></a>

### Ref
<a name="aws-resource-gamelift-script-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `ScriptId`, such as `script-1111aaaa-22bb-33cc-44dd-5555eeee66ff`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-gamelift-script-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-gamelift-script-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The unique Amazon Resource Name (ARN) for the script.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).

`Id`  <a name="Id-fn::getatt"></a>
A unique identifier for a Realtime script.

`SizeOnDisk`  <a name="SizeOnDisk-fn::getatt"></a>
The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at "0".

## Examples
<a name="aws-resource-gamelift-script--examples"></a>

### Create a Realtime Servers Script
<a name="aws-resource-gamelift-script--examples--Create_a_Realtime_Servers_Script"></a>

The following example creates a GameLift script named `MyRealtimeScript`. The zipped script files are located in an S3 bucket, specified by the `S3Bucket` and `S3Key` input parameters. The example also creates the AWS Identity and Access Management role that GameLift assumes so that it has permissions to download the script files.

#### JSON
<a name="aws-resource-gamelift-script--examples--Create_a_Realtime_Servers_Script--json"></a>

```
{
    "Resources": {
        "IAMRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "cloudformation.amazonaws.com",
                                    "gamelift.amazonaws.com"
                                ]
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                },
                "RoleName": "ScriptIAMRole",
                "Policies": [
                    {
                        "PolicyName": "ScriptResourceIAMPolicy",
                        "PolicyDocument": {
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "s3:GetObject",
                                        "s3:GetObjectVersion",
                                        "s3:GetObjectMetadata",
                                        "s3:*Object*"
                                    ],
                                    "Resource": [
                                        "*"
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "ScriptResource": {
            "Type": "AWS::GameLift::Script",
            "Properties": {
                "Name": "MyRealtimeScript",
                "Version": "v1.0",
                "NodeJsVersion": "24.x",
                "StorageLocation": {
                    "Bucket": "amzn-s3-demo-bucket",
                    "Key": "MyScriptFiles.zip",
                    "RoleArn": {
                        "Fn::GetAtt": [
                            "IAMRole",
                            "Arn"
                        ]
                    }
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-gamelift-script--examples--Create_a_Realtime_Servers_Script--yaml"></a>

```
Resources:
  IAMRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service: ["cloudformation.amazonaws.com", "gamelift.amazonaws.com"]
            Action: "sts:AssumeRole"
      RoleName: "ScriptIAMRole"
      Policies:
        - PolicyName: ScriptResourceIAMPolicy
          PolicyDocument:
            Version: '2012-10-17		 	 	 '
            Statement:
              - Effect: Allow
                Action:
                  - "s3:GetObject"
                  - "s3:GetObjectVersion"
                  - "s3:GetObjectMetadata"
                  - "s3:*Object*"
                Resource:
                  - "*"
  ScriptResource:
    Type: AWS::GameLift::Script
    Properties:
      Name: MyRealtimeScript
      Version: v1.0
      NodeJsVersion: 24.x
      StorageLocation:
        Bucket: "amzn-s3-demo-bucket"
        Key: "MyScriptFiles.zip"
        RoleArn: !GetAtt IAMRole.Arn
```

## See also
<a name="aws-resource-gamelift-script--seealso"></a>
+ [ Create GameLift resources using Amazon CloudFront](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Developer Guide*
+ [ Upload script files in Amazon S3](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-script-uploading.html#realtime-script-uploading-s3) in the *Amazon GameLift Developer Guide*
+ [CreateScript](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateScript.html) in the *Amazon GameLift API Reference*
