---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetFindingsStatistics.html
---

# GetFindingsStatistics
<a name="API_GetFindingsStatistics"></a>

Retrieves a list of aggregated finding statistics for an external access or unused access analyzer.

## Request Syntax
<a name="API_GetFindingsStatistics_RequestSyntax"></a>

```
POST /analyzer/findings/statistics HTTP/1.1
Content-type: application/json

{
   "analyzerArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetFindingsStatistics_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetFindingsStatistics_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analyzerArn](#API_GetFindingsStatistics_RequestSyntax) **   <a name="accessanalyzer-GetFindingsStatistics-request-analyzerArn"></a>
The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the statistics.
Type: String
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

## Response Syntax
<a name="API_GetFindingsStatistics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findingsStatistics": [
      { ... }
   ],
   "lastUpdatedAt": "string"
}
```

## Response Elements
<a name="API_GetFindingsStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findingsStatistics](#API_GetFindingsStatistics_ResponseSyntax) **   <a name="accessanalyzer-GetFindingsStatistics-response-findingsStatistics"></a>
A group of external access or unused access findings statistics.
Type: Array of [FindingsStatistics](API_FindingsStatistics.md) objects

 ** [lastUpdatedAt](#API_GetFindingsStatistics_ResponseSyntax) **   <a name="accessanalyzer-GetFindingsStatistics-response-lastUpdatedAt"></a>
The time at which the retrieval of the findings statistics was last updated. If the findings statistics have not been previously retrieved for the specified analyzer, this field will not be populated.
Type: Timestamp

## Errors
<a name="API_GetFindingsStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
Throttling limit exceeded error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 429

 ** ValidationException **
Validation exception error.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetFindingsStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetFindingsStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetFindingsStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetFindingsStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetFindingsStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetFindingsStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetFindingsStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetFindingsStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetFindingsStatistics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetFindingsStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetFindingsStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
