---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/application-ous.html
---

# Application OUs
<a name="application-ous"></a>

## Workloads OU
<a name="workloads-ou"></a>

 The Workloads OU is intended to house most of your business-specific workloads including both production and non-production environments. These workloads can be a mix of commercial off-the-shelf (COTS) applications and your own internally developed custom applications and data services.

 Workloads in this OU often include shared application and data services that are used by other workloads.

### Example structure
<a name="example-structure-2"></a>

 The following example represents a basic structure in which sets of workloads owned by diverse business units or teams reside in two child OUs: Prod and Test. In this example, a common governance and operating model applies across those areas. The data-lake-prod account shown in this example contains data services that are shared with other production workloads and accounts.

 For general guidance on separating production and non-production workloads and resources, refer to [Organizing workload-oriented OUs](advanced-ous.md#organizing-workload-oriented-ous).

![Diagram showing example structure of Workloads OU](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-workloads-ou.png)
