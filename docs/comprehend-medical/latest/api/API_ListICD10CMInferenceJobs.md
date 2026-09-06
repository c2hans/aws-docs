---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListICD10CMInferenceJobs.html
---

# ListICD10CMInferenceJobs
<a name="API_ListICD10CMInferenceJobs"></a>

Gets a list of InferICD10CM jobs that you have submitted.

## Request Syntax
<a name="API_ListICD10CMInferenceJobs_RequestSyntax"></a>

```
{
   "Filter": {
      "JobName": "{{string}}",
      "JobStatus": "{{string}}",
      "SubmitTimeAfter": {{number}},
      "SubmitTimeBefore": {{number}}
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListICD10CMInferenceJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListICD10CMInferenceJobs_RequestSyntax) **   <a name="comprehendmedical-ListICD10CMInferenceJobs-request-Filter"></a>
Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.
Type: [ComprehendMedicalAsyncJobFilter](API_ComprehendMedicalAsyncJobFilter.md) object
Required: No

 ** [MaxResults](#API_ListICD10CMInferenceJobs_RequestSyntax) **   <a name="comprehendmedical-ListICD10CMInferenceJobs-request-MaxResults"></a>
The maximum number of results to return in each page. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListICD10CMInferenceJobs_RequestSyntax) **   <a name="comprehendmedical-ListICD10CMInferenceJobs-request-NextToken"></a>
Identifies the next page of results to return.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListICD10CMInferenceJobs_ResponseSyntax"></a>

```
{
   "ComprehendMedicalAsyncJobPropertiesList": [
      {
         "DataAccessRoleArn": "string",
         "EndTime": number,
         "ExpirationTime": number,
         "InputDataConfig": {
            "S3Bucket": "string",
            "S3Key": "string"
         },
         "JobId": "string",
         "JobName": "string",
         "JobStatus": "string",
         "KMSKey": "string",
         "LanguageCode": "string",
         "ManifestFilePath": "string",
         "Message": "string",
         "ModelVersion": "string",
         "OutputDataConfig": {
            "S3Bucket": "string",
            "S3Key": "string"
         },
         "SubmitTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListICD10CMInferenceJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComprehendMedicalAsyncJobPropertiesList](#API_ListICD10CMInferenceJobs_ResponseSyntax) **   <a name="comprehendmedical-ListICD10CMInferenceJobs-response-ComprehendMedicalAsyncJobPropertiesList"></a>
A list containing the properties of each job that is returned.
Type: Array of [ComprehendMedicalAsyncJobProperties](API_ComprehendMedicalAsyncJobProperties.md) objects

 ** [NextToken](#API_ListICD10CMInferenceJobs_ResponseSyntax) **   <a name="comprehendmedical-ListICD10CMInferenceJobs-response-NextToken"></a>
Identifies the next page of results to return.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListICD10CMInferenceJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
 The request that you made is invalid. Check your request to determine why it's invalid and then retry the request.
HTTP Status Code: 400

 ** TooManyRequestsException **
 You have made too many requests within a short period of time. Wait for a short time and then try your request again. Contact customer support for more information about a service limit increase.
HTTP Status Code: 400

 ** ValidationException **
The filter that you specified for the operation is invalid. Check the filter values that you entered and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListICD10CMInferenceJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/ListICD10CMInferenceJobs)
