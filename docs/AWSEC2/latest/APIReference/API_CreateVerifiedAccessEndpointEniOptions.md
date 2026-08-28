---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessEndpointEniOptions.html
---

# CreateVerifiedAccessEndpointEniOptions
<a name="API_CreateVerifiedAccessEndpointEniOptions"></a>

Describes the network interface options when creating an AWS Verified Access endpoint using the `network-interface` type.

## Contents
<a name="API_CreateVerifiedAccessEndpointEniOptions_Contents"></a>

 ** NetworkInterfaceId **
The ID of the network interface.
Type: String
Required: No

 ** Port **
The IP port number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** PortRange.N **
The port ranges.
Type: Array of [CreateVerifiedAccessEndpointPortRange](API_CreateVerifiedAccessEndpointPortRange.md) objects
Required: No

 ** Protocol **
The IP protocol.
Type: String
Valid Values: `http | https | tcp`
Required: No

## See Also
<a name="API_CreateVerifiedAccessEndpointEniOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVerifiedAccessEndpointEniOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVerifiedAccessEndpointEniOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVerifiedAccessEndpointEniOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
