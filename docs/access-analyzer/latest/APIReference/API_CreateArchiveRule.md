---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CreateArchiveRule.html
---

# CreateArchiveRule
<a name="API_CreateArchiveRule"></a>

Creates an archive rule for the specified analyzer. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.

To learn about filter keys that you can use to create an archive rule, see [IAM Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html) in the **IAM User Guide**.

## Request Syntax
<a name="API_CreateArchiveRule_RequestSyntax"></a>

```
PUT /analyzer/{{analyzerName}}/archive-rule HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "filter": {
      "{{string}}" : {
         "contains": [ "{{string}}" ],
         "eq": [ "{{string}}" ],
         "exists": {{boolean}},
         "neq": [ "{{string}}" ]
      }
   },
   "ruleName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateArchiveRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [analyzerName](#API_CreateArchiveRule_RequestSyntax) **   <a name="accessanalyzer-CreateArchiveRule-request-uri-analyzerName"></a>
The name of the created analyzer.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

## Request Body
<a name="API_CreateArchiveRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateArchiveRule_RequestSyntax) **   <a name="accessanalyzer-CreateArchiveRule-request-clientToken"></a>
A client token.
Type: String
Required: No

 ** [filter](#API_CreateArchiveRule_RequestSyntax) **   <a name="accessanalyzer-CreateArchiveRule-request-filter"></a>
The criteria for the rule.
Type: String to [Criterion](API_Criterion.md) object map
Required: Yes

 ** [ruleName](#API_CreateArchiveRule_RequestSyntax) **   <a name="accessanalyzer-CreateArchiveRule-request-ruleName"></a>
The name of the rule to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

## Response Syntax
<a name="API_CreateArchiveRule_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateArchiveRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateArchiveRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
A conflict exception error.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The resource type.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
Service quote met error.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 402

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
<a name="API_CreateArchiveRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CreateArchiveRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CreateArchiveRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CreateArchiveRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CreateArchiveRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CreateArchiveRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CreateArchiveRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CreateArchiveRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CreateArchiveRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CreateArchiveRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CreateArchiveRule)
