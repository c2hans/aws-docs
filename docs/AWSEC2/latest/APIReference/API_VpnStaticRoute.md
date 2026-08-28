---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnStaticRoute.html
---

# VpnStaticRoute
<a name="API_VpnStaticRoute"></a>

Describes a static route for a VPN connection.

## Contents
<a name="API_VpnStaticRoute_Contents"></a>

 ** destinationCidrBlock **
The CIDR block associated with the local subnet of the customer data center.
Type: String
Required: No

 ** source **
Indicates how the routes were provided.
Type: String
Valid Values: `Static`
Required: No

 ** state **
The current state of the static route.
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

## See Also
<a name="API_VpnStaticRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpnStaticRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpnStaticRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpnStaticRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
