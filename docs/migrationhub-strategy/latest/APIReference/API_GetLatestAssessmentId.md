---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetLatestAssessmentId.html
---

# GetLatestAssessmentId
<a name="API_GetLatestAssessmentId"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Retrieve the latest ID of a specific assessment task.

## Request Syntax
<a name="API_GetLatestAssessmentId_RequestSyntax"></a>

```
GET /get-latest-assessment-id HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLatestAssessmentId_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetLatestAssessmentId_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLatestAssessmentId_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string"
}
```

## Response Elements
<a name="API_GetLatestAssessmentId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_GetLatestAssessmentId_ResponseSyntax) **   <a name="migrationhubstrategy-GetLatestAssessmentId-response-id"></a>
The latest ID for the specific assessment task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 52.
Pattern: `.*[0-9a-z-:]+.*`

## Errors
<a name="API_GetLatestAssessmentId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** DependencyException **
Dependency encountered an error.
HTTP Status Code: 500

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_GetLatestAssessmentId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/GetLatestAssessmentId)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
