---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceRequirementsWithMetadataRequest.html
---

# InstanceRequirementsWithMetadataRequest
<a name="API_InstanceRequirementsWithMetadataRequest"></a>

The architecture type, virtualization type, and other attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.

If you specify `InstanceRequirementsWithMetadataRequest`, you can't specify `InstanceTypes`.

## Contents
<a name="API_InstanceRequirementsWithMetadataRequest_Contents"></a>

 ** ArchitectureType.N **
The architecture type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `i386 | x86_64 | arm64 | x86_64_mac | arm64_mac`
Required: No

 ** InstanceRequirements **
The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.
Type: [InstanceRequirementsRequest](API_InstanceRequirementsRequest.md) object
Required: No

 ** VirtualizationType.N **
The virtualization type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `hvm | paravirtual`
Required: No

## See Also
<a name="API_InstanceRequirementsWithMetadataRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceRequirementsWithMetadataRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceRequirementsWithMetadataRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceRequirementsWithMetadataRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
