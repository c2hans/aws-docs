---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_pricing_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Price List examples using AWS CLI
<a name="cli_2_pricing_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Price List.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `describe-services`
<a name="pricing_DescribeServices_cli_2_topic"></a>

The following code example shows how to use `describe-services`.

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

### `get-attribute-values`
<a name="pricing_GetAttributeValues_cli_2_topic"></a>

The following code example shows how to use `get-attribute-values`.

**AWS CLI**
**To retrieve a list of attribute values**
The following `get-attribute-values` example retrieves a list of values available for the given attribute.

```
aws pricing get-attribute-values \
    --service-code {{AmazonEC2}} \
    --attribute-name {{volumeType}} \
    --max-items {{2}}
```
Output:

```
{
    "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ==",
    "AttributeValues": [
        {
            "Value": "Cold HDD"
        },
        {
            "Value": "General Purpose"
        }
    ]
}
```
+  For API details, see [GetAttributeValues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pricing/get-attribute-values.html) in *AWS CLI Command Reference*.

### `get-products`
<a name="pricing_GetProducts_cli_2_topic"></a>

The following code example shows how to use `get-products`.

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
