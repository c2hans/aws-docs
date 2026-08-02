---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartColumnStatisticsTaskRunSchedule.html
---

# StartColumnStatisticsTaskRunSchedule
<a name="API_StartColumnStatisticsTaskRunSchedule"></a>

Starts a column statistics task run schedule.

## Request Syntax
<a name="API_StartColumnStatisticsTaskRunSchedule_RequestSyntax"></a>

```
{
   "DatabaseName": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartColumnStatisticsTaskRunSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatabaseName](#API_StartColumnStatisticsTaskRunSchedule_RequestSyntax) **   <a name="Glue-StartColumnStatisticsTaskRunSchedule-request-DatabaseName"></a>
The name of the database where the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [TableName](#API_StartColumnStatisticsTaskRunSchedule_RequestSyntax) **   <a name="Glue-StartColumnStatisticsTaskRunSchedule-request-TableName"></a>
The name of the table for which to start a column statistic task run schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Elements
<a name="API_StartColumnStatisticsTaskRunSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartColumnStatisticsTaskRunSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StartColumnStatisticsTaskRunSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartColumnStatisticsTaskRunSchedule)
