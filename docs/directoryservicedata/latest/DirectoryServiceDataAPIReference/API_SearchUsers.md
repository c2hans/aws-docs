---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_SearchUsers.html
---

# SearchUsers
<a name="API_SearchUsers"></a>

 Searches the specified directory for a user. You can find users that match the `SearchString` parameter with the value of their attributes included in the `SearchString` parameter.

 This operation supports pagination with the use of the `NextToken` request and response parameters. If more results are available, the `SearchUsers.NextToken` member contains a token that you pass in the next call to `SearchUsers`. This retrieves the next set of items.

 You can also specify a maximum number of return results with the `MaxResults` parameter.

## Request Syntax
<a name="API_SearchUsers_RequestSyntax"></a>

```
POST /Users/SearchUsers?DirectoryId={{DirectoryId}} HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Realm": "{{string}}",
   "SearchAttributes": [ "{{string}}" ],
   "SearchString": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchUsers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DirectoryId](#API_SearchUsers_RequestSyntax) **   <a name="directoryservicedata-SearchUsers-request-uri-DirectoryId"></a>
 The identifier (ID) of the directory that's associated with the user.
Pattern: `d-[0-9a-f]{10}`
Required: Yes

## Request Body
<a name="API_SearchUsers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_SearchUsers_RequestSyntax) **   <a name="directoryservicedata-SearchUsers-request-MaxResults"></a>
 The maximum number of results to be returned per request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 250.
Required: No

 ** [NextToken](#API_SearchUsers_RequestSyntax) **   <a name="directoryservicedata-SearchUsers-request-NextToken"></a>
 An encoded paging token for paginated calls that can be passed back to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Required: No

 ** [Realm](#API_SearchUsers_RequestSyntax) **   <a name="directoryservicedata-SearchUsers-request-Realm"></a>
 The domain name that's associated with the user.
 This parameter is optional, so you can return users outside of your AWS Managed Microsoft AD domain. When no value is defined, only your AWS Managed Microsoft AD users are returned.
 This value is case insensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`
Required: No

 ** [SearchAttributes](#API_SearchUsers_RequestSyntax) **   <a name="directoryservicedata-SearchUsers-request-SearchAttributes"></a>
 One or more data attributes that are used to search for a user. For a list of supported attributes, see [Directory Service Data Attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z*][A-Za-z-*]*`
Required: Yes

 ** [SearchString](#API_SearchUsers_RequestSyntax) **   <a name="directoryservicedata-SearchUsers-request-SearchString"></a>
 The attribute value that you want to search for.
 Wildcard `(*)` searches aren't supported. For a list of supported attributes, see [Directory Service Data Attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_SearchUsers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DirectoryId": "string",
   "NextToken": "string",
   "Realm": "string",
   "Users": [
      {
         "DistinguishedName": "string",
         "EmailAddress": "string",
         "Enabled": boolean,
         "GivenName": "string",
         "OtherAttributes": {
            "string" : { ... }
         },
         "SAMAccountName": "string",
         "SID": "string",
         "Surname": "string",
         "UserPrincipalName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_SearchUsers_ResponseSyntax) **   <a name="directoryservicedata-SearchUsers-response-DirectoryId"></a>
 The identifier (ID) of the directory where the address block is added.
Type: String
Pattern: `d-[0-9a-f]{10}`

 ** [NextToken](#API_SearchUsers_ResponseSyntax) **   <a name="directoryservicedata-SearchUsers-response-NextToken"></a>
 An encoded paging token for paginated calls that can be passed back to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.

 ** [Realm](#API_SearchUsers_ResponseSyntax) **   <a name="directoryservicedata-SearchUsers-response-Realm"></a>
 The domain that's associated with the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?`

 ** [Users](#API_SearchUsers_ResponseSyntax) **   <a name="directoryservicedata-SearchUsers-response-Users"></a>
 The user information that the request returns.
Type: Array of [User](API_User.md) objects

## Errors
<a name="API_SearchUsers_Errors"></a>

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
<a name="API_SearchUsers_Examples"></a>

### Example
<a name="API_SearchUsers_Example_1"></a>

This example illustrates one usage of SearchUsers.

#### Sample Request
<a name="API_SearchUsers_Example_1_Request"></a>

```
{
  "MaxResults": 123,
  "NextToken": "123456",
  "Realm": "examplecorp.com",
  "SearchAttributes":
  [
    "department"
  ],
  "SearchString": "DevOps"
}
```

#### Sample Response
<a name="API_SearchUsers_Example_1_Response"></a>

```
{
  "DirectoryId": "d-926example",
  "NextToken": "223456",
  "Users":
  [
    {
      "SID": "S-1-5-11-111",
      "SAMAccountName": "twhitlock",
      "EmailAddress": "twhitlock@example.local.com",
      "UserPrincipalName": "twhitlock@examplecorp.com"
    },
    {
      "SID": "S-1-5-11-112",
      "SAMAccountName": "pcandella",
      "EmailAddress": "pcandella@example.local.com",
      "UserPrincipalName": "pcandella@examplecorp.com"
    },
    {
      "SID": "S-1-5-11-113",
      "SAMAccountName": "jstiles",
      "EmailAddress": "jstiles@example.local.com",
      "UserPrincipalName": "jstiles@examplecorp.com"
    }
  ]
}
```

## See Also
<a name="API_SearchUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directory-service-data-2023-05-31/SearchUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directory-service-data-2023-05-31/SearchUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/SearchUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directory-service-data-2023-05-31/SearchUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/SearchUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directory-service-data-2023-05-31/SearchUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directory-service-data-2023-05-31/SearchUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directory-service-data-2023-05-31/SearchUsers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directory-service-data-2023-05-31/SearchUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/SearchUsers)
