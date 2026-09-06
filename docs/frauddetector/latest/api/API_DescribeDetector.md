---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_DescribeDetector.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# DescribeDetector
<a name="API_DescribeDetector"></a>

Gets all versions for a specified detector.

## Request Syntax
<a name="API_DescribeDetector_RequestSyntax"></a>

```
{
   "detectorId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDetector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [detectorId](#API_DescribeDetector_RequestSyntax) **   <a name="FraudDetector-DescribeDetector-request-detectorId"></a>
The detector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** [maxResults](#API_DescribeDetector_RequestSyntax) **   <a name="FraudDetector-DescribeDetector-request-maxResults"></a>
The maximum number of results to return for the request.
Type: Integer
Valid Range: Minimum value of 1000. Maximum value of 2500.
Required: No

 ** [nextToken](#API_DescribeDetector_RequestSyntax) **   <a name="FraudDetector-DescribeDetector-request-nextToken"></a>
The next token from the previous response.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeDetector_ResponseSyntax"></a>

```
{
   "arn": "string",
   "detectorId": "string",
   "detectorVersionSummaries": [
      {
         "description": "string",
         "detectorVersionId": "string",
         "lastUpdatedTime": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDetector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DescribeDetector_ResponseSyntax) **   <a name="FraudDetector-DescribeDetector-response-arn"></a>
The detector ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`

 ** [detectorId](#API_DescribeDetector_ResponseSyntax) **   <a name="FraudDetector-DescribeDetector-response-detectorId"></a>
The detector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`

 ** [detectorVersionSummaries](#API_DescribeDetector_ResponseSyntax) **   <a name="FraudDetector-DescribeDetector-response-detectorVersionSummaries"></a>
The status and description for each detector version.
Type: Array of [DetectorVersionSummary](API_DetectorVersionSummary.md) objects

 ** [nextToken](#API_DescribeDetector_ResponseSyntax) **   <a name="FraudDetector-DescribeDetector-response-nextToken"></a>
The next token to be used for subsequent requests.
Type: String

## Errors
<a name="API_DescribeDetector_Errors"></a>

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
<a name="API_DescribeDetector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/DescribeDetector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/DescribeDetector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/DescribeDetector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/DescribeDetector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/DescribeDetector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/DescribeDetector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/DescribeDetector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/DescribeDetector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/DescribeDetector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/DescribeDetector)
