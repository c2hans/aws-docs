---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/pricing_example_pricing_DescribeServices_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeServices` with a CLI
<a name="pricing_example_pricing_DescribeServices_section"></a>

The following code examples show how to use `DescribeServices`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve service metadata**
This example retrieves the metadata for the Amazon EC2 service code.
Command:

```
aws pricing describe-services --service-code {{AmazonEC2}} --format-version {{aws_v1}} --max-items {{1}}
```
Output:

```
{
  "Services": [
      {
          "ServiceCode": "AmazonEC2",
          "AttributeNames": [
              "volumeType",
              "maxIopsvolume",
              "instance",
              "instanceCapacity10xlarge",
              "locationType",
              "instanceFamily",
              "operatingSystem",
              "clockSpeed",
              "LeaseContractLength",
              "ecu",
              "networkPerformance",
              "instanceCapacity8xlarge",
              "group",
              "maxThroughputvolume",
              "gpuMemory",
              "ebsOptimized",
              "elasticGpuType",
              "maxVolumeSize",
              "gpu",
              "processorFeatures",
              "intelAvxAvailable",
              "instanceCapacity4xlarge",
              "servicecode",
              "groupDescription",
              "processorArchitecture",
              "physicalCores",
              "productFamily",
              "enhancedNetworkingSupported",
              "intelTurboAvailable",
              "memory",
              "dedicatedEbsThroughput",
              "vcpu",
              "OfferingClass",
              "instanceCapacityLarge",
              "capacitystatus",
              "termType",
              "storage",
              "intelAvx2Available",
              "storageMedia",
              "physicalProcessor",
              "provisioned",
              "servicename",
              "PurchaseOption",
              "instanceCapacity18xlarge",
              "instanceType",
              "tenancy",
              "usagetype",
              "normalizationSizeFactor",
              "instanceCapacity2xlarge",
              "instanceCapacity16xlarge",
              "maxIopsBurstPerformance",
              "instanceCapacity12xlarge",
              "instanceCapacity32xlarge",
              "instanceCapacityXlarge",
              "licenseModel",
              "currentGeneration",
              "preInstalledSw",
              "location",
              "instanceCapacity24xlarge",
              "instanceCapacity9xlarge",
              "instanceCapacityMedium",
              "operation"
          ]
      }
  ],
  "FormatVersion": "aws_v1"
}
```
+  For API details, see [DescribeServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pricing/describe-services.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns the metadata for all available service codes in the us-east-1 region.**

```
Get-PLSService -Region us-east-1
```
**Output:**

```
AttributeNames                                                  ServiceCode
--------------                                                  -----------
{productFamily, servicecode, groupDescription, termType...}     AWSBudgets
{productFamily, servicecode, termType, usagetype...}            AWSCloudTrail
{productFamily, servicecode, termType, usagetype...}            AWSCodeCommit
{productFamily, servicecode, termType, usagetype...}            AWSCodeDeploy
{productFamily, servicecode, termType, usagetype...}            AWSCodePipeline
{productFamily, servicecode, termType, usagetype...}            AWSConfig
...
```
**Example 2: Returns the metadata for the Amazon EC2 service in the us-east-1 region.**

```
Get-PLSService -ServiceCode AmazonEC2 -Region us-east-1
```
**Output:**

```
AttributeNames                                                         ServiceCode
--------------                                                         -----------
{volumeType, maxIopsvolume, instanceCapacity10xlarge, locationType...} AmazonEC2
```
+  For API details, see [DescribeServices](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns the metadata for all available service codes in the us-east-1 region.**

```
Get-PLSService -Region us-east-1
```
**Output:**

```
AttributeNames                                                  ServiceCode
--------------                                                  -----------
{productFamily, servicecode, groupDescription, termType...}     AWSBudgets
{productFamily, servicecode, termType, usagetype...}            AWSCloudTrail
{productFamily, servicecode, termType, usagetype...}            AWSCodeCommit
{productFamily, servicecode, termType, usagetype...}            AWSCodeDeploy
{productFamily, servicecode, termType, usagetype...}            AWSCodePipeline
{productFamily, servicecode, termType, usagetype...}            AWSConfig
...
```
**Example 2: Returns the metadata for the Amazon EC2 service in the us-east-1 region.**

```
Get-PLSService -ServiceCode AmazonEC2 -Region us-east-1
```
**Output:**

```
AttributeNames                                                         ServiceCode
--------------                                                         -----------
{volumeType, maxIopsvolume, instanceCapacity10xlarge, locationType...} AmazonEC2
```
+  For API details, see [DescribeServices](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
