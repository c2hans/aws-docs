---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteLaunchAction.html
---

# DeleteLaunchAction
<a name="API_DeleteLaunchAction"></a>

Deletes a resource launch action.

## Request Syntax
<a name="API_DeleteLaunchAction_RequestSyntax"></a>

```
POST /DeleteLaunchAction HTTP/1.1
Content-type: application/json

{
   "actionId": "{{string}}",
   "resourceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteLaunchAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteLaunchAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionId](#API_DeleteLaunchAction_RequestSyntax) **   <a name="drs-DeleteLaunchAction-request-actionId"></a>
Launch action Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [resourceId](#API_DeleteLaunchAction_RequestSyntax) **   <a name="drs-DeleteLaunchAction-request-resourceId"></a>
Launch configuration template Id or Source Server Id
Type: String
Pattern: `(s-[0-9a-zA-Z]{17}$|lct-[0-9a-zA-Z]{17})`
Required: Yes

## Response Syntax
<a name="API_DeleteLaunchAction_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteLaunchAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteLaunchAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DeleteLaunchAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DeleteLaunchAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DeleteLaunchAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DeleteLaunchAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DeleteLaunchAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DeleteLaunchAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DeleteLaunchAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DeleteLaunchAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DeleteLaunchAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DeleteLaunchAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DeleteLaunchAction)
