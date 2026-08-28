---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DescribeUser.html
---

# DescribeUser
<a name="API_DescribeUser"></a>

Returns information about a specific user.

## Request Syntax
<a name="API_DescribeUser_RequestSyntax"></a>

```
POST /Users/DescribeUser?DirectoryId={{DirectoryId}} HTTP/1.1
Content-type: application/json

{
   "OtherAttributes": [ "{{string}}" ],
   "Realm": "{{string}}",
   "SAMAccountName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DirectoryId](#API_DescribeUser_RequestSyntax) **   <a name="directoryservicedata-DescribeUser-request-uri-DirectoryId"></a>
 The identifier (ID) of the directory that's associated with the user.
Pattern: `d-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_DescribeUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [OtherAttributes](#API_DescribeUser_RequestSyntax) **   <a name="directoryservicedata-DescribeUser-request-OtherAttributes"></a>
 One or more attribute names to be returned for the user. A key is an attribute name, and the value is a list of maps. For a list of supported attributes, see [Directory Service Data Attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z*][A-Za-z-*]*`
Required: No

 ** [Realm](#API_DescribeUser_RequestSyntax) **   <a name="directoryservicedata-DescribeUser-request-Realm"></a>
 The domain name that's associated with the user.
 This parameter is optional, so you can return users outside your AWS Managed Microsoft AD domain. When no value is defined, only your AWS Managed Microsoft AD users are returned.
 This value is case insensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`
Required: No

 ** [SAMAccountName](#API_DescribeUser_RequestSyntax) **   <a name="directoryservicedata-DescribeUser-request-SAMAccountName"></a>
 The name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\w\-.]+`
Required: Yes

## Response Syntax
<a name="API_DescribeUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DirectoryId": "string",
   "DistinguishedName": "string",
   "EmailAddress": "string",
   "Enabled": boolean,
   "GivenName": "string",
   "OtherAttributes": {
      "string" : { ... }
   },
   "Realm": "string",
   "SAMAccountName": "string",
   "SID": "string",
   "Surname": "string",
   "UserPrincipalName": "string"
}
```

## Response Elements
<a name="API_DescribeUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-DirectoryId"></a>
 The identifier (ID) of the directory that's associated with the user.
Type: String
Pattern: `d-[0-9a-f]{10}`

 ** [DistinguishedName](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-DistinguishedName"></a>
 The [distinguished name](https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name) of the object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [EmailAddress](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-EmailAddress"></a>
 The email address of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [Enabled](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-Enabled"></a>
 Indicates whether the user account is active.
Type: Boolean

 ** [GivenName](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-GivenName"></a>
 The first name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [OtherAttributes](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-OtherAttributes"></a>
 The attribute values that are returned for the attribute names that are included in the request.
 Attribute names are case insensitive.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Map Entries: Maximum number of 25 items.
Key Length Constraints: Minimum length of 1. Maximum length of 63.
Key Pattern: `[A-Za-z*][A-Za-z-*]*`

 ** [Realm](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-Realm"></a>
 The domain name that's associated with the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`

 ** [SAMAccountName](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-SAMAccountName"></a>
 The name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\w\-.]+`

 ** [SID](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-SID"></a>
 The unique security identifier (SID) of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [Surname](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-Surname"></a>
 The last name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [UserPrincipalName](#API_DescribeUser_ResponseSyntax) **   <a name="directoryservicedata-DescribeUser-response-UserPrincipalName"></a>
 The UPN that is an Internet-style login name for a user and is based on the Internet standard [RFC 822](https://datatracker.ietf.org/doc/html/rfc822). The UPN is shorter than the distinguished name and easier to remember.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_DescribeUser_Errors"></a>

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
<a name="API_DescribeUser_Examples"></a>

### Example
<a name="API_DescribeUser_Example_1"></a>

This example illustrates one usage of DescribeUser.

#### Sample Request
<a name="API_DescribeUser_Example_1_Request"></a>

```
{
  "OtherAttributes": [
    "department",
    "manager",
    "ipPhone"
  ],
  "Realm": "examplecorp.com",
  "SAMAccountName": "twhitlock"
}
```

#### Sample Response
<a name="API_DescribeUser_Example_1_Response"></a>

```
{
  "DirectoryId": "d-926example",
  "DistinguishedName": "Terry Whitlock",
  "EmailAddress": "terry.whitlock@examplecorp.com",
  "Enabled": true,
  "GivenName": "Terry Whitlock",
  "OtherAttributes": {
    "Department": {"S": "communications"},
    "Manager": {"S": "OU=Users,DC=mmajors"},
    "IpPhone": {"S": "111.111.111.111"}
  },
  "SAMAccountName": "twhitlock",
  "SID": "S-1-5-11-112",
  "Surname": "Whitlock",
  "UserPrincipalName": "terry.whitlock"
}
```

## See Also
<a name="API_DescribeUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directory-service-data-2023-05-31/DescribeUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directory-service-data-2023-05-31/DescribeUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/DescribeUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directory-service-data-2023-05-31/DescribeUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/DescribeUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directory-service-data-2023-05-31/DescribeUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directory-service-data-2023-05-31/DescribeUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directory-service-data-2023-05-31/DescribeUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directory-service-data-2023-05-31/DescribeUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/DescribeUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service Data. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservicedata` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
