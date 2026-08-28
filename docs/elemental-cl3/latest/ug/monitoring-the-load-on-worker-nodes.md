---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/monitoring-the-load-on-worker-nodes.html
---

# Monitoring the load on worker nodes
<a name="monitoring-the-load-on-worker-nodes"></a>

You can view information about the overall load on any worker node in an AWS Elemental Conductor Live cluster.

On the **Nodes** page, choose the hostname of the node. (Don't choose the IP Address. Doing so will open the web interface for that node in another tab.)

The **Node Details** page appears for that node, showing these charts:
+ Bandwidth
+ CPU Utilization
+ Disk
+ GPU Frames/Second (if the node is running GPU-enabled software)
+ GPU Temperature (if the node is running GPU-enabled software)
+ Memory
+  Realtime
+ Total Frames/Second

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
