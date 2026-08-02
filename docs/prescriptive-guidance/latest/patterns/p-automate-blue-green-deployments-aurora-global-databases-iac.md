---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html
---

# Automate blue/green deployments of Amazon Aurora global databases by using IaC principles
<a name="p-automate-blue-green-deployments-aurora-global-databases-iac"></a>

*Ishwar Chauthaiwale, ANKIT JAIN, and Ramu Jagini, Amazon Web Services*

## Summary
<a name="p-automate-blue-green-deployments-aurora-global-databases-iac-summary"></a>

Managing database updates, migrations, or scaling efforts can be challenging for organizations that run critical workloads on [Amazon Aurora global databases](https://aws.amazon.com/rds/aurora/global-database/). Ensuring that these operations are carried out seamlessly, with zero downtime, is essential to maintaining service availability and avoiding disruptions for your users.

A blue/green deployment strategy offers a solution to this challenge by allowing you to run two identical environments concurrently: blue (the current environment) and green (the new environment). A blue/green strategy enables you to implement changes, perform testing, and switch traffic between environments with minimal risk and downtime.

This pattern helps you automate the blue/green deployment process for Aurora global databases by using infrastructure as code (IaC) principles. It uses [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), and [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) to simplify blue/green deployments. To improve reliability, it uses global transaction identifiers (GTIDs) for replication. GTID-based replication provides better data consistency and failover capabilities between environments compared with binary log (binlog) replication.

**Note**
This pattern assumes that you're using an Aurora MySQL-Compatible Edition global database cluster. If you're using Aurora PostgreSQL-Compatible instead, please use the PostgreSQL equivalents of the MySQL commands.

By following the steps in this pattern, you can:
+ Provision a green Aurora global database: Using CloudFormation templates, you create a green environment that mirrors your existing blue environment.
+ Set up GTID-based replication: You configure GTID replication to keep the blue and green environments synchronized.
+ Seamlessly switch traffic: You use Route 53 and Lambda to automatically switch the traffic from the blue to the green environment after full synchronization.
+ Finalize the deployment: You validate that the green environment is fully operational as the primary database, and then stop replication and clean up any temporary resources.

The approach in this pattern provides these benefits:
+ Reduces downtime during critical database updates or migrations: Automation ensures a smooth transition between environments with minimal service disruption.
+ Enables rapid rollbacks: If an issue arises after traffic is switched to the green environment, you can quickly revert to the blue environment and maintain service continuity.
+ Enhances testing and verification: The green environment can be fully tested without affecting the live blue environment, which reduces the likelihood of errors in production.
+ Ensures data consistency: GTID-based replication keeps your blue and green environments in sync, which prevents data loss or inconsistencies during migration.
+ Maintains business continuity: Automating your blue/green deployments helps avoid long outages and financial losses by keeping your services available during updates or migrations.

## Prerequisites and limitations
<a name="p-automate-blue-green-deployments-aurora-global-databases-iac-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A source Aurora MySQL-Compatible global database cluster (blue environment). Global databases provide a multi-Region configuration for high availability and disaster recovery. For instructions for setting up a global database cluster, see the [Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-getting-started.html).
+ [GTID-based replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-replication-gtid.html) enabled on the source cluster.

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

**Product versions**
+ Aurora MySQL-Compatible 8.0 or later

## Architecture
<a name="p-automate-blue-green-deployments-aurora-global-databases-iac-architecture"></a>

![Using GTID replication to sync blue and green environments in different Regions.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/19922266-c2e5-460b-9a0f-22e6d6736094/images/7a8c3095-7904-4080-906f-0c403c289a4f.png)

The diagram illustrates the following:
+ Global database setup: An Aurora global database cluster is strategically deployed across two AWS Regions. This configuration enables geographic distribution and Regional redundancy for enhanced disaster recovery capabilities.
+ Primary to secondary Region replication: The logical replication mechanism ensures seamless data synchronization from the primary Region to the secondary Region. This replication maintains data consistency with minimal latency across geographical distances.
+ GTID-based replication between clusters: GTID-based replication maintains transactional consistency and ordered data flow between the blue primary cluster and the green primary cluster, and ensures reliable data synchronization.
+ Blue primary to secondary replication: Logical replication establishes a robust data pipeline between the blue primary cluster and its secondary cluster. This replication enables continuous data synchronization and high availability.
+ Route 53 DNS configuration: Route 53 hosted zone records manage the DNS resolution for all blue and green cluster database endpoints. This configuration provides seamless endpoint mapping and enables efficient traffic routing during failover scenarios.

## Tools
<a name="p-automate-blue-green-deployments-aurora-global-databases-iac-tools"></a>

**AWS services**
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) is a fully managed relational database engine that's built for the cloud and compatible with MySQL and PostgreSQL.
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications that run on AWS. You create a template that describes all the AWS resources that you want, and CloudFormation takes care of provisioning and configuring those resources for you.
+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.

## Best practices
<a name="p-automate-blue-green-deployments-aurora-global-databases-iac-best-practices"></a>

We recommend that you thoroughly review AWS documentation to deepen your understanding of the [blue/green deployment strategy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html), [GTID-based replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-replication-gtid.html), and [weighted routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html) in Route 53. This knowledge is crucial for effectively implementing and managing your database migrations, ensuring data consistency, and optimizing traffic routing. By gaining a comprehensive understanding of these AWS features and best practices, you'll be better equipped to handle future updates, minimize downtime, and maintain a resilient and secure database environment.

For guidelines for using the AWS services for this pattern, see the following AWS documentation:
+ [Best practices with Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html)
+ [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)
+ [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
+ [Best practices for Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices.html)

## Epics
<a name="p-automate-blue-green-deployments-aurora-global-databases-iac-epics"></a>

### Create the green environment
<a name="create-the-green-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a snapshot backup from the blue cluster. | In a blue/green deployment, the green environment represents a new, identical version of your current (blue) database environment. You use the green environment to safely test updates, validate changes, and ensure stability before switching production traffic. It acts as a staging ground for implementing database changes with minimal disruption to the live environment.<br />To create a green environment, you first create a snapshot of the primary (blue) cluster in your Aurora MySQL-Compatible global database. This snapshot serves as the foundation for creating the green environment.<br />To create a snapshot:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />Alternatively, you can use the AWS Command Line Interface (AWS CLI) to create the snapshot:<pre>aws rds create-db-cluster-snapshot --db-cluster-snapshot-identifier blue-green-demo --db-cluster-identifier ex-global-cluster --region eu-west-1</pre><br />Make sure that the snapshot completes successfully before proceeding to the next step. | DBA |
| Generate the CloudFormation template for your global database and its resources. | The CloudFormation IaC generator helps you generate CloudFormation templates from existing AWS resources. Use this feature to create a CloudFormation template for your existing Aurora MySQL-Compatible global database and its associated resources. This template configures subnet groups, security groups, parameter groups, and other settings.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html) | DBA |
| Modify the CloudFormation template for the green environment. | Customize the CloudFormation template to reflect the settings for the green environment. This includes updating resource names and identifiers to ensure that the green environment operates independently of the blue cluster.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)If you use the `SnapshotIdentifier` property to restore a DB cluster, avoid specifying properties such as `GlobalClusterIdentifier`, `MasterUsername`, or `MasterUserPassword`. | DBA |
| Deploy the CloudFormation stack to create resources for the green environment. | In this step, you deploy the customized CloudFormation template to create the resources for the green environment.<br />To deploy the CloudFormation stack:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />CloudFormation initiates the process of creating the green environment resources. This process might take several minutes to complete. | DBA |
| Validate the CloudFormation stack and resources. | When the CloudFormation stack deployment is complete, you’ll need to verify that the green environment has been created successfully:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />After verification, your green environment is ready for further setup, including replication from the blue environment. | DBA |

### Configure GTID-based replication
<a name="configure-gtid-based-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify GTID settings on the blue cluster. | GTIDs provide a highly reliable method for replicating data between your blue and green environments. [GTID-based replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-replication-gtid.html) offers a resilient, simplified approach by assigning a unique identifier to every transaction in the blue environment. This method ensures that data synchronization between environments is seamless, consistent, and easier to manage than traditional binlog replication.<br />Before you configure replication, you need to ensure that GTID-based replication is properly enabled on the blue cluster. This step guarantees that each transaction in the blue environment is uniquely tracked and can be replicated in the green environment.<br />To confirm that GTID is enabled:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />These settings enable GTID tracking for all future transactions in the blue environment. After you confirm these settings, you can start setting up replication. | DBA |
| Create a replication user. | To replicate data from the blue environment to the green environment, you need to create a dedicated replication user on the blue cluster. This user will be responsible for managing the replication process.<br />To set up the replication user:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />This user now has the necessary permissions to replicate data between the two environments. | DBA |
| Configure GTID-based replication on the green cluster. | The next step is to configure the green cluster for GTID-based replication. This setup ensures that the green environment will continuously mirror all transactions that happen in the blue environment.<br />To configure the green cluster:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html) | DBA |
| Start replication on the green cluster. | You can now start the replication process. On the green cluster, run the command:<pre>START SLAVE;</pre><br />This enables the green environment to start synchronizing data, and receiving and applying transactions from the blue environment. | DBA |
| Verify the replication process. | To verify that the green environment is accurately replicating the data from the blue cluster:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />If all indicators are correct, GTID-based replication is functioning smoothly, and the green environment is fully synchronized with the blue environment. | DBA |

### Switch traffic from blue to green cluster
<a name="switch-traffic-from-blue-to-green-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure Route 53 weighted routing policies. | After you verify data consistency between the blue and green environments, you can switch traffic from the blue cluster to the green cluster. This transition should be smooth and should minimize downtime and ensure the integrity of your application’s database. To address these requirements, you can use Route 53 for DNS routing and Lambda to automate traffic switching. Additionally, a well-defined rollback plan ensures that you can revert to the blue cluster in case of any issues.<br />The first step is to configure weighted routing in Route 53. Weighted routing allows you to control the distribution of traffic between the blue and green clusters, and gradually shift traffic from one environment to the other.<br />To configure weighted routing:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />For more information about weighted routing policies, see the [Route 53 documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html). | AWS DevOps |
| Deploy a Lambda function to monitor replication lag. | To ensure that the green environment is fully synchronized with the blue environment, deploy a Lambda function that monitors replication lag between the clusters. This function can check the replication status, specifically the **Seconds\_Behind\_Master** metric, to determine whether the green cluster is ready to handle all traffic.<br />Here’s a sample Lambda function you can use:<pre>import boto3<br /><br />def check_replication_lag(event, context):<br />    client = boto3.client('rds')<br />    response = client.describe_db_instances(DBInstanceIdentifier='green-cluster-instance')<br />    replication_status = response['DBInstances'][0]['ReadReplicaDBInstanceIdentifiers']<br />    if replication_status:<br />        lag = replication_status[0]['ReplicationLag']<br />        return lag<br />    return -1</pre><br />This function checks the replication lag and returns the value. If the lag is zero, the green cluster is fully in sync with the blue cluster. | AWS DevOps |
| Automate DNS weight adjustment by using Lambda. | When the replication lag reaches zero, it's time to switch all traffic to the green cluster. You can automate this transition by using another Lambda function that adjusts the DNS weights in Route 53 to direct 100 percent of traffic to the green cluster.<br />Here’s an example of a Lambda function that automates the traffic switch:<pre>import boto3<br /><br />def switch_traffic(event, context):<br />    route53 = boto3.client('route53')<br />    lag = check_replication_lag(event, context)<br />    if lag == 0:<br />        response = route53.change_resource_record_sets(<br />            HostedZoneId='YOUR_HOSTED_ZONE_ID',<br />            ChangeBatch={<br />                'Changes': [<br />                    {<br />                        'Action': 'UPSERT',<br />                        'ResourceRecordSet': {<br />                            'Name': 'db.example.com',<br />                            'Type': 'CNAME',<br />                            'SetIdentifier': 'GreenCluster',<br />                            'Weight': 100,<br />                            'TTL': 60,<br />                            'ResourceRecords': [{'Value': 'green-cluster-endpoint'}]<br />                        }<br />                    },<br />                    {<br />                        'Action': 'UPSERT',<br />                        'ResourceRecordSet': {<br />                            'Name': 'db.example.com',<br />                            'Type': 'CNAME',<br />                            'SetIdentifier': 'BlueCluster',<br />                            'Weight': 0,<br />                            'TTL': 60,<br />                            'ResourceRecords': [{'Value': 'blue-cluster-endpoint'}]<br />                        }<br />                    }<br />                ]<br />            }<br />        )<br />        return response</pre><br />This function checks replication lag and updates the Route 53 DNS weights when the lag is zero to fully switch traffic to the green cluster.** **During the cutover process, If the blue cluster experiences heavy write traffic, consider temporarily pausing write operations during the cutover. This ensures that replication catches up, and prevents data inconsistencies between the blue and green clusters. | AWS DevOps |
| Verify the traffic switch. | After the Lambda function adjusts the DNS weights, you should verify that all traffic is directed to the green cluster and that the switch was successful.<br />To verify:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />If everything is performing as expected, the traffic switch is complete. | AWS DevOps |
| If you encounter any issues, roll back changes. | Having a rollback plan is critical in case any issues arise after the traffic switch. Here's how to quickly revert to the blue cluster if necessary:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />By implementing this rollback plan, you can ensure minimal disruption to your users in the event of any unexpected issues. | AWS DevOps |

### Validate and stop GTID-based replication
<a name="validate-and-stop-gtid-based-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop GTID-based replication on the green cluster. | After you switch traffic from the blue environment to the green environment, you should validate the success of the transition and ensure that the green cluster is functioning as expected. Additionally, the GTID-based replication between the blue and green clusters must be stopped, because the green environment now serves as the primary database. Completing these tasks ensures that your environment is secure, streamlined, and optimized for ongoing operations.<br />To stop replication:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />When you stop the replication, the green cluster becomes fully independent and operates as the primary database environment for your workloads. | DBA |
| Clean up resources. | Cleaning up any temporary or unused resources that were created during the migration from the blue to the green cluster ensures that your environment remains optimized, secure, and cost-effective. The cleanup includes adjusting security settings, taking final backups, and decommissioning unnecessary resources.<br />To clean up resources:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/p-automate-blue-green-deployments-aurora-global-databases-iac.html)<br />Cleaning up resources helps maintain a secure and streamlined environment, reduces costs, and ensures that only necessary infrastructure remains. | AWS DevOps |

## Related resources
<a name="p-automate-blue-green-deployments-aurora-global-databases-iac-resources"></a>

CloudFormation:
+ [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)
+ [Generate templates from existing resources with IaC Generator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html)
+ [Import entire applications into CloudFormation](https://aws.amazon.com/blogs/devops/import-entire-applications-into-aws-cloudformation/) (AWS blog post)

Amazon Aurora:
+ [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Welcome.html)
+ [Managing an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Aurora.html)

Blue/green deployment strategy:
+ [Overview of Amazon Aurora Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html)

GTID-based replication:
+ [Using GTID-based replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-replication-gtid.html) (Amazon RDS documentation)

AWS Lambda:
+ [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+ [Best practices for working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)

Amazon Route 53:
+ [Amazon Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
+ [Weighted routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html)

MySQL client tools:
+ [PyMYSQL](https://github.com/PyMySQL/PyMySQL)
