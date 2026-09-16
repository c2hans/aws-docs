---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html
---

# DetectFaces
<a name="API_DetectFaces"></a>

Detects faces within an image that is provided as input.

 `DetectFaces` detects the 100 largest faces in the image. For each face detected, the operation returns face details. These details include a bounding box of the face, a confidence value (that the bounding box contains a face), and a fixed set of attributes such as facial landmarks (for example, coordinates of eye and mouth), pose, presence of facial occlusion, and so on.

The face-detection algorithm is most effective on frontal faces. For non-frontal or obscured faces, the algorithm might not detect the faces or might detect faces with lower confidence.

You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file.

**Note**
This is a stateless API operation. That is, the operation does not persist any data.

This operation requires permissions to perform the `rekognition:DetectFaces` action.

## Request Syntax
<a name="API_DetectFaces_RequestSyntax"></a>

```
{
   "Attributes": [ "{{string}}" ],
   "Image": {
      "Bytes": {{blob}},
      "S3Object": {
         "Bucket": "{{string}}",
         "Name": "{{string}}",
         "Version": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_DetectFaces_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Attributes](#API_DetectFaces_RequestSyntax) **   <a name="rekognition-DetectFaces-request-Attributes"></a>
An array of facial attributes you want to be returned. A `DEFAULT` subset of facial attributes - `BoundingBox`, `Confidence`, `Pose`, `Quality`, and `Landmarks` - will always be returned. You can request for specific facial attributes (in addition to the default list) - by using [`"DEFAULT", "FACE_OCCLUDED"`] or just [`"FACE_OCCLUDED"`]. You can request for all facial attributes by using [`"ALL"]`. Requesting more attributes may increase response time.
If you provide both, `["ALL", "DEFAULT"]`, the service uses a logical "AND" operator to determine which attributes to return (in this case, all attributes).
Note that while the FaceOccluded and EyeDirection attributes are supported when using `DetectFaces`, they aren't supported when analyzing videos with `StartFaceDetection` and `GetFaceDetection`.
Type: Array of strings
Valid Values: `DEFAULT | ALL | AGE_RANGE | BEARD | EMOTIONS | EYE_DIRECTION | EYEGLASSES | EYES_OPEN | GENDER | MOUTH_OPEN | MUSTACHE | FACE_OCCLUDED | SMILE | SUNGLASSES`
Required: No

 ** [Image](#API_DetectFaces_RequestSyntax) **   <a name="rekognition-DetectFaces-request-Image"></a>
The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported.
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64-encode image bytes passed using the `Bytes` field. For more information, see [Image specifications](https://docs.aws.amazon.com/rekognition/latest/dg/images-information.html).
Type: [Image](API_Image.md) object
Required: Yes

## Response Syntax
<a name="API_DetectFaces_ResponseSyntax"></a>

```
{
   "FaceDetails": [
      {
         "AgeRange": {
            "High": number,
            "Low": number
         },
         "Beard": {
            "Confidence": number,
            "Value": boolean
         },
         "BoundingBox": {
            "Height": number,
            "Left": number,
            "Top": number,
            "Width": number
         },
         "Confidence": number,
         "Emotions": [
            {
               "Confidence": number,
               "Type": "string"
            }
         ],
         "EyeDirection": {
            "Confidence": number,
            "Pitch": number,
            "Yaw": number
         },
         "Eyeglasses": {
            "Confidence": number,
            "Value": boolean
         },
         "EyesOpen": {
            "Confidence": number,
            "Value": boolean
         },
         "FaceOccluded": {
            "Confidence": number,
            "Value": boolean
         },
         "Gender": {
            "Confidence": number,
            "Value": "string"
         },
         "Landmarks": [
            {
               "Type": "string",
               "X": number,
               "Y": number
            }
         ],
         "MouthOpen": {
            "Confidence": number,
            "Value": boolean
         },
         "Mustache": {
            "Confidence": number,
            "Value": boolean
         },
         "Pose": {
            "Pitch": number,
            "Roll": number,
            "Yaw": number
         },
         "Quality": {
            "Brightness": number,
            "Sharpness": number
         },
         "Smile": {
            "Confidence": number,
            "Value": boolean
         },
         "Sunglasses": {
            "Confidence": number,
            "Value": boolean
         }
      }
   ],
   "OrientationCorrection": "string"
}
```

## Response Elements
<a name="API_DetectFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FaceDetails](#API_DetectFaces_ResponseSyntax) **   <a name="rekognition-DetectFaces-response-FaceDetails"></a>
Details of each face found in the image.
Type: Array of [FaceDetail](API_FaceDetail.md) objects

 ** [OrientationCorrection](#API_DetectFaces_ResponseSyntax) **   <a name="rekognition-DetectFaces-response-OrientationCorrection"></a>
The value of `OrientationCorrection` is always null.
If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata.
Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren't translated and represent the object locations before the image is rotated.
Type: String
Valid Values: `ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270`

## Errors
<a name="API_DetectFaces_Errors"></a>

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
<a name="API_DetectFaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/DetectFaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/DetectFaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectFaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/DetectFaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DetectFaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/DetectFaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/DetectFaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectFaces)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectFaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectFaces)
