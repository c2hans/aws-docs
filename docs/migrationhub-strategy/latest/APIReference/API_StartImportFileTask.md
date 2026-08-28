---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartImportFileTask.html
---

# StartImportFileTask
<a name="API_StartImportFileTask"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Starts a file import.

## Request Syntax
<a name="API_StartImportFileTask_RequestSyntax"></a>

```
POST /start-import-file-task HTTP/1.1
Content-type: application/json

{
   "dataSourceType": "{{string}}",
   "groupId": [
      {
         "name": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "name": "{{string}}",
   "S3Bucket": "{{string}}",
   "s3bucketForReportData": "{{string}}",
   "s3key": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartImportFileTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartImportFileTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataSourceType](#API_StartImportFileTask_RequestSyntax) **   <a name="migrationhubstrategy-StartImportFileTask-request-dataSourceType"></a>
Specifies the source that the servers are coming from. By default, Strategy Recommendations assumes that the servers specified in the import file are available in AWS Application Discovery Service.
Type: String
Valid Values: `ApplicationDiscoveryService | MPA | Import | StrategyRecommendationsApplicationDataCollector`
Required: No

 ** [groupId](#API_StartImportFileTask_RequestSyntax) **   <a name="migrationhubstrategy-StartImportFileTask-request-groupId"></a>
Groups the resources in the import file together with a unique name. This ID can be as filter in `ListApplicationComponents` and `ListServers`.
Type: Array of [Group](API_Group.md) objects
Required: No

 ** [name](#API_StartImportFileTask_RequestSyntax) **   <a name="migrationhubstrategy-StartImportFileTask-request-name"></a>
 A descriptive name for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*[a-zA-Z0-9_-]+.*`
Required: Yes

 ** [S3Bucket](#API_StartImportFileTask_RequestSyntax) **   <a name="migrationhubstrategy-StartImportFileTask-request-S3Bucket"></a>
 The S3 bucket where the import file is located. The bucket name is required to begin with `migrationhub-strategy-`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `.*[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+.*`
Required: Yes

 ** [s3bucketForReportData](#API_StartImportFileTask_RequestSyntax) **   <a name="migrationhubstrategy-StartImportFileTask-request-s3bucketForReportData"></a>
 The S3 bucket where Strategy Recommendations uploads import results. The bucket name is required to begin with migrationhub-strategy-.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `.*[0-9a-z]+[0-9a-z\.\-]*[0-9a-z]+.*`
Required: No

 ** [s3key](#API_StartImportFileTask_RequestSyntax) **   <a name="migrationhubstrategy-StartImportFileTask-request-s3key"></a>
 The Amazon S3 key name of the import file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_StartImportFileTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string"
}
```

## Response Elements
<a name="API_StartImportFileTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_StartImportFileTask_ResponseSyntax) **   <a name="migrationhubstrategy-StartImportFileTask-response-id"></a>
 The ID for a specific import task. The ID is unique within an AWS account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`

## Errors
<a name="API_StartImportFileTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
 The AWS account has reached its quota of imports. Contact AWS Support to increase the quota for this account.
HTTP Status Code: 402

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_StartImportFileTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/StartImportFileTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/StartImportFileTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/StartImportFileTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/StartImportFileTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/StartImportFileTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/StartImportFileTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/StartImportFileTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/StartImportFileTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/StartImportFileTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/StartImportFileTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
