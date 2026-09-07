---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/gaining-insights-from-manufacturing-data.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Gaining insights from manufacturing data
<a name="gaining-insights-from-manufacturing-data"></a>

Manufacturers embrace the cloud to deliver digital innovation that scales across the enterprise, and want to leverage the cloud to holistically analyze and extract insights from the manufacturing data. In combination, the AWS Cloud and edge services address these use cases by helping manufacturers ingest, structure, and store data from a variety of current and legacy systems and equipment, and create a combined single source of contextual data set. This data allows for holistic analysis and easy consumption to digitally transform and improve business operations. The following figure shows the typical steps to get insights from factory data.

![A diagram showing data to insights.](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/images/data-to-insights.png)

*Data to insights*

Extracting, structuring, and ingesting data from OT resources to the cloud is the first step to enabling data analysis. AWS has a variety of analytics services in the cloud for processing, analyzing, and generating insights, but the ingestion stage requires hybrid components and interaction with OT resources. Following are some of the key AWS services to enable data ingestion from an OT environment (levels 1-3) to the cloud. Refer to this [Manufacturing on AWS](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/manufacturing-on-aws-ra.pdf) reference architecture diagram for visual representation.
+  [**AWS IoT Core**](https://aws.amazon.com/iot-core/) — Ingest data from the IoT device via [MQTT](https://mqtt.org/).
+  **[AWS IoT Greengrass](https://aws.amazon.com/greengrass/)** — Ingest data from legacy and IoT devices via MQTT, or various inbuilt / custom connectors and [AWS Lambda](https://aws.amazon.com/lambda/) functions.
+  **[AWS IoT SiteWise](https://aws.amazon.com/iot-sitewise/)** — Collect, organize, and analyze machine data using [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/), [EtherNet/IP](https://www.odva.org/technology-standards/key-technologies/ethernet-ip/), [Modbus](https://modbus.org/), MQTT, or directly via API calls.
+  **[Amazon Kinesis](https://aws.amazon.com/kinesis/)** — Ingesting streaming data.
+  **[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)** — Ingest logs and infrastructure metrics.
+  **[AWS Data Sync](https://aws.amazon.com/datasync)** — Ingest and sync on-premises file data to [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3).
+  **[Storage Gateway](https://aws.amazon.com/storagegateway)** — Serves as a local file server to ingest data to Amazon S3.
+  **[AWS Transfer for SFTP](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-sftp.html)** — Server as a cloud FTP server to ingest files to Amazon S3.
+  **[Database Migration Service](https://aws.amazon.com/dms/)** — Migrate or sync on-premises databases to the cloud.

Apart from AWS services, third-party integrations and services are also available for data ingestion, providing customers a wide portfolio of options to bring their manufacturing data to the cloud.

While the specific mechanisms for each service are different, typically a component of these services is deployed at the edge (ISA 95 / Purdue model level 3 or below). These components serve as the intermediary to provide services like protocol conversion, secure cloud connectivity, local data transformation, and caching.
