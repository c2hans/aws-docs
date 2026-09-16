---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateModelCard.html
---

# UpdateModelCard
<a name="API_UpdateModelCard"></a>

Update an Amazon SageMaker Model Card.

**Important**
You cannot update both model card content and model card status in a single call.

## Request Syntax
<a name="API_UpdateModelCard_RequestSyntax"></a>

```
{
   "Content": "{{string}}",
   "ModelCardName": "{{string}}",
   "ModelCardStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateModelCard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Content](#API_UpdateModelCard_RequestSyntax) **   <a name="sagemaker-UpdateModelCard-request-Content"></a>
The updated model card content. Content must be in [model card JSON schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema) and provided as a string.
When updating model card content, be sure to include the full content and not just updated content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100000.
Pattern: `.*`
Required: No

 ** [ModelCardName](#API_UpdateModelCard_RequestSyntax) **   <a name="sagemaker-UpdateModelCard-request-ModelCardName"></a>
The name or Amazon Resource Name (ARN) of the model card to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model-card/.*)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [ModelCardStatus](#API_UpdateModelCard_RequestSyntax) **   <a name="sagemaker-UpdateModelCard-request-ModelCardStatus"></a>
The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.
+  `Draft`: The model card is a work in progress.
+  `PendingReview`: The model card is pending review.
+  `Approved`: The model card is approved.
+  `Archived`: The model card is archived. No more updates should be made to the model card, but it can still be exported.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`
Required: No

## Response Syntax
<a name="API_UpdateModelCard_ResponseSyntax"></a>

```
{
   "ModelCardArn": "string"
}
```

## Response Elements
<a name="API_UpdateModelCard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelCardArn](#API_UpdateModelCard_ResponseSyntax) **   <a name="sagemaker-UpdateModelCard-response-ModelCardArn"></a>
The Amazon Resource Name (ARN) of the updated model card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_UpdateModelCard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateModelCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateModelCard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateModelCard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateModelCard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateModelCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateModelCard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateModelCard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateModelCard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateModelCard)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateModelCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateModelCard)
