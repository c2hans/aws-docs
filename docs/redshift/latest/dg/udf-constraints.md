---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/udf-constraints.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Python UDF constraints
<a name="udf-constraints"></a>

Within the constraints listed in this topic, you can use UDFs anywhere you use the Amazon Redshift built-in scalar functions. For more information, see [SQL functions reference](c_SQL_functions.md).

Amazon Redshift Python UDFs have the following constraints:
+ Python UDFs cannot access the network or read or write to the file system.
+ The total size of user-installed Python libraries cannot exceed 100 MB.
+ Amazon Redshift can only run one Python UDF at a time for provisioned clusters using automatic workload management (WLM) and for serverless workgroups. If you try to run more than one UDF concurrently, Amazon Redshift queues the remaining Python UDFs to run in the workload management queues. SQL UDFs don’t have a concurrency limit when using automatic WLM.
+  When using manual WLM for provisioned clusters, the number of Python UDFs that can run concurrently per cluster is limited to one-fourth of the cluster’s total concurrency level. For example, a provisioned cluster with a concurrency of 15 can run a maximum of three concurrent Python UDFs.
+ When using Python UDFs, Amazon Redshift doesn't support the SUPER and HLLSKETCH data types.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
