---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkforce.html
---

# UpdateWorkforce
<a name="API_UpdateWorkforce"></a>

Use this operation to update your workforce. You can use this operation to require that workers use specific IP addresses to work on tasks and to update your OpenID Connect (OIDC) Identity Provider (IdP) workforce configuration.

The worker portal is now supported in VPC and public internet.

 Use `SourceIpConfig` to restrict worker access to tasks to a specific range of IP addresses. You specify allowed IP addresses by creating a list of up to ten [CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html). By default, a workforce isn't restricted to specific IP addresses. If you specify a range of IP addresses, workers who attempt to access tasks using any IP address outside the specified range are denied and get a `Not Found` error message on the worker portal.

To restrict public internet access for all workers, configure the `SourceIpConfig` CIDR value. For example, when using `SourceIpConfig` with an `IpAddressType` of `IPv4`, you can restrict access to the IPv4 CIDR block "10.0.0.0/16". When using an `IpAddressType` of `dualstack`, you can specify both the IPv4 and IPv6 CIDR blocks, such as "10.0.0.0/16" for IPv4 only, "2001:db8:1234:1a00::/56" for IPv6 only, or "10.0.0.0/16" and "2001:db8:1234:1a00::/56" for dual stack.

**Important**
Amazon SageMaker does not support Source Ip restriction for worker portals in VPC.

Use `OidcConfig` to update the configuration of a workforce created using your own OIDC IdP.

**Important**
You can only update your OIDC IdP configuration when there are no work teams associated with your workforce. You can delete work teams using the [DeleteWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkteam.html) operation.

After restricting access to a range of IP addresses or updating your OIDC IdP configuration with this operation, you can view details about your update workforce using the [DescribeWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeWorkforce.html) operation.

**Important**
This operation only applies to private workforces.

## Request Syntax
<a name="API_UpdateWorkforce_RequestSyntax"></a>

```
{
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
   "WorkforceName": "{{string}}",
   "WorkforceVpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "Subnets": [ "{{string}}" ],
      "VpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateWorkforce_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IpAddressType](#API_UpdateWorkforce_RequestSyntax) **   <a name="sagemaker-UpdateWorkforce-request-IpAddressType"></a>
Use this parameter to specify whether you want `IPv4` only or `dualstack` (`IPv4` and `IPv6`) to support your labeling workforce.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** [OidcConfig](#API_UpdateWorkforce_RequestSyntax) **   <a name="sagemaker-UpdateWorkforce-request-OidcConfig"></a>
Use this parameter to update your OIDC Identity Provider (IdP) configuration for a workforce made using your own IdP.
Type: [OidcConfig](API_OidcConfig.md) object
Required: No

 ** [SourceIpConfig](#API_UpdateWorkforce_RequestSyntax) **   <a name="sagemaker-UpdateWorkforce-request-SourceIpConfig"></a>
A list of one to ten worker IP address ranges ([CIDRs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)) that can be used to access tasks assigned to this workforce.
Maximum: Ten CIDR values
Type: [SourceIpConfig](API_SourceIpConfig.md) object
Required: No

 ** [WorkforceName](#API_UpdateWorkforce_RequestSyntax) **   <a name="sagemaker-UpdateWorkforce-request-WorkforceName"></a>
The name of the private workforce that you want to update. You can find your workforce name by using the [ListWorkforces](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListWorkforces.html) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]){0,62}`
Required: Yes

 ** [WorkforceVpcConfig](#API_UpdateWorkforce_RequestSyntax) **   <a name="sagemaker-UpdateWorkforce-request-WorkforceVpcConfig"></a>
Use this parameter to update your VPC configuration for a workforce.
Type: [WorkforceVpcConfigRequest](API_WorkforceVpcConfigRequest.md) object
Required: No

## Response Syntax
<a name="API_UpdateWorkforce_ResponseSyntax"></a>

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
<a name="API_UpdateWorkforce_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Workforce](#API_UpdateWorkforce_ResponseSyntax) **   <a name="sagemaker-UpdateWorkforce-response-Workforce"></a>
A single private workforce. You can create one private work force in each AWS Region. By default, any workforce-related API operation used in a specific region will apply to the workforce created in that region. To learn how to create a private workforce, see [Create a Private Workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html).
Type: [Workforce](API_Workforce.md) object

## Errors
<a name="API_UpdateWorkforce_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

## See Also
<a name="API_UpdateWorkforce_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateWorkforce)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateWorkforce)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateWorkforce)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateWorkforce)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateWorkforce)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateWorkforce)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateWorkforce)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateWorkforce)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateWorkforce)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateWorkforce)
