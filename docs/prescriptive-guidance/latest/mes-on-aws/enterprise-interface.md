---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/enterprise-interface.html
---

# Interface with other enterprise applications
<a name="enterprise-interface"></a>

Because MES sits at the edge of operational technology (OT) and information technology (IT), it must interact with enterprise applications and OT data sources. Depending on the organizational solution landscape, MES can interact with ERP to get production and purchase order information, master data about parts and products, inventory availability, and bill of materials. MES would also report back to ERP for the status of orders, actual material and labor consumption during production, and machine status. If PLM is present, MES can interact with it to get a detailed bill of process (BOP), work instructions, and, in some cases, the bill of materials (BOM). MES would also report to PLM about process execution information, non-conformances, and BOM variations.

## Architecture
<a name="enterprise-interface-architecture"></a>

Considering the wide variety of PLM and ERP systems, the design for this pattern varies, based on the systems MES interacts with. The following diagram illustrates a sample architecture.

![MES architecture for interfacing with other enterprise applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/73000135-5c37-429c-aaeb-9e0ca9b6902d.png)

1. Organizations might have ERP instances in the AWS Cloud or elsewhere.

1. As with ERP, a PLM system could be in the AWS Cloud or elsewhere.

1. Organizations can import data from ERP and PLM to an Amazon Simple Storage Service (Amazon S3) bucket. If those systems are hosted in the AWS Cloud, the file vault might be another S3 bucket and can be replicated for MES. Another way to connect to those applications is through the API by using Amazon API Gateway.

1. Regardless of how organizations import the data from ERP and PLM, an AWS Lambda function can process the received information and route the data to microservice databases, because the ERP and PLM interfaces and this type of data processing are primarily event-driven.
