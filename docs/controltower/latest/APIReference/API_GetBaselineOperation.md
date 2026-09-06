---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaselineOperation.html
---

# GetBaselineOperation
<a name="API_GetBaselineOperation"></a>

Returns the details of an asynchronous baseline operation, as initiated by any of these APIs: `EnableBaseline`, `DisableBaseline`, `UpdateEnabledBaseline`, `ResetEnabledBaseline`. A status message is displayed in case of operation failure. For usage examples, see [*the AWS Control Tower User Guide*](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html).

## Request Syntax
<a name="API_GetBaselineOperation_RequestSyntax"></a>

```
POST /get-baseline-operation HTTP/1.1
Content-type: application/json

{
   "operationIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetBaselineOperation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetBaselineOperation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [operationIdentifier](#API_GetBaselineOperation_RequestSyntax) **   <a name="controltower-GetBaselineOperation-request-operationIdentifier"></a>
The operation ID returned from mutating asynchronous APIs (Enable, Disable, Update, Reset).
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_GetBaselineOperation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "baselineOperation": {
      "endTime": "string",
      "operationIdentifier": "string",
      "operationType": "string",
      "startTime": "string",
      "status": "string",
      "statusMessage": "string"
   }
}
```

## Response Elements
<a name="API_GetBaselineOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [baselineOperation](#API_GetBaselineOperation_ResponseSyntax) **   <a name="controltower-GetBaselineOperation-response-baselineOperation"></a>
A `baselineOperation` object that shows information about the specified operation ID.
Type: [BaselineOperation](API_BaselineOperation.md) object

## Errors
<a name="API_GetBaselineOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetBaselineOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/GetBaselineOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/GetBaselineOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/GetBaselineOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/GetBaselineOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/GetBaselineOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/GetBaselineOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/GetBaselineOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/GetBaselineOperation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/GetBaselineOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/GetBaselineOperation)
