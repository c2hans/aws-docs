---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrial.html
---

# DescribeTrial
<a name="API_DescribeTrial"></a>

Provides a list of a trial's properties.

## Request Syntax
<a name="API_DescribeTrial_RequestSyntax"></a>

```
{
   "TrialName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTrial_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrialName](#API_DescribeTrial_RequestSyntax) **   <a name="sagemaker-DescribeTrial-request-TrialName"></a>
The name of the trial to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_DescribeTrial_ResponseSyntax"></a>

```
{
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
   "DisplayName": "string",
   "ExperimentName": "string",
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
   "MetadataProperties": {
      "CommitId": "string",
      "GeneratedBy": "string",
      "ProjectId": "string",
      "Repository": "string"
   },
   "Source": {
      "SourceArn": "string",
      "SourceType": "string"
   },
   "TrialArn": "string",
   "TrialName": "string"
}
```

## Response Elements
<a name="API_DescribeTrial_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedBy](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-CreatedBy"></a>
Who created the trial.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-CreationTime"></a>
When the trial was created.
Type: Timestamp

 ** [DisplayName](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-DisplayName"></a>
The name of the trial as displayed. If `DisplayName` isn't specified, `TrialName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

 ** [ExperimentName](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-ExperimentName"></a>
The name of the experiment the trial is part of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

 ** [LastModifiedBy](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-LastModifiedBy"></a>
Who last modified the trial.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedTime](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-LastModifiedTime"></a>
When the trial was last modified.
Type: Timestamp

 ** [MetadataProperties](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object

 ** [Source](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-Source"></a>
The Amazon Resource Name (ARN) of the source and, optionally, the job type.
Type: [TrialSource](API_TrialSource.md) object

 ** [TrialArn](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-TrialArn"></a>
The Amazon Resource Name (ARN) of the trial.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial/.*`

 ** [TrialName](#API_DescribeTrial_ResponseSyntax) **   <a name="sagemaker-DescribeTrial-response-TrialName"></a>
The name of the trial.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

## Errors
<a name="API_DescribeTrial_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTrial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeTrial)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeTrial)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeTrial)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeTrial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeTrial)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeTrial)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeTrial)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeTrial)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeTrial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeTrial)
