---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetExportJobV2.html
---

# GetExportJobV2
<a name="API_GetExportJobV2"></a>

Returns the details of a single findings export job, including its current `Status`, the `Destination` it writes to, the `OutputConfiguration` it was started with, and its `StartedAt` and `EndedAt` timestamps. Use this operation to poll an export job that you started with `StartExportJobV2` until it reaches a terminal state (`SUCCEEDED`, `FAILED`, or `CANCELLED`).

If the job failed, the response includes a `FailureCode` and `FailureMessage` that describe the reason. Input values such as `Scopes` and `Filters` are echoed back as they were submitted, with relative date ranges returned unresolved. If no export job matches the `ExportJobId` that you provide, this operation returns a `ResourceNotFoundException`.

## Request Syntax
<a name="API_GetExportJobV2_RequestSyntax"></a>

```
GET /exportjobsv2/{{ExportJobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetExportJobV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExportJobId](#API_GetExportJobV2_RequestSyntax) **   <a name="securityhub-GetExportJobV2-request-uri-ExportJobId"></a>
The unique identifier of the export job to retrieve. This is the value returned by `StartExportJobV2`.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9]+$`
Required: Yes

## Request Body
<a name="API_GetExportJobV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetExportJobV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_GetExportJobV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataType](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-DataType"></a>
The category of data that the export job produces.
Type: String
Valid Values: `FINDINGS`

 ** [Destination](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-Destination"></a>
The destination that the export job writes to.
Type: [ExportDestination](API_ExportDestination.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [EndedAt](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-EndedAt"></a>
The time when the export job reached a terminal state (`SUCCEEDED`, `FAILED`, or `CANCELLED`). This parameter is absent while the job is `RUNNING`.
For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp

 ** [ExportJobId](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-ExportJobId"></a>
The unique identifier of the export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9]+$`

 ** [FailureCode](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-FailureCode"></a>
A code that classifies why the export job failed. Present only when `Status` is `FAILED`.
Type: String
Valid Values: `ACCESS_DENIED | RESOURCE_NOT_FOUND | INTERNAL_ERROR`

 ** [FailureMessage](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-FailureMessage"></a>
A human-readable message that provides more detail about why the export job failed. Present only when `Status` is `FAILED`.
Type: String
Pattern: `.*\S.*`

 ** [Name](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-Name"></a>
The user-provided name of the export job, if one was specified when the job was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [OutputConfiguration](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-OutputConfiguration"></a>
The output configuration that the export job was started with, including the format and any filters or selected fields.
Type: [ExportOutput](API_ExportOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Scopes](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-Scopes"></a>
The organization scopes that the export job was started with, echoed verbatim. This parameter is absent if the caller didn't supply `Scopes`. It contains only the organization or organizational unit (OU) identifiers that the caller submitted; it never contains resolved member-account identifiers.
Type: [ExportScopes](API_ExportScopes.md) object

 ** [StartedAt](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-StartedAt"></a>
The time when the export job was created.
For more information about the validation and formatting of timestamp fields in Security Hub, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp

 ** [Status](#API_GetExportJobV2_ResponseSyntax) **   <a name="securityhub-GetExportJobV2-response-Status"></a>
The current state of the export job.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | CANCELLED`

## Errors
<a name="API_GetExportJobV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_GetExportJobV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetExportJobV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetExportJobV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetExportJobV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetExportJobV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetExportJobV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetExportJobV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetExportJobV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetExportJobV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetExportJobV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetExportJobV2)
