---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_GetListsMetadata.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# GetListsMetadata
<a name="API_GetListsMetadata"></a>

 Gets the metadata of either all the lists under the account or the specified list.

## Request Syntax
<a name="API_GetListsMetadata_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "name": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetListsMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_GetListsMetadata_RequestSyntax) **   <a name="FraudDetector-GetListsMetadata-request-maxResults"></a>
 The maximum number of objects to return for the request.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 50.
Required: No

 ** [name](#API_GetListsMetadata_RequestSyntax) **   <a name="FraudDetector-GetListsMetadata-request-name"></a>
 The name of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: No

 ** [nextToken](#API_GetListsMetadata_RequestSyntax) **   <a name="FraudDetector-GetListsMetadata-request-nextToken"></a>
 The next token for the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_GetListsMetadata_ResponseSyntax"></a>

```
{
   "lists": [
      {
         "arn": "string",
         "createdTime": "string",
         "description": "string",
         "name": "string",
         "updatedTime": "string",
         "variableType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetListsMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lists](#API_GetListsMetadata_ResponseSyntax) **   <a name="FraudDetector-GetListsMetadata-response-lists"></a>
 The metadata of the specified list or all lists under the account.
Type: Array of [AllowDenyList](API_AllowDenyList.md) objects

 ** [nextToken](#API_GetListsMetadata_ResponseSyntax) **   <a name="FraudDetector-GetListsMetadata-response-nextToken"></a>
 The next page token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_GetListsMetadata_Errors"></a>

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
<a name="API_GetListsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/GetListsMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/GetListsMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/GetListsMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/GetListsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/GetListsMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/GetListsMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/GetListsMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/GetListsMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/GetListsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/GetListsMetadata)
