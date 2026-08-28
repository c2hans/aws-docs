---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateReportGroup.html
---

# CreateReportGroup
<a name="API_CreateReportGroup"></a>

 Creates a report group. A report group contains a collection of reports.

## Request Syntax
<a name="API_CreateReportGroup_RequestSyntax"></a>

```
{
   "exportConfig": {
      "exportConfigType": "{{string}}",
      "s3Destination": {
         "bucket": "{{string}}",
         "bucketOwner": "{{string}}",
         "encryptionDisabled": {{boolean}},
         "encryptionKey": "{{string}}",
         "packaging": "{{string}}",
         "path": "{{string}}"
      }
   },
   "name": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateReportGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [exportConfig](#API_CreateReportGroup_RequestSyntax) **   <a name="CodeBuild-CreateReportGroup-request-exportConfig"></a>
 A `ReportExportConfig` object that contains information about where the report group test results are exported.
Type: [ReportExportConfig](API_ReportExportConfig.md) object
Required: Yes

 ** [name](#API_CreateReportGroup_RequestSyntax) **   <a name="CodeBuild-CreateReportGroup-request-name"></a>
 The name of the report group.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Required: Yes

 ** [type](#API_CreateReportGroup_RequestSyntax) **   <a name="CodeBuild-CreateReportGroup-request-type"></a>
 The type of report group.
Type: String
Valid Values: `TEST | CODE_COVERAGE`
Required: Yes

 ** [tags](#API_CreateReportGroup_RequestSyntax) **   <a name="CodeBuild-CreateReportGroup-request-tags"></a>
 A list of tag key and value pairs associated with this report group.
These tags are available for use by AWS services that support AWS CodeBuild report group tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateReportGroup_ResponseSyntax"></a>

```
{
   "reportGroup": {
      "arn": "string",
      "created": number,
      "exportConfig": {
         "exportConfigType": "string",
         "s3Destination": {
            "bucket": "string",
            "bucketOwner": "string",
            "encryptionDisabled": boolean,
            "encryptionKey": "string",
            "packaging": "string",
            "path": "string"
         }
      },
      "lastModified": number,
      "name": "string",
      "status": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "type": "string"
   }
}
```

## Response Elements
<a name="API_CreateReportGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [reportGroup](#API_CreateReportGroup_ResponseSyntax) **   <a name="CodeBuild-CreateReportGroup-response-reportGroup"></a>
 Information about the report group that was created.
Type: [ReportGroup](API_ReportGroup.md) object

## Errors
<a name="API_CreateReportGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountLimitExceededException **
An AWS service limit was exceeded for the calling AWS account.
HTTP Status Code: 400

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified AWS resource cannot be created, because an AWS resource with the same settings already exists.
HTTP Status Code: 400

## See Also
<a name="API_CreateReportGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/CreateReportGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/CreateReportGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/CreateReportGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/CreateReportGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/CreateReportGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/CreateReportGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/CreateReportGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/CreateReportGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/CreateReportGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/CreateReportGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
