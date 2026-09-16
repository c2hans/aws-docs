---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCisScanReport.html
---

# GetCisScanReport
<a name="API_GetCisScanReport"></a>

Retrieves a CIS scan report.

## Request Syntax
<a name="API_GetCisScanReport_RequestSyntax"></a>

```
POST /cis/scan/report/get HTTP/1.1
Content-type: application/json

{
   "reportFormat": "{{string}}",
   "scanArn": "{{string}}",
   "targetAccounts": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetCisScanReport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetCisScanReport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [reportFormat](#API_GetCisScanReport_RequestSyntax) **   <a name="inspector2-GetCisScanReport-request-reportFormat"></a>
 The format of the report. Valid values are `PDF` and `CSV`. If no value is specified, the report format defaults to `PDF`.
Type: String
Valid Values: `PDF | CSV`
Required: No

 ** [scanArn](#API_GetCisScanReport_RequestSyntax) **   <a name="inspector2-GetCisScanReport-request-scanArn"></a>
The scan ARN.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/cis-scan/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [targetAccounts](#API_GetCisScanReport_RequestSyntax) **   <a name="inspector2-GetCisScanReport-request-targetAccounts"></a>
The target accounts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## Response Syntax
<a name="API_GetCisScanReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string",
   "url": "string"
}
```

## Response Elements
<a name="API_GetCisScanReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_GetCisScanReport_ResponseSyntax) **   <a name="inspector2-GetCisScanReport-response-status"></a>
The status.
Type: String
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`

 ** [url](#API_GetCisScanReport_ResponseSyntax) **   <a name="inspector2-GetCisScanReport-response-url"></a>
 The URL where a PDF or CSV of the CIS scan report can be downloaded.
Type: String

## Errors
<a name="API_GetCisScanReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetCisScanReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetCisScanReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetCisScanReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetCisScanReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetCisScanReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetCisScanReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetCisScanReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetCisScanReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetCisScanReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetCisScanReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetCisScanReport)
