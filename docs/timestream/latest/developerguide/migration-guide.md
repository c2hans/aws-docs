---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/migration-guide.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Migration Guide
<a name="migration-guide"></a>

This guide presents two approaches for migrating time-series data from Amazon Timestream for LiveAnalytics to Timestream for InfluxDB, and to [Aurora](https://docs.aws.amazon.com//AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) or [RDS PostgreSQL](https://docs.aws.amazon.com//AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html) with a intermediate layer for [Amazon S3](https://aws.amazon.com/s3/). For migrations to other database services, we recommend consulting the specific documentation for importing data from S3 into your chosen service.

In this guide, we walk through following steps:

1. Export your data from Timestream for LiveAnalytics to Amazon S3.

1. Ingesting data to Timestream for InfluxDB.

1. Ingestion data to PostgreSQL.

**Topics**
+ [Exporting Timestream data to Amazon S3](export-timestream-data.md)
+ [Timestream for InfluxDB as a Target](timestream-influxdb-target.md)
+ [Aurora/RDS Postgres as a target](aurora-postgres-target.md)
