---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

A resource is one of the following: the ARN for an AWS resource that is supported by AWS Global Accelerator to be added as an endpoint, or a CIDR range that specifies a bring your own IP (BYOIP) address pool.

## Contents
<a name="API_Resource_Contents"></a>

 ** Cidr **   <a name="globalaccelerator-Type-Resource-Cidr"></a>
An IP address range, in CIDR format, that is specified as resource. The address must be provisioned and advertised in AWS Global Accelerator by following the bring your own IP address (BYOIP) process for Global Accelerator
 For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the AWS Global Accelerator Developer Guide.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** EndpointId **   <a name="globalaccelerator-Type-Resource-EndpointId"></a>
The endpoint ID for the endpoint that is specified as a AWS resource.
An endpoint ID for the cross-account feature is the ARN of an AWS resource, such as a Network Load Balancer, that Global Accelerator supports as an endpoint for an accelerator.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** Region **   <a name="globalaccelerator-Type-Resource-Region"></a>
The AWS Region where a shared endpoint resource is located.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
