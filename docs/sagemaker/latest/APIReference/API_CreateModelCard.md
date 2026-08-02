---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelCard.html
---

# CreateModelCard
<a name="API_CreateModelCard"></a>

Creates an Amazon SageMaker Model Card.

For information about how to use model cards, see [Amazon SageMaker Model Card](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html).

## Request Syntax
<a name="API_CreateModelCard_RequestSyntax"></a>

```
{
   "Content": "{{string}}",
   "ModelCardName": "{{string}}",
   "ModelCardStatus": "{{string}}",
   "SecurityConfig": {
      "KmsKeyId": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateModelCard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Content](#API_CreateModelCard_RequestSyntax) **   <a name="sagemaker-CreateModelCard-request-Content"></a>
The content of the model card. Content must be in [model card JSON schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema) and provided as a string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100000.
Pattern: `.*`
Required: Yes

 ** [ModelCardName](#API_CreateModelCard_RequestSyntax) **   <a name="sagemaker-CreateModelCard-request-ModelCardName"></a>
The unique name of the model card.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ModelCardStatus](#API_CreateModelCard_RequestSyntax) **   <a name="sagemaker-CreateModelCard-request-ModelCardStatus"></a>
The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.
+  `Draft`: The model card is a work in progress.
+  `PendingReview`: The model card is pending review.
+  `Approved`: The model card is approved.
+  `Archived`: The model card is archived. No more updates should be made to the model card, but it can still be exported.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`
Required: Yes

 ** [SecurityConfig](#API_CreateModelCard_RequestSyntax) **   <a name="sagemaker-CreateModelCard-request-SecurityConfig"></a>
An optional Key Management Service key to encrypt, decrypt, and re-encrypt model card content for regulated workloads with highly sensitive data.
Type: [ModelCardSecurityConfig](API_ModelCardSecurityConfig.md) object
Required: No

 ** [Tags](#API_CreateModelCard_RequestSyntax) **   <a name="sagemaker-CreateModelCard-request-Tags"></a>
Key-value pairs used to manage metadata for model cards.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateModelCard_ResponseSyntax"></a>

```
{
   "ModelCardArn": "string"
}
```

## Response Elements
<a name="API_CreateModelCard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelCardArn](#API_CreateModelCard_ResponseSyntax) **   <a name="sagemaker-CreateModelCard-response-ModelCardArn"></a>
The Amazon Resource Name (ARN) of the successfully created model card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateModelCard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateModelCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateModelCard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateModelCard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateModelCard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateModelCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateModelCard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateModelCard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateModelCard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateModelCard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateModelCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateModelCard)
