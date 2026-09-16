---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ModifyReportDefinition.html
---

# ModifyReportDefinition
<a name="API_cur_ModifyReportDefinition"></a>

Allows you to programmatically update your report preferences.

## Request Syntax
<a name="API_cur_ModifyReportDefinition_RequestSyntax"></a>

```
{
   "ReportDefinition": {
      "AdditionalArtifacts": [ "{{string}}" ],
      "AdditionalSchemaElements": [ "{{string}}" ],
      "BillingViewArn": "{{string}}",
      "Compression": "{{string}}",
      "Format": "{{string}}",
      "RefreshClosedReports": {{boolean}},
      "ReportName": "{{string}}",
      "ReportStatus": {
         "lastDelivery": "{{string}}",
         "lastStatus": "{{string}}"
      },
      "ReportVersioning": "{{string}}",
      "S3Bucket": "{{string}}",
      "S3Prefix": "{{string}}",
      "S3Region": "{{string}}",
      "TimeUnit": "{{string}}"
   },
   "ReportName": "{{string}}"
}
```

## Request Parameters
<a name="API_cur_ModifyReportDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReportDefinition](#API_cur_ModifyReportDefinition_RequestSyntax) **   <a name="awscostmanagement-cur_ModifyReportDefinition-request-ReportDefinition"></a>
The definition of AWS Cost and Usage Report. You can specify the report name, time unit, report format, compression format, S3 bucket, additional artifacts, and schema elements in the definition.
Type: [ReportDefinition](API_cur_ReportDefinition.md) object
Required: Yes

 ** [ReportName](#API_cur_ModifyReportDefinition_RequestSyntax) **   <a name="awscostmanagement-cur_ModifyReportDefinition-request-ReportName"></a>
The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[0-9A-Za-z!\-_.*\'()]+`
Required: Yes

## Response Elements
<a name="API_cur_ModifyReportDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_cur_ModifyReportDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
An error on the server occurred during the processing of your request. Try again later.
 ** Message **
A message to show the detail of the exception.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
A message to show the detail of the exception.
HTTP Status Code: 400

## See Also
<a name="API_cur_ModifyReportDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cur-2017-01-06/ModifyReportDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cur-2017-01-06/ModifyReportDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cur-2017-01-06/ModifyReportDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cur-2017-01-06/ModifyReportDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cur-2017-01-06/ModifyReportDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cur-2017-01-06/ModifyReportDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cur-2017-01-06/ModifyReportDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cur-2017-01-06/ModifyReportDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cur-2017-01-06/ModifyReportDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cur-2017-01-06/ModifyReportDefinition)
