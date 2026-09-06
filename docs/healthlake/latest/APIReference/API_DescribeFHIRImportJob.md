---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRImportJob.html
---

# DescribeFHIRImportJob
<a name="API_DescribeFHIRImportJob"></a>

Get the import job properties to learn more about the job or job progress.

## Request Syntax
<a name="API_DescribeFHIRImportJob_RequestSyntax"></a>

```
{
   "DatastoreId": "{{string}}",
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFHIRImportJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatastoreId](#API_DescribeFHIRImportJob_RequestSyntax) **   <a name="HealthLake-DescribeFHIRImportJob-request-DatastoreId"></a>
The data store identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

 ** [JobId](#API_DescribeFHIRImportJob_RequestSyntax) **   <a name="HealthLake-DescribeFHIRImportJob-request-JobId"></a>
The import job identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

## Response Syntax
<a name="API_DescribeFHIRImportJob_ResponseSyntax"></a>

```
{
   "ImportJobProperties": {
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
}
```

## Response Elements
<a name="API_DescribeFHIRImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImportJobProperties](#API_DescribeFHIRImportJob_ResponseSyntax) **   <a name="HealthLake-DescribeFHIRImportJob-response-ImportJobProperties"></a>
The import job properties.
Type: [ImportJobProperties](API_ImportJobProperties.md) object

## Errors
<a name="API_DescribeFHIRImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeFHIRImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/DescribeFHIRImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/DescribeFHIRImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/DescribeFHIRImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/DescribeFHIRImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/DescribeFHIRImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/DescribeFHIRImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/DescribeFHIRImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/DescribeFHIRImportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DescribeFHIRImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/DescribeFHIRImportJob)
