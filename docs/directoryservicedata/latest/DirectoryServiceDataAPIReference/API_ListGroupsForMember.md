---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroupsForMember.html
---

# ListGroupsForMember
<a name="API_ListGroupsForMember"></a>

 Returns group information for the specified member.

 This operation supports pagination with the use of the `NextToken` request and response parameters. If more results are available, the `ListGroupsForMember.NextToken` member contains a token that you pass in the next call to `ListGroupsForMember`. This retrieves the next set of items.

 You can also specify a maximum number of return results with the `MaxResults` parameter.

## Request Syntax
<a name="API_ListGroupsForMember_RequestSyntax"></a>

```
POST /GroupMemberships/ListGroupsForMember?DirectoryId={{DirectoryId}} HTTP/1.1
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
<a name="API_ListGroupsForMember_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DirectoryId](#API_ListGroupsForMember_RequestSyntax) **   <a name="directoryservicedata-ListGroupsForMember-request-uri-DirectoryId"></a>
 The identifier (ID) of the directory that's associated with the member.
Pattern: `d-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_ListGroupsForMember_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListGroupsForMember_RequestSyntax) **   <a name="directoryservicedata-ListGroupsForMember-request-MaxResults"></a>
 The maximum number of results to be returned per request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

 ** [MemberRealm](#API_ListGroupsForMember_RequestSyntax) **   <a name="directoryservicedata-ListGroupsForMember-request-MemberRealm"></a>
 The domain name that's associated with the group member.
 This parameter is optional, so you can limit your results to the group members in a specific domain.
 This parameter is case insensitive and defaults to `Realm`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`
Required: No

 ** [NextToken](#API_ListGroupsForMember_RequestSyntax) **   <a name="directoryservicedata-ListGroupsForMember-request-NextToken"></a>
 An encoded paging token for paginated calls that can be passed back to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: No

 ** [Realm](#API_ListGroupsForMember_RequestSyntax) **   <a name="directoryservicedata-ListGroupsForMember-request-Realm"></a>
 The domain name that's associated with the group.
 This parameter is optional, so you can return groups outside of your AWS Managed Microsoft AD domain. When no value is defined, only your AWS Managed Microsoft AD groups are returned.
 This value is case insensitive and defaults to your AWS Managed Microsoft AD domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`
Required: No

 ** [SAMAccountName](#API_ListGroupsForMember_RequestSyntax) **   <a name="directoryservicedata-ListGroupsForMember-request-SAMAccountName"></a>
 The `SAMAccountName` of the user, group, or computer that's a member of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[^:;|=+"*?<>/\\,\[\]@]+`
Required: Yes

## Response Syntax
<a name="API_ListGroupsForMember_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DirectoryId": "string",
   "Groups": [
      {
         "GroupScope": "string",
         "GroupType": "string",
         "SAMAccountName": "string",
         "SID": "string"
      }
   ],
   "MemberRealm": "string",
   "NextToken": "string",
   "Realm": "string"
}
```

## Response Elements
<a name="API_ListGroupsForMember_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_ListGroupsForMember_ResponseSyntax) **   <a name="directoryservicedata-ListGroupsForMember-response-DirectoryId"></a>
 The identifier (ID) of the directory that's associated with the member.
Type: String
Pattern: `d-[0-9a-f]{10}`

 ** [Groups](#API_ListGroupsForMember_ResponseSyntax) **   <a name="directoryservicedata-ListGroupsForMember-response-Groups"></a>
 The group information that the request returns.
Type: Array of [GroupSummary](API_GroupSummary.md) objects

 ** [MemberRealm](#API_ListGroupsForMember_ResponseSyntax) **   <a name="directoryservicedata-ListGroupsForMember-response-MemberRealm"></a>
 The domain that's associated with the member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`

 ** [NextToken](#API_ListGroupsForMember_ResponseSyntax) **   <a name="directoryservicedata-ListGroupsForMember-response-NextToken"></a>
 An encoded paging token for paginated calls that can be passed back to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [Realm](#API_ListGroupsForMember_ResponseSyntax) **   <a name="directoryservicedata-ListGroupsForMember-response-Realm"></a>
 The domain that's associated with the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`

## Errors
<a name="API_ListGroupsForMember_Errors"></a>

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
<a name="API_ListGroupsForMember_Examples"></a>

### Example
<a name="API_ListGroupsForMember_Example_1"></a>

This example illustrates one usage of ListGroupsForMember.

#### Sample Request
<a name="API_ListGroupsForMember_Example_1_Request"></a>

```
{
  "MaxResults": 123,
  "SAMAccountName": "twhitlock",
  "MemberRealm": "example.local",
  "NextToken": "123456",
  "Realm": "examplecorp.com"
}
```

#### Sample Response
<a name="API_ListGroupsForMember_Example_1_Response"></a>

```
{
  "DirectoryId": "d-926example",
  "Groups": [
    {
      "GroupScope": "BuiltinLocal",
      "GroupType": "Security",
      "SAMAccountName": "Administrators",
      "SID": "S-1-5-32-544"
    },
    {
      "GroupScope": "BuiltinLocal",
      "GroupType": "Security",
      "SAMAccountName": "Users",
      "SID": "S-1-5-32-545"
    }
  ],
  "NextToken": "223456"
}
```

## See Also
<a name="API_ListGroupsForMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directory-service-data-2023-05-31/ListGroupsForMember)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directory-service-data-2023-05-31/ListGroupsForMember)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/ListGroupsForMember)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directory-service-data-2023-05-31/ListGroupsForMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/ListGroupsForMember)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directory-service-data-2023-05-31/ListGroupsForMember)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directory-service-data-2023-05-31/ListGroupsForMember)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directory-service-data-2023-05-31/ListGroupsForMember)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directory-service-data-2023-05-31/ListGroupsForMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/ListGroupsForMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service Data. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservicedata` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
