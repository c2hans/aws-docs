---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html
---

# SearchUsersByImage
<a name="API_SearchUsersByImage"></a>

Searches for UserIDs using a supplied image. It first detects the largest face in the image, and then searches a specified collection for matching UserIDs.

The operation returns an array of UserIDs that match the face in the supplied image, ordered by similarity score with the highest similarity first. It also returns a bounding box for the face found in the input image.

Information about faces detected in the supplied image, but not used for the search, is returned in an array of `UnsearchedFace` objects. If no valid face is detected in the image, the response will contain an empty `UserMatches` list and no `SearchedFace` object.

## Request Syntax
<a name="API_SearchUsersByImage_RequestSyntax"></a>

```
{
   "CollectionId": "{{string}}",
   "Image": {
      "Bytes": {{blob}},
      "S3Object": {
         "Bucket": "{{string}}",
         "Name": "{{string}}",
         "Version": "{{string}}"
      }
   },
   "MaxUsers": {{number}},
   "QualityFilter": "{{string}}",
   "UserMatchThreshold": {{number}}
}
```

## Request Parameters
<a name="API_SearchUsersByImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CollectionId](#API_SearchUsersByImage_RequestSyntax) **   <a name="rekognition-SearchUsersByImage-request-CollectionId"></a>
The ID of an existing collection containing the UserID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [Image](#API_SearchUsersByImage_RequestSyntax) **   <a name="rekognition-SearchUsersByImage-request-Image"></a>
Provides the input image either as bytes or an S3 object.
You pass image bytes to an Amazon Rekognition API operation by using the `Bytes` property. For example, you would use the `Bytes` property to pass an image loaded from a local file system. Image bytes passed by using the `Bytes` property must be base64-encoded. Your code may not need to encode image bytes if you are using an AWS SDK to call Amazon Rekognition API operations.
For more information, see [Analyzing an image loaded from a local file system](https://docs.aws.amazon.com/rekognition/latest/dg/images-bytes.html) .
 You pass images stored in an S3 bucket to an Amazon Rekognition API operation by using the `S3Object` property. Images stored in an S3 bucket do not need to be base64-encoded.
The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations.
If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes using the Bytes property is not supported. You must first upload the image to an Amazon S3 bucket and then call the operation using the S3Object property.
For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object. For more information, see [How Amazon Rekognition works with IAM](https://docs.aws.amazon.com/rekognition/latest/dg/security_iam_service-with-iam.html).
Type: [Image](API_Image.md) object
Required: Yes

 ** [MaxUsers](#API_SearchUsersByImage_RequestSyntax) **   <a name="rekognition-SearchUsersByImage-request-MaxUsers"></a>
Maximum number of UserIDs to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [QualityFilter](#API_SearchUsersByImage_RequestSyntax) **   <a name="rekognition-SearchUsersByImage-request-QualityFilter"></a>
A filter that specifies a quality bar for how much filtering is done to identify faces. Filtered faces aren't searched for in the collection. The default value is NONE.
Type: String
Valid Values: `NONE | AUTO | LOW | MEDIUM | HIGH`
Required: No

 ** [UserMatchThreshold](#API_SearchUsersByImage_RequestSyntax) **   <a name="rekognition-SearchUsersByImage-request-UserMatchThreshold"></a>
Specifies the minimum confidence in the UserID match to return. Default value is 80.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## Response Syntax
<a name="API_SearchUsersByImage_ResponseSyntax"></a>

```
{
   "FaceModelVersion": "string",
   "SearchedFace": {
      "FaceDetail": {
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
   },
   "UnsearchedFaces": [
      {
         "FaceDetails": {
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
         },
         "Reasons": [ "string" ]
      }
   ],
   "UserMatches": [
      {
         "Similarity": number,
         "User": {
            "UserId": "string",
            "UserStatus": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchUsersByImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FaceModelVersion](#API_SearchUsersByImage_ResponseSyntax) **   <a name="rekognition-SearchUsersByImage-response-FaceModelVersion"></a>
Version number of the face detection model associated with the input collection CollectionId.
Type: String

 ** [SearchedFace](#API_SearchUsersByImage_ResponseSyntax) **   <a name="rekognition-SearchUsersByImage-response-SearchedFace"></a>
A list of FaceDetail objects containing the BoundingBox for the largest face in image, as well as the confidence in the bounding box, that was searched for matches. If no valid face is detected in the image the response will contain no SearchedFace object.
Type: [SearchedFaceDetails](API_SearchedFaceDetails.md) object

 ** [UnsearchedFaces](#API_SearchUsersByImage_ResponseSyntax) **   <a name="rekognition-SearchUsersByImage-response-UnsearchedFaces"></a>
List of UnsearchedFace objects. Contains the face details infered from the specified image but not used for search. Contains reasons that describe why a face wasn't used for Search.
Type: Array of [UnsearchedFace](API_UnsearchedFace.md) objects

 ** [UserMatches](#API_SearchUsersByImage_ResponseSyntax) **   <a name="rekognition-SearchUsersByImage-response-UserMatches"></a>
An array of UserID objects that matched the input face, along with the confidence in the match. The returned structure will be empty if there are no matches. Returned if the SearchUsersByImageResponse action is successful.
Type: Array of [UserMatch](API_UserMatch.md) objects
Array Members: Maximum number of 500 items.

## Errors
<a name="API_SearchUsersByImage_Errors"></a>

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

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_SearchUsersByImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/SearchUsersByImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/SearchUsersByImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SearchUsersByImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/SearchUsersByImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/SearchUsersByImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/SearchUsersByImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/SearchUsersByImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/SearchUsersByImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/SearchUsersByImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/SearchUsersByImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
