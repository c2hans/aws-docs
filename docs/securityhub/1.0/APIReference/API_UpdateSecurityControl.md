---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateSecurityControl.html
---

# UpdateSecurityControl
<a name="API_UpdateSecurityControl"></a>

 Updates the properties of a security control.

## Request Syntax
<a name="API_UpdateSecurityControl_RequestSyntax"></a>

```
PATCH /securityControl/update HTTP/1.1
Content-type: application/json

{
   "LastUpdateReason": "{{string}}",
   "Parameters": {
      "{{string}}" : {
         "Value": { ... },
         "ValueType": "{{string}}"
      }
   },
   "SecurityControlId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSecurityControl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateSecurityControl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LastUpdateReason](#API_UpdateSecurityControl_RequestSyntax) **   <a name="securityhub-UpdateSecurityControl-request-LastUpdateReason"></a>
 The most recent reason for updating the properties of the security control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.
Type: String
Pattern: `^([^\u0000-\u007F]|[-_ a-zA-Z0-9])+$`
Required: No

 ** [Parameters](#API_UpdateSecurityControl_RequestSyntax) **   <a name="securityhub-UpdateSecurityControl-request-Parameters"></a>
 An object that specifies which security control parameters to update.
Type: String to [ParameterConfiguration](API_ParameterConfiguration.md) object map
Key Pattern: `.*\S.*`
Required: Yes

 ** [SecurityControlId](#API_UpdateSecurityControl_RequestSyntax) **   <a name="securityhub-UpdateSecurityControl-request-SecurityControlId"></a>
 The Amazon Resource Name (ARN) or ID of the control to update.
Type: String
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_UpdateSecurityControl_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateSecurityControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateSecurityControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceInUseException **
 The request was rejected because it conflicts with the resource's availability. For example, you tried to update a security control that's currently in the `UPDATING` state.
HTTP Status Code: 400

 ** ResourceInUseException **
 The request was rejected because it conflicts with the resource's availability. For example, you tried to update a security control that's currently in the `UPDATING` state.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_UpdateSecurityControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateSecurityControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateSecurityControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateSecurityControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateSecurityControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateSecurityControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateSecurityControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateSecurityControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateSecurityControl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateSecurityControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateSecurityControl)
