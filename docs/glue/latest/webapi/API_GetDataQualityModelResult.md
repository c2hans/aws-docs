---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDataQualityModelResult.html
---

# GetDataQualityModelResult
<a name="API_GetDataQualityModelResult"></a>

Retrieve a statistic's predictions for a given Profile ID.

## Request Syntax
<a name="API_GetDataQualityModelResult_RequestSyntax"></a>

```
{
   "ProfileId": "{{string}}",
   "StatisticId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDataQualityModelResult_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProfileId](#API_GetDataQualityModelResult_RequestSyntax) **   <a name="Glue-GetDataQualityModelResult-request-ProfileId"></a>
The Profile ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [StatisticId](#API_GetDataQualityModelResult_RequestSyntax) **   <a name="Glue-GetDataQualityModelResult-request-StatisticId"></a>
The Statistic ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetDataQualityModelResult_ResponseSyntax"></a>

```
{
   "CompletedOn": number,
   "Model": [
      {
         "ActualValue": number,
         "Date": number,
         "InclusionAnnotation": "string",
         "LowerBound": number,
         "PredictedValue": number,
         "UpperBound": number
      }
   ]
}
```

## Response Elements
<a name="API_GetDataQualityModelResult_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompletedOn](#API_GetDataQualityModelResult_ResponseSyntax) **   <a name="Glue-GetDataQualityModelResult-response-CompletedOn"></a>
The timestamp when the data quality model training completed.
Type: Timestamp

 ** [Model](#API_GetDataQualityModelResult_ResponseSyntax) **   <a name="Glue-GetDataQualityModelResult-response-Model"></a>
A list of `StatisticModelResult`
Type: Array of [StatisticModelResult](API_StatisticModelResult.md) objects

## Errors
<a name="API_GetDataQualityModelResult_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

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
<a name="API_GetDataQualityModelResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDataQualityModelResult)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDataQualityModelResult)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDataQualityModelResult)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDataQualityModelResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDataQualityModelResult)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDataQualityModelResult)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDataQualityModelResult)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDataQualityModelResult)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDataQualityModelResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDataQualityModelResult)
