---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_S3OnDeviceServiceConfiguration.html
---

# S3OnDeviceServiceConfiguration
<a name="API_S3OnDeviceServiceConfiguration"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Amazon S3 compatible storage on Snowball Edge devices configuration items.

## Contents
<a name="API_S3OnDeviceServiceConfiguration_Contents"></a>

 ** FaultTolerance **   <a name="Snowball-Type-S3OnDeviceServiceConfiguration-FaultTolerance"></a>
>Fault tolerance level of the cluster. This indicates the number of nodes that can go down without degrading the performance of the cluster. This additional input helps when the specified `StorageLimit` matches more than one Amazon S3 compatible storage on Snowball Edge devices service configuration.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 4.
Required: No

 ** ServiceSize **   <a name="Snowball-Type-S3OnDeviceServiceConfiguration-ServiceSize"></a>
Applicable when creating a cluster. Specifies how many nodes are needed for Amazon S3 compatible storage on Snowball Edge devices. If specified, the other input can be omitted.
Type: Integer
Valid Range: Minimum value of 3. Maximum value of 16.
Required: No

 ** StorageLimit **   <a name="Snowball-Type-S3OnDeviceServiceConfiguration-StorageLimit"></a>
If the specified storage limit value matches storage limit of one of the defined configurations, that configuration will be used. If the specified storage limit value does not match any defined configuration, the request will fail. If more than one configuration has the same storage limit as specified, the other input need to be provided.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** StorageUnit **   <a name="Snowball-Type-S3OnDeviceServiceConfiguration-StorageUnit"></a>
Storage unit. Currently the only supported unit is TB.
Type: String
Valid Values: `TB`
Required: No

## See Also
<a name="API_S3OnDeviceServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/S3OnDeviceServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/S3OnDeviceServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/S3OnDeviceServiceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
