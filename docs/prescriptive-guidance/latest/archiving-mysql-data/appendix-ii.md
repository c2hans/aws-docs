---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/appendix-ii.html
---

# Appendix II
<a name="appendix-ii"></a>

This section provides the benchmarking results for pt-archiver tools in different scenarios. The [sysbench](https://github.com/akopytov/sysbench) tool is used in this testing to put load on the database. All the tests are performed on Amazon RDS for MySQL instance running on `db.r6g.8xlarge` instance class.

The following sysbench commands were used to prepare and run the load on the database:

```
sysbench oltp_read_write --db-driver=mysql --mysql-db=<DATABASE> --mysql-user=<USER> --mysql-password=<PASSWORD> --mysql-host=<ENDPOINT> --tables=1000 --table-size=2000000 --threads=500 prepare
sysbench oltp_read_write --db-driver=mysql --mysql-db=<DATABASE> --mysql-user=<USER> --mysql-password=<PASSWORD> --mysql-host=<ENDPOINT> --tables=1000 --rate=500 --threads=500 run
```

## Archiving a table that has no primary key and only one index (no load on the database)
<a name="archiving-a-table-that-has-no-primary-key-and-only-one-index--no-load-on-the-database-.bfd5cf3d-b1b6-5fe8-97c5-42318321b714"></a>

```
Started at 2022-11-07T05:29:12, ended at 2022-11-07T06:03:31
Action     Count           Time        Pct
commit    600050           1715.3582   83.31
select    300025           166.5470    8.09
inserting   300024         165.4025    8.03
other       0               11.6644    0.57
```

It took around 34 minutes to archive 300,024 rows. This table had 2 million rows, but the tool archived only the rows with unique data for the indexed column.

## Archiving a table that has a primary key (no load on the database)
<a name="archiving-a-table-that-has-a-primary-key--no-load-on-the-database-.b1613d34-df80-5b5a-8e41-67488fb053d8"></a>

```
Started at 2022-11-16T08:53:49, ended at 2022-11-16T12:38:18
Action         Count        Time            Pct
commit       4000000        11065.9534      82.16
select       2000000        1278.1854        9.49
inserting    1999999        1050.4961        7.80
other              0        74.1519          0.55
```

It took around 3 hours, 44 minutes, and 29 seconds to archive 1,999,999 rows.

The following graph shows that pt-archiver consumes very little CPU and resources when run on its own without any load existing in the system.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/images/guide-img/1d38fd71-63ca-45ea-bf1f-9f493d5364d0/images/842ca695-2414-4401-a2e8-18872393e0c8.png)

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/images/guide-img/1d38fd71-63ca-45ea-bf1f-9f493d5364d0/images/6756ce49-82a3-4a8d-a7fa-dabc644688fe.png)

## Archiving table that has a primary key (with load on the database)
<a name="archiving-table-that-has-a-primary-key--with-load-on-the-database-.551a8bc8-e6cd-5123-a177-18940c22be03"></a>

```
Started at 2022-11-16T17:37:07, ended at 2022-11-17T03:20:43
Action         Count          Time           Pct
commit       4000000         19688.8362      56.23
inserting    1999999         13933.4418      39.79
select       2000000          1305.1770       3.73
other              0            89.1787       0.25
```

It took around 9 hours, 43 minutes, and 36 seconds to archive 1999999 rows.

The following graph shows that during the test, the CPU utilization was up to 15 percent due to the load applied by sysbench. After the load completed, pt-archiver continued to work consuming minimal CPU as expected to complete the archival.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/images/guide-img/1d38fd71-63ca-45ea-bf1f-9f493d5364d0/images/c845b1f2-dd80-4d23-b919-ae2c1325c4d9.png)

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/images/guide-img/1d38fd71-63ca-45ea-bf1f-9f493d5364d0/images/e3083921-8dc0-415a-b696-0fb086f8a318.png)

As is evident from the graphs, pt-archiver doesn't archive aggressively when there is a load on your database.
