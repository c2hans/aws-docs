---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartRecommendationReportGeneration.html
---

# StartRecommendationReportGeneration
<a name="API_StartRecommendationReportGeneration"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Starts generating a recommendation report.

## Request Syntax
<a name="API_StartRecommendationReportGeneration_RequestSyntax"></a>

```
POST /start-recommendation-report-generation HTTP/1.1
Content-type: application/json

{
   "groupIdFilter": [
      {
         "name": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "outputFormat": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartRecommendationReportGeneration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartRecommendationReportGeneration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [groupIdFilter](#API_StartRecommendationReportGeneration_RequestSyntax) **   <a name="migrationhubstrategy-StartRecommendationReportGeneration-request-groupIdFilter"></a>
 Groups the resources in the recommendation report with a unique name.
Type: Array of [Group](API_Group.md) objects
Required: No

 ** [outputFormat](#API_StartRecommendationReportGeneration_RequestSyntax) **   <a name="migrationhubstrategy-StartRecommendationReportGeneration-request-outputFormat"></a>
 The output format for the recommendation report file. The default format is Microsoft Excel.
Type: String
Valid Values: `Excel | Json`
Required: No

## Response Syntax
<a name="API_StartRecommendationReportGeneration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string"
}
```

## Response Elements
<a name="API_StartRecommendationReportGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_StartRecommendationReportGeneration_ResponseSyntax) **   <a name="migrationhubstrategy-StartRecommendationReportGeneration-response-id"></a>
 The ID of the recommendation report generation task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 52.
Pattern: `.*[0-9a-z-:]+.*`

## Errors
<a name="API_StartRecommendationReportGeneration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** ConflictException **
 Exception to indicate that there is an ongoing task when a new task is created. Return when once the existing tasks are complete.
HTTP Status Code: 409

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_StartRecommendationReportGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/StartRecommendationReportGeneration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
