---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListSNOMEDCTInferenceJobs.html
---

# ListSNOMEDCTInferenceJobs
<a name="API_ListSNOMEDCTInferenceJobs"></a>

 Gets a list of InferSNOMEDCT jobs a user has submitted.

## Request Syntax
<a name="API_ListSNOMEDCTInferenceJobs_RequestSyntax"></a>

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
<a name="API_ListSNOMEDCTInferenceJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListSNOMEDCTInferenceJobs_RequestSyntax) **   <a name="comprehendmedical-ListSNOMEDCTInferenceJobs-request-Filter"></a>
Provides information for filtering a list of detection jobs.
Type: [ComprehendMedicalAsyncJobFilter](API_ComprehendMedicalAsyncJobFilter.md) object
Required: No

 ** [MaxResults](#API_ListSNOMEDCTInferenceJobs_RequestSyntax) **   <a name="comprehendmedical-ListSNOMEDCTInferenceJobs-request-MaxResults"></a>
 The maximum number of results to return in each page. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListSNOMEDCTInferenceJobs_RequestSyntax) **   <a name="comprehendmedical-ListSNOMEDCTInferenceJobs-request-NextToken"></a>
 Identifies the next page of InferSNOMEDCT results to return.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListSNOMEDCTInferenceJobs_ResponseSyntax"></a>

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
<a name="API_ListSNOMEDCTInferenceJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComprehendMedicalAsyncJobPropertiesList](#API_ListSNOMEDCTInferenceJobs_ResponseSyntax) **   <a name="comprehendmedical-ListSNOMEDCTInferenceJobs-response-ComprehendMedicalAsyncJobPropertiesList"></a>
 A list containing the properties of each job that is returned.
Type: Array of [ComprehendMedicalAsyncJobProperties](API_ComprehendMedicalAsyncJobProperties.md) objects

 ** [NextToken](#API_ListSNOMEDCTInferenceJobs_ResponseSyntax) **   <a name="comprehendmedical-ListSNOMEDCTInferenceJobs-response-NextToken"></a>
 Identifies the next page of results to return.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListSNOMEDCTInferenceJobs_Errors"></a>

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
<a name="API_ListSNOMEDCTInferenceJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
