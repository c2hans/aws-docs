---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeWorkteam.html
---

# DescribeWorkteam
<a name="API_DescribeWorkteam"></a>

Gets information about a specific work team. You can see information such as the creation date, the last updated date, membership information, and the work team's Amazon Resource Name (ARN).

## Request Syntax
<a name="API_DescribeWorkteam_RequestSyntax"></a>

```
{
   "WorkteamName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWorkteam_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WorkteamName](#API_DescribeWorkteam_RequestSyntax) **   <a name="sagemaker-DescribeWorkteam-request-WorkteamName"></a>
The name of the work team to return a description of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeWorkteam_ResponseSyntax"></a>

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
<a name="API_DescribeWorkteam_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Workteam](#API_DescribeWorkteam_ResponseSyntax) **   <a name="sagemaker-DescribeWorkteam-response-Workteam"></a>
A `Workteam` instance that contains information about the work team.
Type: [Workteam](API_Workteam.md) object

## Errors
<a name="API_DescribeWorkteam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeWorkteam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeWorkteam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeWorkteam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeWorkteam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeWorkteam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeWorkteam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeWorkteam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeWorkteam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeWorkteam)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeWorkteam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeWorkteam)
