---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ResourceConfigurationDefinition.html
---

# ResourceConfigurationDefinition
<a name="API_ResourceConfigurationDefinition"></a>

Describes a resource configuration.

## Contents
<a name="API_ResourceConfigurationDefinition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** arnResource **   <a name="vpclattice-Type-ResourceConfigurationDefinition-arnResource"></a>
The Amazon Resource Name (ARN) of the resource.
Type: [ArnResource](API_ArnResource.md) object
Required: No

 ** dnsResource **   <a name="vpclattice-Type-ResourceConfigurationDefinition-dnsResource"></a>
The DNS name of the resource.
Type: [DnsResource](API_DnsResource.md) object
Required: No

 ** ipResource **   <a name="vpclattice-Type-ResourceConfigurationDefinition-ipResource"></a>
The IP resource.
Type: [IpResource](API_IpResource.md) object
Required: No

## See Also
<a name="API_ResourceConfigurationDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ResourceConfigurationDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ResourceConfigurationDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ResourceConfigurationDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
