---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_VpcEndpoint.html
---

# VpcEndpoint
<a name="API_VpcEndpoint"></a>

The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.

## Contents
<a name="API_VpcEndpoint_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** NetworkInterfaces.NetworkInterface.N **
One or more network interfaces of the endpoint. Also known as an interface endpoint.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Required: No

 ** VpcEndpointId **
The connection endpoint ID for connecting an Amazon Redshift cluster through the proxy.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** VpcId **
The VPC identifier that the endpoint is associated.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_VpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/VpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/VpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/VpcEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
