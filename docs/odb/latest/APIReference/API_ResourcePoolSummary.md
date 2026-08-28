---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ResourcePoolSummary.html
---

# ResourcePoolSummary
<a name="API_ResourcePoolSummary"></a>

The configuration of a resource pool for an Autonomous Database.

## Contents
<a name="API_ResourcePoolSummary_Contents"></a>

 ** availableComputeCapacity **   <a name="odb-Type-ResourcePoolSummary-availableComputeCapacity"></a>
The available compute capacity in the resource pool.
Type: Integer
Required: No

 ** availableStorageCapacityInTBs **   <a name="odb-Type-ResourcePoolSummary-availableStorageCapacityInTBs"></a>
The available storage capacity in the resource pool, in TB.
Type: Double
Required: No

 ** isDisabled **   <a name="odb-Type-ResourcePoolSummary-isDisabled"></a>
Indicates whether the resource pool is disabled.
Type: Boolean
Required: No

 ** poolSize **   <a name="odb-Type-ResourcePoolSummary-poolSize"></a>
The number of Autonomous Databases that the resource pool can contain.
Type: Integer
Required: No

 ** poolStorageSizeInTBs **   <a name="odb-Type-ResourcePoolSummary-poolStorageSizeInTBs"></a>
The total storage size of the resource pool, in terabytes (TB).
Type: Integer
Required: No

 ** totalComputeCapacity **   <a name="odb-Type-ResourcePoolSummary-totalComputeCapacity"></a>
The total compute capacity of the resource pool.
Type: Integer
Required: No

## See Also
<a name="API_ResourcePoolSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ResourcePoolSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ResourcePoolSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ResourcePoolSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
