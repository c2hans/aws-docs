---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/pricing_example_pricing_GetProducts_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetProducts` with a CLI
<a name="pricing_example_pricing_GetProducts_section"></a>

The following code examples show how to use `GetProducts`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve a list of products**
This example retrieves a list of products that match the given criteria.
Command:

```
aws pricing get-products --filters {{file://filters.json}} --format-version {{aws_v1}} --max-results {{1}} --service-code {{AmazonEC2}}
```
filters.json:

```
        [
  {
    "Type": "TERM_MATCH",
    "Field": "ServiceCode",
    "Value": "AmazonEC2"
  },
  {
    "Type": "TERM_MATCH",
    "Field": "volumeType",
    "Value": "Provisioned IOPS"
  }
]
```
Output:

```
{
  "FormatVersion": "aws_v1",
  "NextToken": "WGDY7ko8fQXdlaUZVdasFQ==:RVSagyIFn770XQOzdUIcO9BY6ucBG9itXAZGZF/zioUzOsUKh6PCcPWaOyPZRiMePb986TeoKYB9l55fw/CyoMq5ymnGmT1Vj39TljbbAlhcqnVfTmPIilx8Uy5bdDaBYy/e/2Ofw9Edzsykbs8LTBuNbiDQ+BBds5yeI9AQkUepruKk3aEahFPxJ55kx/zk",
  "PriceList": [
      "{\"product\":{\"productFamily\":\"Storage\",\"attributes\":{\"storageMedia\":\"SSD-backed\",\"maxThroughputvolume\":\"320 MB/sec\",\"volumeType\":\"Provisioned IOPS\",\"maxIopsvolume\":\"20000\",\"servicecode\":\"AmazonEC2\",\"usagetype\":\"APS1-EBS:VolumeUsage.piops\",\"locationType\":\"AWS Region\",\"location\":\"Asia Pacific (Singapore)\",\"servicename\":\"Amazon Elastic Compute Cloud\",\"maxVolumeSize\":\"16 TiB\",\"operation\":\"\"},\"sku\":\"3MKHN58N7RDDVGKJ\"},\"serviceCode\":\"AmazonEC2\",\"terms\":{\"OnDemand\":{\"3MKHN58N7RDDVGKJ.JRTCKXETXF\":{\"priceDimensions\":{\"3MKHN58N7RDDVGKJ.JRTCKXETXF.6YS6EN2CT7\":{\"unit\":\"GB-Mo\",\"endRange\":\"Inf\",\"description\":\"$0.138 per GB-month of Provisioned IOPS SSD (io1)  provisioned storage - Asia Pacific (Singapore)\",\"appliesTo\":[],\"rateCode\":\"3MKHN58N7RDDVGKJ.JRTCKXETXF.6YS6EN2CT7\",\"beginRange\":\"0\",\"pricePerUnit\":{\"USD\":\"0.1380000000\"}}},\"sku\":\"3MKHN58N7RDDVGKJ\",\"effectiveDate\":\"2018-08-01T00:00:00Z\",\"offerTermCode\":\"JRTCKXETXF\",\"termAttributes\":{}}}},\"version\":\"20180808005701\",\"publicationDate\":\"2018-08-08T00:57:01Z\"}"
  ]
}
```
+  For API details, see [GetProducts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pricing/get-products.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

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

**Tools for PowerShell V5**
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
+  For API details, see [GetProducts](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
