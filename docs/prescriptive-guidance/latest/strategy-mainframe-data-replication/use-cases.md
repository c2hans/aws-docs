---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-mainframe-data-replication/use-cases.html
---

# Use cases for replicating mainframe data to the AWS Cloud
<a name="use-cases"></a>

This section reviews several common use cases that have emerged as prime candidates for mainframe data replication to the AWS Cloud. These use cases span various industries and operational requirements, and each presents unique challenges and opportunities. In these scenarios, data replication can play a pivotal role in driving business innovation, agility, and resilience.

This section discusses the following use cases:
+ [Use case 1: Change data capture](#use-cases-cdc)
+ [Use case 2: Real-time reporting and dashboards](#use-cases-reporting)
+ [Use case 3: Messaging protocols](#use-cases-protocols)
+ [Use case 4: New channels and interfaces](#use-cases-channels)
+ [Use case 5: Regulatory compliance and data archiving](#use-cases-compliance)
+ [Use case 6: Offload processing and batch replication](#use-cases-batch)

## Use case 1: Change data capture
<a name="use-cases-cdc"></a>

Change data capture (CDC) is ideal for scenarios where near real-time data replication is required. It captures and replicates only changed data from the mainframe to the AWS Cloud. This minimizes replication overhead and latency.

### Selection criteria
<a name="selection-criteria.d5c4993d-9191-52f4-95c2-a752608f9544"></a>
+ Real-time or near real-time data replication requirements
+ High-frequency data updates with low tolerance for latency
+ Need for efficient utilization of network bandwidth and resources

### Advantages
<a name="advantages.01d137ee-81ba-5e8d-92e5-9fcf4dbc07a2"></a>
+ Reduced replication overhead and network bandwidth utilization
+ Minimized latency makes updated data available sooner
+ Efficient utilization of resources due to selective replication of changed data

### Disadvantages
<a name="disadvantages.e42a32fc-a90c-59eb-89fd-d810eea5f0f2"></a>
+ Complexity in implementing and managing CDC mechanisms
+ Potential for increased resource utilization on mainframe systems due to capturing changes
+ Dependency on the reliability and performance of CDC tools and processes

### Strategy
<a name="strategy.bebce05b-99b9-56f3-a1ad-87680e555688"></a>
+ Select a CDC tool that is compatible with mainframe databases and AWS services
+ Configure the CDC tool to capture and replicate only the relevant data changes
+ Implement monitoring and validation mechanisms to maintain data consistency and reliability
+ Consider implementing failover mechanisms that promote continuous availability and data integrity

## Use case 2: Real-time reporting and dashboards
<a name="use-cases-reporting"></a>

For immediate visualization and analysis, real-time reporting and dashboards require continuous data replication from mainframe systems to the AWS Cloud. This use case is common in industries where real-time insights are critical for decision-making, such as banking, insurance, retail, healthcare, and manufacturing.

### Selection criteria
<a name="selection-criteria.6d9ce19b-9c28-5adc-96ec-e0cc1272aabf"></a>
+ Need for immediate access to updated data for analytics and visualization
+ Requirement for real-time monitoring of business metrics and key performance indicators (KPIs)
+ High demand for agility and responsiveness in decision-making processes

### Advantages
<a name="advantages.f2b20408-bc84-5d05-9092-e1d0b58d99fb"></a>
+ Provides immediate access to updated data for real-time analysis and decision-making
+ Enables proactive monitoring of business performance and timely interventions
+ Facilitates dynamic and interactive visualization of data for stakeholders

### Disadvantages
<a name="disadvantages.96828b08-9759-56aa-abde-637e5a710260"></a>
+ Increased complexity in data replication and processing to achieve real-time updates
+ Higher resource consumption and infrastructure costs due to continuous replication
+ Dependency on robust monitoring and alerting mechanisms to validate data freshness and reliability

### Strategy
<a name="strategy.6bbdf7d2-4d32-53ef-8370-b97e024c3d68"></a>
+ Implement CDC or messaging protocols for real-time data replication
+ Use AWS services, such as [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), for real-time data streaming and processing
+ Design and deploy real-time reporting and dashboard solutions on the AWS Cloud so that you can immediately access the updated data
+ Implement monitoring and alerting mechanisms to promptly detect and address data replication issues

## Use case 3: Messaging protocols
<a name="use-cases-protocols"></a>

Messaging protocols and systems, such as Apache Kafka or IBM MQ, facilitate asynchronous communication and data transfer between the mainframe and the AWS Cloud. They are suitable for scenarios that require decoupled and scalable data integration.

### Selection criteria
<a name="selection-criteria.ea461c24-509c-5aa4-ad20-603d961fadd0"></a>
+ Asynchronous data transfer requirements
+ Need for scalable and decoupled data integration architecture
+ Support for real-time or near real-time data replication with low latency

### Advantages
<a name="advantages.d8d8593f-81e0-5bf9-8465-c1ce49e9060f"></a>
+ Decoupled and scalable architecture that enables flexible data integration
+ Support for real-time or near real-time data replication with low latency
+ Built-in features for reliability, message queuing, and fault tolerance

### Disadvantages
<a name="disadvantages.590cfdc3-baa5-58b6-9979-a9551096dabe"></a>
+ Complexity in configuring and managing messaging infrastructure
+ Potential for increased resource consumption and operational overhead
+ Dependency on messaging platform reliability and performance

### Strategy
<a name="strategy.22012f07-7126-561b-9182-a287166c67fb"></a>
+ Choose a messaging system, such as Apache Kafka or IBM MQ, that is compatible with both the mainframe and the AWS Cloud
+ Design messaging topics or queues that facilitate data transfer and replication
+ Implement message producers and consumers on the mainframe and cloud in order to exchange data
+ Configure monitoring and alerting mechanisms to validate message processing and replication reliability

## Use case 4: New channels and interfaces
<a name="use-cases-channels"></a>

A mainframe *channel* is a connection that moves data into and out of a mainframe computer. Channels are part of the channel subsystem. For immediate exposure and consumption, new channels and interfaces require continuous data replication from the mainframe systems to the cloud.

### Selection criteria
<a name="selection-criteria.379a6541-3f36-5057-925e-2dbe31c861f1"></a>
+ Need for immediate access to updated data for new channels
+ Access to mainframe data with new interfaces
+ High demand for new channels
+ Integration with diverse systems, platforms, or cloud environments

### Advantages
<a name="advantages.e5d28e5f-7534-5ed6-8642-627b211b19ac"></a>
+ Unlocking mainframe data access by enabling new channels to consume mainframe data
+ Facilitating integration with diverse systems, platforms, or cloud environments
+ Enabling more flexible and efficient data movement across different infrastructures

### Disadvantages
<a name="disadvantages.d9c79290-beb5-5249-a928-4bda4c454575"></a>
+ Introducing new interfaces or channels for data replication might require additional security measures to help protect data and comply with regulations
+ Integrating new interfaces with existing systems and workflows can be challenging, especially in complex or legacy environments

### Strategy
<a name="strategy.ffc8e7af-4aff-529a-ab24-047b98179c61"></a>
+ Implement CDC or messaging protocols for real-time data replication
+ Use AWS services, such as Kinesis Data Streams, for real-time data streaming and processing
+ Implement monitoring and alerting mechanisms to promptly detect and address data replication issues

## Use case 5: Regulatory compliance and data archiving
<a name="use-cases-compliance"></a>

Regulatory compliance and data archiving involve replicating mainframe data to the cloud for long-term retention. It's critical to comply with data retention policies and regulations. This use case is prevalent in regulated industries, such as banking, healthcare, and pharmaceuticals.

### Selection criteria
<a name="selection-criteria.de5af1d8-34bc-599c-8600-8e3f06e92373"></a>
+ Need for long-term retention of historical data for regulatory compliance or legal requirements
+ Requirement for secure and scalable storage solutions for archived data
+ Compliance with data privacy regulations and industry-specific mandates for data retention and archiving

### Advantages
<a name="advantages.2981396e-1e09-50dc-9665-5096c970b284"></a>
+ Compliance with regulatory requirements and industry-specific mandates for data retention
+ Scalable and cost-effective storage solutions for long-term archiving of historical data
+ Efficient retrieval and access to archived data for audit or legal purposes

### Disadvantages
<a name="disadvantages.4b13e131-1377-54db-ad75-8517994af05e"></a>
+ Complexity in managing and organizing archived data for efficient retrieval and access
+ Potential for increased storage costs associated with long-term retention of large volumes of data
+ Dependency on robust data encryption and access controls to protect archived data from unauthorized access

### Strategy
<a name="strategy.095ae69d-f7a3-58e8-a57a-befe3492b746"></a>
+ Implement data lifecycle policies to automate the archival and retention of historical data
+ Use AWS storage offerings, such as [Amazon Glacier storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/glacier-storage-classes.html), for cost-effective long-term storage
+ Encrypt archived data at rest and implement access controls that help prevent unauthorized access
+ Establish audit trails and logging mechanisms that track access to archived data and comply with regulatory requirements

## Use case 6: Offload processing and batch replication
<a name="use-cases-batch"></a>

Offload processing and batch replication involves scheduling periodic batch jobs that extract data from the mainframe and load it to the AWS Cloud. It is suitable for scenarios where real-time replication is not required and batch processing is acceptable.

### Selection criteria
<a name="selection-criteria.0e9919b8-9706-511a-9a45-b28fee5bf0e9"></a>
+ Real-time data replication is not required
+ Batch processing is acceptable for data updates
+ Lower frequency of data updates with moderate tolerance for latency

### Advantages
<a name="advantages.d0c07f08-2382-5579-bd30-34bb698088a0"></a>
+ Offloading compute-intensive operations, such as data transformation, compression, or encryption, from the primary mainframe system can enhance overall system performance and reduce bottlenecks
+ Predictable resource utilization and lower impact on mainframe systems
+ Flexibility in scheduling replication jobs based on business requirements

### Disadvantages
<a name="disadvantages.addf14dd-78b9-5e8b-920a-715637cc74c6"></a>
+ Higher latency in data availability compared to real-time or near real-time replication
+ Potential for data inconsistency between the mainframe and cloud due to periodic updates
+ Limited suitability for scenarios that require timely access to updated data

### Strategy
<a name="strategy.c0e35a58-4a0a-5a0c-ad5a-dbdca4975448"></a>
+ Develop batch replication jobs that extract and load data from the mainframe to the AWS Cloud
+ Schedule replication jobs based on your business requirements and data update frequencies
+ Implement checks to validate data consistency and integrity
+ Consider optimizing batch replication processes to reduce latency and resource consumption

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
