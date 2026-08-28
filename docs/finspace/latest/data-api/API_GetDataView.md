---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_GetDataView.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# GetDataView
<a name="API_GetDataView"></a>

Gets information about a Dataview.

## Request Syntax
<a name="API_GetDataView_RequestSyntax"></a>

```
GET /datasets/{{datasetId}}/dataviewsv2/{{dataviewId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataView_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_GetDataView_RequestSyntax) **   <a name="finspace-GetDataView-request-uri-datasetId"></a>
The unique identifier for the Dataset used in the Dataview.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

 ** [dataviewId](#API_GetDataView_RequestSyntax) **   <a name="finspace-GetDataView-request-uri-dataViewId"></a>
The unique identifier for the Dataview.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

## Request Body
<a name="API_GetDataView_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "asOfTimestamp": number,
   "autoUpdate": boolean,
   "createTime": number,
   "datasetId": "string",
   "dataViewArn": "string",
   "dataViewId": "string",
   "destinationTypeParams": {
      "destinationType": "string",
      "s3DestinationExportFileFormat": "string",
      "s3DestinationExportFileFormatOptions": {
         "string" : "string"
      }
   },
   "errorInfo": {
      "errorCategory": "string",
      "errorMessage": "string"
   },
   "lastModifiedTime": number,
   "partitionColumns": [ "string" ],
   "sortColumns": [ "string" ],
   "status": "string"
}
```

## Response Elements
<a name="API_GetDataView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [asOfTimestamp](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-asOfTimestamp"></a>
Time range to use for the Dataview. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long

 ** [autoUpdate](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-autoUpdate"></a>
Flag to indicate Dataview should be updated automatically.
Type: Boolean

 ** [createTime](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-createTime"></a>
The timestamp at which the Dataview was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long

 ** [datasetId](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-datasetId"></a>
The unique identifier for the Dataset used in the Dataview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

 ** [dataViewArn](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-dataViewArn"></a>
The ARN identifier of the Dataview.
Type: String

 ** [dataViewId](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-dataViewId"></a>
The unique identifier for the Dataview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

 ** [destinationTypeParams](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-destinationTypeParams"></a>
Options that define the destination type for the Dataview.
Type: [DataViewDestinationTypeParams](API_DataViewDestinationTypeParams.md) object

 ** [errorInfo](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-errorInfo"></a>
Information about an error that occurred for the Dataview.
Type: [DataViewErrorInfo](API_DataViewErrorInfo.md) object

 ** [lastModifiedTime](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-lastModifiedTime"></a>
The last time that a Dataview was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long

 ** [partitionColumns](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-partitionColumns"></a>
Ordered set of column names used to partition data.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`

 ** [sortColumns](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-sortColumns"></a>
Columns to be used for sorting the data.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`

 ** [status](#API_GetDataView_ResponseSyntax) **   <a name="finspace-GetDataView-response-status"></a>
The status of a Dataview creation.
+  `RUNNING` – Dataview creation is running.
+  `STARTING` – Dataview creation is starting.
+  `FAILED` – Dataview creation has failed.
+  `CANCELLED` – Dataview creation has been cancelled.
+  `TIMEOUT` – Dataview creation has timed out.
+  `SUCCESS` – Dataview creation has succeeded.
+  `PENDING` – Dataview creation is pending.
+  `FAILED_CLEANUP_FAILED` – Dataview creation failed and resource cleanup failed.
Type: String
Valid Values: `RUNNING | STARTING | FAILED | CANCELLED | TIMEOUT | SUCCESS | PENDING | FAILED_CLEANUP_FAILED`

## Errors
<a name="API_GetDataView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request conflicts with an existing resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetDataView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/GetDataView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/GetDataView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/GetDataView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/GetDataView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/GetDataView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/GetDataView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/GetDataView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/GetDataView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/GetDataView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/GetDataView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
