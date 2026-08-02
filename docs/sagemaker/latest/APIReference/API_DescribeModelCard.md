---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelCard.html
---

# DescribeModelCard
<a name="API_DescribeModelCard"></a>

Describes the content, creation time, and security configuration of an Amazon SageMaker Model Card.

**Important**
To retrieve only metadata about a model card without requiring `kms:Decrypt` permission on the associated customer-managed AWS KMS key, set `IncludedData` to `MetadataOnly`. The default is `AllData`, which returns the full model card `Content` and requires `kms:Decrypt` permission when a customer-managed key is configured.

## Request Syntax
<a name="API_DescribeModelCard_RequestSyntax"></a>

```
{
   "IncludedData": "{{string}}",
   "ModelCardName": "{{string}}",
   "ModelCardVersion": {{number}}
}
```

## Request Parameters
<a name="API_DescribeModelCard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IncludedData](#API_DescribeModelCard_RequestSyntax) **   <a name="sagemaker-DescribeModelCard-request-IncludedData"></a>
Specifies the level of model card data to include in the response. Use this parameter to call `DescribeModelCard` without requiring `kms:Decrypt` permission on the customer-managed AWS KMS key.
+  `AllData`: Returns the full model card `Content`. This option requires `kms:Decrypt` permission on the customer-managed key, if one is associated with the model card. This is the default.
+  `MetadataOnly`: Returns the model card with sanitized `Content` that includes only a small set of unencrypted metadata fields. This option does not require `kms:Decrypt` permission. For the list of fields preserved in the response, see `Content`.
If you don't specify a value, SageMaker returns `AllData`.
Type: String
Valid Values: `AllData | MetadataOnly`
Required: No

 ** [ModelCardName](#API_DescribeModelCard_RequestSyntax) **   <a name="sagemaker-DescribeModelCard-request-ModelCardName"></a>
The name or Amazon Resource Name (ARN) of the model card to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:model-card/.*)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [ModelCardVersion](#API_DescribeModelCard_RequestSyntax) **   <a name="sagemaker-DescribeModelCard-request-ModelCardVersion"></a>
The version of the model card to describe. If a version is not provided, then the latest version of the model card is described.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeModelCard_ResponseSyntax"></a>

```
{
   "Content": "string",
   "CreatedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "CreationTime": number,
   "LastModifiedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "LastModifiedTime": number,
   "ModelCardArn": "string",
   "ModelCardName": "string",
   "ModelCardProcessingStatus": "string",
   "ModelCardStatus": "string",
   "ModelCardVersion": number,
   "SecurityConfig": {
      "KmsKeyId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeModelCard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Content](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-Content"></a>
The content of the model card. Content is provided as a string in the [model card JSON schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema).
When you set `IncludedData` to `MetadataOnly` in the request, SageMaker returns a sanitized version of `Content` that includes only the following JSON paths, when present in the model card:
+  `model_overview.model_id`
+  `model_overview.model_name`
+  `intended_uses.risk_rating`
+  `model_package_details.model_package_group_name`
+  `model_package_details.model_package_arn`
All other fields are removed from `Content` when `IncludedData` is `MetadataOnly`, including model description, training details, evaluation details, business details, and additional information. To retrieve the complete `Content`, set `IncludedData` to `AllData` or omit the parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100000.
Pattern: `.*`

 ** [CreatedBy](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-CreationTime"></a>
The date and time the model card was created.
Type: Timestamp

 ** [LastModifiedBy](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedTime](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-LastModifiedTime"></a>
The date and time the model card was last modified.
Type: Timestamp

 ** [ModelCardArn](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-ModelCardArn"></a>
The Amazon Resource Name (ARN) of the model card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-card/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ModelCardName](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-ModelCardName"></a>
The name of the model card.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ModelCardProcessingStatus](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-ModelCardProcessingStatus"></a>
The processing status of model card deletion. The `ModelCardProcessingStatus` updates throughout the different deletion steps.
+  `DeletePending`: Model card deletion request received.
+  `DeleteInProgress`: Model card deletion is in progress.
+  `ContentDeleted`: Deleted model card content.
+  `ExportJobsDeleted`: Deleted all export jobs associated with the model card.
+  `DeleteCompleted`: Successfully deleted the model card.
+  `DeleteFailed`: The model card failed to delete.
Type: String
Valid Values: `DeleteInProgress | DeletePending | ContentDeleted | ExportJobsDeleted | DeleteCompleted | DeleteFailed`

 ** [ModelCardStatus](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-ModelCardStatus"></a>
The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.
+  `Draft`: The model card is a work in progress.
+  `PendingReview`: The model card is pending review.
+  `Approved`: The model card is approved.
+  `Archived`: The model card is archived. No more updates should be made to the model card, but it can still be exported.
Type: String
Valid Values: `Draft | PendingReview | Approved | Archived`

 ** [ModelCardVersion](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-ModelCardVersion"></a>
The version of the model card.
Type: Integer

 ** [SecurityConfig](#API_DescribeModelCard_ResponseSyntax) **   <a name="sagemaker-DescribeModelCard-response-SecurityConfig"></a>
The security configuration used to protect model card content.
Type: [ModelCardSecurityConfig](API_ModelCardSecurityConfig.md) object

## Errors
<a name="API_DescribeModelCard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeModelCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeModelCard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeModelCard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeModelCard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeModelCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeModelCard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeModelCard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeModelCard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeModelCard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeModelCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeModelCard)
