---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroupMembers.html
---

# ListGroupMembers
<a name="API_ListGroupMembers"></a>

 Returns member information for the specified group.

 This operation supports pagination with the use of the `NextToken` request and response parameters. If more results are available, the `ListGroupMembers.NextToken` member contains a token that you pass in the next call to `ListGroupMembers`. This retrieves the next set of items.

 You can also specify a maximum number of return results with the `MaxResults` parameter.

## Request Syntax
<a name="API_ListGroupMembers_RequestSyntax"></a>

```
POST /GroupMemberships/ListGroupMembers?DirectoryId={{DirectoryId}} HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "MemberRealm": "{{string}}",
   "NextToken": "{{string}}",
   "Realm": "{{string}}",
   "SAMAccountName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListGroupMembers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DirectoryId](#API_ListGroupMembers_RequestSyntax) **   <a name="directoryservicedata-ListGroupMembers-request-uri-DirectoryId"></a>
 The identifier (ID) of the directory that's associated with the group.
Pattern: `d-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_ListGroupMembers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListGroupMembers_RequestSyntax) **   <a name="directoryservicedata-ListGroupMembers-request-MaxResults"></a>
 The maximum number of results to be returned per request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

 ** [MemberRealm](#API_ListGroupMembers_RequestSyntax) **   <a name="directoryservicedata-ListGroupMembers-request-MemberRealm"></a>
 The domain name that's associated with the group member. This parameter defaults to the AWS Managed Microsoft AD domain.
 This parameter is optional and case insensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`
Required: No

 ** [NextToken](#API_ListGroupMembers_RequestSyntax) **   <a name="directoryservicedata-ListGroupMembers-request-NextToken"></a>
An encoded paging token for paginated calls that can be passed back to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: No

 ** [Realm](#API_ListGroupMembers_RequestSyntax) **   <a name="directoryservicedata-ListGroupMembers-request-Realm"></a>
 The domain name that's associated with the group.
 This parameter is optional, so you can return members from a group outside of your AWS Managed Microsoft AD domain. When no value is defined, only members of your AWS Managed Microsoft AD groups are returned.
 This value is case insensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`
Required: No

 ** [SAMAccountName](#API_ListGroupMembers_RequestSyntax) **   <a name="directoryservicedata-ListGroupMembers-request-SAMAccountName"></a>
 The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^:;|=+"*?<>/\\,\[\]@]+`
Required: Yes

## Response Syntax
<a name="API_ListGroupMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DirectoryId": "string",
   "MemberRealm": "string",
   "Members": [
      {
         "MemberType": "string",
         "SAMAccountName": "string",
         "SID": "string"
      }
   ],
   "NextToken": "string",
   "Realm": "string"
}
```

## Response Elements
<a name="API_ListGroupMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_ListGroupMembers_ResponseSyntax) **   <a name="directoryservicedata-ListGroupMembers-response-DirectoryId"></a>
Identifier (ID) of the directory associated with the group.
Type: String
Pattern: `d-[0-9a-f]{10}`

 ** [MemberRealm](#API_ListGroupMembers_ResponseSyntax) **   <a name="directoryservicedata-ListGroupMembers-response-MemberRealm"></a>
 The domain name that's associated with the member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`

 ** [Members](#API_ListGroupMembers_ResponseSyntax) **   <a name="directoryservicedata-ListGroupMembers-response-Members"></a>
 The member information that the request returns.
Type: Array of [Member](API_Member.md) objects

 ** [NextToken](#API_ListGroupMembers_ResponseSyntax) **   <a name="directoryservicedata-ListGroupMembers-response-NextToken"></a>
 An encoded paging token for paginated calls that can be passed back to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [Realm](#API_ListGroupMembers_ResponseSyntax) **   <a name="directoryservicedata-ListGroupMembers-response-Realm"></a>
 The domain name that's associated with the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`

## Errors
<a name="API_ListGroupMembers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permission to perform the request or access the directory. It can also occur when the `DirectoryId` doesn't exist or the user, member, or group might be outside of your organizational unit (OU).
 Make sure that you have the authentication and authorization to perform the action. Review the directory information in the request, and make sure that the object isn't outside of your OU.
 ** Reason **
 Reason the request was unauthorized.
HTTP Status Code: 403

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
<a name="API_ListGroupMembers_Examples"></a>

### Example
<a name="API_ListGroupMembers_Example_1"></a>

This example illustrates one usage of ListGroupMembers.

#### Sample Request
<a name="API_ListGroupMembers_Example_1_Request"></a>

```
{
  "SAMAccountName": "Marketing",
  "MaxResults": 123,
  "MemberRealm": "example.local",
  "NextToken": "123456",
  "Realm": "examplecorp.com"
}
```

#### Sample Response
<a name="API_ListGroupMembers_Example_1_Response"></a>

```
{
  "DirectoryId": "d-926example",
  "Members": [
    {
      "SID": "S-1-5-11-111",
      "SAMAccountName": "twhitlock"
    },
    {
      "SID": "S-1-5-11-112",
      "SAMAccountName": "pcandella"
    },
    {
      "SID": "S-1-5-11-113",
      "SAMAccountName": "jstiles"
    }
  ],
  "NextToken": "223456"
}
```

## See Also
<a name="API_ListGroupMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directory-service-data-2023-05-31/ListGroupMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directory-service-data-2023-05-31/ListGroupMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/ListGroupMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directory-service-data-2023-05-31/ListGroupMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/ListGroupMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directory-service-data-2023-05-31/ListGroupMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directory-service-data-2023-05-31/ListGroupMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directory-service-data-2023-05-31/ListGroupMembers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directory-service-data-2023-05-31/ListGroupMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/ListGroupMembers)
