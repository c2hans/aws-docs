---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_TagResource.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# TagResource
<a name="API_TagResource"></a>

Assigns tags to a resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "resourceARN": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceARN](#API_TagResource_RequestSyntax) **   <a name="FraudDetector-TagResource-request-resourceARN"></a>
The resource ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: Yes

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="FraudDetector-TagResource-request-tags"></a>
The tags to assign to the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

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
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/TagResource)
