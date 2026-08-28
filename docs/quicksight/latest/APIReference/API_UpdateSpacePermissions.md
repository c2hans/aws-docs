---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateSpacePermissions.html
---

# UpdateSpacePermissions
<a name="API_UpdateSpacePermissions"></a>

Updates the permissions for an Amazon QuickSight space.

## Request Syntax
<a name="API_UpdateSpacePermissions_RequestSyntax"></a>

```
PUT /v1/accounts/{{AwsAccountId}}/spaces/{{SpaceId}}/permissions HTTP/1.1
Content-type: application/json

{
   "GrantPermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "RevokePermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateSpacePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateSpacePermissions_RequestSyntax) **   <a name="QS-UpdateSpacePermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the space.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [SpaceId](#API_UpdateSpacePermissions_RequestSyntax) **   <a name="QS-UpdateSpacePermissions-request-uri-SpaceId"></a>
The ID of the space that you want to update permissions for.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

## Request Body
<a name="API_UpdateSpacePermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantPermissions](#API_UpdateSpacePermissions_RequestSyntax) **   <a name="QS-UpdateSpacePermissions-request-GrantPermissions"></a>
The permissions that you want to grant on the space.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

 ** [RevokePermissions](#API_UpdateSpacePermissions_RequestSyntax) **   <a name="QS-UpdateSpacePermissions-request-RevokePermissions"></a>
The permissions that you want to revoke from the space.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Required: No

## Response Syntax
<a name="API_UpdateSpacePermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "permissions": [
      {
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "requestId": "string",
   "spaceArn": "string",
   "spaceId": "string"
}
```

## Response Elements
<a name="API_UpdateSpacePermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [spaceId](#API_UpdateSpacePermissions_ResponseSyntax) **   <a name="QS-UpdateSpacePermissions-response-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z-_=.+]+`

 ** [permissions](#API_UpdateSpacePermissions_ResponseSyntax) **   <a name="QS-UpdateSpacePermissions-response-permissions"></a>
The updated permissions for the space.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.

 ** [requestId](#API_UpdateSpacePermissions_ResponseSyntax) **   <a name="QS-UpdateSpacePermissions-response-requestId"></a>
The AWS request ID for this operation.
Type: String

 ** [spaceArn](#API_UpdateSpacePermissions_ResponseSyntax) **   <a name="QS-UpdateSpacePermissions-response-spaceArn"></a>
The ARN of the space.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

## Errors
<a name="API_UpdateSpacePermissions_Errors"></a>

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

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

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

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateSpacePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateSpacePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateSpacePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateSpacePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateSpacePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateSpacePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateSpacePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateSpacePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateSpacePermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateSpacePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateSpacePermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
