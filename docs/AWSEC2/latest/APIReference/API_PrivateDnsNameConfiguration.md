---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PrivateDnsNameConfiguration.html
---

# PrivateDnsNameConfiguration
<a name="API_PrivateDnsNameConfiguration"></a>

Information about the private DNS name for the service endpoint.

## Contents
<a name="API_PrivateDnsNameConfiguration_Contents"></a>

 ** name **
The name of the record subdomain the service provider needs to create. The service provider adds the `value` text to the `name`.
Type: String
Required: No

 ** state **
The verification state of the VPC endpoint service.
Consumers of the endpoint service can use the private name only when the state is `verified`.
Type: String
Valid Values: `pendingVerification | verified | failed`
Required: No

 ** type **
The endpoint service verification type, for example TXT.
Type: String
Required: No

 ** value **
The value the service provider adds to the private DNS name domain record before verification.
Type: String
Required: No

## See Also
<a name="API_PrivateDnsNameConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PrivateDnsNameConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PrivateDnsNameConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PrivateDnsNameConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
