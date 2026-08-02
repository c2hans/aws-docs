---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/pacemaker-tutorial-prerequisites.html
---

# Prerequisites and cluster setup
<a name="pacemaker-tutorial-prerequisites"></a>

In this section, you set up the infrastructure for the high availability tutorial. You create a security group, create a key pair, launch Amazon EC2 instances, install Pacemaker and DRBD, create a cluster, and configure block-level replication between instances.

## Create and configure a security group
<a name="pacemaker-tutorial-prerequisites-sg"></a>

Create a security group that allows all traffic between cluster instances. For this tutorial, you open all ports to simplify setup. This step requires a VPC. If you don't have one, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html).

**Console**
+ Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
+ In the navigation pane, choose **Security Groups**, then choose **Create security group**.
+ Enter a name (for example, `pacemaker-cluster-sg`) and a description.
+ Select your VPC.
+ Choose **Create security group**.
+ After creation, select the new security group and edit its inbound rules. Choose **Add rule**. Set **Type** to **All traffic** and **Source** to the security group's own ID. This allows all traffic between instances in this security group.
+ Add a second inbound rule for SSH access. Set **Type** to **SSH** and **Source** to **My IP**.

**AWS Command Line Interface**
+ Create the security group.

  ```
  aws ec2 create-security-group \
    --group-name pacemaker-cluster-sg \
    --description "Security group for Pacemaker HA cluster" \
    --vpc-id {{your-vpc-id}}
  ```

  Note the `GroupId` from the output (for example, `sg-0123456789abcdef0`).
+ Add an inbound rule to allow all traffic from instances in the same security group.

  ```
  aws ec2 authorize-security-group-ingress \
    --group-id {{security-group-id}} \
    --protocol all \
    --source-group {{security-group-id}}
  ```
+ Add an inbound rule to allow SSH access from your IP address.

  ```
  aws ec2 authorize-security-group-ingress \
    --group-id {{security-group-id}} \
    --protocol tcp \
    --port 22 \
    --cidr {{your-ip}}/32
  ```

## Create a key pair
<a name="pacemaker-tutorial-prerequisites-keypair"></a>

Create a key pair to use for SSH access to all instances. Use the same key pair for all instances in this tutorial.

**Console**
+ Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
+ In the navigation pane, choose **Key Pairs**, then choose **Create key pair**.
+ Enter a name (for example, `pacemaker-key`).
+ Select **RSA** as the key pair type and **.pem** as the file format.
+ Choose **Create key pair**. The private key file downloads automatically.

**Warning**
Save the private key file (`.pem`) in a secure location. You cannot download it again. You need this file to SSH into your instances.

**AWS Command Line Interface**
+ Create the key pair.

  ```
  aws ec2 create-key-pair \
    --key-name {{key-name}} \
    --query 'KeyMaterial' \
    --output text > pacemaker-key.pem
  ```
+ Set the correct permissions on the private key file.

  ```
  chmod 400 pacemaker-key.pem
  ```

## Launch EC2 instances
<a name="pacemaker-tutorial-prerequisites-instances"></a>

Launch two Ubuntu Amazon EC2 instances in the security group you created. A small instance type (for example, `t3.small`) is sufficient for this tutorial.

**Console**
+ Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
+ Choose **Launch instances**.
+ Enter a name for the instance (for example, `pacemaker-instance-1`).
+ Under **Application and OS Images**, search for **Ubuntu** and select an Ubuntu Server AMI (for example, Ubuntu Server 24.04 LTS).
+ Under **Instance type**, select **t3.small**.
+ Under **Key pair**, select the key you created earlier.
+ Under **Network settings**, choose **Edit**, select your VPC and a subnet, and under **Firewall (security groups)**, choose **Select existing security group** and select `pacemaker-cluster-sg`.
+ Choose **Launch instance**.
+ Repeat for each additional instance (for example, `pacemaker-instance-2`). Ensure all instances are in the same VPC and security group.

**AWS Command Line Interface**
+ Launch an instance.

  ```
  aws ec2 run-instances \
    --image-id {{ubuntu-ami-id}} \
    --instance-type t3.small \
    --key-name {{key-name}} \
    --security-group-ids {{security-group-id}} \
    --subnet-id {{subnet-id}} \
    --count 1 \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=pacemaker-instance-1}]'
  ```

  Repeat with `Value=pacemaker-instance-2` for the second instance.

You need the private IP address of each instance for cluster configuration.
+ **Console:** In the Amazon EC2 console, select an instance and find the **Private IPv4 address** in the **Details** tab.
+ **AWS Command Line Interface:**

  ```
  aws ec2 describe-instances \
    --filters "Name=tag:Name,Values=pacemaker-instance-*" \
    --query "Reservations[*].Instances[*].[Tags[?Key=='Name'].Value|[0],PrivateIpAddress]" \
    --output table
  ```

## Install Pacemaker utilities
<a name="pacemaker-tutorial-prerequisites-install"></a>

SSH into each instance and install Pacemaker utilities.

```
ssh -i pacemaker-key.pem ubuntu@{{instance-public-ip}}
```

```
sudo apt update
sudo apt install -y pacemaker pcs resource-agents-extra resource-agents-common resource-agents-base
```

## Configure network communication
<a name="pacemaker-tutorial-prerequisites-network"></a>

1. **Test communication between instances.** On the destination instance, run the following command to listen for pings from the source instance.

   ```
   sudo tcpdump host {{source-instance-private-ip}}
   ```

   On the source instance, run the following command to ping the destination instance.

   ```
   ping -c 4 {{destination-instance-private-ip}}
   ```

   You should see ping responses on both sides. If not, verify that your security group allows all traffic between instances.

1. **Disable cloud-init hostname management.** On Ubuntu Amazon EC2 instances, cloud-init can revert hostname and `/etc/hosts` changes on reboot. Run this on each instance to prevent that.

   ```
   sudo bash -c 'cat > /etc/cloud/cloud.cfg.d/99-preserve-hostconfig.cfg <<EOF
   preserve_hostname: true
   manage_etc_hosts: false
   EOF'
   ```

1. **Set the hostname on each instance.** Pacemaker uses hostnames to identify cluster instances.

   On instance 1:

   ```
   sudo hostnamectl set-hostname instance1
   ```

   On instance 2:

   ```
   sudo hostnamectl set-hostname instance2
   ```

1. **Configure `/etc/hosts`.** On each instance, append the private IP and hostname pairs to `/etc/hosts`. This allows instances to resolve each other by hostname.

   ```
   sudo tee -a /etc/hosts <<EOF
   {{instance1-private-ip}} instance1
   {{instance2-private-ip}} instance2
   EOF
   ```

## Create the Pacemaker cluster
<a name="pacemaker-tutorial-prerequisites-cluster"></a>

1. **Start the pcs daemon** on each instance.

   ```
   sudo systemctl enable pcsd.service
   sudo systemctl start pcsd.service
   ```

1. **Set the hacluster password.** The `hacluster` user is a system account created automatically when you install the `pcs` package. Pacemaker uses this account for cluster authentication between instances. Set the same password on each instance.

   ```
   sudo passwd hacluster
   ```

1. **Authorize pcs hosts.** Authorize the cluster instances with each other. Run this on each instance.

   ```
   sudo pcs host auth instance1 instance2
   ```

   You will be prompted for the `hacluster` username and password.

1. **Set up the cluster.** Run this command on one instance only. The `--force` flag destroys any existing cluster on the device.

   ```
   sudo pcs cluster setup my-gg-cluster instance1 instance2 --force
   ```

1. **Start the cluster.** Run this command on one instance only.

   ```
   sudo pcs cluster start --all
   sudo pcs cluster enable --all
   ```

1. **Verify the cluster status** on either instance.

   ```
   sudo pcs status
   ```

## Set up DRBD
<a name="pacemaker-tutorial-prerequisites-drbd"></a>

[DRBD](https://linbit.com/drbd/) (Distributed Replicated Block Device) is a Linux kernel module that replicates storage devices between instances in real time. It works at the block device level — the raw disk level below the filesystem — so all data written to disk on one instance is mirrored to the other. This ensures that if the primary instance fails, the standby instance has an identical copy of the data.

1. **Create and attach EBS volumes.** Create an EBS volume for each instance. The volume must be in the same Availability Zone as the instance.

**Console**
   + Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
   + In the navigation pane, choose **Volumes**, then choose **Create volume**.
   + Set **Volume type** to **gp3**, **Size** to **8 GiB**, and **Availability Zone** to the same zone as your instance.
   + Choose **Create volume**.
   + Select the new volume, choose **Actions** > **Attach volume**, select the target instance, set the device name to `/dev/xvdbz`, and choose **Attach volume**.
   + Repeat for each instance.

**AWS Command Line Interface**
   + Create a volume in the same Availability Zone as your instance.

     ```
     aws ec2 create-volume \
       --volume-type gp3 \
       --size 8 \
       --availability-zone {{instance-availability-zone}}
     ```

     Note the `VolumeId` from the output.
   + Attach the volume to an instance.

     ```
     aws ec2 attach-volume \
       --volume-id {{volume-id}} \
       --instance-id {{instance-id}} \
       --device /dev/xvdbz
     ```

     Repeat for each instance.

1. **Verify the volume.** SSH into each instance and verify the volume is attached by listing block devices.

   ```
   lsblk
   ```

   On Nitro-based instance types such as `t3.small`, the volume appears as an NVMe device (for example, `/dev/nvme1n1`) instead of `/dev/xvdbz`. Use `lsblk` to identify the actual device name, and use that name in the DRBD configuration.

1. **Install DRBD utilities** on each instance.

   ```
   sudo apt install -y drbd-utils
   ```

1. **Configure the DRBD resource.** Create the DRBD resource configuration directory and file on both instances.

   ```
   sudo mkdir -p /etc/drbd.d
   sudo vi /etc/drbd.d/greengrass.res
   ```

   Add the following configuration. Replace the hostnames and IP addresses with your values.

   ```
   resource greengrass {
       protocol C;

       on instance1 {
           device    /dev/drbd0;
           disk      /dev/{{instance1-device-name}};
           address   {{instance1-private-ip}}:7788;
           meta-disk internal;
       }

       on instance2 {
           device    /dev/drbd0;
           disk      /dev/{{instance2-device-name}};
           address   {{instance2-private-ip}}:7788;
           meta-disk internal;
       }
   }
   ```

1. **Create and start the DRBD resource.** Run on both instances.

   ```
   sudo drbdadm create-md greengrass
   sudo drbdadm up greengrass
   ```

   Verify with `lsblk` that `drbd0` appears under your EBS volume device (for example, `xvdbz` or `nvme1n1`).

1. **Set the primary instance.** Run the following commands on instance1 only to force it to be primary and wait for synchronization.

   ```
   sudo drbdadm -- --overwrite-data-of-peer primary greengrass
   sudo drbdadm status
   ```

   Wait until both instances show `UpToDate` for the disk state. Once synchronized, all other instances become standby instances.

1. **Format and mount the DRBD device.**

   On the primary instance only, format the DRBD device:

   ```
   sudo mkfs.ext4 /dev/drbd0
   ```

   On all instances, create the mount directory:

   ```
   sudo mkdir -p /greengrass/v2
   ```

   On the primary instance only, mount the DRBD device:

   ```
   sudo mount /dev/drbd0 /greengrass/v2
   ```

1. **Verify DRBD sync status.**

   ```
   sudo drbdadm status
   mount | grep 'drbd'
   ```
