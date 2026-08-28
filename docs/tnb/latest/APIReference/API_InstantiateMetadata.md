---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_InstantiateMetadata.html
---

# InstantiateMetadata
<a name="API_InstantiateMetadata"></a>

Metadata related to the configuration properties used during instantiation of the network instance.

## Contents
<a name="API_InstantiateMetadata_Contents"></a>

 ** nsdInfoId **   <a name="TNB-Type-InstantiateMetadata-nsdInfoId"></a>
The network service descriptor used for instantiating the network instance.
Type: String
Pattern: `np-[a-f0-9]{17}`
Required: Yes

 ** additionalParamsForNs **   <a name="TNB-Type-InstantiateMetadata-additionalParamsForNs"></a>
The configurable properties used during instantiation.
Type: JSON value
Required: No

## See Also
<a name="API_InstantiateMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/InstantiateMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/InstantiateMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/InstantiateMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
