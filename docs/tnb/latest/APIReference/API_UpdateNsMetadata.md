---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateNsMetadata.html
---

# UpdateNsMetadata
<a name="API_UpdateNsMetadata"></a>

Metadata related to the configuration properties used during update of a network instance.

## Contents
<a name="API_UpdateNsMetadata_Contents"></a>

 ** nsdInfoId **   <a name="TNB-Type-UpdateNsMetadata-nsdInfoId"></a>
The network service descriptor used for updating the network instance.
Type: String
Pattern: `np-[a-f0-9]{17}`
Required: Yes

 ** additionalParamsForNs **   <a name="TNB-Type-UpdateNsMetadata-additionalParamsForNs"></a>
The configurable properties used during update.
Type: JSON value
Required: No

## See Also
<a name="API_UpdateNsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/UpdateNsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/UpdateNsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/UpdateNsMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
