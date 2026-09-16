---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateActionTarget.html
---

# UpdateActionTarget
<a name="API_UpdateActionTarget"></a>

Updates the name and description of a custom action target in Security Hub CSPM.

## Request Syntax
<a name="API_UpdateActionTarget_RequestSyntax"></a>

```
PATCH /actionTargets/{{ActionTargetArn+}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateActionTarget_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ActionTargetArn](#API_UpdateActionTarget_RequestSyntax) **   <a name="securityhub-UpdateActionTarget-request-uri-ActionTargetArn"></a>
The ARN of the custom action target to update.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdateActionTarget_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateActionTarget_RequestSyntax) **   <a name="securityhub-UpdateActionTarget-request-Description"></a>
The updated description for the custom action target.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [Name](#API_UpdateActionTarget_RequestSyntax) **   <a name="securityhub-UpdateActionTarget-request-Name"></a>
The updated name of the custom action target.
Type: String
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_UpdateActionTarget_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateActionTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateActionTarget_Errors"></a>

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

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_UpdateActionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateActionTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateActionTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateActionTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateActionTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateActionTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateActionTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateActionTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateActionTarget)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateActionTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateActionTarget)
