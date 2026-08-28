---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableIpamInternetRegistryAssociation.html
---

# EnableIpamInternetRegistryAssociation
<a name="API_EnableIpamInternetRegistryAssociation"></a>

Enables Resource Public Key Infrastructure (RPKI) on an existing IPAM internet registry association by providing BGP Public Key Infrastructure (BPKI) certificate details. After enabling, you can create Route Origin Authorizations (ROAs) for prefixes registered with the internet registry.

## Request Parameters
<a name="API_EnableIpamInternetRegistryAssociation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ChildHandle**
The child handle for the BPKI certificate hierarchy from the Parent Response XML.
Type: String
Required: Yes

 **ClientToken**
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation ignores the request, but does not return an error.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamInternetRegistryAssociationId**
The ID of the IPAM internet registry association to enable.
Type: String
Required: Yes

 **ParentBpkiTa**
The parent BPKI Trust Anchor certificate in PEM format from the Parent Response XML.
Type: String
Required: Yes

 **ParentHandle**
The parent handle for the BPKI certificate hierarchy from the Parent Response XML.
Type: String
Required: Yes

 **RpkiVersion**
The RPKI version to use from the Parent Response XML.
Type: String
Required: Yes

 **ServiceUri**
The RPKI service URI for the publication point from the Parent Response XML.
Type: String
Required: Yes

## Response Elements
<a name="API_EnableIpamInternetRegistryAssociation_ResponseElements"></a>

The following elements are returned by the service.

 **ipamInternetRegistryAssociation**
Information about the enabled internet registry association.
Type: [IpamInternetRegistryAssociation](API_IpamInternetRegistryAssociation.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_EnableIpamInternetRegistryAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_EnableIpamInternetRegistryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableIpamInternetRegistryAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
