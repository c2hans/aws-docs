---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeArtifact.html
---

# DescribeArtifact
<a name="API_DescribeArtifact"></a>

Describes an artifact.

## Request Syntax
<a name="API_DescribeArtifact_RequestSyntax"></a>

```
{
   "ArtifactArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeArtifact_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArtifactArn](#API_DescribeArtifact_RequestSyntax) **   <a name="sagemaker-DescribeArtifact-request-ArtifactArn"></a>
The Amazon Resource Name (ARN) of the artifact to describe.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:artifact/.*`
Required: Yes

## Response Syntax
<a name="API_DescribeArtifact_ResponseSyntax"></a>

```
{
   "ArtifactArn": "string",
   "ArtifactName": "string",
   "ArtifactType": "string",
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
   "LineageGroupArn": "string",
   "MetadataProperties": {
      "CommitId": "string",
      "GeneratedBy": "string",
      "ProjectId": "string",
      "Repository": "string"
   },
   "Properties": {
      "string" : "string"
   },
   "Source": {
      "SourceTypes": [
         {
            "SourceIdType": "string",
            "Value": "string"
         }
      ],
      "SourceUri": "string"
   }
}
```

## Response Elements
<a name="API_DescribeArtifact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArtifactArn](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-ArtifactArn"></a>
The Amazon Resource Name (ARN) of the artifact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:artifact/.*`

 ** [ArtifactName](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-ArtifactName"></a>
The name of the artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial|experiment-trial-component|artifact|action|context)\/)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,119})`

 ** [ArtifactType](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-ArtifactType"></a>
The type of the artifact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [CreatedBy](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-CreationTime"></a>
When the artifact was created.
Type: Timestamp

 ** [LastModifiedBy](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedTime](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-LastModifiedTime"></a>
When the artifact was last modified.
Type: Timestamp

 ** [LineageGroupArn](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-LineageGroupArn"></a>
The Amazon Resource Name (ARN) of the lineage group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:lineage-group/.*`

 ** [MetadataProperties](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object

 ** [Properties](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-Properties"></a>
A list of the artifact's properties.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 30 items.
Key Length Constraints: Minimum length of 0. Maximum length of 2500.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 2500.
Value Pattern: `.*`

 ** [Source](#API_DescribeArtifact_ResponseSyntax) **   <a name="sagemaker-DescribeArtifact-response-Source"></a>
The source of the artifact.
Type: [ArtifactSource](API_ArtifactSource.md) object

## Errors
<a name="API_DescribeArtifact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeArtifact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeArtifact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeArtifact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeArtifact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeArtifact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeArtifact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeArtifact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeArtifact)
