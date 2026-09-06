---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-applicationinferenceprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ApplicationInferenceProfile
<a name="aws-resource-bedrock-applicationinferenceprofile"></a>

Specifies an inference profile as a resource in a top-level template. Use the `ModelSource` field to specify the inference profile to copy into the resource. For more information about using inference profiles in Amazon Bedrock, see [Improve resilience with cross-region inference ](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrock-applicationinferenceprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-applicationinferenceprofile-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::ApplicationInferenceProfile",
  "Properties" : {
      "[Description](#cfn-bedrock-applicationinferenceprofile-description)" : {{String}},
      "[InferenceProfileName](#cfn-bedrock-applicationinferenceprofile-inferenceprofilename)" : {{String}},
      "[ModelSource](#cfn-bedrock-applicationinferenceprofile-modelsource)" : {{InferenceProfileModelSource}},
      "[Tags](#cfn-bedrock-applicationinferenceprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-applicationinferenceprofile-syntax.yaml"></a>

```
Type: AWS::Bedrock::ApplicationInferenceProfile
Properties:
  [Description](#cfn-bedrock-applicationinferenceprofile-description): {{String}}
  [InferenceProfileName](#cfn-bedrock-applicationinferenceprofile-inferenceprofilename): {{String}}
  [ModelSource](#cfn-bedrock-applicationinferenceprofile-modelsource): {{
    InferenceProfileModelSource}}
  [Tags](#cfn-bedrock-applicationinferenceprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrock-applicationinferenceprofile-properties"></a>

`Description`  <a name="cfn-bedrock-applicationinferenceprofile-description"></a>
The description of the inference profile.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z:.][ _-]?)+$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InferenceProfileName`  <a name="cfn-bedrock-applicationinferenceprofile-inferenceprofilename"></a>
The name of the inference profile.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][ _-]?)+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelSource`  <a name="cfn-bedrock-applicationinferenceprofile-modelsource"></a>
Contains configurations for the inference profile to copy as the resource.
*Required*: No
*Type*: [InferenceProfileModelSource](aws-properties-bedrock-applicationinferenceprofile-inferenceprofilemodelsource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrock-applicationinferenceprofile-tags"></a>
A list of tags associated with the inference profile.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrock-applicationinferenceprofile-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-applicationinferenceprofile-return-values"></a>

### Ref
<a name="aws-resource-bedrock-applicationinferenceprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the inference profile ID.

For example, `{ "Ref": "myInferenceProfile" }` could return the value `"IP12345678"`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-applicationinferenceprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrock-applicationinferenceprofile-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the inference profile was created.

`InferenceProfileArn`  <a name="InferenceProfileArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the inference profile.

`InferenceProfileId`  <a name="InferenceProfileId-fn::getatt"></a>
The unique identifier of the inference profile.

`InferenceProfileIdentifier`  <a name="InferenceProfileIdentifier-fn::getatt"></a>
The ID or Amazon Resource Name (ARN) of the inference profile.

`Models`  <a name="Models-fn::getatt"></a>
A list of information about each model in the inference profile.

`Status`  <a name="Status-fn::getatt"></a>
The status of the inference profile. `ACTIVE` means that the inference profile is ready to be used.

`Type`  <a name="Type-fn::getatt"></a>
The type of the inference profile. The following types are possible:
+ `SYSTEM_DEFINED` – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.
+ `APPLICATION` – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the inference profile was last updated.

## Examples
<a name="aws-resource-bedrock-applicationinferenceprofile--examples"></a>

### Create an inference profile
<a name="aws-resource-bedrock-applicationinferenceprofile--examples--Create_an_inference_profile"></a>

The following example creates an inference profile for the Anthropic Claude 3.5 Sonnet model in the US West (Oregon) region:

#### YAML
<a name="aws-resource-bedrock-applicationinferenceprofile--examples--Create_an_inference_profile--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Example Application Inference Profile
Resources:
  ExampleApplicationInferenceProfile:
    Type: AWS::Bedrock::ApplicationInferenceProfile
    Properties:
      ModelSource:
        CopyFrom: "arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-3-5-sonnet-20240620-v1:0"
      InferenceProfileName: Example Application Inference Profile Name
      Description: Description of ExampleApplicationInferenceProfile
```

#### JSON
<a name="aws-resource-bedrock-applicationinferenceprofile--examples--Create_an_inference_profile--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Example Application Inference Profile",
    "Resources": {
        "ExampleApplicationInferenceProfile": {
            "Type": "AWS::Bedrock::ApplicationInferenceProfile",
            "Properties": {
                "ModelSource": {
                    "CopyFrom": "arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-3-5-sonnet-20240620-v1:0"
                },
                "InferenceProfileName": "Example Application Inference Profile Name",
                "Description": "Description of ExampleApplicationInferenceProfile"
            }
        }
    }
}
```
