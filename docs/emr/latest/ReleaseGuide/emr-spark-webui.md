---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-webui.html
---

# Access the Spark web UIs
<a name="emr-spark-webui"></a>

You can view the Spark web UIs by following the procedures to create an SSH tunnel or create a proxy in the section called [Connect to the cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node.html) in the Amazon EMR Management Guide and then navigating to the YARN ResourceManager for your cluster. Choose the link under **Tracking UI** for your application. If your application is running, you see **ApplicationMaster**. This takes you to the application master's web UI at port 20888 wherever the driver is located. The driver may be located on the cluster's primary node if you run in YARN client mode. If you are running an application in YARN cluster mode, the driver is located in the ApplicationMaster for the application on the cluster. If your application has finished, you see **History**, which takes you to the Spark HistoryServer UI port number at 18080 of the EMR cluster's primary node. This is for applications that have already completed. You can also navigate to the Spark HistoryServer UI directly at http://{{master-public-dns-name}}:18080/.

With Amazon EMR release 5.25.0 and later, you can access Spark history server UI from the console without setting up a web proxy through an SSH connection. For more information, see [View persistent application user interfaces](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
