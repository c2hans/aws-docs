---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateArtifact.html
---

# CreateArtifact
<a name="API_CreateArtifact"></a>

Creates an *artifact*. An artifact is a lineage tracking entity that represents a URI addressable object or data. Some examples are the S3 URI of a dataset and the ECR registry path of an image. For more information, see [Amazon SageMaker ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html).

## Request Syntax
<a name="API_CreateArtifact_RequestSyntax"></a>

```
{
   "ArtifactName": "{{string}}",
   "ArtifactType": "{{string}}",
   "MetadataProperties": {
      "CommitId": "{{string}}",
      "GeneratedBy": "{{string}}",
      "ProjectId": "{{string}}",
      "Repository": "{{string}}"
   },
   "Properties": {
      "{{string}}" : "{{string}}"
   },
   "Source": {
      "SourceTypes": [
         {
            "SourceIdType": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "SourceUri": "{{string}}"
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
<a name="API_CreateArtifact_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArtifactName](#API_CreateArtifact_RequestSyntax) **   <a name="sagemaker-CreateArtifact-request-ArtifactName"></a>
The name of the artifact. Must be unique to your account in an AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** [ArtifactType](#API_CreateArtifact_RequestSyntax) **   <a name="sagemaker-CreateArtifact-request-ArtifactType"></a>
The artifact type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [MetadataProperties](#API_CreateArtifact_RequestSyntax) **   <a name="sagemaker-CreateArtifact-request-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object
Required: No

 ** [Properties](#API_CreateArtifact_RequestSyntax) **   <a name="sagemaker-CreateArtifact-request-Properties"></a>
A list of properties to add to the artifact.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2500.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Value Pattern: `.*`
Required: No

 ** [Source](#API_CreateArtifact_RequestSyntax) **   <a name="sagemaker-CreateArtifact-request-Source"></a>
The ID, ID type, and URI of the source.
Type: [ArtifactSource](API_ArtifactSource.md) object
Required: Yes

 ** [Tags](#API_CreateArtifact_RequestSyntax) **   <a name="sagemaker-CreateArtifact-request-Tags"></a>
A list of tags to apply to the artifact.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateArtifact_ResponseSyntax"></a>

```
{
   "ArtifactArn": "string"
}
```

## Response Elements
<a name="API_CreateArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArtifactArn](#API_CreateArtifact_ResponseSyntax) **   <a name="sagemaker-CreateArtifact-response-ArtifactArn"></a>
The Amazon Resource Name (ARN) of the artifact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:artifact/.*`

## Errors
<a name="API_CreateArtifact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateArtifact)
