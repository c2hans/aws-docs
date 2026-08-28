---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeLineageGroup.html
---

# DescribeLineageGroup
<a name="API_DescribeLineageGroup"></a>

Provides a list of properties for the requested lineage group. For more information, see [ Cross-Account Lineage Tracking ](https://docs.aws.amazon.com/sagemaker/latest/dg/xaccount-lineage-tracking.html) in the *Amazon SageMaker Developer Guide*.

## Request Syntax
<a name="API_DescribeLineageGroup_RequestSyntax"></a>

```
{
   "LineageGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLineageGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LineageGroupName](#API_DescribeLineageGroup_RequestSyntax) **   <a name="sagemaker-DescribeLineageGroup-request-LineageGroupName"></a>
The name of the lineage group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_DescribeLineageGroup_ResponseSyntax"></a>

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
   "Description": "string",
   "DisplayName": "string",
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
   "LineageGroupName": "string"
}
```

## Response Elements
<a name="API_DescribeLineageGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedBy](#API_DescribeLineageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeLineageGroup-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeLineageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeLineageGroup-response-CreationTime"></a>
The creation time of lineage group.
Type: Timestamp

 ** [Description](#API_DescribeLineageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeLineageGroup-response-Description"></a>
The description of the lineage group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`

 ** [DisplayName](#API_DescribeLineageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeLineageGroup-response-DisplayName"></a>
The display name of the lineage group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

 ** [LastModifiedBy](#API_DescribeLineageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeLineageGroup-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedTime](#API_DescribeLineageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeLineageGroup-response-LastModifiedTime"></a>
The last modified time of the lineage group.
Type: Timestamp

 ** [LineageGroupArn](#API_DescribeLineageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeLineageGroup-response-LineageGroupArn"></a>
The Amazon Resource Name (ARN) of the lineage group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:lineage-group/.*`

 ** [LineageGroupName](#API_DescribeLineageGroup_ResponseSyntax) **   <a name="sagemaker-DescribeLineageGroup-response-LineageGroupName"></a>
The name of the lineage group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

## Errors
<a name="API_DescribeLineageGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeLineageGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeLineageGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeLineageGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeLineageGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeLineageGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeLineageGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeLineageGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeLineageGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeLineageGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeLineageGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeLineageGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
