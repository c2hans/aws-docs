---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/accessing-prebid-server-logs-from-efs.html
---

# Accessing Prebid Server logs from EFS
<a name="accessing-prebid-server-logs-from-efs"></a>

The following procedure describes how to access Prebid Server logs from EFS.

 **To create an EC2 instance that will function as a bastion host**

1. Sign in to the [Amazon EC2 console](https://console.aws.amazon.com/ec2/).

1. Choose **Launch instance**.

1. Provide a name and leave the default Amazon Machine Image and instance type.

1. Choose **Key pair**, and select a key pair. Create one if you don’t already have any.

1. Under **Network settings**, choose **Edit**.

1. Select `PrebidVpc`.

1. Select the public subnet that is the 10.8.0.0 network - `PrebidVpc/Prebid-PublicSubnet1`.

1. Select **Create security group** and use default settings.

1. Leave the default storage settings and choose **Launch instance**.

 **To enable incoming NFS connections to the EFS access point**

1. Navigate to the [Amazon EFS console](https://console.aws.amazon.com/efs/home).

1. In the navigation pane, choose **File systems**.

1. Open the EFS file system that is in the prebid stack.

1. Choose the **Network** tab and note the security group ID for the security group with `PrebidfsEfsSecurityGroup` in the name.

1. Navigate to the [Amazon EC2 console](https://console.aws.amazon.com/ec2/home).

1. In the navigation pane, choose **Security Groups**.

1. Open the solution’s security group and choose **Edit inbound rules**.

1. Under **Edit inbound rules**:

   1. Choose **Add rule**.

   1. Under **Type**, select **NFS**.

   1. Under **Source**, select **Custom**.

   1. Enter `10.0.0.0/8` for **CIDR blocks**.

   1. Choose **Save rules**.

1. Return to the EFS system and choose **File system policy**.

1. Choose **Edit**, add `elasticfilesystem:ClientMount` to the list of allowed actions, and choose **Save**.

 **To mount the EFS file system**

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Open the solution’s stack, select the **Resources** tab, and select the EFS file system.

1. Choose **Attach**.

1. Copy the NFS mount command.

1. SSH into the EC2 instance that you just created.

1. Make a mount point directory:

   ```
   sudo mkdir efs
   ```

1. Paste the NFS mount command that you copied earlier. It looks similar to this:

   ```
   sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-xxxxxxxxxxxxxxxxx.efs.us-east-1.amazonaws.com:/ efs
   ```
