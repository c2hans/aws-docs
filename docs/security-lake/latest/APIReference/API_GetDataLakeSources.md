---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetDataLakeSources.html
---

# GetDataLakeSources
<a name="API_GetDataLakeSources"></a>

Retrieves a snapshot of the current Region, including whether Amazon Security Lake is enabled for those accounts and which sources Security Lake is collecting data from.

## Request Syntax
<a name="API_GetDataLakeSources_RequestSyntax"></a>

```
POST /v1/datalake/sources HTTP/1.1
Content-type: application/json

{
   "accounts": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetDataLakeSources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDataLakeSources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accounts](#API_GetDataLakeSources_RequestSyntax) **   <a name="securitylake-GetDataLakeSources-request-accounts"></a>
The AWS account ID for which a static snapshot of the current AWS Region, including enabled accounts and log sources, is retrieved.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** [maxResults](#API_GetDataLakeSources_RequestSyntax) **   <a name="securitylake-GetDataLakeSources-request-maxResults"></a>
The maximum limit of accounts for which the static snapshot of the current Region, including enabled accounts and log sources, is retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetDataLakeSources_RequestSyntax) **   <a name="securitylake-GetDataLakeSources-request-nextToken"></a>
Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.
Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_GetDataLakeSources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataLakeArn": "string",
   "dataLakeSources": [
      {
         "account": "string",
         "eventClasses": [ "string" ],
         "sourceName": "string",
         "sourceStatuses": [
            {
               "resource": "string",
               "status": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetDataLakeSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataLakeArn](#API_GetDataLakeSources_ResponseSyntax) **   <a name="securitylake-GetDataLakeSources-response-dataLakeArn"></a>
The Amazon Resource Name (ARN) created by you to provide to the subscriber. For more information about ARNs and how to use them in policies, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws|aws-us-gov|aws-cn):securitylake:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9_/.\-]{0,63}:[A-Za-z0-9][A-Za-z0-9_/.\-]{0,127}`

 ** [dataLakeSources](#API_GetDataLakeSources_ResponseSyntax) **   <a name="securitylake-GetDataLakeSources-response-dataLakeSources"></a>
The list of enabled accounts and enabled sources.
Type: Array of [DataLakeSource](API_DataLakeSource.md) objects

 ** [nextToken](#API_GetDataLakeSources_ResponseSyntax) **   <a name="securitylake-GetDataLakeSources-response-nextToken"></a>
Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.
Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_GetDataLakeSources_Errors"></a>

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
<a name="API_GetDataLakeSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securitylake-2018-05-10/GetDataLakeSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securitylake-2018-05-10/GetDataLakeSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/GetDataLakeSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securitylake-2018-05-10/GetDataLakeSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/GetDataLakeSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securitylake-2018-05-10/GetDataLakeSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securitylake-2018-05-10/GetDataLakeSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securitylake-2018-05-10/GetDataLakeSources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securitylake-2018-05-10/GetDataLakeSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/GetDataLakeSources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
