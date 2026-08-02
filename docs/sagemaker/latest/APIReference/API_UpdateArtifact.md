---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateArtifact.html
---

# UpdateArtifact
<a name="API_UpdateArtifact"></a>

Updates an artifact.

## Request Syntax
<a name="API_UpdateArtifact_RequestSyntax"></a>

```
{
   "ArtifactArn": "{{string}}",
   "ArtifactName": "{{string}}",
   "Properties": {
      "{{string}}" : "{{string}}"
   },
   "PropertiesToRemove": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateArtifact_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArtifactArn](#API_UpdateArtifact_RequestSyntax) **   <a name="sagemaker-UpdateArtifact-request-ArtifactArn"></a>
The Amazon Resource Name (ARN) of the artifact to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:artifact/.*`
Required: Yes

 ** [ArtifactName](#API_UpdateArtifact_RequestSyntax) **   <a name="sagemaker-UpdateArtifact-request-ArtifactName"></a>
The new name for the artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** [Properties](#API_UpdateArtifact_RequestSyntax) **   <a name="sagemaker-UpdateArtifact-request-Properties"></a>
The new list of properties. Overwrites the current property list.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2500.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Value Pattern: `.*`
Required: No

 ** [PropertiesToRemove](#API_UpdateArtifact_RequestSyntax) **   <a name="sagemaker-UpdateArtifact-request-PropertiesToRemove"></a>
A list of properties to remove.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 2500.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_UpdateArtifact_ResponseSyntax"></a>

```
{
   "ArtifactArn": "string"
}
```

## Response Elements
<a name="API_UpdateArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArtifactArn](#API_UpdateArtifact_ResponseSyntax) **   <a name="sagemaker-UpdateArtifact-response-ArtifactArn"></a>
The Amazon Resource Name (ARN) of the artifact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:artifact/.*`

## Errors
<a name="API_UpdateArtifact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateArtifact)
