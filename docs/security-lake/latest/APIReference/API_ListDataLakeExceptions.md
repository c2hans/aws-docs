---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListDataLakeExceptions.html
---

# ListDataLakeExceptions
<a name="API_ListDataLakeExceptions"></a>

Lists the Amazon Security Lake exceptions that you can use to find the source of problems and fix them.

## Request Syntax
<a name="API_ListDataLakeExceptions_RequestSyntax"></a>

```
POST /v1/datalake/exceptions HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "regions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListDataLakeExceptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDataLakeExceptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListDataLakeExceptions_RequestSyntax) **   <a name="securitylake-ListDataLakeExceptions-request-maxResults"></a>
Lists the maximum number of failures in Security Lake.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListDataLakeExceptions_RequestSyntax) **   <a name="securitylake-ListDataLakeExceptions-request-nextToken"></a>
Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.
Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [regions](#API_ListDataLakeExceptions_RequestSyntax) **   <a name="securitylake-ListDataLakeExceptions-request-regions"></a>
The AWS Regions from which exceptions are retrieved.
Type: Array of strings
Pattern: `(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+`
Required: No

## Response Syntax
<a name="API_ListDataLakeExceptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "exceptions": [
      {
         "exception": "string",
         "region": "string",
         "remediation": "string",
         "timestamp": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataLakeExceptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exceptions](#API_ListDataLakeExceptions_ResponseSyntax) **   <a name="securitylake-ListDataLakeExceptions-response-exceptions"></a>
Lists the failures that cannot be retried.
Type: Array of [DataLakeException](API_DataLakeException.md) objects

 ** [nextToken](#API_ListDataLakeExceptions_ResponseSyntax) **   <a name="securitylake-ListDataLakeExceptions-response-nextToken"></a>
Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.
Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListDataLakeExceptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific AWS action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.
 ** errorCode **
A coded string to provide more information about the access denied exception. You can use the error code to check the exception type.
HTTP Status Code: 403

 ** BadRequestException **
The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
 ** resourceName **
The resource name.
 ** resourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
That the rate of requests to Security Lake is exceeding the request quotas for your AWS account.
 ** retryAfterSeconds **
Retry the request after the specified time.
 ** serviceCode **
The code for the service in Service Quotas.
HTTP Status Code: 429

## See Also
<a name="API_ListDataLakeExceptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/ListDataLakeExceptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/ListDataLakeExceptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/ListDataLakeExceptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/ListDataLakeExceptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/ListDataLakeExceptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/ListDataLakeExceptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/ListDataLakeExceptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/ListDataLakeExceptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/ListDataLakeExceptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/ListDataLakeExceptions)
