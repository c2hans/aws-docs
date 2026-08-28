---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeJobLogItems.html
---

# DescribeJobLogItems
<a name="API_DescribeJobLogItems"></a>

Retrieves detailed job log items with paging.

## Request Syntax
<a name="API_DescribeJobLogItems_RequestSyntax"></a>

```
POST /DescribeJobLogItems HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "jobID": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeJobLogItems_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeJobLogItems_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_DescribeJobLogItems_RequestSyntax) **   <a name="mgn-DescribeJobLogItems-request-accountID"></a>
Request to describe Job log Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [jobID](#API_DescribeJobLogItems_RequestSyntax) **   <a name="mgn-DescribeJobLogItems-request-jobID"></a>
Request to describe Job log job ID.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `mgnjob-[0-9a-zA-Z]{17}`
Required: Yes

 ** [maxResults](#API_DescribeJobLogItems_RequestSyntax) **   <a name="mgn-DescribeJobLogItems-request-maxResults"></a>
Request to describe Job log item maximum results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeJobLogItems_RequestSyntax) **   <a name="mgn-DescribeJobLogItems-request-nextToken"></a>
Request to describe Job log next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeJobLogItems_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "event": "string",
         "eventData": {
            "attemptCount": number,
            "conversionServerID": "string",
            "maxAttemptsCount": number,
            "rawError": "string",
            "sourceServerID": "string",
            "targetInstanceID": "string"
         },
         "logDateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeJobLogItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeJobLogItems_ResponseSyntax) **   <a name="mgn-DescribeJobLogItems-response-items"></a>
Request to describe Job log response items.
Type: Array of [JobLog](API_JobLog.md) objects

 ** [nextToken](#API_DescribeJobLogItems_ResponseSyntax) **   <a name="mgn-DescribeJobLogItems-response-nextToken"></a>
Request to describe Job log response next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeJobLogItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeJobLogItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DescribeJobLogItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DescribeJobLogItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
