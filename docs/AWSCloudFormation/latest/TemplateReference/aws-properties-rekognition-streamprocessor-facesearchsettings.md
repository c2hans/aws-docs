---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rekognition-streamprocessor-facesearchsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::StreamProcessor FaceSearchSettings
<a name="aws-properties-rekognition-streamprocessor-facesearchsettings"></a>

The input parameters used to recognize faces in a streaming video analyzed by a Amazon Rekognition stream processor. `FaceSearchSettings` is a request parameter for [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor). For more information, see [FaceSearchSettings](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceSearchSettings).

## Syntax
<a name="aws-properties-rekognition-streamprocessor-facesearchsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rekognition-streamprocessor-facesearchsettings-syntax.json"></a>

```
{
  "[CollectionId](#cfn-rekognition-streamprocessor-facesearchsettings-collectionid)" : {{String}},
  "[FaceMatchThreshold](#cfn-rekognition-streamprocessor-facesearchsettings-facematchthreshold)" : {{Number}}
}
```

### YAML
<a name="aws-properties-rekognition-streamprocessor-facesearchsettings-syntax.yaml"></a>

```
  [CollectionId](#cfn-rekognition-streamprocessor-facesearchsettings-collectionid): {{String}}
  [FaceMatchThreshold](#cfn-rekognition-streamprocessor-facesearchsettings-facematchthreshold): {{Number}}
```

## Properties
<a name="aws-properties-rekognition-streamprocessor-facesearchsettings-properties"></a>

`CollectionId`  <a name="cfn-rekognition-streamprocessor-facesearchsettings-collectionid"></a>
The ID of a collection that contains faces that you want to search for.
*Required*: Yes
*Type*: String
*Pattern*: `\A[a-zA-Z0-9_\.\-]+$`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FaceMatchThreshold`  <a name="cfn-rekognition-streamprocessor-facesearchsettings-facematchthreshold"></a>
Minimum face match confidence score that must be met to return a result for a recognized face. The default is 80. 0 is the lowest confidence. 100 is the highest confidence. Values between 0 and 100 are accepted, and values lower than 80 are set to 80.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
