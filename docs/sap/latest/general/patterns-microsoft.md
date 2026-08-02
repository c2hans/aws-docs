---
source_url: https://docs.aws.amazon.com/sap/latest/general/patterns-microsoft.html
---

# SAP on AWS architecture patterns for Microsoft SQL server
<a name="patterns-microsoft"></a>

This document provides information about architecture patterns for deploying SAP workloads in AWS Cloud on Microsoft SQL servers. These patterns offer highly available and resilient implementation options while considering your recovery time and point objectives.

Work backwards from your business requirements to define an approach that meets the availability goals of your SAP systems and data. For each failure scenario, the resiliency requirements, acceptable data loss, and mean time to recover need to be proportionate to the criticality of the component and the supported business applications.

You can customize these patterns for your specific business criteria. You should consider the risk and impact of each failure type, and the cost of mitigation when choosing a pattern.

**Topics**
+ [Patterns](#patterns)
+ [Comparison matrix](#comparison)
+ [Single Region architecture patterns for Microsoft SQL server](single-region.md)
+ [Multi-Region patterns for Microsoft SQL server](multi-region.md)

## Patterns
<a name="patterns"></a>

The architecture patterns are divided into two categories.
+  [Single Region patterns](https://docs.aws.amazon.com/sap/latest/general/single-region.html)
+  [Multi-Region patterns](https://docs.aws.amazon.com/sap/latest/general/multi-region.html)

## Comparison matrix
<a name="comparison"></a>

The following table provides a comparison of all the architecture patterns discussed further.

<table>
<tbody>
  <tr><td rowspan="2"> **Patterns** </td><td colspan="3"> **Business requirements** </td><td colspan="2"> **Solution characteristics** </td><td colspan="2"> **Implementation details** </td></tr>
  <tr><td> **Resilience type** </td><td> **Recovery point objective** </td><td> **Recovery time objective** </td><td> **Cost** </td><td> **Complexity** </td><td> **SQL AlwaysOn** </td><td> **Amazon S3 replication** </td></tr>
  <tr><td>Pattern 1</td><td rowspan="2">Single Region disaster recovery</td><td>Near zero\*</td><td>Low</td><td>Medium</td><td>Medium</td><td>2-tier</td><td>N/A</td></tr>
  <tr><td>Pattern 2</td><td>Medium</td><td>High</td><td>Very low</td><td>Very low</td><td>N/A</td><td>N/A</td></tr>
  <tr><td>Pattern 3</td><td rowspan="4">Multi-Region disaster recovery</td><td>Medium</td><td>High</td><td>Medium</td><td>Medium</td><td>2-tier</td><td>Cross Region</td></tr>
  <tr><td>Pattern 4</td><td>Near zero\*</td><td>Low</td><td>High</td><td>High</td><td>3-tier</td><td>Cross Region</td></tr>
  <tr><td>Pattern 5</td><td>Medium</td><td>High</td><td>Low</td><td>Low</td><td>N/A</td><td>Cross Region</td></tr>
  <tr><td>Pattern 6</td><td>Low</td><td>Low</td><td>Medium</td><td>Medium</td><td>N/A</td><td>N/A</td></tr>
</tbody>
</table>

 *\*To achieve near zero recovery point objective, database replication must be setup in synchronous data commit mode within the same AWS Region.*
