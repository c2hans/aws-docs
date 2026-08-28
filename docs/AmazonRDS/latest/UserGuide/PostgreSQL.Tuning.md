---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Tuning.html
---

# Tuning with wait events for RDS for PostgreSQL
<a name="PostgreSQL.Tuning"></a>

Wait events are an important tuning tool for RDS for PostgreSQL. When you can find out why sessions are waiting for resources and what they are doing, you're better able to reduce bottlenecks. You can use the information in this section to find possible causes and corrective actions. This section also discusses basic PostgreSQL tuning concepts.

The wait events in this section are specific to RDS for PostgreSQL.

**Topics**
+ [Essential concepts for RDS for PostgreSQL tuning](PostgreSQL.Tuning.concepts.md)
+ [RDS for PostgreSQL wait events](PostgreSQL.Tuning.concepts.summary.md)
+ [Client:ClientRead](wait-event.clientread.md)
+ [Client:ClientWrite](wait-event.clientwrite.md)
+ [CPU](wait-event.cpu.md)
+ [IO:BufFileRead and IO:BufFileWrite](wait-event.iobuffile.md)
+ [IO:DataFileRead](wait-event.iodatafileread.md)
+ [IO:WALWrite](wait-event.iowalwrite.md)
+ [IPC:parallel wait events](rpg-ipc-parallel.md)
+ [IPC:ProcArrayGroupUpdate](apg-rpg-ipcprocarraygroup.md)
+ [Lock:advisory](wait-event.lockadvisory.md)
+ [Lock:extend](wait-event.lockextend.md)
+ [Lock:Relation](wait-event.lockrelation.md)
+ [Lock:transactionid](wait-event.locktransactionid.md)
+ [Lock:tuple](wait-event.locktuple.md)
+ [LWLock:BufferMapping (LWLock:buffer\_mapping)](wait-event.lwl-buffer-mapping.md)
+ [LWLock:BufferIO (IPC:BufferIO)](wait-event.lwlockbufferio.md)
+ [LWLock:buffer\_content (BufferContent)](wait-event.lwlockbuffercontent.md)
+ [LWLock:lock\_manager (LWLock:lockmanager)](wait-event.lw-lock-manager.md)
+ [LWLock:pg\_stat\_statements](apg-rpg-lwlockpgstat.md)
+ [LWLock:SubtransSLRU (LWLock:SubtransControlLock)](wait-event.lwlocksubtransslru.md)
+ [Timeout:PgSleep](wait-event.timeoutpgsleep.md)
+ [Timeout:VacuumDelay](wait-event.timeoutvacuumdelay.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
