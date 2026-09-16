---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeExperiment.html
---

# DescribeExperiment
<a name="API_DescribeExperiment"></a>

Provides a list of an experiment's properties.

## Request Syntax
<a name="API_DescribeExperiment_RequestSyntax"></a>

```
{
   "ExperimentName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeExperiment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExperimentName](#API_DescribeExperiment_RequestSyntax) **   <a name="sagemaker-DescribeExperiment-request-ExperimentName"></a>
The name of the experiment to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_DescribeExperiment_ResponseSyntax"></a>

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
   "Description": "string",
   "DisplayName": "string",
   "ExperimentArn": "string",
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
   "Source": {
      "SourceArn": "string",
      "SourceType": "string"
   }
}
```

## Response Elements
<a name="API_DescribeExperiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedBy](#API_DescribeExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeExperiment-response-CreatedBy"></a>
Who created the experiment.
Type: [UserContext](API_UserContext.md) object

 ** [Description](#API_DescribeExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeExperiment-response-Description"></a>
The description of the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`

 ** [DisplayName](#API_DescribeExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeExperiment-response-DisplayName"></a>
The name of the experiment as displayed. If `DisplayName` isn't specified, `ExperimentName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

 ** [ExperimentArn](#API_DescribeExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeExperiment-response-ExperimentArn"></a>
The Amazon Resource Name (ARN) of the experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment/.*`

 ** [ExperimentName](#API_DescribeExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeExperiment-response-ExperimentName"></a>
The name of the experiment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

 ** [LastModifiedBy](#API_DescribeExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeExperiment-response-LastModifiedBy"></a>
Who last modified the experiment.
Type: [UserContext](API_UserContext.md) object

 ** [Source](#API_DescribeExperiment_ResponseSyntax) **   <a name="sagemaker-DescribeExperiment-response-Source"></a>
The Amazon Resource Name (ARN) of the source and, optionally, the type.
Type: [ExperimentSource](API_ExperimentSource.md) object

## Errors
<a name="API_DescribeExperiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeExperiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeExperiment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeExperiment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeExperiment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeExperiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeExperiment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeExperiment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeExperiment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeExperiment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeExperiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeExperiment)
