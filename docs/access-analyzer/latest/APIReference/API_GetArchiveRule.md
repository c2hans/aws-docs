---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetArchiveRule.html
---

# GetArchiveRule
<a name="API_GetArchiveRule"></a>

Retrieves information about an archive rule.

To learn about filter keys that you can use to create an archive rule, see [IAM Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html) in the **IAM User Guide**.

## Request Syntax
<a name="API_GetArchiveRule_RequestSyntax"></a>

```
GET /analyzer/{{analyzerName}}/archive-rule/{{ruleName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetArchiveRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analyzerName](#API_GetArchiveRule_RequestSyntax) **   <a name="accessanalyzer-GetArchiveRule-request-uri-analyzerName"></a>
The name of the analyzer to retrieve rules from.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

 ** [ruleName](#API_GetArchiveRule_RequestSyntax) **   <a name="accessanalyzer-GetArchiveRule-request-uri-ruleName"></a>
The name of the rule to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

## Request Body
<a name="API_GetArchiveRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetArchiveRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "archiveRule": {
      "createdAt": "string",
      "filter": {
         "string" : {
            "contains": [ "string" ],
            "eq": [ "string" ],
            "exists": boolean,
            "neq": [ "string" ]
         }
      },
      "ruleName": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_GetArchiveRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [archiveRule](#API_GetArchiveRule_ResponseSyntax) **   <a name="accessanalyzer-GetArchiveRule-response-archiveRule"></a>
Contains information about an archive rule. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.
Type: [ArchiveRuleSummary](API_ArchiveRuleSummary.md) object

## Errors
<a name="API_GetArchiveRule_Errors"></a>

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
<a name="API_GetArchiveRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/GetArchiveRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/GetArchiveRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/GetArchiveRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/GetArchiveRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/GetArchiveRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/GetArchiveRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/GetArchiveRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/GetArchiveRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/GetArchiveRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/GetArchiveRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
