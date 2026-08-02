---
source_url: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-sc.html
---

# Service Catalog in AWS GovCloud (US)
<a name="govcloud-sc"></a>

AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. AWS Service Catalog allows you to centrally manage commonly deployed IT services, and helps you achieve consistent governance and meet your compliance requirements, while enabling users to quickly deploy only the approved IT services they need.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West)
+  AWS GovCloud (US-East)

## How Service Catalog differs
<a name="govcloud-sc-diffs"></a>

The following differences apply to Service Catalog:
+ In AWS GovCloud (US) Copy Product is only supported within AWS GovCloud (US) Regions in the GovCloud partition.
+ Stack Sets are not currently supported.

## Documentation
<a name="govcloud-sc-docs"></a>

 [AWS Service Catalog documentation](https://docs.aws.amazon.com/servicecatalog/index.html).

## Export-controlled content
<a name="govcloud-sc-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ No export-controlled data may be entered, stored, or processed by AWS Service Catalog. For example, AWS Service Catalog metadata is not permitted to contain export-controlled data. This metadata includes all the configuration data that you enter when creating and maintaining your Products, Actions, and Tag Options.
