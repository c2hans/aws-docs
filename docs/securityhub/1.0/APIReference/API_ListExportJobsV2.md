---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListExportJobsV2.html
---

# ListExportJobsV2
<a name="API_ListExportJobsV2"></a>

Returns the findings export jobs in your account as a paginated list of `ExportSummary` objects. You can filter the results by job `Status` or `DataType`.

To page through the results, use the `MaxResults` and `NextToken` parameters. If the response includes a `NextToken` value, pass it in a subsequent request to retrieve the next page of results.

Each `ExportSummary` reports the output `Format` of the job but not its full `OutputConfiguration`. To retrieve the filters and selected fields that a job was started with, call `GetExportJobV2`.

## Request Syntax
<a name="API_ListExportJobsV2_RequestSyntax"></a>

```
GET /exportjobsv2?DataType={{DataType}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&Status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListExportJobsV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataType](#API_ListExportJobsV2_RequestSyntax) **   <a name="securityhub-ListExportJobsV2-request-uri-DataType"></a>
Filters the results to export jobs that produce the specified data type.
Valid Values: `FINDINGS`

 ** [MaxResults](#API_ListExportJobsV2_RequestSyntax) **   <a name="securityhub-ListExportJobsV2-request-uri-MaxResults"></a>
The maximum number of results to return in a single call. Valid range is 1–20.
Valid Range: Minimum value of 1. Maximum value of 20.

 ** [NextToken](#API_ListExportJobsV2_RequestSyntax) **   <a name="securityhub-ListExportJobsV2-request-uri-NextToken"></a>
The token required for pagination. On your first call, set the value of this parameter to `NULL`. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.

 ** [Status](#API_ListExportJobsV2_RequestSyntax) **   <a name="securityhub-ListExportJobsV2-request-uri-Status"></a>
Filters the results to export jobs that have the specified status.
Valid Values: `RUNNING | SUCCEEDED | FAILED | CANCELLED`

## Request Body
<a name="API_ListExportJobsV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListExportJobsV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "DataType": "string",
         "Destination": { ... },
         "EndedAt": "string",
         "ExportJobId": "string",
         "FailureCode": "string",
         "FailureMessage": "string",
         "Name": "string",
         "OutputConfiguration": { ... },
         "Scopes": {
            "AwsOrganizations": [
               {
                  "OrganizationalUnitId": "string",
                  "OrganizationId": "string"
               }
            ]
         },
         "StartedAt": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListExportJobsV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListExportJobsV2_ResponseSyntax) **   <a name="securityhub-ListExportJobsV2-response-Items"></a>
The export jobs that match the request, as `ExportSummary` objects.
Type: Array of [ExportSummary](API_ExportSummary.md) objects

 ** [NextToken](#API_ListExportJobsV2_ResponseSyntax) **   <a name="securityhub-ListExportJobsV2-response-NextToken"></a>
The pagination token to use to request the next page of results. Otherwise, this parameter is null.
Type: String

## Errors
<a name="API_ListExportJobsV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_ListExportJobsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListExportJobsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListExportJobsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListExportJobsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListExportJobsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListExportJobsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListExportJobsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListExportJobsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListExportJobsV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListExportJobsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListExportJobsV2)
