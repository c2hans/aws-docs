---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRImportJobs.html
---

# ListFHIRImportJobs
<a name="API_ListFHIRImportJobs"></a>

List all FHIR import jobs associated with an account and their statuses.

## Request Syntax
<a name="API_ListFHIRImportJobs_RequestSyntax"></a>

```
{
   "DatastoreId": "{{string}}",
   "JobName": "{{string}}",
   "JobStatus": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SubmittedAfter": {{number}},
   "SubmittedBefore": {{number}}
}
```

## Request Parameters
<a name="API_ListFHIRImportJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatastoreId](#API_ListFHIRImportJobs_RequestSyntax) **   <a name="HealthLake-ListFHIRImportJobs-request-DatastoreId"></a>
Limits the response to the import job with the specified data store ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

 ** [JobName](#API_ListFHIRImportJobs_RequestSyntax) **   <a name="HealthLake-ListFHIRImportJobs-request-JobName"></a>
Limits the response to the import job with the specified job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** [JobStatus](#API_ListFHIRImportJobs_RequestSyntax) **   <a name="HealthLake-ListFHIRImportJobs-request-JobStatus"></a>
Limits the response to the import job with the specified job status.
Type: String
Valid Values: `SUBMITTED | QUEUED | IN_PROGRESS | COMPLETED_WITH_ERRORS | COMPLETED | FAILED | CANCEL_SUBMITTED | CANCEL_IN_PROGRESS | CANCEL_COMPLETED | CANCEL_FAILED`
Required: No

 ** [MaxResults](#API_ListFHIRImportJobs_RequestSyntax) **   <a name="HealthLake-ListFHIRImportJobs-request-MaxResults"></a>
Limits the number of results returned for `ListFHIRImportJobs` to a maximum quantity specified by the user.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListFHIRImportJobs_RequestSyntax) **   <a name="HealthLake-ListFHIRImportJobs-request-NextToken"></a>
The pagination token used to identify the next page of results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`
Required: No

 ** [SubmittedAfter](#API_ListFHIRImportJobs_RequestSyntax) **   <a name="HealthLake-ListFHIRImportJobs-request-SubmittedAfter"></a>
Limits the response to FHIR import jobs submitted after a user-specified date.
Type: Timestamp
Required: No

 ** [SubmittedBefore](#API_ListFHIRImportJobs_RequestSyntax) **   <a name="HealthLake-ListFHIRImportJobs-request-SubmittedBefore"></a>
Limits the response to FHIR import jobs submitted before a user- specified date.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_ListFHIRImportJobs_ResponseSyntax"></a>

```
{
   "ImportJobPropertiesList": [
      {
         "DataAccessRoleArn": "string",
         "DatastoreId": "string",
         "EndTime": number,
         "InputDataConfig": { ... },
         "JobId": "string",
         "JobName": "string",
         "JobOutputDataConfig": { ... },
         "JobProgressReport": {
            "Throughput": number,
            "TotalFilesConverted": number,
            "TotalNumberOfFilesReadWithCustomerError": number,
            "TotalNumberOfImportedFiles": number,
            "TotalNumberOfImportedNonFhirFiles": number,
            "TotalNumberOfNonFhirFilesReadWithCustomerError": number,
            "TotalNumberOfNonFhirResourcesImported": number,
            "TotalNumberOfNonFhirResourcesScanned": number,
            "TotalNumberOfNonFhirResourcesWithCustomerError": number,
            "TotalNumberOfResourcesImported": number,
            "TotalNumberOfResourcesScanned": number,
            "TotalNumberOfResourcesWithCustomerError": number,
            "TotalNumberOfScannedFiles": number,
            "TotalNumberOfScannedNonFhirFiles": number,
            "TotalResourcesGenerated": number,
            "TotalSizeOfScannedFilesInMB": number,
            "TotalSizeOfScannedNonFhirFilesInMB": number
         },
         "JobStatus": "string",
         "Message": "string",
         "SubmitTime": number,
         "ValidationLevel": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFHIRImportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImportJobPropertiesList](#API_ListFHIRImportJobs_ResponseSyntax) **   <a name="HealthLake-ListFHIRImportJobs-response-ImportJobPropertiesList"></a>
The properties for listed import jobs.
Type: Array of [ImportJobProperties](API_ImportJobProperties.md) objects

 ** [NextToken](#API_ListFHIRImportJobs_ResponseSyntax) **   <a name="HealthLake-ListFHIRImportJobs-response-NextToken"></a>
The pagination token used to identify the next page of results to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`

## Errors
<a name="API_ListFHIRImportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested data store was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListFHIRImportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/ListFHIRImportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/ListFHIRImportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/ListFHIRImportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/ListFHIRImportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/ListFHIRImportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/ListFHIRImportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/ListFHIRImportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/ListFHIRImportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/ListFHIRImportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/ListFHIRImportJobs)
