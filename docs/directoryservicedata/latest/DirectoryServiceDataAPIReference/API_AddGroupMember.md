---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_AddGroupMember.html
---

# AddGroupMember
<a name="API_AddGroupMember"></a>

Adds an existing user, group, or computer as a group member.

## Request Syntax
<a name="API_AddGroupMember_RequestSyntax"></a>

```
POST /GroupMemberships/AddGroupMember?DirectoryId={{DirectoryId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "GroupName": "{{string}}",
   "MemberName": "{{string}}",
   "MemberRealm": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AddGroupMember_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DirectoryId](#API_AddGroupMember_RequestSyntax) **   <a name="directoryservicedata-AddGroupMember-request-uri-DirectoryId"></a>
 The identifier (ID) of the directory that's associated with the group.
Pattern: `d-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_AddGroupMember_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_AddGroupMember_RequestSyntax) **   <a name="directoryservicedata-AddGroupMember-request-ClientToken"></a>
 A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call.
 A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours.
 If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an `ConflictException`.
 This parameter is optional when using the AWS CLI or SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x00-\x7F]+`
Required: No

 ** [GroupName](#API_AddGroupMember_RequestSyntax) **   <a name="directoryservicedata-AddGroupMember-request-GroupName"></a>
 The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^:;|=+"*?<>/\\,\[\]@]+`
Required: Yes

 ** [MemberName](#API_AddGroupMember_RequestSyntax) **   <a name="directoryservicedata-AddGroupMember-request-MemberName"></a>
 The `SAMAccountName` of the user, group, or computer to add as a group member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[^:;|=+"*?<>/\\,\[\]@]+`
Required: Yes

 ** [MemberRealm](#API_AddGroupMember_RequestSyntax) **   <a name="directoryservicedata-AddGroupMember-request-MemberRealm"></a>
 The domain name that's associated with the group member. This parameter is required only when adding a member outside of your AWS Managed Microsoft AD domain to a group inside of your AWS Managed Microsoft AD domain. This parameter defaults to the AWS Managed Microsoft AD domain.
 This parameter is case insensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`
Required: No

## Response Syntax
<a name="API_AddGroupMember_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AddGroupMember_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddGroupMember_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permission to perform the request or access the directory. It can also occur when the `DirectoryId` doesn't exist or the user, member, or group might be outside of your organizational unit (OU).
 Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU.
 ** Reason **
 Reason the request was unauthorized.
HTTP Status Code: 403

 ** ConflictException **
 This error will occur when you try to create a resource that conflicts with an existing object. It can also occur when adding a member to a group that the member is already in.
 This error can be caused by a request sent within the 8-hour idempotency window with the same client token but different input parameters. Client tokens should not be re-used across different requests. After 8 hours, any request with the same client token is treated as a new request.
HTTP Status Code: 409

 ** DirectoryUnavailableException **
 The request could not be completed due to a problem in the configuration or current state of the specified directory.
 ** Reason **
 Reason the request failed for the specified directory.
HTTP Status Code: 400

 ** InternalServerException **
 The operation didn't succeed because an internal error occurred. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second has been exceeded.
 ** RetryAfterSeconds **
 The recommended amount of seconds to retry after a throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 The request isn't valid. Review the details in the error message to update the invalid parameters or values in your request.
 ** Reason **
 Reason the request failed validation.
HTTP Status Code: 400

## Examples
<a name="API_AddGroupMember_Examples"></a>

### Example
<a name="API_AddGroupMember_Example_1"></a>

This example illustrates one usage of AddGroupMember.

#### Sample Request
<a name="API_AddGroupMember_Example_1_Request"></a>

```
{
  "ClientToken": "550e8400-e29b-41d4-a716-446655440000",
  "GroupName": "GRP_MKTG",
  "MemberName": "Pat Candella",
  "MemberRealm": "europe.example.com"
}
```

#### Sample Response
<a name="API_AddGroupMember_Example_1_Response"></a>

```
HTTP/1.1 200
```

## See Also
<a name="API_AddGroupMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directory-service-data-2023-05-31/AddGroupMember)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directory-service-data-2023-05-31/AddGroupMember)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/AddGroupMember)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directory-service-data-2023-05-31/AddGroupMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/AddGroupMember)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directory-service-data-2023-05-31/AddGroupMember)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directory-service-data-2023-05-31/AddGroupMember)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directory-service-data-2023-05-31/AddGroupMember)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directory-service-data-2023-05-31/AddGroupMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/AddGroupMember)
