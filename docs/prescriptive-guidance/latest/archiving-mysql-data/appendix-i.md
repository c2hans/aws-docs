---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/appendix-i.html
---

# Appendix I
<a name="appendix-i"></a>

All the tests are performed on an Amazon RDS for MySQL instance running on the `db.r6g.8xlarge` instance class.

The following [sysbench](https://github.com/akopytov/sysbench) commands were used to prepare and run the load on the database.

```
sysbench oltp_read_write --db-driver=mysql --mysql-db=<DATABASE> --mysql-user=<USER> --mysql-password=<PASSWORD> --mysql-host=<ENDPOINT> --tables=500 --table-size=2000000 --threads=500 prepare
sysbench oltp_read_write --db-driver=mysql --mysql-db=employees --mysql-user=admin --mysql-password=qwertyuiop --mysql-host=mysql8.cbbhujzeoxed.us-east-1.rds.amazonaws.com --tables=500 --rate=500 --time=7200 run
```

In the following graph, an OLTP workload was running, and the pt-archiver process started where arrow is marked.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/images/guide-img/1d38fd71-63ca-45ea-bf1f-9f493d5364d0/images/144a2f6d-7ff8-4238-9d47-105c9ae3ecfb.png)

There is no significant change in the CPU utilization with pt-archiver running in parallel, which infers that pt-archiver doesn't impact OLTP queries while running.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/images/guide-img/1d38fd71-63ca-45ea-bf1f-9f493d5364d0/images/31e314cb-a05b-4bdf-8a4f-9c91659ecb00.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
