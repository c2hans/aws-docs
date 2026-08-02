---
source_url: https://docs.aws.amazon.com/whitepapers/latest/deploying-oracle-soa-suite-12c/scalability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scalability
<a name="scalability"></a>

 When you use AWS, you can scale your application easily because of the elastic nature of the cloud. You can scale your application vertically and horizontally.

## Vertical scaling
<a name="vertical-scaling"></a>

 You can vertically scale (scale up) your application by changing the Amazon EC2 instance type on which your Oracle WebLogic Managed Servers are deployed to a larger instance type, and then increasing the Oracle WebLogic JVM heap size. You can modify the Java heap size with the `- Xms` (initial heap size) and `- Xmx` (maximum heap size) parameters. Ideally, you should set both the initial heap size (`-Xms`) and the maximum heap size (`-Xmx`) to the same value to minimize garbage collections and optimize performance.

 For example, you can start with an `r5.large` instance with 2 vCPUs and 16 GiB RAM, and scale up all the way to an `x1e.32xlarge` instance with 128 vCPUs and 3,904 GiB RAM. For the most updated list of Amazon EC2 instance types, refer to [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/).

 After you select a new instance type, you simply restart the instance for the changes to take effect. Typically, the resizing operation is completed in a few minutes, the Amazon EBS volumes remain attached to the instances, and no data migration is required.

## Horizontal scaling
<a name="horizontal-scaling"></a>

 You can horizontally scale (scale out) your application by adding more Managed Servers to your Oracle WebLogic Server Cluster depending on the user traffic or on a particular schedule. You launch new EC2 instances to deploy, and configure additional Managed Servers, add them to the Oracle Server Cluster, and register your instances with ELB.

 You can automate this process with [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) and Oracle WebLogic scripting. For more information, refer to the next section in this document, *Configure automatic scaling on your Oracle WebLogic server cluster*.

 Amazon EC2 Auto Scaling for scaling out your Oracle WebLogic Server Cluster also requires scripting, which can be an additional technical investment. Although we recommend that you use Amazon EC2 Auto Scaling, sometimes you may not have the time or the technical resources to implement it while migrating your Oracle WebLogic Server application to AWS. A simpler alternative might be to use *standby* instances.

### Standby instances
<a name="standby-instances"></a>

 To meet extra capacity requirements, additional instances of the WebLogic Managed Servers are preinstalled and configured on EC2 instances. These standby instances can be shut down until the extra capacity is required. You do not incur compute charges when instances are shut down, you incur only [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) [storage charges](https://aws.amazon.com/ebs/pricing/). These pre-installed standby instances provide you with the flexibility to meet additional capacity when you need it.

## Configure automatic scaling on your Oracle WebLogic server cluster
<a name="configure-automatic-scaling-on-your-oracle-weblogic-server-cluster"></a>

 You can use Amazon EC2 Auto Scaling to horizontally scale your applications based on demand. This helps you to maintain steady, predictable performance at the lowest possible cost. For example, you can configure Amazon EC2 Auto Scaling to automatically create and add more Managed Servers to your Oracle WebLogic Server Cluster as the traffic increases, and to stop and remove Managed Servers from the Oracle WebLogic Server Cluster as the traffic decreases. For more information about Amazon EC2 Auto Scaling, refer to the [Amazon EC2 Auto Scaling Documentation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html).

 To configure automatic scaling for your Oracle WebLogic Server Cluster on AWS, complete these major steps:

1.  **Install and configure Oracle WebLogic Server** – The first step is to configure Amazon EFS for shared storage, install Oracle WebLogic, and configure the Oracle WebLogic Domain and the Oracle WebLogic Server Cluster. Amazon EFS stores the WebLogic product binaries, common files and scripts, domain configuration files, and logs.

1.  **Configure Amazon EC2 Auto Scaling** – Next, you have to configure Amazon EC2 Auto Scaling to launch and terminate EC2 instances—or Oracle WebLogic Machines—based on the application workload.

1.  **Configure WebLogic scaling scripts** – Finally, you create WebLogic Scripting Tool (WLST) scripts. These scripts create and add or remove the Managed Servers from the WebLogic Server Cluster when Amazon EC2 Auto Scaling launches or terminates EC2 instances in the Auto Scaling group.
