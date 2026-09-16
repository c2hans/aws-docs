---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListMediaAnalysisJobs.html
---

# ListMediaAnalysisJobs
<a name="API_ListMediaAnalysisJobs"></a>

**Important**
Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Rekognition feature availability changes](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html).
 **This change does not impact the availability of other Amazon Rekognition features.**

Returns a list of media analysis jobs. Results are sorted by `CreationTimestamp` in descending order.

## Request Syntax
<a name="API_ListMediaAnalysisJobs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMediaAnalysisJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListMediaAnalysisJobs_RequestSyntax) **   <a name="rekognition-ListMediaAnalysisJobs-request-MaxResults"></a>
The maximum number of results to return per paginated call. The largest value user can specify is 100. If user specifies a value greater than 100, an `InvalidParameterException` error occurs. The default value is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListMediaAnalysisJobs_RequestSyntax) **   <a name="rekognition-ListMediaAnalysisJobs-request-NextToken"></a>
Pagination token, if the previous response was incomplete.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListMediaAnalysisJobs_ResponseSyntax"></a>

```
{
   "MediaAnalysisJobs": [
      {
         "CompletionTimestamp": number,
         "CreationTimestamp": number,
         "FailureDetails": {
            "Code": "string",
            "Message": "string"
         },
         "Input": {
            "S3Object": {
               "Bucket": "string",
               "Name": "string",
               "Version": "string"
            }
         },
         "JobId": "string",
         "JobName": "string",
         "KmsKeyId": "string",
         "ManifestSummary": {
            "S3Object": {
               "Bucket": "string",
               "Name": "string",
               "Version": "string"
            }
         },
         "OperationsConfig": {
            "DetectModerationLabels": {
               "MinConfidence": number,
               "ProjectVersion": "string"
            }
         },
         "OutputConfig": {
            "S3Bucket": "string",
            "S3KeyPrefix": "string"
         },
         "Results": {
            "ModelVersions": {
               "Moderation": "string"
            },
            "S3Object": {
               "Bucket": "string",
               "Name": "string",
               "Version": "string"
            }
         },
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMediaAnalysisJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MediaAnalysisJobs](#API_ListMediaAnalysisJobs_ResponseSyntax) **   <a name="rekognition-ListMediaAnalysisJobs-response-MediaAnalysisJobs"></a>
Contains a list of all media analysis jobs.
Type: Array of [MediaAnalysisJobDescription](API_MediaAnalysisJobDescription.md) objects

 ** [NextToken](#API_ListMediaAnalysisJobs_ResponseSyntax) **   <a name="rekognition-ListMediaAnalysisJobs-response-NextToken"></a>
Pagination token, if the previous response was incomplete.
Type: String
Length Constraints: Maximum length of 1024.

## Errors
<a name="API_ListMediaAnalysisJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidPaginationTokenException **
Pagination token in the request is not valid.
HTTP Status Code: 400

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_ListMediaAnalysisJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/ListMediaAnalysisJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/ListMediaAnalysisJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ListMediaAnalysisJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/ListMediaAnalysisJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ListMediaAnalysisJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/ListMediaAnalysisJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/ListMediaAnalysisJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/ListMediaAnalysisJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/ListMediaAnalysisJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ListMediaAnalysisJobs)
