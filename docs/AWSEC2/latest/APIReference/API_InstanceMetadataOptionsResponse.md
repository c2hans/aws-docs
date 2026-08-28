---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceMetadataOptionsResponse.html
---

# InstanceMetadataOptionsResponse
<a name="API_InstanceMetadataOptionsResponse"></a>

The metadata options for the instance.

## Contents
<a name="API_InstanceMetadataOptionsResponse_Contents"></a>

 ** httpEndpoint **
Indicates whether the HTTP metadata endpoint on your instances is enabled or disabled.
If the value is `disabled`, you cannot access your instance metadata.
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** httpProtocolIpv6 **
Indicates whether the IPv6 endpoint for the instance metadata service is enabled or disabled.
Default: `disabled`
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** httpPutResponseHopLimit **
The maximum number of hops that the metadata token can travel.
Possible values: Integers from `1` to `64`
Type: Integer
Required: No

 ** httpTokens **
Indicates whether IMDSv2 is required.
+  `optional` - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.
+  `required` - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.
Type: String
Valid Values: `optional | required`
Required: No

 ** instanceMetadataTags **
Indicates whether access to instance tags from the instance metadata is enabled or disabled. For more information, see [View tags for your EC2 instances using instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html).
Type: String
Valid Values: `disabled | enabled`
Required: No

 ** state **
The state of the metadata option changes.
 `pending` - The metadata options are being updated and the instance is not ready to process metadata traffic with the new selection.
 `applied` - The metadata options have been successfully applied on the instance.
Type: String
Valid Values: `pending | applied`
Required: No

## See Also
<a name="API_InstanceMetadataOptionsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceMetadataOptionsResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceMetadataOptionsResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceMetadataOptionsResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
