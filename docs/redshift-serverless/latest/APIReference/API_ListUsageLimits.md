---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListUsageLimits.html
---

# ListUsageLimits
<a name="API_ListUsageLimits"></a>

Lists all usage limits within Amazon Redshift Serverless.

## Request Syntax
<a name="API_ListUsageLimits_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceArn": "{{string}}",
   "usageType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUsageLimits_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListUsageLimits_RequestSyntax) **   <a name="redshiftserverless-ListUsageLimits-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListUsageLimits_RequestSyntax) **   <a name="redshiftserverless-ListUsageLimits-request-nextToken"></a>
If your initial `ListUsageLimits` operation returns a `nextToken`, you can include the returned `nextToken` in following `ListUsageLimits` operations, which returns results in the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: No

 ** [resourceArn](#API_ListUsageLimits_RequestSyntax) **   <a name="redshiftserverless-ListUsageLimits-request-resourceArn"></a>
The Amazon Resource Name (ARN) associated with the resource whose usage limits you want to list.
Type: String
Required: No

 ** [usageType](#API_ListUsageLimits_RequestSyntax) **   <a name="redshiftserverless-ListUsageLimits-request-usageType"></a>
The Amazon Redshift Serverless feature whose limits you want to see.
Type: String
Valid Values: `serverless-compute | cross-region-datasharing`
Required: No

## Response Syntax
<a name="API_ListUsageLimits_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "usageLimits": [
      {
         "amount": number,
         "breachAction": "string",
         "period": "string",
         "resourceArn": "string",
         "usageLimitArn": "string",
         "usageLimitId": "string",
         "usageType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUsageLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListUsageLimits_ResponseSyntax) **   <a name="redshiftserverless-ListUsageLimits-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [usageLimits](#API_ListUsageLimits_ResponseSyntax) **   <a name="redshiftserverless-ListUsageLimits-response-usageLimits"></a>
An array of returned usage limit objects.
Type: Array of [UsageLimit](API_UsageLimit.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_ListUsageLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** InvalidPaginationException **
The provided pagination token is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListUsageLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListUsageLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListUsageLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListUsageLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListUsageLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListUsageLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListUsageLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListUsageLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListUsageLimits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListUsageLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListUsageLimits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
