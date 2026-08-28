---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_UpdateGroup.html
---

# UpdateGroup
<a name="API_UpdateGroup"></a>

 Updates group information.

## Request Syntax
<a name="API_UpdateGroup_RequestSyntax"></a>

```
POST /Groups/UpdateGroup?DirectoryId={{DirectoryId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "GroupScope": "{{string}}",
   "GroupType": "{{string}}",
   "OtherAttributes": {
      "{{string}}" : { ... }
   },
   "SAMAccountName": "{{string}}",
   "UpdateType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DirectoryId](#API_UpdateGroup_RequestSyntax) **   <a name="directoryservicedata-UpdateGroup-request-uri-DirectoryId"></a>
 The identifier (ID) of the directory that's associated with the group.
Pattern: `d-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_UpdateGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateGroup_RequestSyntax) **   <a name="directoryservicedata-UpdateGroup-request-ClientToken"></a>
 A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call.
 A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours.
 If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an `ConflictException`.
 This parameter is optional when using the AWS CLI or SDK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x00-\x7F]+`
Required: No

 ** [GroupScope](#API_UpdateGroup_RequestSyntax) **   <a name="directoryservicedata-UpdateGroup-request-GroupScope"></a>
 The scope of the AD group. For details, see [Active Directory security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope).
Type: String
Valid Values: `DomainLocal | Global | Universal | BuiltinLocal`
Required: No

 ** [GroupType](#API_UpdateGroup_RequestSyntax) **   <a name="directoryservicedata-UpdateGroup-request-GroupType"></a>
 The AD group type. For details, see [Active Directory security group type](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work).
Type: String
Valid Values: `Distribution | Security`
Required: No

 ** [OtherAttributes](#API_UpdateGroup_RequestSyntax) **   <a name="directoryservicedata-UpdateGroup-request-OtherAttributes"></a>
 An expression that defines one or more attributes with the data type and the value of each attribute.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Map Entries: Maximum number of 25 items.
Key Length Constraints: Minimum length of 1. Maximum length of 63.
Key Pattern: `[A-Za-z*][A-Za-z-*]*`
Required: No

 ** [SAMAccountName](#API_UpdateGroup_RequestSyntax) **   <a name="directoryservicedata-UpdateGroup-request-SAMAccountName"></a>
 The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^:;|=+"*?<>/\\,\[\]@]+`
Required: Yes

 ** [UpdateType](#API_UpdateGroup_RequestSyntax) **   <a name="directoryservicedata-UpdateGroup-request-UpdateType"></a>
 The type of update to be performed. If no value exists for the attribute, use `ADD`. Otherwise, use `REPLACE` to change an attribute value or `REMOVE` to clear the attribute value.
Type: String
Valid Values: `ADD | REPLACE | REMOVE`
Required: No

## Response Syntax
<a name="API_UpdateGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateGroup_Errors"></a>

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
<a name="API_UpdateGroup_Examples"></a>

### Example
<a name="API_UpdateGroup_Example_1"></a>

This example illustrates one usage of UpdateGroup.

#### Sample Request
<a name="API_UpdateGroup_Example_1_Request"></a>

```
{
  "ClientToken": "550e8400-e29b-41d4-a716-446655440000",
  "GroupScope": "Global",
  "GroupType": "Security",
  "OtherAttributes":
  {
    "PreferredLanguage":{"S":"English"},
    "Co":{"S":"US"}
  },
  "SAMAccountName": "GuestsLocal",
  "UpdateType": "REPLACE"
}
```

#### Sample Response
<a name="API_UpdateGroup_Example_1_Response"></a>

```
{
  "DirectoryId": "112233abcd",
  "SAMAccountName": "GuestsLocal",
  "SID": "S-1-5-44-567"
}
```

## See Also
<a name="API_UpdateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directory-service-data-2023-05-31/UpdateGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directory-service-data-2023-05-31/UpdateGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/UpdateGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directory-service-data-2023-05-31/UpdateGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/UpdateGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directory-service-data-2023-05-31/UpdateGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directory-service-data-2023-05-31/UpdateGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directory-service-data-2023-05-31/UpdateGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directory-service-data-2023-05-31/UpdateGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/UpdateGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service Data. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservicedata` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
