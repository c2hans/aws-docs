---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateUserProficiencies.html
---

# AssociateUserProficiencies
<a name="API_AssociateUserProficiencies"></a>

Associates a set of proficiencies with a user.

## Request Syntax
<a name="API_AssociateUserProficiencies_RequestSyntax"></a>

```
POST /users/{{InstanceId}}/{{UserId}}/associate-proficiencies HTTP/1.1
Content-type: application/json

{
   "UserProficiencies": [
      {
         "AttributeName": "{{string}}",
         "AttributeValue": "{{string}}",
         "Level": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_AssociateUserProficiencies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_AssociateUserProficiencies_RequestSyntax) **   <a name="connect-AssociateUserProficiencies-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN of the instance).
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_AssociateUserProficiencies_RequestSyntax) **   <a name="connect-AssociateUserProficiencies-request-uri-UserId"></a>
The identifier of the user account.
Required: Yes

## Request Body
<a name="API_AssociateUserProficiencies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [UserProficiencies](#API_AssociateUserProficiencies_RequestSyntax) **   <a name="connect-AssociateUserProficiencies-request-UserProficiencies"></a>
The proficiencies to associate with the user.
Type: Array of [UserProficiency](API_UserProficiency.md) objects
Required: Yes

## Response Syntax
<a name="API_AssociateUserProficiencies_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateUserProficiencies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateUserProficiencies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_AssociateUserProficiencies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateUserProficiencies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateUserProficiencies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateUserProficiencies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateUserProficiencies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateUserProficiencies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateUserProficiencies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateUserProficiencies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateUserProficiencies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateUserProficiencies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateUserProficiencies)
