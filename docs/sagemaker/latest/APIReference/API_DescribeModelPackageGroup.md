---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelPackageGroup.html
---

# DescribeModelPackageGroup
<a name="API_DescribeModelPackageGroup"></a>

Gets a description for the specified model group.

## Request Syntax
<a name="API_DescribeModelPackageGroup_RequestSyntax"></a>

```
{
   "ModelPackageGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeModelPackageGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ModelPackageGroupName](#API_DescribeModelPackageGroup_RequestSyntax) **   <a name="sagemaker-DescribeModelPackageGroup-request-ModelPackageGroupName"></a>
The name of the model group to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)`
Required: Yes

## Response Syntax
<a name="API_DescribeModelPackageGroup_ResponseSyntax"></a>

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
   "ManagedConfiguration": {
      "ManagedStorageType": "string"
   },
   "ModelPackageGroupArn": "string",
   "ModelPackageGroupDescription": "string",
   "ModelPackageGroupName": "string",
   "ModelPackageGroupStatus": "string"
}
```

## Response Elements
<a name="API_DescribeModelPackageGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedBy](#API_DescribeModelPackageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackageGroup-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeModelPackageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackageGroup-response-CreationTime"></a>
The time that the model group was created.
Type: Timestamp

 ** [ManagedConfiguration](#API_DescribeModelPackageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackageGroup-response-ManagedConfiguration"></a>
The managed configuration of the model package group.
Type: [ManagedConfiguration](API_ManagedConfiguration.md) object

 ** [ModelPackageGroupArn](#API_DescribeModelPackageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackageGroup-response-ModelPackageGroupArn"></a>
The Amazon Resource Name (ARN) of the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package-group/[\S]{1,2048}`

 ** [ModelPackageGroupDescription](#API_DescribeModelPackageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackageGroup-response-ModelPackageGroupDescription"></a>
A description of the model group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`

 ** [ModelPackageGroupName](#API_DescribeModelPackageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackageGroup-response-ModelPackageGroupName"></a>
The name of the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [ModelPackageGroupStatus](#API_DescribeModelPackageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeModelPackageGroup-response-ModelPackageGroupStatus"></a>
The status of the model group.
Type: String
Valid Values: `Pending | InProgress | Completed | Failed | Deleting | DeleteFailed`

## Errors
<a name="API_DescribeModelPackageGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeModelPackageGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeModelPackageGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeModelPackageGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeModelPackageGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeModelPackageGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeModelPackageGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeModelPackageGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeModelPackageGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeModelPackageGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeModelPackageGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeModelPackageGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
