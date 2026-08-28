---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-build.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Build
<a name="aws-resource-gamelift-build"></a>

The `AWS::GameLift::Build` resource creates a game server build that is installed and run on instances in an Amazon GameLift fleet. This resource points to an Amazon S3 location that contains a zip file with all of the components of the game server build.

## Syntax
<a name="aws-resource-gamelift-build-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-gamelift-build-syntax.json"></a>

```
{
  "Type" : "AWS::GameLift::Build",
  "Properties" : {
      "[Name](#cfn-gamelift-build-name)" : {{String}},
      "[OperatingSystem](#cfn-gamelift-build-operatingsystem)" : {{String}},
      "[ServerSdkVersion](#cfn-gamelift-build-serversdkversion)" : {{String}},
      "[StorageLocation](#cfn-gamelift-build-storagelocation)" : {{StorageLocation}},
      "[Tags](#cfn-gamelift-build-tags)" : {{[ Tag, ... ]}},
      "[Version](#cfn-gamelift-build-version)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-gamelift-build-syntax.yaml"></a>

```
Type: AWS::GameLift::Build
Properties:
  [Name](#cfn-gamelift-build-name): {{String}}
  [OperatingSystem](#cfn-gamelift-build-operatingsystem): {{String}}
  [ServerSdkVersion](#cfn-gamelift-build-serversdkversion): {{String}}
  [StorageLocation](#cfn-gamelift-build-storagelocation): {{
    StorageLocation}}
  [Tags](#cfn-gamelift-build-tags): {{
    - Tag}}
  [Version](#cfn-gamelift-build-version): {{String}}
```

## Properties
<a name="aws-resource-gamelift-build-properties"></a>

`Name`  <a name="cfn-gamelift-build-name"></a>
A descriptive label that is associated with a build. Build names do not need to be unique.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperatingSystem`  <a name="cfn-gamelift-build-operatingsystem"></a>
The operating system that your game server binaries run on. This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later.
Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/). For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
*Required*: No
*Type*: String
*Allowed values*: `AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2023 | WINDOWS_2012 | WINDOWS_2016 | WINDOWS_2022`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerSdkVersion`  <a name="cfn-gamelift-build-serversdkversion"></a>
A server SDK version you used when integrating your game server build with Amazon GameLift Servers. For more information see [Integrate games with custom game servers](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html). By default Amazon GameLift Servers sets this value to `4.0.2`.
*Required*: No
*Type*: String
*Pattern*: `^\d+\.\d+\.\d+$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageLocation`  <a name="cfn-gamelift-build-storagelocation"></a>
Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift Servers to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.
If a `StorageLocation` is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift Servers will report a `SizeOnDisk` of 0.
*Required*: No
*Type*: [StorageLocation](aws-properties-gamelift-build-storagelocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-gamelift-build-tags"></a>
A list of labels to assign to the new build resource. Tags are developer defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*. Once the resource is created, you can use [TagResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListTagsForResource.html) to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
*Required*: No
*Type*: Array of [Tag](aws-properties-gamelift-build-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-gamelift-build-version"></a>
Version information that is associated with this build. Version strings do not need to be unique.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-gamelift-build-return-values"></a>

### Ref
<a name="aws-resource-gamelift-build-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the build ID, such as `build-1111aaaa-22bb-33cc-44dd-5555eeee66ff`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-gamelift-build-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-gamelift-build-return-values-fn--getatt-fn--getatt"></a>

`BuildArn`  <a name="BuildArn-fn::getatt"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers build resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::build/build-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`. In a GameLift build ARN, the resource ID matches the *BuildId* value.

`BuildId`  <a name="BuildId-fn::getatt"></a>
A unique identifier for the build.

## Examples
<a name="aws-resource-gamelift-build--examples"></a>

### Create a Custom Game Server Build
<a name="aws-resource-gamelift-build--examples--Create_a_Custom_Game_Server_Build"></a>

The following example creates a GameLift build named `MyGameServerBuild`. The build package is located in an S3 bucket, specified by the `S3Bucket` and `S3Key` input parameters. The example also creates the AWS Identity and Access Management role that GameLift assumes so that it has permissions to download the build package files.

#### JSON
<a name="aws-resource-gamelift-build--examples--Create_a_Custom_Game_Server_Build--json"></a>

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
                "RoleName": "BuildIAMRole",
                "Policies": [
                    {
                        "PolicyName": "gamelift-s3-access-policy",
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
                                        "arn:aws:s3:::amzn-s3-demo-bucket/*"
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "BuildResource": {
            "Type": "AWS::GameLift::Build",
            "Properties": {
                "Name": "MyGameServerBuild",
                "Version": "v1.0",
                "OperatingSystem": "WINDOWS_2012",
                "ServerSdkVersion: "5.0.0",
                "StorageLocation": {
                    "Bucket": "amzn-s3-demo-bucket",
                    "Key": "MyGameBuildFiles.zip",
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
<a name="aws-resource-gamelift-build--examples--Create_a_Custom_Game_Server_Build--yaml"></a>

```
Resources:
  IAMRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service: ["cloudformation.amazonaws.com", "gamelift.amazonaws.com"]
            Action: "sts:AssumeRole"
      RoleName: "BuildIAMRole"
      Policies:
        - PolicyName: gamelift-s3-access-policy
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
                  - "arn:aws:s3:::amzn-s3-demo-bucket/*"
  BuildResource:
    Type: AWS::GameLift::Build
    Properties:
      Name: MyGameServerBuild
      Version: v1.0
      OperatingSystem: WINDOWS_2012
      ServerSdkVersion: 5.0.0
      StorageLocation:
        Bucket: "amzn-s3-demo-bucket"
        Key: "MyGameBuildFiles.zip"
        RoleArn: !GetAtt IAMRole.Arn
```

## See also
<a name="aws-resource-gamelift-build--seealso"></a>
+ [ Create GameLift resources using Amazon CloudFront](https://docs.aws.amazon.com/gamelift/latest/developerguide/resources-cloudformation.html) in the *Amazon GameLift Developer Guide*
+ [ Create a build with files in Amazon S3](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build) in the *Amazon GameLift Developer Guide*
+ [ Upload script files in Amazon S3](https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-script-uploading.html#realtime-script-uploading-s3) in the *Amazon GameLift Developer Guide*
+ [CreateBuild](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateBuild.html) in the *Amazon GameLift API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
