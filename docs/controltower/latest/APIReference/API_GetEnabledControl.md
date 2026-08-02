---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetEnabledControl.html
---

# GetEnabledControl
<a name="API_GetEnabledControl"></a>

Retrieves details about an enabled control. For usage examples, see the [https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html](https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html).

## Request Syntax
<a name="API_GetEnabledControl_RequestSyntax"></a>

```
POST /get-enabled-control HTTP/1.1
Content-type: application/json

{
   "enabledControlIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetEnabledControl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEnabledControl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [enabledControlIdentifier](#API_GetEnabledControl_RequestSyntax) **   <a name="controltower-GetEnabledControl-request-enabledControlIdentifier"></a>
The `controlIdentifier` of the enabled control.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: Yes

## Response Syntax
<a name="API_GetEnabledControl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "enabledControlDetails": {
      "arn": "string",
      "controlIdentifier": "string",
      "driftStatusSummary": {
         "driftStatus": "string",
         "types": {
            "inheritance": {
               "status": "string"
            },
            "resource": {
               "status": "string"
            }
         }
      },
      "parameters": [
         {
            "key": "string",
            "value": JSON value
         }
      ],
      "parentIdentifier": "string",
      "statusSummary": {
         "lastOperationIdentifier": "string",
         "status": "string"
      },
      "targetIdentifier": "string",
      "targetRegions": [
         {
            "name": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetEnabledControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [enabledControlDetails](#API_GetEnabledControl_ResponseSyntax) **   <a name="controltower-GetEnabledControl-response-enabledControlDetails"></a>
Information about the enabled control.
Type: [EnabledControlDetails](API_EnabledControlDetails.md) object

## Errors
<a name="API_GetEnabledControl_Errors"></a>

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
<a name="API_GetEnabledControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/GetEnabledControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/GetEnabledControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/GetEnabledControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/GetEnabledControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/GetEnabledControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/GetEnabledControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/GetEnabledControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/GetEnabledControl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/GetEnabledControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/GetEnabledControl)
