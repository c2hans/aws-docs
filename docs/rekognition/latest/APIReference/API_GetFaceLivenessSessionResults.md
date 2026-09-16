---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceLivenessSessionResults.html
---

# GetFaceLivenessSessionResults
<a name="API_GetFaceLivenessSessionResults"></a>

Retrieves the results of a specific Face Liveness session. It requires the `sessionId` as input, which was created using `CreateFaceLivenessSession`. Returns the corresponding Face Liveness confidence score, a reference image that includes a face bounding box, and audit images that also contain face bounding boxes. The Face Liveness confidence score ranges from 0 to 100.

The number of audit images returned by `GetFaceLivenessSessionResults` is defined by the `AuditImagesLimit` paramater when calling `CreateFaceLivenessSession`. Reference images are always returned when possible.

## Request Syntax
<a name="API_GetFaceLivenessSessionResults_RequestSyntax"></a>

```
{
   "SessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetFaceLivenessSessionResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SessionId](#API_GetFaceLivenessSessionResults_RequestSyntax) **   <a name="rekognition-GetFaceLivenessSessionResults-request-SessionId"></a>
A unique 128-bit UUID. This is used to uniquely identify the session and also acts as an idempotency token for all operations associated with the session.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Response Syntax
<a name="API_GetFaceLivenessSessionResults_ResponseSyntax"></a>

```
{
   "AuditImages": [
      {
         "BoundingBox": {
            "Height": number,
            "Left": number,
            "Top": number,
            "Width": number
         },
         "Bytes": blob,
         "S3Object": {
            "Bucket": "string",
            "Name": "string",
            "Version": "string"
         }
      }
   ],
   "Challenge": {
      "Type": "string",
      "Version": "string"
   },
   "Confidence": number,
   "ReferenceImage": {
      "BoundingBox": {
         "Height": number,
         "Left": number,
         "Top": number,
         "Width": number
      },
      "Bytes": blob,
      "S3Object": {
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "SessionId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetFaceLivenessSessionResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuditImages](#API_GetFaceLivenessSessionResults_ResponseSyntax) **   <a name="rekognition-GetFaceLivenessSessionResults-response-AuditImages"></a>
A set of images from the Face Liveness video that can be used for audit purposes. It includes a bounding box of the face and the Base64-encoded bytes that return an image. If the CreateFaceLivenessSession request included an OutputConfig argument, the image will be uploaded to an S3Object specified in the output configuration. If no Amazon S3 bucket is defined, raw bytes are sent instead.
Type: Array of [AuditImage](API_AuditImage.md) objects

 ** [Challenge](#API_GetFaceLivenessSessionResults_ResponseSyntax) **   <a name="rekognition-GetFaceLivenessSessionResults-response-Challenge"></a>
Contains information regarding the challenge type used for the Face Liveness check.
Type: [Challenge](API_Challenge.md) object

 ** [Confidence](#API_GetFaceLivenessSessionResults_ResponseSyntax) **   <a name="rekognition-GetFaceLivenessSessionResults-response-Confidence"></a>
Probabalistic confidence score for if the person in the given video was live, represented as a float value between 0 to 100.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [ReferenceImage](#API_GetFaceLivenessSessionResults_ResponseSyntax) **   <a name="rekognition-GetFaceLivenessSessionResults-response-ReferenceImage"></a>
A high-quality image from the Face Liveness video that can be used for face comparison or search. It includes a bounding box of the face and the Base64-encoded bytes that return an image. If the CreateFaceLivenessSession request included an OutputConfig argument, the image will be uploaded to an S3Object specified in the output configuration. In case the reference image is not returned, it's recommended to retry the Liveness check.
Type: [AuditImage](API_AuditImage.md) object

 ** [SessionId](#API_GetFaceLivenessSessionResults_ResponseSyntax) **   <a name="rekognition-GetFaceLivenessSessionResults-response-SessionId"></a>
The sessionId for which this request was called.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [Status](#API_GetFaceLivenessSessionResults_ResponseSyntax) **   <a name="rekognition-GetFaceLivenessSessionResults-response-Status"></a>
Represents a status corresponding to the state of the session. Possible statuses are: CREATED, IN\_PROGRESS, SUCCEEDED, FAILED, EXPIRED.
Type: String
Valid Values: `CREATED | IN_PROGRESS | SUCCEEDED | FAILED | EXPIRED`

## Errors
<a name="API_GetFaceLivenessSessionResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** SessionNotFoundException **
Occurs when a given sessionId is not found.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_GetFaceLivenessSessionResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/GetFaceLivenessSessionResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/GetFaceLivenessSessionResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetFaceLivenessSessionResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/GetFaceLivenessSessionResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GetFaceLivenessSessionResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/GetFaceLivenessSessionResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/GetFaceLivenessSessionResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetFaceLivenessSessionResults)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetFaceLivenessSessionResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetFaceLivenessSessionResults)
