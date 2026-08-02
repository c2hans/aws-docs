---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamScope.html
---

# CreateIpamScope
<a name="API_CreateIpamScope"></a>

Create an IPAM scope. In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict.

For more information, see [Add a scope](https://docs.aws.amazon.com/vpc/latest/ipam/add-scope-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Request Parameters
<a name="API_CreateIpamScope_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **Description**
A description for the scope you're creating.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ExternalAuthorityConfiguration**
The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external system and the external resource identifier that identifies your account or instance in that system.
In IPAM, an external authority is a third-party IP address management system that provides CIDR blocks when you provision address space for top-level IPAM pools. This allows you to use your existing IP management system to control which address ranges are allocated to AWS while using Amazon VPC IPAM to manage subnets within those ranges.
Type: [ExternalAuthorityConfiguration](API_ExternalAuthorityConfiguration.md) object
Required: No

 **IpamId**
The ID of the IPAM for which you're creating this scope.
Type: String
Required: Yes

 **TagSpecification.N**
The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateIpamScope_ResponseElements"></a>

The following elements are returned by the service.

 **ipamScope**
Information about the created scope.
Type: [IpamScope](API_IpamScope.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateIpamScope_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateIpamScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateIpamScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateIpamScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateIpamScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateIpamScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateIpamScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateIpamScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateIpamScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateIpamScope)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateIpamScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateIpamScope)
