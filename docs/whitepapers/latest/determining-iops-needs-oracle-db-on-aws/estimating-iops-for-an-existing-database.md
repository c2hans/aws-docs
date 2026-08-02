---
source_url: https://docs.aws.amazon.com/whitepapers/latest/determining-iops-needs-oracle-db-on-aws/estimating-iops-for-an-existing-database.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Estimating IOPS for an existing database
<a name="estimating-iops-for-an-existing-database"></a>

 The best way to estimate the actual IOPS that is necessary for your database is to query the system tables over a period of time and find the peak IOPS usage of your existing database. To do this, you measure IOPS over a period of time and select the highest value. You can get this information from the `GV$SYSSTAT` *dynamic performance* *view*, which is a special view in Oracle Database that provides database performance information. This view is continuously updated while the database is open and in use. Oracle Enterprise Manager and Automatic Workload Repository (AWR) reports also use these views to gather data. There is a `GV$` view for almost all `V$` views. `GV$` views contain data for all nodes in a Real Application Cluster (RAC) identified by an instance ID. You can also use `GV$` views for non-RAC systems, which have only one row for each performance criterion.

 To determine IOPS, you can modify the following sample Oracle PL/SQL script for your needs and run the script during peak database load in your environment. For better accuracy, run this during the same peak period for a few days and then choose the highest value as the peak IOPS.

 Because the sample script captures data and stores the `PEAK_IOPS_MEASUREMENT` table, you must first create the table with this code:

```
CREATE TABLE peak_iops_measurement (capture_timestamp date,
total_read_io number, total_write_io number, total_io number,
total_read_bytes number, total_write_bytes number, total_bytes
number);
```

 The following script runs for an hour (`run_duration := 3600`) and captures data every five seconds (`capture_gap := 5`). It then calculates the average I/O and throughput per second for those 5 seconds, and stores this information in the table. To best fit your needs, you can modify the `run_duration` and `capture_gap` values to change the number of seconds that the script runs and the frequency in seconds that data is captured.

```
DECLARE
run_duration number := 60;
capture_gap number := 5;
loop_count number :=run_duration/capture_gap;
rdio number;
wtio number;
prev_rdio number :=0;
prev_wtio number :=0;

rdbt number;
wtbt number;
prev_rdbt number;
prev_wtbt number;

BEGIN
  FOR i in 1..loop_count LOOP
  SELECT SUM(value) INTO rdio from gv$sysstat
  WHERE name ='physical read total IO requests';
  SELECT SUM(value) INTO wtio from gv$sysstat
  WHERE name ='physical write total IO requests';
  SELECT SUM(value)* 0.000008 INTO rdbt from gv$sysstat
  WHERE name ='physical read total bytes';
SELECT SUM(value* 0.000008) INTO wtbt from gv$sysstat
WHERE name ='physical write total bytes';

IF i > 1  THEN
INSERT INTO peak_iops_measurement (capture_timestamp,total_read_io,
total_write_io, total_io, total_read_bytes,total_write_bytes, total_bytes)
VALUES (sysdate,(rdio-prev_rdio)/5,(wtio-prev_wtio)/5,((rdio-prev_rdio)/5)+
((wtio-prev_wtio))/5,(rdbt-prev_rdbt)/5,(wtbt-prev_wtbt)/5,((rdbt-prev_rdbt)/5)+
((wtbt-prev_wtbt))/5);

END IF;

prev_rdio := rdio;
prev_wtio := wtio;

prev_rdbt := rdbt;
prev_wtbt := wtbt;

DBMS_LOCK.SLEEP(capture_gap);

END LOOP;
COMMIT;
EXCEPTION
   WHEN OTHERS THEN
      ROLLBACK;
END;
/
```

 The important values are `total_io` and `total_bytes`. The script captures the split of time spent in read and write operations that you can use for comparison later.

 After you have collected data for a sufficient amount of time, you can find the peak IOPS used by your database by running the following query, which takes the highest value from the column `total_io`.

```
SELECT MAX(total_io) PeakIOPS FROM peak_iops_measurement;
```

 To prepare for any unforeseen performance spikes, we recommend that you add an additional 10 percent to this peak IOPS number to account for the actual IOPS that your database needs. This actual IOPS is the total number of IOPS you should provision for your Amazon EBS volume (`gp2` or `io1`).
