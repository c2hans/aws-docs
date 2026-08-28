---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-synthetics-canary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary
<a name="aws-resource-synthetics-canary"></a>

Creates or updates a canary. Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once.

Canaries are automated scripts that run at specified intervals against an endpoint. They include Python or Node.js code to create a Lambda function. This code needs to be packaged in a certain way, depending on the language. For more information, see [Writing a canary script](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary.html).

To create canaries, you must have the `CloudWatchSyntheticsFullAccess` policy. If you are creating a new IAM role for the canary, you also need the the `iam:CreateRole`, `iam:CreatePolicy` and `iam:AttachRolePolicy` permissions. For more information, see [Necessary Roles and Permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles).

Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see [Security Considerations for Synthetics Canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html).

## Syntax
<a name="aws-resource-synthetics-canary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-synthetics-canary-syntax.json"></a>

```
{
  "Type" : "AWS::Synthetics::Canary",
  "Properties" : {
      "[ArtifactConfig](#cfn-synthetics-canary-artifactconfig)" : {{ArtifactConfig}},
      "[ArtifactS3Location](#cfn-synthetics-canary-artifacts3location)" : {{String}},
      "[BrowserConfigs](#cfn-synthetics-canary-browserconfigs)" : {{[ BrowserConfig, ... ]}},
      "[Code](#cfn-synthetics-canary-code)" : {{Code}},
      "[DryRunAndUpdate](#cfn-synthetics-canary-dryrunandupdate)" : {{Boolean}},
      "[ExecutionRoleArn](#cfn-synthetics-canary-executionrolearn)" : {{String}},
      "[FailureRetentionPeriod](#cfn-synthetics-canary-failureretentionperiod)" : {{Integer}},
      "[KmsKeyArn](#cfn-synthetics-canary-kmskeyarn)" : {{String}},
      "[Name](#cfn-synthetics-canary-name)" : {{String}},
      "[ProvisionedResourceCleanup](#cfn-synthetics-canary-provisionedresourcecleanup)" : {{String}},
      "[Replicas](#cfn-synthetics-canary-replicas)" : {{[ Replica, ... ]}},
      "[ResourcesToReplicateTags](#cfn-synthetics-canary-resourcestoreplicatetags)" : {{[ String, ... ]}},
      "[RunConfig](#cfn-synthetics-canary-runconfig)" : {{RunConfig}},
      "[RuntimeVersion](#cfn-synthetics-canary-runtimeversion)" : {{String}},
      "[Schedule](#cfn-synthetics-canary-schedule)" : {{Schedule}},
      "[StartCanaryAfterCreation](#cfn-synthetics-canary-startcanaryaftercreation)" : {{Boolean}},
      "[SuccessRetentionPeriod](#cfn-synthetics-canary-successretentionperiod)" : {{Integer}},
      "[Tags](#cfn-synthetics-canary-tags)" : {{[ Tag, ... ]}},
      "[VisualReferences](#cfn-synthetics-canary-visualreferences)" : {{[ VisualReference, ... ]}},
      "[VPCConfig](#cfn-synthetics-canary-vpcconfig)" : {{VPCConfig}}
    }
}
```

### YAML
<a name="aws-resource-synthetics-canary-syntax.yaml"></a>

```
Type: AWS::Synthetics::Canary
Properties:
  [ArtifactConfig](#cfn-synthetics-canary-artifactconfig): {{
    ArtifactConfig}}
  [ArtifactS3Location](#cfn-synthetics-canary-artifacts3location): {{String}}
  [BrowserConfigs](#cfn-synthetics-canary-browserconfigs): {{
    - BrowserConfig}}
  [Code](#cfn-synthetics-canary-code): {{
    Code}}
  [DryRunAndUpdate](#cfn-synthetics-canary-dryrunandupdate): {{Boolean}}
  [ExecutionRoleArn](#cfn-synthetics-canary-executionrolearn): {{String}}
  [FailureRetentionPeriod](#cfn-synthetics-canary-failureretentionperiod): {{Integer}}
  [KmsKeyArn](#cfn-synthetics-canary-kmskeyarn): {{String}}
  [Name](#cfn-synthetics-canary-name): {{String}}
  [ProvisionedResourceCleanup](#cfn-synthetics-canary-provisionedresourcecleanup): {{String}}
  [Replicas](#cfn-synthetics-canary-replicas): {{
    - Replica}}
  [ResourcesToReplicateTags](#cfn-synthetics-canary-resourcestoreplicatetags): {{
    - String}}
  [RunConfig](#cfn-synthetics-canary-runconfig): {{
    RunConfig}}
  [RuntimeVersion](#cfn-synthetics-canary-runtimeversion): {{String}}
  [Schedule](#cfn-synthetics-canary-schedule): {{
    Schedule}}
  [StartCanaryAfterCreation](#cfn-synthetics-canary-startcanaryaftercreation): {{Boolean}}
  [SuccessRetentionPeriod](#cfn-synthetics-canary-successretentionperiod): {{Integer}}
  [Tags](#cfn-synthetics-canary-tags): {{
    - Tag}}
  [VisualReferences](#cfn-synthetics-canary-visualreferences): {{
    - VisualReference}}
  [VPCConfig](#cfn-synthetics-canary-vpcconfig): {{
    VPCConfig}}
```

## Properties
<a name="aws-resource-synthetics-canary-properties"></a>

`ArtifactConfig`  <a name="cfn-synthetics-canary-artifactconfig"></a>
A structure that contains the configuration for canary artifacts, including the encryption-at-rest settings for artifacts that the canary uploads to Amazon S3.
*Required*: No
*Type*: [ArtifactConfig](aws-properties-synthetics-canary-artifactconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ArtifactS3Location`  <a name="cfn-synthetics-canary-artifacts3location"></a>
The location in Amazon S3 where Synthetics stores artifacts from the runs of this canary. Artifacts include the log file, screenshots, and HAR files. Specify the full location path, including `s3://` at the beginning of the path.
*Required*: Yes
*Type*: String
*Pattern*: `^(s3|S3)://`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BrowserConfigs`  <a name="cfn-synthetics-canary-browserconfigs"></a>
A structure that specifies the browser type to use for a canary run. CloudWatch Synthetics supports running canaries on both `CHROME` and `FIREFOX` browsers.
If not specified, `browserConfigs` defaults to Chrome.
*Required*: No
*Type*: Array of [BrowserConfig](aws-properties-synthetics-canary-browserconfig.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Code`  <a name="cfn-synthetics-canary-code"></a>
Use this structure to input your script code for the canary. This structure contains the Lambda handler with the location where the canary should start running the script. If the script is stored in an S3 bucket, the bucket name, key, and version are also included. If the script is passed into the canary directly, the script code is contained in the value of `Script`.
*Required*: Yes
*Type*: [Code](aws-properties-synthetics-canary-code.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DryRunAndUpdate`  <a name="cfn-synthetics-canary-dryrunandupdate"></a>
Specifies whether to perform a dry run before updating the canary. If set to `true`, CloudFormation will execute a dry run to validate the changes before applying them to the canary. If the dry run succeeds, the canary will be updated with the changes. If the dry run fails, the CloudFormation deployment will fail with the dry run’s failure reason.
 If set to `false` or omitted, the canary will be updated directly without first performing a dry run. The default value is `false`.
For more information, see [Performing safe canary updates ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/performing-safe-canary-upgrades.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-synthetics-canary-executionrolearn"></a>
The ARN of the IAM role to be used to run the canary. This role must already exist, and must include `lambda.amazonaws.com` as a principal in the trust policy. The role must also have the following permissions:
+  `s3:PutObject`
+  `s3:GetBucketLocation`
+  `s3:ListAllMyBuckets`
+  `cloudwatch:PutMetricData`
+  `logs:CreateLogGroup`
+  `logs:CreateLogStream`
+  `logs:PutLogEvents`
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailureRetentionPeriod`  <a name="cfn-synthetics-canary-failureretentionperiod"></a>
The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-synthetics-canary-kmskeyarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9-]+:kms:[a-z0-9-]+:[0-9]{12}:(key/([a-f0-9-]{36}|mrk-[a-f0-9]{32})|alias/[a-zA-Z0-9:/_.-]+)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-synthetics-canary-name"></a>
The name for this canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account.
Do not include secrets or proprietary information in your canary names. The canary name makes up part of the canary ARN, and the ARN is included in outbound calls over the internet. For more information, see [Security Considerations for Synthetics Canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html).
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-z_\-]{1,255}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProvisionedResourceCleanup`  <a name="cfn-synthetics-canary-provisionedresourcecleanup"></a>
Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If it is `AUTOMATIC`, the Lambda functions and layers will be deleted when the canary is deleted.
If the value of this parameter is `OFF`, then the value of the `DeleteLambda` parameter of the [DeleteCanary](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html) operation determines whether the Lambda functions and layers will be deleted.
*Required*: No
*Type*: String
*Allowed values*: `AUTOMATIC | OFF`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Replicas`  <a name="cfn-synthetics-canary-replicas"></a>
Property description not available.
*Required*: No
*Type*: Array of [Replica](aws-properties-synthetics-canary-replica.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesToReplicateTags`  <a name="cfn-synthetics-canary-resourcestoreplicatetags"></a>
To have the tags that you apply to this canary also be applied to the Lambda function that the canary uses, specify this property with the value `lambda-function`. If you do this, CloudWatch Synthetics will keep the tags of the canary and the Lambda function synchronized. Any future changes you make to the canary's tags will also be applied to the function.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunConfig`  <a name="cfn-synthetics-canary-runconfig"></a>
A structure that contains input information for a canary run. If you omit this structure, the frequency of the canary is used as canary's timeout value, up to a maximum of 900 seconds.
*Required*: No
*Type*: [RunConfig](aws-properties-synthetics-canary-runconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeVersion`  <a name="cfn-synthetics-canary-runtimeversion"></a>
Specifies the runtime version to use for the canary. For more information about runtime versions, see [ Canary Runtime Versions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schedule`  <a name="cfn-synthetics-canary-schedule"></a>
A structure that contains information about how often the canary is to run, and when these runs are to stop.
*Required*: Yes
*Type*: [Schedule](aws-properties-synthetics-canary-schedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartCanaryAfterCreation`  <a name="cfn-synthetics-canary-startcanaryaftercreation"></a>
Specify TRUE to have the canary start making runs immediately after it is created.
A canary that you create using CloudFormation can't be used to monitor the CloudFormation stack that creates the canary or to roll back that stack if there is a failure.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessRetentionPeriod`  <a name="cfn-synthetics-canary-successretentionperiod"></a>
The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.
This setting affects the range of information returned by [GetCanaryRuns](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html), as well as the range of information displayed in the Synthetics console.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-synthetics-canary-tags"></a>
The list of key-value pairs that are associated with the canary.
*Required*: No
*Type*: Array of [Tag](aws-properties-synthetics-canary-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualReferences`  <a name="cfn-synthetics-canary-visualreferences"></a>
A list of visual reference configurations for the canary, one for each browser type that the canary is configured to run on. Visual references are used for visual monitoring comparisons.
`syn-nodejs-puppeteer-11.0` and above, and `syn-nodejs-playwright-3.0` and above, only supports `visualReferences`. `visualReference` field is not supported.
Versions older than `syn-nodejs-puppeteer-11.0` supports both `visualReference` and `visualReferences` for backward compatibility. It is recommended to use `visualReferences` for consistency and future compatibility.
*Required*: No
*Type*: Array of [VisualReference](aws-properties-synthetics-canary-visualreference.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VPCConfig`  <a name="cfn-synthetics-canary-vpcconfig"></a>
If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see [ Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).
*Required*: No
*Type*: [VPCConfig](aws-properties-synthetics-canary-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-synthetics-canary-return-values"></a>

### Ref
<a name="aws-resource-synthetics-canary-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the canary, such as `MyCanary`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-synthetics-canary-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-synthetics-canary-return-values-fn--getatt-fn--getatt"></a>

`Code.SourceLocationArn`  <a name="Code.SourceLocationArn-fn::getatt"></a>
When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the Lambda layer where Synthetics stores the canary script code.
For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

`Id`  <a name="Id-fn::getatt"></a>
The ID of the canary.

`State`  <a name="State-fn::getatt"></a>
The state of the canary. For example, `RUNNING`.

## Examples
<a name="aws-resource-synthetics-canary--examples"></a>

**Topics**
+ [Canary with script stored in an Amazon S3 bucket](#aws-resource-synthetics-canary--examples--Canary_with_script_stored_in_an_Amazon_S3_bucket)
+ [Canary with script passed through CloudFormation](#aws-resource-synthetics-canary--examples--Canary_with_script_passed_through_CloudFormation)

### Canary with script stored in an Amazon S3 bucket
<a name="aws-resource-synthetics-canary--examples--Canary_with_script_stored_in_an_Amazon_S3_bucket"></a>

This example creates a canary that uses an existing script stored in an S3 bucket. The canary is started as soon as it is created.

#### JSON
<a name="aws-resource-synthetics-canary--examples--Canary_with_script_stored_in_an_Amazon_S3_bucket--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "CloudFormation Sample Template for CloudWatch Synthetics: Create a Canary using this template",
    "Resources": {
        "SyntheticsCanary": {
            "Type": "AWS::Synthetics::Canary",
            "Properties": {
                "Name": {
                    "Ref": "samplecanary"
                },
                "ExecutionRoleArn": {
                    "Ref": "arn:aws:iam::123456789012:role/my-lambda-execution-role-to-run-canary"
                },
                "Code": {
                    "Handler": "pageLoadBlueprint.handler",
                    "S3Bucket": "aws-synthetics-code-myaccount-canary1",
                    "S3Key": "my-script-location"
                },
                "ArtifactS3Location": "s3://my-results-bucket",
                "RuntimeVersion": "syn-nodejs-puppeteer-6.2",
                "Schedule": {
                    "Expression": "rate(1 minute)",
                    "DurationInSeconds": 3600
                },
                "RunConfig": {
                    "TimeoutInSeconds": 60
                },
                "FailureRetentionPeriod": 30,
                "SuccessRetentionPeriod": 30,
                "StartCanaryAfterCreation": true,
                "Tags": [
                    {
                        "Key": "key00AtCreate",
                        "Value": "value001AtCreate"
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-synthetics-canary--examples--Canary_with_script_stored_in_an_Amazon_S3_bucket--yaml"></a>

```
Resources:
    SyntheticsCanary:
        Type: 'AWS::Synthetics::Canary'
        Properties:
            Name: samplecanary
            ExecutionRoleArn: 'arn:aws:iam::123456789012:role/my-lambda-execution-role-to-run-canary'
            Code: {Handler: pageLoadBlueprint.handler, S3Bucket: aws-synthetics-code-myaccount-canary1, S3Key: my-script-location}
            ArtifactS3Location: s3://my-results-bucket
            RuntimeVersion: syn-nodejs-puppeteer-6.2
            Schedule: {Expression: 'rate(1 minute)', DurationInSeconds: 3600}
            RunConfig: {TimeoutInSeconds: 60}
            FailureRetentionPeriod: 30
            SuccessRetentionPeriod: 30
            Tags: [{Key: key00AtCreate, Value: value001AtCreate}]
            StartCanaryAfterCreation: true
```

### Canary with script passed through CloudFormation
<a name="aws-resource-synthetics-canary--examples--Canary_with_script_passed_through_CloudFormation"></a>

This example creates a canary and passes the script code directly into the canary.

#### JSON
<a name="aws-resource-synthetics-canary--examples--Canary_with_script_passed_through_CloudFormation--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "CloudFormation Sample Template for CloudWatch Synthetics: Create a Canary using this template",
    "Resources": {
        "SyntheticsCanary": {
            "Type": "AWS::Synthetics::Canary",
            "Properties": {
                "Name": {
                    "Ref": "samplecanary"
                },
                "ExecutionRoleArn": {
                    "Ref": "arn:aws:iam::123456789012:role/my-lambda-execution-role-to-run-canary"
                },
                "Code": {
                    "Handler": "pageLoadBlueprint.handler",
                    "Script": "var synthetics = require('Synthetics');\nconst log = require('SyntheticsLogger');\n\nconst pageLoadBlueprint = async function () {\n\n    // INSERT URL here\n    const URL = \"https://amazon.com\";\n\n    let page = await synthetics.getPage();\n    const response = await page.goto(URL, {waitUntil: 'domcontentloaded', timeout: 30000});\n    //Wait for page to render.\n    //Increase or decrease wait time based on endpoint being monitored.\n    await page.waitFor(15000);\n    await synthetics.takeScreenshot('loaded', 'loaded');\n    let pageTitle = await page.title();\n    log.info('Page title: ' + pageTitle);\n    if (response.status() !== 200) {\n        throw \"Failed to load page!\";\n    }\n};\n\nexports.handler = async () => {\n    return await pageLoadBlueprint();\n};\n"
                },
                "ArtifactS3Location": "s3://my-results-bucket",
                "RuntimeVersion": "syn-nodejs-puppeteer-6.2",
                "Schedule": {
                    "Expression": "rate(1 minute)",
                    "DurationInSeconds": 3600
                },
                "RunConfig": {
                    "TimeoutInSeconds": 60
                },
                "FailureRetentionPeriod": 30,
                "SuccessRetentionPeriod": 30,
                "StartCanaryAfterCreation": false,
                "Tags": [
                    {
                        "Id": "key00AtCreate",
                        "Value": "value001AtCreate"
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-synthetics-canary--examples--Canary_with_script_passed_through_CloudFormation--yaml"></a>

```
Resources:
    SyntheticsCanary:
        Type: 'AWS::Synthetics::Canary'
        Properties:
            Name: samplecanary
            ExecutionRoleArn: 'arn:aws:iam::123456789012:role/my-lambda-execution-role-to-run-canary'
            Code: {Handler: pageLoadBlueprint.handler, Script: "var synthetics = require('Synthetics');\nconst log = require('SyntheticsLogger');\nconst pageLoadBlueprint = async function () {\n// INSERT URL here\nconst URL = \"https://amazon.com\";\n\nlet page = await synthetics.getPage();\nconst response = await page.goto(URL, {waitUntil: 'domcontentloaded', timeout: 30000});\n//Wait for page to render.\n//Increase or decrease wait time based on endpoint being monitored.\nawait page.waitFor(15000);\nawait synthetics.takeScreenshot('loaded', 'loaded');\nlet pageTitle = await page.title();\nlog.info('Page title: ' + pageTitle);\nif (response.status() !== 200) {\n     throw \"Failed to load page!\";\n}\n};\n\nexports.handler = async () => {\nreturn await pageLoadBlueprint();\n};\n"}
            ArtifactS3Location: s3://my-results-bucket
            RuntimeVersion: syn-nodejs-puppeteer-6.2
            Schedule: {Expression: 'rate(1 minute)', DurationInSeconds: 3600}
            RunConfig: {TimeoutInSeconds: 60}
            FailureRetentionPeriod: 30
            SuccessRetentionPeriod: 30
            Tags: [{Key: key00AtCreate, Value: value001AtCreate}]
            StartCanaryAfterCreation: false
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
