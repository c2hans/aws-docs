---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListColumnStatisticsTaskRuns.html
---

# ListColumnStatisticsTaskRuns
<a name="API_ListColumnStatisticsTaskRuns"></a>

List all task runs for a particular account.

## Request Syntax
<a name="API_ListColumnStatisticsTaskRuns_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListColumnStatisticsTaskRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListColumnStatisticsTaskRuns_RequestSyntax) **   <a name="Glue-ListColumnStatisticsTaskRuns-request-MaxResults"></a>
The maximum size of the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListColumnStatisticsTaskRuns_RequestSyntax) **   <a name="Glue-ListColumnStatisticsTaskRuns-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_ListColumnStatisticsTaskRuns_ResponseSyntax"></a>

```
{
   "ColumnStatisticsTaskRunIds": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListColumnStatisticsTaskRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ColumnStatisticsTaskRunIds](#API_ListColumnStatisticsTaskRuns_ResponseSyntax) **   <a name="Glue-ListColumnStatisticsTaskRuns-response-ColumnStatisticsTaskRunIds"></a>
A list of column statistics task run IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [NextToken](#API_ListColumnStatisticsTaskRuns_ResponseSyntax) **   <a name="Glue-ListColumnStatisticsTaskRuns-response-NextToken"></a>
A continuation token, if not all task run IDs have yet been returned.
Type: String

## Errors
<a name="API_ListColumnStatisticsTaskRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListColumnStatisticsTaskRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListColumnStatisticsTaskRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListColumnStatisticsTaskRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListColumnStatisticsTaskRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListColumnStatisticsTaskRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListColumnStatisticsTaskRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListColumnStatisticsTaskRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListColumnStatisticsTaskRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListColumnStatisticsTaskRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListColumnStatisticsTaskRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListColumnStatisticsTaskRuns)
