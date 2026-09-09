---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeWorkforce.html
---

# DescribeWorkforce
<a name="API_DescribeWorkforce"></a>

Lists private workforce information, including workforce name, Amazon Resource Name (ARN), and, if applicable, allowed IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)). Allowable IP address ranges are the IP addresses that workers can use to access tasks.

**Important**
This operation applies only to private workforces.

## Request Syntax
<a name="API_DescribeWorkforce_RequestSyntax"></a>

```
{
   "WorkforceName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWorkforce_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WorkforceName](#API_DescribeWorkforce_RequestSyntax) **   <a name="sagemaker-DescribeWorkforce-request-WorkforceName"></a>
The name of the private workforce whose access you want to restrict. `WorkforceName` is automatically set to `default` when a workforce is created and cannot be modified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeWorkforce_ResponseSyntax"></a>

```
{
   "Workforce": {
      "CognitoConfig": {
         "ClientId": "string",
         "UserPool": "string"
      },
      "FailureReason": "string",
      "IpAddressType": "string",
      "OidcConfig": {
         "AuthenticationRequestExtraParams": {
            "string" : "string"
         },
         "AuthorizationEndpoint": "string",
         "ClientId": "string",
         "Issuer": "string",
         "JwksUri": "string",
         "LogoutEndpoint": "string",
         "Scope": "string",
         "TokenEndpoint": "string",
         "UserInfoEndpoint": "string"
      },
      "SourceIpConfig": {
         "Cidrs": [ "string" ]
      },
      "Status": "string",
      "SubDomain": "string",
      "WorkforceArn": "string",
      "WorkforceName": "string",
      "WorkforceVpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ],
         "VpcEndpointId": "string",
         "VpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeWorkforce_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Workforce](#API_DescribeWorkforce_ResponseSyntax) **   <a name="sagemaker-DescribeWorkforce-response-Workforce"></a>
A single private workforce, which is automatically created when you create your first private work team. You can create one private work force in each AWS Region. By default, any workforce-related API operation used in a specific region will apply to the workforce created in that region. To learn how to create a private workforce, see [Create a Private Workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html).
Type: [Workforce](API_Workforce.md) object

## Errors
<a name="API_DescribeWorkforce_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeWorkforce_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeWorkforce)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeWorkforce)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeWorkforce)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeWorkforce)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeWorkforce)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeWorkforce)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeWorkforce)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeWorkforce)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeWorkforce)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeWorkforce)
