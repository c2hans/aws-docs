---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_ListUsers.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# ListUsers
<a name="API_ListUsers"></a>

Lists all available users in FinSpace.

## Request Syntax
<a name="API_ListUsers_RequestSyntax"></a>

```
GET /user?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListUsers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListUsers_RequestSyntax) **   <a name="finspace-ListUsers-request-uri-maxResults"></a>
The maximum number of results per page.
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** [nextToken](#API_ListUsers_RequestSyntax) **   <a name="finspace-ListUsers-request-uri-nextToken"></a>
A token that indicates where a results page should begin.

## Request Body
<a name="API_ListUsers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListUsers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "users": [
      {
         "apiAccess": "string",
         "apiAccessPrincipalArn": "string",
         "createTime": number,
         "emailAddress": "string",
         "firstName": "string",
         "lastDisabledTime": number,
         "lastEnabledTime": number,
         "lastLoginTime": number,
         "lastModifiedTime": number,
         "lastName": "string",
         "status": "string",
         "type": "string",
         "userId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListUsers_ResponseSyntax) **   <a name="finspace-ListUsers-response-nextToken"></a>
A token that indicates where a results page should begin.
Type: String

 ** [users](#API_ListUsers_ResponseSyntax) **   <a name="finspace-ListUsers-response-users"></a>
A list of all the users.
Type: Array of [User](API_User.md) objects

## Errors
<a name="API_ListUsers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/ListUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/ListUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/ListUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/ListUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/ListUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/ListUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/ListUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/ListUsers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/ListUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/ListUsers)
