---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteActionTarget.html
---

# DeleteActionTarget
<a name="API_DeleteActionTarget"></a>

Deletes a custom action target from Security Hub CSPM.

Deleting a custom action target does not affect any findings or insights that were already sent to Amazon CloudWatch Events using the custom action.

## Request Syntax
<a name="API_DeleteActionTarget_RequestSyntax"></a>

```
DELETE /actionTargets/{{ActionTargetArn+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteActionTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ActionTargetArn](#API_DeleteActionTarget_RequestSyntax) **   <a name="securityhub-DeleteActionTarget-request-uri-ActionTargetArn"></a>
The Amazon Resource Name (ARN) of the custom action target to delete.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_DeleteActionTarget_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteActionTarget_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ActionTargetArn": "string"
}
```

## Response Elements
<a name="API_DeleteActionTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActionTargetArn](#API_DeleteActionTarget_ResponseSyntax) **   <a name="securityhub-DeleteActionTarget-response-ActionTargetArn"></a>
The ARN of the custom action target that was deleted.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_DeleteActionTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_DeleteActionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DeleteActionTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DeleteActionTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DeleteActionTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DeleteActionTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DeleteActionTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DeleteActionTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DeleteActionTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DeleteActionTarget)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DeleteActionTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DeleteActionTarget)
