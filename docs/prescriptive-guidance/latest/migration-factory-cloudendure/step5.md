---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/step5.html
---

# Step 5. Cut over
<a name="step5"></a>

The last step in a typical rehost migration is to schedule a cutover window and prepare the resources to support the cutover.

## Verify the replication status
<a name="5-verify-replication"></a>

First, you must verify the replication status and make sure that the status of all servers in the given wave is healthy.

As in [step 3](step3.md), you can run a Cloud Migration Factory script to automate this step. The script retries every 5 minutes until the status of every server in the given wave changes to healthy, and updates the replication status in the Cloud Migration Factory database.

For detailed instructions, see [Verify the replication status](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#verify-the-replication-status) in the *Cloud Migration Factory Implementation Guide*.

## Shut down source servers in preparation for cutover
<a name="5-shutdown"></a>

After you verify the source servers' replication status, you are ready to shut down the source servers to stop transactions from the client applications to the servers. Usually, you can shut down the source servers in the cutover window. Shutting down the source servers manually could take you 5 minutes per server, and, for large waves, it could take a few hours in total. Instead, you can run a Cloud Migration Factory automation script to shut down all your servers in the given wave.

For detailed instructions, see [Shut down the in-scope source servers](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#shut-down-the-in-scope-source-servers) in the *Cloud Migration Factory Implementation Guide*.

## Launch target EC2 instances for cutover
<a name="5-launch-ec2"></a>

After shutting down the source servers, you can launch the target EC2 server instances. As in [step 4](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/step4.html), you can use a single Launch servers button to launch all the servers in the given wave in cutover mode. The only difference here is that you choose `Cutover` as the launch type. As in boot-up testing, the Launch servers button automates the following processes:
+ Verifying replication status and making sure that the lag time is less than 180 minutes.
+ Updating the Amazon EC2 launch templates for all servers in the given wave with the metadata in the Cloud Migration Factory database.
+ Sending all servers to an MGN job and launching them in cutover mode.

For detailed instructions, see [Launch instances for cutover](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#launch-instances-for-cutover) in the *Cloud Migration Factory Implementation Guide*.

## Verify instance boot-up status
<a name="5-status-check"></a>

After launching the instances in the cutover mode, wait for at least 15 minutes before the next step, which is verifying instance boot-up status. When cutover launch is complete, you can run the Cloud Migration Factory automation script to verify the 2/2 status for all machines in the given wave.

If an instance fails the 2/2 status checks, contact [AWS Support](https://aws.amazon.com/premiumsupport/) for assistance.

For detailed instructions, see [Verify the target instance status](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#verify-the-target-instance-status) in the *Cloud Migration Factory Implementation Guide*.

## (Optional) Get new IP addresses for target instances
<a name="5-get-ip"></a>

If the target server instances use new IP addresses, the next step is to update the DNS server with the new IP addresses. In some scenarios, target instances support dynamic DNS registration and register the new IP address automatically with the DNS server. For example, if a Windows server uses a domain controller as the DNS server, DNS registration could be automatic. On the other hand, if the DNS update is a manual process, you need to get the new IP addresses for all the target instances. In this case, you can use the Cloud Migration Factory automation script to export the new IP addresses for all the instances in the given wave to a CSV file.

For detailed instructions, see [Retrieve the target instance IP](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-command-prompt.html#retrieve-the-target-instance-ip) in the *Cloud Migration Factory Implementation Guide*.

## Test RDP/SSH access to target servers
<a name="5-test-rdp"></a>

After you update the DNS records, you can connect to the target instances with the host name. In this step, you check to see if you can log in to the operating system by using Remote Desktop Protocol (RDP) or through Secure Shell (SSH) access. You can manually log in to each server individually, but it is more efficient to test the server connection by using the Cloud Migration Factory automation script.

For detailed instructions, see [Verify the target server connections](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-command-prompt.html#verify-the-target-server-connections) in the *Cloud Migration Factory Implementation Guide*.

## Reconfigure application and networking settings
<a name="5-config-app"></a>

After the migration team completes operating system level testing, the application team makes changes at the application level. These changes might include the following:
+ If the application requires a load balancer, change the application endpoint in the load balancer to point to the new instance IPs in AWS.
+ Change the connection string for the application web tier to connect to the database.
+ Change other application-specific settings.

## Test the application
<a name="5-test-app"></a>

Application testing, which takes place after the updates described in the previous section, is generally handled by the application owner or support team. It involves logging in to the new servers and confirming that the application works as expected. If it doesn't, the application owner or support team works with the migration team to troubleshoot and fix issues.

## Complete the cutover
<a name="5-complete-cutover"></a>

This is the final step of the migration. The application owner decides whether the target application in AWS meets their expectations from both functionality and performance perspectives. If a rollback is required, it usually involves these activities:
+ Terminating all AWS instances for the affected application.
+ Turning on on-premises servers for the given application.
+ Reverting DNS records to the old server IP addresses.
