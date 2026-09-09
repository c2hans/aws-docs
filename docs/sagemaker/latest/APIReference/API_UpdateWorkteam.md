---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkteam.html
---

# UpdateWorkteam
<a name="API_UpdateWorkteam"></a>

Updates an existing work team with new member definitions or description.

## Request Syntax
<a name="API_UpdateWorkteam_RequestSyntax"></a>

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
   "WorkerAccessConfiguration": {
      "S3Presign": {
         "IamPolicyConstraints": {
            "SourceIp": "{{string}}",
            "VpcSourceIp": "{{string}}"
         }
      }
   },
   "WorkteamName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateWorkteam_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateWorkteam_RequestSyntax) **   <a name="sagemaker-UpdateWorkteam-request-Description"></a>
An updated description for the work team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.+`
Required: No

 ** [MemberDefinitions](#API_UpdateWorkteam_RequestSyntax) **   <a name="sagemaker-UpdateWorkteam-request-MemberDefinitions"></a>
A list of `MemberDefinition` objects that contains objects that identify the workers that make up the work team.
Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use `CognitoMemberDefinition`. For workforces created using your own OIDC identity provider (IdP) use `OidcMemberDefinition`. You should not provide input for both of these parameters in a single request.
For workforces created using Amazon Cognito, private work teams correspond to Amazon Cognito *user groups* within the user pool used to create a workforce. All of the `CognitoMemberDefinition` objects that make up the member definition must have the same `ClientId` and `UserPool` values. To add a Amazon Cognito user group to an existing worker pool, see [Adding groups to a User Pool](). For more information about user pools, see [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).
For workforces created using your own OIDC IdP, specify the user groups that you want to include in your private work team in `OidcMemberDefinition` by listing those groups in `Groups`. Be aware that user groups that are already in the work team must also be listed in `Groups` when you make this request to remain on the work team. If you do not include these user groups, they will no longer be associated with the work team you update.
Type: Array of [MemberDefinition](API_MemberDefinition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [NotificationConfiguration](#API_UpdateWorkteam_RequestSyntax) **   <a name="sagemaker-UpdateWorkteam-request-NotificationConfiguration"></a>
Configures SNS topic notifications for available or expiring work items
Type: [NotificationConfiguration](API_NotificationConfiguration.md) object
Required: No

 ** [WorkerAccessConfiguration](#API_UpdateWorkteam_RequestSyntax) **   <a name="sagemaker-UpdateWorkteam-request-WorkerAccessConfiguration"></a>
Use this optional parameter to constrain access to an Amazon S3 resource based on the IP address using supported IAM global condition keys. The Amazon S3 resource is accessed in the worker portal using a Amazon S3 presigned URL.
Type: [WorkerAccessConfiguration](API_WorkerAccessConfiguration.md) object
Required: No

 ** [WorkteamName](#API_UpdateWorkteam_RequestSyntax) **   <a name="sagemaker-UpdateWorkteam-request-WorkteamName"></a>
The name of the work team to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_UpdateWorkteam_ResponseSyntax"></a>

```
{
   "Workteam": {
      "Description": "string",
      "MemberDefinitions": [
         {
            "CognitoMemberDefinition": {
               "ClientId": "string",
               "UserGroup": "string",
               "UserPool": "string"
            },
            "OidcMemberDefinition": {
               "Groups": [ "string" ]
            }
         }
      ],
      "NotificationConfiguration": {
         "NotificationTopicArn": "string"
      },
      "ProductListingIds": [ "string" ],
      "SubDomain": "string",
      "WorkerAccessConfiguration": {
         "S3Presign": {
            "IamPolicyConstraints": {
               "SourceIp": "string",
               "VpcSourceIp": "string"
            }
         }
      },
      "WorkforceArn": "string",
      "WorkteamArn": "string",
      "WorkteamName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateWorkteam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Workteam](#API_UpdateWorkteam_ResponseSyntax) **   <a name="sagemaker-UpdateWorkteam-response-Workteam"></a>
A `Workteam` object that describes the updated work team.
Type: [Workteam](API_Workteam.md) object

## Errors
<a name="API_UpdateWorkteam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_UpdateWorkteam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateWorkteam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateWorkteam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateWorkteam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateWorkteam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateWorkteam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateWorkteam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateWorkteam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateWorkteam)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateWorkteam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateWorkteam)
