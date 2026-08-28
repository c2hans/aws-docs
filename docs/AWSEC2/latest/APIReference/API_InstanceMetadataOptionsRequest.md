---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceMetadataOptionsRequest.html
---

# InstanceMetadataOptionsRequest
<a name="API_InstanceMetadataOptionsRequest"></a>

The metadata options for the instance.

## Contents
<a name="API_InstanceMetadataOptionsRequest_Contents"></a>

 ** HttpEndpoint **
Enables or disables the HTTP metadata endpoint on your instances.
If you specify a value of `disabled`, you cannot access your instance metadata.
Default: `enabled`
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** HttpProtocolIpv6 **
Enables or disables the IPv6 endpoint for the instance metadata service.
Default: `disabled`
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** HttpPutResponseHopLimit **
The maximum number of hops that the metadata token can travel.
Possible values: Integers from 1 to 64
Type: Integer
Required: No

 ** HttpTokens **
Indicates whether IMDSv2 is required.
+  `optional` - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.
+  `required` - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.
Default:
+ If the value of `ImdsSupport` for the Amazon Machine Image (AMI) for your instance is `v2.0` and the account level default is set to `no-preference`, the default is `required`.
+ If the value of `ImdsSupport` for the Amazon Machine Image (AMI) for your instance is `v2.0`, but the account level default is set to `V1 or V2`, the default is `optional`.
The default value can also be affected by other combinations of parameters. For more information, see [Order of precedence for instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#instance-metadata-options-order-of-precedence) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `optional | required`
Required: No

 ** InstanceMetadataTags **
Set to `enabled` to allow access to instance tags from the instance metadata. Set to `disabled` to turn off access to instance tags from the instance metadata. For more information, see [View tags for your EC2 instances using instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html).
Default: `disabled`
Type: String
Valid Values: `disabled | enabled`
Required: No

## See Also
<a name="API_InstanceMetadataOptionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceMetadataOptionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceMetadataOptionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceMetadataOptionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
