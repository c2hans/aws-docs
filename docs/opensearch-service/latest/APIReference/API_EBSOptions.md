---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_EBSOptions.html
---

# EBSOptions
<a name="API_EBSOptions"></a>

Container for the parameters required to enable EBS-based storage for an OpenSearch Service domain.

## Contents
<a name="API_EBSOptions_Contents"></a>

 ** EBSEnabled **   <a name="opensearchservice-Type-EBSOptions-EBSEnabled"></a>
Indicates whether EBS volumes are attached to data nodes in an OpenSearch Service domain.
Type: Boolean
Required: No

 ** Iops **   <a name="opensearchservice-Type-EBSOptions-Iops"></a>
Specifies the baseline input/output (I/O) performance of EBS volumes attached to data nodes. Applicable only for the `gp3` and provisioned IOPS EBS volume types.
Type: Integer
Required: No

 ** Throughput **   <a name="opensearchservice-Type-EBSOptions-Throughput"></a>
Specifies the throughput (in MiB/s) of the EBS volumes attached to data nodes. Applicable only for the `gp3` volume type.
Type: Integer
Required: No

 ** VolumeSize **   <a name="opensearchservice-Type-EBSOptions-VolumeSize"></a>
Specifies the size (in GiB) of EBS volumes attached to data nodes.
Type: Integer
Required: No

 ** VolumeType **   <a name="opensearchservice-Type-EBSOptions-VolumeType"></a>
Specifies the type of EBS volumes attached to data nodes.
Type: String
Valid Values: `standard | gp2 | io1 | gp3`
Required: No

## See Also
<a name="API_EBSOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/EBSOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/EBSOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/EBSOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
