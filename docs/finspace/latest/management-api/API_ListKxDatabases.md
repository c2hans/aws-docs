---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxDatabases.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# ListKxDatabases
<a name="API_ListKxDatabases"></a>

Returns a list of all the databases in the kdb environment.

## Request Syntax
<a name="API_ListKxDatabases_RequestSyntax"></a>

```
GET /kx/environments/{{environmentId}}/databases?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListKxDatabases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_ListKxDatabases_RequestSyntax) **   <a name="finspace-ListKxDatabases-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`
Required: Yes

 ** [maxResults](#API_ListKxDatabases_RequestSyntax) **   <a name="finspace-ListKxDatabases-request-uri-maxResults"></a>
The maximum number of results to return in this request.
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [nextToken](#API_ListKxDatabases_RequestSyntax) **   <a name="finspace-ListKxDatabases-request-uri-nextToken"></a>
A token that indicates where a results page should begin.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Request Body
<a name="API_ListKxDatabases_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListKxDatabases_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "kxDatabases": [
      {
         "createdTimestamp": number,
         "databaseName": "string",
         "lastModifiedTimestamp": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListKxDatabases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kxDatabases](#API_ListKxDatabases_ResponseSyntax) **   <a name="finspace-ListKxDatabases-response-kxDatabases"></a>
A list of databases in the kdb environment.
Type: Array of [KxDatabaseListEntry](API_KxDatabaseListEntry.md) objects

 ** [nextToken](#API_ListKxDatabases_ResponseSyntax) **   <a name="finspace-ListKxDatabases-response-nextToken"></a>
A token that indicates where a results page should begin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Errors
<a name="API_ListKxDatabases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListKxDatabases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/ListKxDatabases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/ListKxDatabases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/ListKxDatabases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/ListKxDatabases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/ListKxDatabases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/ListKxDatabases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/ListKxDatabases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/ListKxDatabases)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/ListKxDatabases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/ListKxDatabases)
