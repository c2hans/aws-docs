---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html
---

# DetectLabels
<a name="API_DetectLabels"></a>

Detects instances of real-world entities within an image (JPEG or PNG) provided as input. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; and concepts like landscape, evening, and nature.

For an example, see [Analyzing images stored in an Amazon S3 bucket](https://docs.aws.amazon.com/rekognition/latest/dg/images-s3.html).

You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.

 **Optional Parameters**

You can specify one or both of the `GENERAL_LABELS` and `IMAGE_PROPERTIES` feature types when calling the DetectLabels API. Including `GENERAL_LABELS` will ensure the response includes the labels detected in the input image, while including `IMAGE_PROPERTIES `will ensure the response includes information about the image quality and color.

When using `GENERAL_LABELS` and/or `IMAGE_PROPERTIES` you can provide filtering criteria to the Settings parameter. You can filter with sets of individual labels or with label categories. You can specify inclusive filters, exclusive filters, or a combination of inclusive and exclusive filters. For more information on filtering see [Detecting Labels in an Image](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html).

When getting labels, you can specify `MinConfidence` to control the confidence threshold for the labels returned. The default is 55%. You can also add the `MaxLabels` parameter to limit the number of labels returned. The default and upper limit is 1000 labels. These arguments are only valid when supplying GENERAL\_LABELS as a feature type.

 **Response Elements**

 For each object, scene, and concept the API returns one or more labels. The API returns the following types of information about labels:
+  Name - The name of the detected label.
+  Confidence - The level of confidence in the label assigned to a detected object.
+  Parents - The ancestor labels for a detected label. DetectLabels returns a hierarchical taxonomy of detected labels. For example, a detected car might be assigned the label car. The label car has two parent labels: Vehicle (its parent) and Transportation (its grandparent). The response includes the all ancestors for a label, where every ancestor is a unique label. In the previous example, Car, Vehicle, and Transportation are returned as unique labels in the response.
+  Aliases - Possible Aliases for the label.
+  Categories - The label categories that the detected label belongs to.
+  BoundingBox — Bounding boxes are described for all instances of detected common object labels, returned in an array of Instance objects. An Instance object contains a BoundingBox object, describing the location of the label on the input image. It also includes the confidence for the accuracy of the detected bounding box.

 The API returns the following information regarding the image, as part of the ImageProperties structure:
+ Quality - Information about the Sharpness, Brightness, and Contrast of the input image, scored between 0 to 100. Image quality is returned for the entire image, as well as the background and the foreground.
+ Dominant Color - An array of the dominant colors in the image.
+ Foreground - Information about the sharpness, brightness, and dominant colors of the input image’s foreground.
+ Background - Information about the sharpness, brightness, and dominant colors of the input image’s background.

The list of returned labels will include at least one label for every detected object, along with information about that label. In the following example, suppose the input image has a lighthouse, the sea, and a rock. The response includes all three labels, one for each object, as well as the confidence in the label:

 `{Name: lighthouse, Confidence: 98.4629}`

 `{Name: rock,Confidence: 79.2097}`

 ` {Name: sea,Confidence: 75.061}`

The list of labels can include multiple labels for the same object. For example, if the input image shows a flower (for example, a tulip), the operation might return the following three labels.

 `{Name: flower,Confidence: 99.0562}`

 `{Name: plant,Confidence: 99.0562}`

 `{Name: tulip,Confidence: 99.0562}`

In this example, the detection algorithm more precisely identifies the flower as a tulip.

**Note**
If the object detected is a person, the operation doesn't provide the same facial details that the [DetectFaces](API_DetectFaces.md) operation provides.

This is a stateless API operation that doesn't return any data.

This operation requires permissions to perform the `rekognition:DetectLabels` action.

## Request Syntax
<a name="API_DetectLabels_RequestSyntax"></a>

```
{
   "Features": [ "{{string}}" ],
   "Image": {
      "Bytes": {{blob}},
      "S3Object": {
         "Bucket": "{{string}}",
         "Name": "{{string}}",
         "Version": "{{string}}"
      }
   },
   "MaxLabels": {{number}},
   "MinConfidence": {{number}},
   "Settings": {
      "GeneralLabels": {
         "LabelCategoryExclusionFilters": [ "{{string}}" ],
         "LabelCategoryInclusionFilters": [ "{{string}}" ],
         "LabelExclusionFilters": [ "{{string}}" ],
         "LabelInclusionFilters": [ "{{string}}" ]
      },
      "ImageProperties": {
         "MaxDominantColors": {{number}}
      }
   }
}
```

## Request Parameters
<a name="API_DetectLabels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Features](#API_DetectLabels_RequestSyntax) **   <a name="rekognition-DetectLabels-request-Features"></a>
A list of the types of analysis to perform. Specifying GENERAL\_LABELS uses the label detection feature, while specifying IMAGE\_PROPERTIES returns information regarding image color and quality. If no option is specified GENERAL\_LABELS is used by default.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `GENERAL_LABELS | IMAGE_PROPERTIES`
Required: No

 ** [Image](#API_DetectLabels_RequestSyntax) **   <a name="rekognition-DetectLabels-request-Image"></a>
The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. Images stored in an S3 Bucket do not need to be base64-encoded.
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the `Bytes` field. For more information, see [Image specifications](https://docs.aws.amazon.com/rekognition/latest/dg/images-information.html).
Type: [Image](API_Image.md) object
Required: Yes

 ** [MaxLabels](#API_DetectLabels_RequestSyntax) **   <a name="rekognition-DetectLabels-request-MaxLabels"></a>
Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels. Only valid when GENERAL\_LABELS is specified as a feature type in the Feature input parameter.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [MinConfidence](#API_DetectLabels_RequestSyntax) **   <a name="rekognition-DetectLabels-request-MinConfidence"></a>
Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with confidence lower than this specified value.
If `MinConfidence` is not specified, the operation returns labels with a confidence values greater than or equal to 55 percent. Only valid when GENERAL\_LABELS is specified as a feature type in the Feature input parameter.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [Settings](#API_DetectLabels_RequestSyntax) **   <a name="rekognition-DetectLabels-request-Settings"></a>
A list of the filters to be applied to returned detected labels and image properties. Specified filters can be inclusive, exclusive, or a combination of both. Filters can be used for individual labels or label categories. The exact label names or label categories must be supplied. For a full list of labels and label categories, see [Detecting labels](https://docs.aws.amazon.com/rekognition/latest/dg/labels.html).
Type: [DetectLabelsSettings](API_DetectLabelsSettings.md) object
Required: No

## Response Syntax
<a name="API_DetectLabels_ResponseSyntax"></a>

```
{
   "ImageProperties": {
      "Background": {
         "DominantColors": [
            {
               "Blue": number,
               "CSSColor": "string",
               "Green": number,
               "HexCode": "string",
               "PixelPercent": number,
               "Red": number,
               "SimplifiedColor": "string"
            }
         ],
         "Quality": {
            "Brightness": number,
            "Contrast": number,
            "Sharpness": number
         }
      },
      "DominantColors": [
         {
            "Blue": number,
            "CSSColor": "string",
            "Green": number,
            "HexCode": "string",
            "PixelPercent": number,
            "Red": number,
            "SimplifiedColor": "string"
         }
      ],
      "Foreground": {
         "DominantColors": [
            {
               "Blue": number,
               "CSSColor": "string",
               "Green": number,
               "HexCode": "string",
               "PixelPercent": number,
               "Red": number,
               "SimplifiedColor": "string"
            }
         ],
         "Quality": {
            "Brightness": number,
            "Contrast": number,
            "Sharpness": number
         }
      },
      "Quality": {
         "Brightness": number,
         "Contrast": number,
         "Sharpness": number
      }
   },
   "LabelModelVersion": "string",
   "Labels": [
      {
         "Aliases": [
            {
               "Name": "string"
            }
         ],
         "Categories": [
            {
               "Name": "string"
            }
         ],
         "Confidence": number,
         "Instances": [
            {
               "BoundingBox": {
                  "Height": number,
                  "Left": number,
                  "Top": number,
                  "Width": number
               },
               "Confidence": number,
               "DominantColors": [
                  {
                     "Blue": number,
                     "CSSColor": "string",
                     "Green": number,
                     "HexCode": "string",
                     "PixelPercent": number,
                     "Red": number,
                     "SimplifiedColor": "string"
                  }
               ]
            }
         ],
         "Name": "string",
         "Parents": [
            {
               "Name": "string"
            }
         ]
      }
   ],
   "OrientationCorrection": "string"
}
```

## Response Elements
<a name="API_DetectLabels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageProperties](#API_DetectLabels_ResponseSyntax) **   <a name="rekognition-DetectLabels-response-ImageProperties"></a>
Information about the properties of the input image, such as brightness, sharpness, contrast, and dominant colors.
Type: [DetectLabelsImageProperties](API_DetectLabelsImageProperties.md) object

 ** [LabelModelVersion](#API_DetectLabels_ResponseSyntax) **   <a name="rekognition-DetectLabels-response-LabelModelVersion"></a>
Version number of the label detection model that was used to detect labels.
Type: String

 ** [Labels](#API_DetectLabels_ResponseSyntax) **   <a name="rekognition-DetectLabels-response-Labels"></a>
An array of labels for the real-world objects detected.
Type: Array of [Label](API_Label.md) objects

 ** [OrientationCorrection](#API_DetectLabels_ResponseSyntax) **   <a name="rekognition-DetectLabels-response-OrientationCorrection"></a>
The value of `OrientationCorrection` is always null.
If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata.
Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren't translated and represent the object locations before the image is rotated.
Type: String
Valid Values: `ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270`

## Errors
<a name="API_DetectLabels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** ImageTooLargeException **
The input image size exceeds the allowed limit. If you are calling [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md), the image size or resolution exceeds the allowed limit. For more information, see [Guidelines and quotas in Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html).
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidImageFormatException **
The provided image format is not supported.
HTTP Status Code: 400

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** InvalidS3ObjectException **
Amazon Rekognition is unable to access the S3 object specified in the request.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_DetectLabels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/DetectLabels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/DetectLabels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectLabels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/DetectLabels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DetectLabels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/DetectLabels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/DetectLabels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectLabels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectLabels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectLabels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
