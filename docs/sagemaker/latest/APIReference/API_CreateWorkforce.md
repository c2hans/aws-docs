---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateWorkforce.html
---

# CreateWorkforce
<a name="API_CreateWorkforce"></a>

Use this operation to create a workforce. This operation will return an error if a workforce already exists in the AWS Region that you specify. You can only create one workforce in each AWS Region per AWS account.

If you want to create a new workforce in an AWS Region where a workforce already exists, use the [DeleteWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkforce.html) API operation to delete the existing workforce and then use `CreateWorkforce` to create a new workforce.

To create a private workforce using Amazon Cognito, you must specify a Cognito user pool in `CognitoConfig`. You can also create an Amazon Cognito workforce using the Amazon SageMaker console. For more information, see [ Create a Private Workforce (Amazon Cognito)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html).

To create a private workforce using your own OIDC Identity Provider (IdP), specify your IdP configuration in `OidcConfig`. Your OIDC IdP must support *groups* because groups are used by Ground Truth and Amazon A2I to create work teams. For more information, see [ Create a Private Workforce (OIDC IdP)](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private-oidc.html).

## Request Syntax
<a name="API_CreateWorkforce_RequestSyntax"></a>

```
{
   "CognitoConfig": {
      "ClientId": "{{string}}",
      "UserPool": "{{string}}"
   },
   "IpAddressType": "{{string}}",
   "OidcConfig": {
      "AuthenticationRequestExtraParams": {
         "{{string}}" : "{{string}}"
      },
      "AuthorizationEndpoint": "{{string}}",
      "ClientId": "{{string}}",
      "ClientSecret": "{{string}}",
      "Issuer": "{{string}}",
      "JwksUri": "{{string}}",
      "LogoutEndpoint": "{{string}}",
      "Scope": "{{string}}",
      "TokenEndpoint": "{{string}}",
      "UserInfoEndpoint": "{{string}}"
   },
   "SourceIpConfig": {
      "Cidrs": [ "{{string}}" ]
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "WorkforceName": "{{string}}",
   "WorkforceVpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "Subnets": [ "{{string}}" ],
      "VpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateWorkforce_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CognitoConfig](#API_CreateWorkforce_RequestSyntax) **   <a name="sagemaker-CreateWorkforce-request-CognitoConfig"></a>
Use this parameter to configure an Amazon Cognito private workforce. A single Cognito workforce is created using and corresponds to a single [ Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).
Do not use `OidcConfig` if you specify values for `CognitoConfig`.
Type: [CognitoConfig](API_CognitoConfig.md) object
Required: No

 ** [IpAddressType](#API_CreateWorkforce_RequestSyntax) **   <a name="sagemaker-CreateWorkforce-request-IpAddressType"></a>
Use this parameter to specify whether you want `IPv4` only or `dualstack` (`IPv4` and `IPv6`) to support your labeling workforce.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** [OidcConfig](#API_CreateWorkforce_RequestSyntax) **   <a name="sagemaker-CreateWorkforce-request-OidcConfig"></a>
Use this parameter to configure a private workforce using your own OIDC Identity Provider.
Do not use `CognitoConfig` if you specify values for `OidcConfig`.
Type: [OidcConfig](API_OidcConfig.md) object
Required: No

 ** [SourceIpConfig](#API_CreateWorkforce_RequestSyntax) **   <a name="sagemaker-CreateWorkforce-request-SourceIpConfig"></a>
A list of IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)). Used to create an allow list of IP addresses for a private workforce. Workers will only be able to log in to their worker portal from an IP address within this range. By default, a workforce isn't restricted to specific IP addresses.
Type: [SourceIpConfig](API_SourceIpConfig.md) object
Required: No

 ** [Tags](#API_CreateWorkforce_RequestSyntax) **   <a name="sagemaker-CreateWorkforce-request-Tags"></a>
An array of key-value pairs that contain metadata to help you categorize and organize our workforce. Each tag consists of a key and a value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [WorkforceName](#API_CreateWorkforce_RequestSyntax) **   <a name="sagemaker-CreateWorkforce-request-WorkforceName"></a>
The name of the private workforce.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]){0,62}`
Required: Yes

 ** [WorkforceVpcConfig](#API_CreateWorkforce_RequestSyntax) **   <a name="sagemaker-CreateWorkforce-request-WorkforceVpcConfig"></a>
Use this parameter to configure a workforce using VPC.
Type: [WorkforceVpcConfigRequest](API_WorkforceVpcConfigRequest.md) object
Required: No

## Response Syntax
<a name="API_CreateWorkforce_ResponseSyntax"></a>

```
{
   "WorkforceArn": "string"
}
```

## Response Elements
<a name="API_CreateWorkforce_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkforceArn](#API_CreateWorkforce_ResponseSyntax) **   <a name="sagemaker-CreateWorkforce-response-WorkforceArn"></a>
The Amazon Resource Name (ARN) of the workforce.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:workforce/.*`

## Errors
<a name="API_CreateWorkforce_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateWorkforce_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateWorkforce)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateWorkforce)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateWorkforce)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateWorkforce)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateWorkforce)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateWorkforce)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateWorkforce)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateWorkforce)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateWorkforce)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateWorkforce)
