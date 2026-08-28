---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteUser.html
---

# DeleteUser
<a name="API_DeleteUser"></a>

Deletes a user account from the specified Connect Customer instance.

For information about what happens to a user's data when their account is deleted, see [Delete Users from Your Connect Customer Instance](https://docs.aws.amazon.com/connect/latest/adminguide/delete-users.html) in the *Connect Customer Administrator Guide*.

**Important**
After calling DeleteUser, call [DeleteQuickConnect](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteQuickConnect.html) to delete any records related to the deleted users. This will help you:
Avoid dangling resources that impact your service quotas.
Remove deleted users so they don't appear to agents as transfer options.
Avoid the disruption of other Connect Customer processes, such as instance replication and syncing if you're using [Connect Customer Global Resiliency](https://docs.aws.amazon.com/connect/latest/adminguide/setup-connect-global-resiliency.html).

## Request Syntax
<a name="API_DeleteUser_RequestSyntax"></a>

```
DELETE /users/{{InstanceId}}/{{UserId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DeleteUser_RequestSyntax) **   <a name="connect-DeleteUser-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_DeleteUser_RequestSyntax) **   <a name="connect-DeleteUser-request-uri-UserId"></a>
The identifier of the user.
Required: Yes

## Request Body
<a name="API_DeleteUser_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteUser_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteUser_Errors"></a>

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
<a name="API_DeleteUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DeleteUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DeleteUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DeleteUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DeleteUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DeleteUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DeleteUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DeleteUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DeleteUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DeleteUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DeleteUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
