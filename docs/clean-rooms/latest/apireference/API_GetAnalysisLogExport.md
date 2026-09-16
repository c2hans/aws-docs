---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetAnalysisLogExport.html
---

# GetAnalysisLogExport
<a name="API_GetAnalysisLogExport"></a>

Returns information about an analysis log export, including its current status and, if the export failed, the reason for the failure.

Poll this operation until the `status` is `SUCCESS` or `FAILED`. An export can't be canceled after it starts.

## Request Syntax
<a name="API_GetAnalysisLogExport_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/analysislogexports/{{analysisLogExportIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAnalysisLogExport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analysisLogExportIdentifier](#API_GetAnalysisLogExport_RequestSyntax) **   <a name="API-GetAnalysisLogExport-request-uri-analysisLogExportIdentifier"></a>
The unique identifier of the analysis log export to retrieve.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_GetAnalysisLogExport_RequestSyntax) **   <a name="API-GetAnalysisLogExport-request-uri-membershipIdentifier"></a>
A unique identifier for the membership that the analysis log export belongs to. Currently accepts the membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetAnalysisLogExport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAnalysisLogExport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analysisLogExport": {
      "analysisId": "string",
      "analysisLogExportId": "string",
      "analysisType": "string",
      "createTime": number,
      "error": {
         "code": "string",
         "message": "string"
      },
      "membershipId": "string",
      "resultConfiguration": {
         "outputConfiguration": {
            "s3": {
               "bucket": "string",
               "keyPrefix": "string"
            }
         }
      },
      "status": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_GetAnalysisLogExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisLogExport](#API_GetAnalysisLogExport_ResponseSyntax) **   <a name="API-GetAnalysisLogExport-response-analysisLogExport"></a>
The analysis log export processing metadata.
Type: [AnalysisLogExport](API_AnalysisLogExport.md) object

## Errors
<a name="API_GetAnalysisLogExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetAnalysisLogExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/GetAnalysisLogExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/GetAnalysisLogExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/GetAnalysisLogExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/GetAnalysisLogExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/GetAnalysisLogExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/GetAnalysisLogExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/GetAnalysisLogExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/GetAnalysisLogExport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/GetAnalysisLogExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/GetAnalysisLogExport)
