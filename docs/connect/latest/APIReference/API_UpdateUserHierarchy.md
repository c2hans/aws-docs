---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserHierarchy.html
---

# UpdateUserHierarchy
<a name="API_UpdateUserHierarchy"></a>

Assigns the specified hierarchy group to the specified user.

## Request Syntax
<a name="API_UpdateUserHierarchy_RequestSyntax"></a>

```
POST /users/{{InstanceId}}/{{UserId}}/hierarchy HTTP/1.1
Content-type: application/json

{
   "HierarchyGroupId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateUserHierarchy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateUserHierarchy_RequestSyntax) **   <a name="connect-UpdateUserHierarchy-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_UpdateUserHierarchy_RequestSyntax) **   <a name="connect-UpdateUserHierarchy-request-uri-UserId"></a>
The identifier of the user account.
Required: Yes

## Request Body
<a name="API_UpdateUserHierarchy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [HierarchyGroupId](#API_UpdateUserHierarchy_RequestSyntax) **   <a name="connect-UpdateUserHierarchy-request-HierarchyGroupId"></a>
The identifier of the hierarchy group.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateUserHierarchy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateUserHierarchy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateUserHierarchy_Errors"></a>

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
<a name="API_UpdateUserHierarchy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateUserHierarchy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateUserHierarchy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateUserHierarchy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateUserHierarchy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateUserHierarchy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateUserHierarchy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateUserHierarchy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateUserHierarchy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateUserHierarchy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateUserHierarchy)
