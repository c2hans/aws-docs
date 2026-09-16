---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_GetLabels.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# GetLabels
<a name="API_GetLabels"></a>

Gets all labels or a specific label if name is provided. This is a paginated API. If you provide a null `maxResults`, this action retrieves a maximum of 50 records per page. If you provide a `maxResults`, the value must be between 10 and 50. To get the next page results, provide the pagination token from the `GetGetLabelsResponse` as part of your request. A null pagination token fetches the records from the beginning.

## Request Syntax
<a name="API_GetLabels_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "name": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetLabels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_GetLabels_RequestSyntax) **   <a name="FraudDetector-GetLabels-request-maxResults"></a>
The maximum number of objects to return for the request.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 50.
Required: No

 ** [name](#API_GetLabels_RequestSyntax) **   <a name="FraudDetector-GetLabels-request-name"></a>
The name of the label or labels to get.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** [nextToken](#API_GetLabels_RequestSyntax) **   <a name="FraudDetector-GetLabels-request-nextToken"></a>
The next token for the subsequent request.
Type: String
Required: No

## Response Syntax
<a name="API_GetLabels_ResponseSyntax"></a>

```
{
   "labels": [
      {
         "arn": "string",
         "createdTime": "string",
         "description": "string",
         "lastUpdatedTime": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetLabels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [labels](#API_GetLabels_ResponseSyntax) **   <a name="FraudDetector-GetLabels-response-labels"></a>
An array of labels.
Type: Array of [Label](API_Label.md) objects

 ** [nextToken](#API_GetLabels_ResponseSyntax) **   <a name="FraudDetector-GetLabels-response-nextToken"></a>
The next page token.
Type: String

## Errors
<a name="API_GetLabels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception indicating the specified resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_GetLabels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/GetLabels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/GetLabels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/GetLabels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/GetLabels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/GetLabels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/GetLabels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/GetLabels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/GetLabels)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/GetLabels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/GetLabels)
