---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateWorkteam.html
---

# CreateWorkteam
<a name="API_CreateWorkteam"></a>

Creates a new work team for labeling your data. A work team is defined by one or more Amazon Cognito user pools. You must first create the user pools before you can create a work team.

You cannot create more than 25 work teams in an account and region.

## Request Syntax
<a name="API_CreateWorkteam_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "MemberDefinitions": [
      {
         "CognitoMemberDefinition": {
            "ClientId": "{{string}}",
            "UserGroup": "{{string}}",
            "UserPool": "{{string}}"
         },
         "OidcMemberDefinition": {
            "Groups": [ "{{string}}" ]
         }
      }
   ],
   "NotificationConfiguration": {
      "NotificationTopicArn": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "WorkerAccessConfiguration": {
      "S3Presign": {
         "IamPolicyConstraints": {
            "SourceIp": "{{string}}",
            "VpcSourceIp": "{{string}}"
         }
      }
   },
   "WorkforceName": "{{string}}",
   "WorkteamName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateWorkteam_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateWorkteam_RequestSyntax) **   <a name="sagemaker-CreateWorkteam-request-Description"></a>
A description of the work team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.+`
Required: Yes

 ** [MemberDefinitions](#API_CreateWorkteam_RequestSyntax) **   <a name="sagemaker-CreateWorkteam-request-MemberDefinitions"></a>
A list of `MemberDefinition` objects that contains objects that identify the workers that make up the work team.
Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use `CognitoMemberDefinition`. For workforces created using your own OIDC identity provider (IdP) use `OidcMemberDefinition`. Do not provide input for both of these parameters in a single request.
For workforces created using Amazon Cognito, private work teams correspond to Amazon Cognito *user groups* within the user pool used to create a workforce. All of the `CognitoMemberDefinition` objects that make up the member definition must have the same `ClientId` and `UserPool` values. To add a Amazon Cognito user group to an existing worker pool, see [Adding groups to a User Pool](). For more information about user pools, see [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).
For workforces created using your own OIDC IdP, specify the user groups that you want to include in your private work team in `OidcMemberDefinition` by listing those groups in `Groups`.
Type: Array of [MemberDefinition](API_MemberDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [NotificationConfiguration](#API_CreateWorkteam_RequestSyntax) **   <a name="sagemaker-CreateWorkteam-request-NotificationConfiguration"></a>
Configures notification of workers regarding available or expiring work items.
Type: [NotificationConfiguration](API_NotificationConfiguration.md) object
Required: No

 ** [Tags](#API_CreateWorkteam_RequestSyntax) **   <a name="sagemaker-CreateWorkteam-request-Tags"></a>
An array of key-value pairs.
For more information, see [Resource Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) and [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what) in the * AWS Billing and Cost Management User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [WorkerAccessConfiguration](#API_CreateWorkteam_RequestSyntax) **   <a name="sagemaker-CreateWorkteam-request-WorkerAccessConfiguration"></a>
Use this optional parameter to constrain access to an Amazon S3 resource based on the IP address using supported IAM global condition keys. The Amazon S3 resource is accessed in the worker portal using a Amazon S3 presigned URL.
Type: [WorkerAccessConfiguration](API_WorkerAccessConfiguration.md) object
Required: No

 ** [WorkforceName](#API_CreateWorkteam_RequestSyntax) **   <a name="sagemaker-CreateWorkteam-request-WorkforceName"></a>
The name of the workforce.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]){0,62}`
Required: No

 ** [WorkteamName](#API_CreateWorkteam_RequestSyntax) **   <a name="sagemaker-CreateWorkteam-request-WorkteamName"></a>
The name of the work team. Use this name to identify the work team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_CreateWorkteam_ResponseSyntax"></a>

```
{
   "WorkteamArn": "string"
}
```

## Response Elements
<a name="API_CreateWorkteam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkteamArn](#API_CreateWorkteam_ResponseSyntax) **   <a name="sagemaker-CreateWorkteam-response-WorkteamArn"></a>
The Amazon Resource Name (ARN) of the work team. You can use this ARN to identify the work team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workteam/.*`

## Errors
<a name="API_CreateWorkteam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateWorkteam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateWorkteam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateWorkteam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateWorkteam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateWorkteam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateWorkteam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateWorkteam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateWorkteam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateWorkteam)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateWorkteam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateWorkteam)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
