---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/monitoring.html
---

# Monitoring and troubleshooting
<a name="monitoring"></a>

You can monitor AWS Transform MGN by using [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [Amazon EventBridge](https://aws.amazon.com/eventbridge), and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), which collect raw data and process it into readable, near-real-time metrics. For more information, see [Monitoring AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/monitoring-overview.html) in the AWS documentation.

If you encounter any issues and want to launch new test or cutover instances, you can revert the test or cutover action. This will revert the lifecycle status of your source servers to the previous stage, indicating that these servers have not undergone a cutover. During a revert, you will also have the option to delete your test or cutover instances for cost-saving purposes. For more information, see [Troubleshooting](https://docs.aws.amazon.com/mgn/latest/ug/troubleshooting.html) in the MGN documentation.

When the Agent has been installed, the source server appears on the MGN console, and you can see the server details to check replication progress.

## Testing connectivity and name resolution from the source server
<a name="source"></a>

Log in to the source server by using Windows remote desktop protocol (RDP), Secure Shell (SSH), or AWS Systems Manager Session Manager, and test the following:
+ Connectivity over HTTPS on TCP port 443 to the MGN endpoint.
  + On Windows (in PowerShell):

    ```
    Test-NetConnection -ComputerName mgn.<aws_region>.amazonaws.com -Port 443
    ```
  + On Linux or Windows (cmd):

    ```
    Telnet mgn.<aws_region>.amazonaws.com 443
    ```
+ Connectivity over HTTPS on TCP port 443 to the Amazon S3 endpoint.
  + On Windows (in PowerShell):

    ```
    Test-NetConnection -ComputerName <s3_endpoint_name> -Port 443
    ```
  + On Linux or Windows (cmd):

    ```
    Telnet <s3_endpoint_name> 443
    ```
+ Connectivity on TCP port 1500 to the replication server IP:
  + On Windows (in PowerShell):

    ```
    Test-NetConnection -ComputerName <Replication_Server_Private_IP> -Port 1500
    ```
  + On Linux or Windows (cmd):

    ```
    Telnet <Replication_Server_Private_IP> 1500
    ```

In addition, make sure that the Amazon EC2 and MGN API endpoints resolve to private IPs by using the following commands. (You can use the same commands on Windows and Linux.)
+ `nslookup ec2.<aws_region>.amazonaws.com`
+ `nslookup mgn.<aws_region>.amazonaws.com`

## Testing connectivity and name resolution from the staging area network
<a name="staging"></a>

To test connectivity from the staging area, launch a temporarily Amazon EC2 instance in the staging subnet and test the following:
+ Connectivity over HTTPS on TCP port 443 to the MGN endpoint.
  + On Windows (in PowerShell):

    ```
    Test-NetConnection -ComputerName mgn.<aws_region>.amazonaws.com -Port 443
    ```
  + On Linux or Windows (cmd):

    ```
    Telnet mgn.<aws_region>.amazonaws.com 443
    ```
+ Connectivity over HTTPS on TCP port 443 to the Amazon EC2 endpoint.
  + On Windows (in PowerShell):

    ```
    Test-NetConnection -ComputerName ec2.<aws_region>.amazonaws.com -Port 443
    ```
  + On Linux or Windows (cmd):

    ```
    Telnet ec2.<aws_region>.amazonaws.com 443
    ```

If replication initialization stalls at the "Downloading replication software" step after the Agent is installed on the source server, verify the following.
+ Name resolution:

  ```
  nslookup s3.<aws_region>.amazonaws.com
  ```
**Note**
The Amazon S3 endpoint will resolve to a public IP but will connect privately through the Amazon S3 gateway endpoint.
+ Connectivity over HTTPS protocol on the TCP/443 port.
  + On Windows:

    ```
    Test-NetConnection -ComputerName s3.<aws_region>.amazonaws.com -Port 443
    ```
  + On Linux:

    ```
    Telnet s3.<aws_region>.amazonaws.com 443
    ```
