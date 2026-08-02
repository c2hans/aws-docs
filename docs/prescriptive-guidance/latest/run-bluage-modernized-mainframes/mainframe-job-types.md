---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/run-bluage-modernized-mainframes/mainframe-job-types.html
---

# Mainframe job types
<a name="mainframe-job-types"></a>

This guide covers both batch and real-time mainframe jobs.

## Batch jobs
<a name="batch-jobs"></a>

*Batch jobs* are scheduled to run at regular intervals through a mechanism such as CRON or by integration with an external trigger. These jobs process inputs, such as flat file data or database contents, to produce outputs. Examples of mainframe databases include IBM Db2, which supports relational databases, and IBM Information Management System (IMS), which supports hierarchical databases. FTP and message queues are common output destinations for these jobs. Batch jobs need to run only when required.

## Real-time services
<a name="real-time-services"></a>

*Real-time services* are jobs that listen for requests on a protocol, such as [IBM Customer Information Control System (CICS)](https://www.ibm.com/docs/en/zos-basic-skills?topic=zos-introduction-cics). They receive the job input through the request and respond in kind with the generated output. These jobs need to run all the time, and they require highly available infrastructure to support them.
