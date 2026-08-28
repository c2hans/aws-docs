---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ValidStorageOptions.html
---

# ValidStorageOptions
<a name="API_ValidStorageOptions"></a>

Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the `DescribeValidDBInstanceModifications` action.

## Contents
<a name="API_ValidStorageOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IopsToStorageRatio.DoubleRange.N **
The valid range of Provisioned IOPS to gibibytes of storage multiplier. For example, 3-10, which means that provisioned IOPS can be between 3 and 10 times storage.
Type: Array of [DoubleRange](API_DoubleRange.md) objects
Required: No

 ** ProvisionedIops.Range.N **
The valid range of provisioned IOPS. For example, 1000-256,000.
Type: Array of [Range](API_Range.md) objects
Required: No

 ** ProvisionedStorageThroughput.Range.N **
The valid range of provisioned storage throughput. For example, 500-4,000 mebibytes per second (MiBps).
Type: Array of [Range](API_Range.md) objects
Required: No

 ** StorageSize.Range.N **
The valid range of storage in gibibytes (GiB). For example, 100 to 16,384.
Type: Array of [Range](API_Range.md) objects
Required: No

 ** StorageThroughputToIopsRatio.DoubleRange.N **
The valid range of storage throughput to provisioned IOPS ratios. For example, 0-0.25.
Type: Array of [DoubleRange](API_DoubleRange.md) objects
Required: No

 ** StorageType **
The valid storage types for your DB instance. For example: gp2, gp3, io1, io2.
Type: String
Required: No

 ** SupportsStorageAutoscaling **
Indicates whether or not Amazon RDS can automatically scale storage for DB instances that use the new instance class.
Type: Boolean
Required: No

## See Also
<a name="API_ValidStorageOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ValidStorageOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ValidStorageOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ValidStorageOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
