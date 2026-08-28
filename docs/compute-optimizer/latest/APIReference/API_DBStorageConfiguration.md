---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_DBStorageConfiguration.html
---

# DBStorageConfiguration
<a name="API_DBStorageConfiguration"></a>

 The configuration of the recommended RDS storage.

## Contents
<a name="API_DBStorageConfiguration_Contents"></a>

 ** allocatedStorage **   <a name="computeoptimizer-Type-DBStorageConfiguration-allocatedStorage"></a>
 The size of the DB storage in gigabytes (GB).
Type: Integer
Required: No

 ** iops **   <a name="computeoptimizer-Type-DBStorageConfiguration-iops"></a>
 The provisioned IOPs of the DB storage.
Type: Integer
Required: No

 ** maxAllocatedStorage **   <a name="computeoptimizer-Type-DBStorageConfiguration-maxAllocatedStorage"></a>
 The maximum limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.
Type: Integer
Required: No

 ** storageThroughput **   <a name="computeoptimizer-Type-DBStorageConfiguration-storageThroughput"></a>
 The storage throughput of the DB storage.
Type: Integer
Required: No

 ** storageType **   <a name="computeoptimizer-Type-DBStorageConfiguration-storageType"></a>
 The type of DB storage.
Type: String
Required: No

## See Also
<a name="API_DBStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/DBStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/DBStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/DBStorageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
