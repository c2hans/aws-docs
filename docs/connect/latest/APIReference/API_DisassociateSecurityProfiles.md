---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateSecurityProfiles.html
---

# DisassociateSecurityProfiles
<a name="API_DisassociateSecurityProfiles"></a>

 Disassociates a security profile attached to a Q in Connect AI Agent Entity in an Amazon Connect instance.

## Request Syntax
<a name="API_DisassociateSecurityProfiles_RequestSyntax"></a>

```
POST /disassociate-security-profiles/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "EntityArn": "{{string}}",
   "EntityType": "{{string}}",
   "SecurityProfiles": [
      {
         "Id": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_DisassociateSecurityProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DisassociateSecurityProfiles_RequestSyntax) **   <a name="connect-DisassociateSecurityProfiles-request-uri-InstanceId"></a>
 The identifier of the Amazon Connect instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DisassociateSecurityProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EntityArn](#API_DisassociateSecurityProfiles_RequestSyntax) **   <a name="connect-DisassociateSecurityProfiles-request-EntityArn"></a>
 ARN of a Q in Connect AI Agent.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [EntityType](#API_DisassociateSecurityProfiles_RequestSyntax) **   <a name="connect-DisassociateSecurityProfiles-request-EntityType"></a>
 Only supported type is AI\_AGENT.
Type: String
Valid Values: `USER | AI_AGENT`
Required: Yes

 ** [SecurityProfiles](#API_DisassociateSecurityProfiles_RequestSyntax) **   <a name="connect-DisassociateSecurityProfiles-request-SecurityProfiles"></a>
 List of Security Profile Object.
Type: Array of [SecurityProfileItem](API_SecurityProfileItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_DisassociateSecurityProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateSecurityProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateSecurityProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConditionalOperationFailedException **
Request processing failed because dependent condition failed.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_DisassociateSecurityProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DisassociateSecurityProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DisassociateSecurityProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DisassociateSecurityProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DisassociateSecurityProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DisassociateSecurityProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DisassociateSecurityProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DisassociateSecurityProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DisassociateSecurityProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DisassociateSecurityProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DisassociateSecurityProfiles)
