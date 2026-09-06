---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDefaultQBusinessApplication.html
---

# UpdateDefaultQBusinessApplication
<a name="API_UpdateDefaultQBusinessApplication"></a>

Updates a Amazon Q Business application that is linked to a Quick Sight account.

## Request Syntax
<a name="API_UpdateDefaultQBusinessApplication_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/default-qbusiness-application?namespace={{Namespace}} HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDefaultQBusinessApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDefaultQBusinessApplication_RequestSyntax) **   <a name="QS-UpdateDefaultQBusinessApplication-request-uri-AwsAccountId"></a>
The ID of the Quick Sight account that is connected to the Amazon Q Business application that you want to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [Namespace](#API_UpdateDefaultQBusinessApplication_RequestSyntax) **   <a name="QS-UpdateDefaultQBusinessApplication-request-uri-Namespace"></a>
The Quick Sight namespace that contains the linked Amazon Q Business application. If this field is left blank, the default namespace is used. Currently, the default namespace is the only valid value for this parameter.
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`

## Request Body
<a name="API_UpdateDefaultQBusinessApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_UpdateDefaultQBusinessApplication_RequestSyntax) **   <a name="QS-UpdateDefaultQBusinessApplication-request-ApplicationId"></a>
The ID of the Amazon Q Business application that you want to update.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_UpdateDefaultQBusinessApplication_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateDefaultQBusinessApplication_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateDefaultQBusinessApplication_ResponseSyntax) **   <a name="QS-UpdateDefaultQBusinessApplication-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_UpdateDefaultQBusinessApplication_ResponseSyntax) **   <a name="QS-UpdateDefaultQBusinessApplication-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateDefaultQBusinessApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateDefaultQBusinessApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDefaultQBusinessApplication)
