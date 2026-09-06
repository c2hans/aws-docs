---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-terms-concepts.html
---

# Understanding call analytics terminology for the Amazon Chime SDK
<a name="ca-terms-concepts"></a>

The following terminology and concepts are central to understanding how to use Amazon Chime SDK call analytics.

**Amazon Athena**
An interactive query service that enables you to analyze data in Amazon S3 using standard SQL. Athena is serverless, so you have no infrastructure to manage, and you pay only for the queries that you run. To use Athena, point to your data in Amazon S3, define the schema, and use standard SQL queries. You can also use workgroups to group users and control the resources they have access to when running queries. Workgroups enable you to manage query concurrency and prioritize query execution across different groups of users and workloads. For more information, refer to [What is Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html).

**Amazon Kinesis Data Firehose**
An extract, transform, and load (ETL) service that reliably captures, transforms, and delivers streaming data to data lakes, data stores, and analytics services. For more information, refer to [What Is Amazon Kinesis Data Firehose](https://aws.amazon.com/kinesis/data-firehose/).

**Call analytics data warehouse**
Optional storage for call analytics data. The warehouse stores data in a parquet-based data file format in an Amazon S3 bucket. You can use standard SQL to query the data. You enable the warehouse in a call analytics configuration.

**Glue Data Catalog**
A centralized metadata repository for data assets across various data sources. The catalog consists of databases and tables. For call analytics, the metadata in the table tells Athena the location of your Amazon S3 bucket. It also specifies the data structure, such as column names, data types, and the table's name. Databases only hold the metadata and schema information for a dataset. For more information, refer to [Understanding the AWS Glue data catalog table structure for the Amazon Chime SDK](ca-data-model-diagram.md), later in this section.

**Media insights pipeline**
 A temporary resource identified by a unique `MediaPipelineId`. Created by using a call analytics pipeline configuration and runtime parameters. The runtime parameters specify the data source for the pipeline.

**Media insights pipeline configuration**
A static configuration used to create media insights pipelines. You can use a configuration to instantiate one or more pipelines.

**Media insights pipeline configuration element**
The media insights pipeline configuration element includes instructions for either processing media using a processor element or delivering generated insights using a sink element.

**Media insights pipeline task**
A temporary sub-resource of a media insights pipeline. Tasks hold metadata about the status of a process for a specific stream ARN and channel ID. Identified by a unique ID. Created by starting voice analytics on a media insights pipeline.

**Speaker search**
A voice analytics feature that helps you to recognize call participants.

**Voice analytics**
An Amazon Chime SDK feature that includes speaker search and voice tone analysis.

**Voice embedding**
A vector representation of a caller's voice, plus a unique ID.

**Voice enhancement**
A system that enhances the audio quality of phone calls.

**Voice profile**
The combination of a voice embedding, its ID, and its expiration date.

**Voice profile domain**
A collection of voice profiles.

**Voice tone analysis**
A voice analytics feature that enables you to analyze caller voices for a `positive`, `negative`, or `neutral` sentiment.

For more information about the APIs used to create call insights configurations, initiate pipelines, and run voice analytics, refer to [ Amazon Chime SDK Media Pipelines](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Media_Pipelines.html), in the *Amazon Chime SDK API Reference*.

**Note**
We strongly recommend using the media insights pipeline APIs to run call analytics, because only those APIs provide new features. For more information about the differences between the media pipeline and voice namespaces, refer to [Using voice APIs to run voice analytics for the Amazon Chime SDK](va-in-voice-namespace.md), later in this section.
