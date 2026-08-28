---
source_url: https://docs.aws.amazon.com/MSKC/latest/mskc/API_CapacityUpdate.html
---

# CapacityUpdate
<a name="API_CapacityUpdate"></a>

The target capacity for the connector. The capacity can be auto scaled or provisioned.

## Contents
<a name="API_CapacityUpdate_Contents"></a>

 ** autoScaling **   <a name="MSKC-Type-CapacityUpdate-autoScaling"></a>
The target auto scaling setting.
Type: [AutoScalingUpdate](API_AutoScalingUpdate.md) object
Required: No

 ** provisionedCapacity **   <a name="MSKC-Type-CapacityUpdate-provisionedCapacity"></a>
The target settings for provisioned capacity.
Type: [ProvisionedCapacityUpdate](API_ProvisionedCapacityUpdate.md) object
Required: No

## See Also
<a name="API_CapacityUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/CapacityUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/CapacityUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/CapacityUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MSK Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MSKC` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
