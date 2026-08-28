---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_4_pricing_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Price List examples using Tools for PowerShell V4
<a name="powershell_4_pricing_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with AWS Price List.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-PLSAttributeValue`
<a name="pricing_GetAttributeValues_powershell_4_topic"></a>

The following code example shows how to use `Get-PLSAttributeValue`.

**Tools for PowerShell V4**
**Example 1: Returns the values for the attribute 'volumeType' for Amazon EC2 in the us-east-1 region.**

```
Get-PLSAttributeValue -ServiceCode AmazonEC2 -AttributeName "volumeType" -region us-east-1
```
**Output:**

```
Value
-----
Cold HDD
General Purpose
Magnetic
Provisioned IOPS
Throughput Optimized HDD
```
+  For API details, see [GetAttributeValues](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-PLSProduct`
<a name="pricing_GetProducts_powershell_4_topic"></a>

The following code example shows how to use `Get-PLSProduct`.

**Tools for PowerShell V4**
**Example 1: Returns details of all products for Amazon EC2.**

```
Get-PLSProduct -ServiceCode AmazonEC2 -Region us-east-1
```
**Output:**

```
{"product":{"productFamily":"Compute Instance","attributes":{"enhancedNetworkingSupported":"Yes","memory":"30.5 GiB","dedicatedEbsThroughput":"800 Mbps","vcpu":"4","locationType":"AWS Region","storage":"EBS only","instanceFamily":"Memory optimized","operatingSystem":"SUSE","physicalProcessor":"Intel Xeon E5-2686 v4 (Broadwell)","clockSpeed":"2.3 GHz","ecu":"Variable","networkPerformance":"Up to 10 Gigabit","servicename":"Amazon Elastic Compute Cloud","instanceType":"r4.xlarge","tenancy":"Shared","usagetype":"USW2-BoxUsage:r4.xlarge","normalizationSizeFactor":"8","processorFeatures":"Intel AVX, Intel AVX2, Intel Turbo","servicecode":"AmazonEC2","licenseModel":"No License required","currentGeneration":"Yes","preInstalledSw":"NA","location":"US West (Oregon)","processorArchitecture":"64-bit","operation":"RunInstances:000g"},...
```
**Example 2: Returns data for Amazon EC2 in the us-east-1 region filtered by volume types of 'General Purpose' that are SSD-backed.**

```
Get-PLSProduct -ServiceCode AmazonEC2 -Filter @{Type="TERM_MATCH";Field="volumeType";Value="General Purpose"},@{Type="TERM_MATCH";Field="storageMedia";Value="SSD-backed"} -Region us-east-1
```
**Output:**

```
{"product":{"productFamily":"Storage","attributes":{"storageMedia":"SSD-backed","maxThroughputvolume":"160 MB/sec","volumeType":"General Purpose","maxIopsvolume":"10000",...
```
+  For API details, see [GetProducts](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-PLSService`
<a name="pricing_DescribeServices_powershell_4_topic"></a>

The following code example shows how to use `Get-PLSService`.

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
