---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteArtifact.html
---

# DeleteArtifact
<a name="API_DeleteArtifact"></a>

Deletes an artifact. Either `ArtifactArn` or `Source` must be specified.

## Request Syntax
<a name="API_DeleteArtifact_RequestSyntax"></a>

```
{
   "ArtifactArn": "{{string}}",
   "Source": {
      "SourceTypes": [
         {
            "SourceIdType": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "SourceUri": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_DeleteArtifact_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArtifactArn](#API_DeleteArtifact_RequestSyntax) **   <a name="sagemaker-DeleteArtifact-request-ArtifactArn"></a>
The Amazon Resource Name (ARN) of the artifact to delete.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:artifact/.*`
Required: No

 ** [Source](#API_DeleteArtifact_RequestSyntax) **   <a name="sagemaker-DeleteArtifact-request-Source"></a>
The URI of the source.
Type: [ArtifactSource](API_ArtifactSource.md) object
Required: No

## Response Syntax
<a name="API_DeleteArtifact_ResponseSyntax"></a>

```
{
   "ArtifactArn": "string"
}
```

## Response Elements
<a name="API_DeleteArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArtifactArn](#API_DeleteArtifact_ResponseSyntax) **   <a name="sagemaker-DeleteArtifact-response-ArtifactArn"></a>
The Amazon Resource Name (ARN) of the artifact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:artifact/.*`

## Errors
<a name="API_DeleteArtifact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteArtifact)
