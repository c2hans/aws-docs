---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-network-modules.html
---

# Step 1: Enable Network modules
<a name="enable-network-modules"></a>

Follow these steps to enable the Network modules.

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **Network** from the left navigation pane.

1. Choose **Deploy New Module**.

1. Based on your use cases, follow the steps in [Create Amazon VPC](#create-amazon-vpc) for generating a new VPC, or follow the steps in [Import Amazon VPC](#import-amazon-vpc) for importing the existing VPC by providing the required attributes.

## Option 1.a: Create Amazon VPC
<a name="create-amazon-vpc"></a>

1. For **Select Region**, select the Region where you want the VPC to be created. There should be only one hub Region option if you haven’t deployed any spoke Regions.

1. For **Select Network** module, select Create Amazon VPC and choose **Next**.

1. For **Configure VPC settings**, review the parameters for this module and modify them as necessary. This module uses the following default values.

<table>
<thead>
  <tr><th> <b>Parameter</b> </th><th> <b>Default</b> </th><th> <b>Description</b> </th></tr>
</thead>
<tbody>
  <tr><td> <b>Availability Zones</b> </td><td> <code>&lt;Region&gt;a, &lt;Region&gt;b</code> </td><td>(Select 2) List of Availability Zones to use for the subnets in the VPC. The logical order is preserved.</td></tr>
  <tr><td> <b>VPC CIDR</b> </td><td> <code>10.0.0.0/16</code> </td><td>CIDR block for the VPC.</td></tr>
  <tr><td> <b>Private Subnet CIDR List</b> </td><td> <code>10.0.0.0/19, 10.0.32.0/19</code> </td><td>Comma delimited list of CIDR blocks for private subnets 1 and 2, located in Availability Zones 1 and 2, respectively.<br /> <b>Note:</b> CIDR ranges in each Region must not overlap. The default values provided don’t overlap with each other, and are within the default VPC CIDR range provided.</td></tr>
  <tr><td> <b>Public Subnet CIDR List</b> </td><td> <code>10.0.128.0/20, 10.0.144.0/20</code> </td><td>Comma delimited list of CIDR blocks for public subnets 1 and 2, located in Availability Zones 1 and 2, respectively.<br /> <b>Note:</b> CIDR ranges in each Region must not overlap. The default values provided don’t overlap with each other, and are within the default VPC CIDR range provided.</td></tr>
  <tr><td> <b>Enable VPC Flow Logs</b> </td><td> <code>true</code> </td><td>Set to <code>true</code> to create VPC flow logs for the VPC and publish them to CloudWatch. If you set it to <code>false</code>, the VPC flow logs won’t be created.</td></tr>
  <tr><td> <b>VPC Flow Logs Traffic Type</b> </td><td> <code>REJECT</code> </td><td>The type of traffic to log. You can log traffic that the resource accepts (<code>ACCEPT</code>) or rejects (<code>REJECT</code>), or <code>ALL</code> Traffic.</td></tr>
</tbody>
</table>

1. For **Configure Tag Settings**, review the tags for this module and modify them as necessary. By default, this module uses tags defined in the main solution stack.

1. Choose **Next**.

1. On the **Review** page, verify all the parameters that you provided and choose **Deploy Module** if you confirm that they are correct.

1. The status of the network module shows as **Enabling in progress**. The deployment of this module takes approximately five minutes. After the deployment is complete, the status of the network module shows as **Enabled**.

## Option 1.b: Import Amazon VPC
<a name="import-amazon-vpc"></a>

## Pre-deployment requirements
<a name="pre-deployment-requirements"></a>

1. Availability Zones

   1. Ensure that selected Availability Zones host the necessary default instance types used by MCS:

      1. t3.large, m5.xlarge, g4dn.xlarge, r6g.large

      1. If other instance types are desired, ensure that they are available in the VPC’s Availability Zones

   1. Use AWS CLI command to verify, e.g. for us-east-1:

      ```
      $ aws ec2 describe-instance-type-offerings \
        --location-type availability-zone \
        --filters Name=instance-type,Values=t3.large,m5.xlarge,g4dn.xlarge,r6g.large \
        --region us-east-1 \
        --query 'InstanceTypeOfferings[].Location' \
        --output text | tr '\t' '\n' | sort | uniq
      ```

1. Subnet Configuration

   1. At least 2 public subnets across different Availability Zones which will be used by MCS

   1. At least 2 private subnets across different Availability Zones which will be used by MCS

1. Internet Connectivity

   1. Public subnets must have route tables with routes to an Internet Gateway (IGW)

   1. Private subnets must have route tables with routes to NAT Gateways (NGW)

1. Required VPC Endpoints

   1. Interface Endpoints

      1. com.amazonaws.[region].ssm

      1. com.amazonaws.[region].ssmmessages

      1. com.amazonaws.[region].ec2

      1. com.amazonaws.[region].ec2messages

   1. Gateway Endpoint

      1. com.amazonaws.[region].s3

**Note**
All endpoints must be associated with the private subnets where MCS workloads will run. If the Endpoint already exists, this requires that you navigate to that endpoint’s configuration page, select "Manage Subnets", and ensure that the endpoint is associated with the private subnets that you will provide to MCS. If the Endpoint does not already exist, ensure that during creation of the endpoint, that the subnets that you will provide to MCS are selected.
In addition, the security group associated with these endpoints must be configured to allow all traffic from the VPC CIDR source.

VPC Peering must be configured between hub and spoke VPCs. For more information, see [Work with VPC peering connections](https://docs.aws.amazon.com/vpc/latest/peering/working-with-vpc-peering.html). Ensure that the route tables are configured correctly for the VPC peering connection. For more information, see [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html).

## Validation Testing
<a name="validation-testing"></a>

Before proceeding with the MCS Unmanaged VPC Module deployment, validate your VPC configuration:

1. Launch an Amazon Linux 2023 instance in one of the private subnets

1. Ensure the instance has an IAM Role with `AmazonSSMManagedInstanceCore` permissions

1. Attempt to connect to the instance using AWS Systems Manager Session Manager

1. If you see "Instance is not connected to Session Manager" or the "Connect" button is disabled, troubleshoot your VPC endpoint configuration, network routes, and security groups.

1. A successful connection confirms proper network configuration.

## Deploying the MCS Unmanaged VPC Module
<a name="deploying-the-mcs-unmanaged-vpc-module"></a>

1. For **Select Region**, select the Region where you want the VPC to be imported from. There should be only one hub Region option if you have not deployed any spoke Regions.
**Note**
The VPC must exist in the same account and Region where the Network module is being enabled.

1. For **Select Network** module, select **Import Amazon VPC** and choose **Next**.

1. For **Configure VPC settings**, review the parameters for this module and modify them as necessary. This module uses the following default values.

<table>
<thead>
  <tr><th> <b>Parameter</b> </th><th> <b>Default</b> </th><th> <b>Description</b> </th><th> <b>Notes</b> </th></tr>
</thead>
<tbody>
  <tr><td> <b>VPC ID</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Identifier of the existing VPC.</td><td></td></tr>
  <tr><td> <b>VPC CIDR</b> </td><td> {{&lt;Requires input&gt;}} </td><td>VPC CIDR block.</td><td></td></tr>
  <tr><td> <b>Private Subnet IDs</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Exactly two comma separated Subnet IDs for the private subnets.</td><td></td></tr>
  <tr><td> <b>Public Subnet IDs</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Exactly two comma separated Subnet IDs for the public subnets.</td><td></td></tr>
  <tr><td> <b>Private Subnet Route Table IDs</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Exactly two comma separated Route table IDs for private subnets.</td><td>See Notes below</td></tr>
  <tr><td> <b>Public Subnet Route Table IDs</b> </td><td> {{&lt;Requires input&gt;}} </td><td>Exactly two comma separated Route table IDs for public subnets.</td><td>See Notes below</td></tr>
  <tr><td> <b>Availability Zones</b> </td><td> {{&lt;Requires input&gt;}} </td><td>(Select 2) List of Availability Zones to use for the subnets in the VPC. The logical order is preserved.</td><td></td></tr>
</tbody>
</table>

**Note**
If there is only one Route Table available, you can duplicate the entry. MCS expects exactly two comma delimited values to be provided. For example:

   ```
   rtb-prv123456,rtb-prv123456
   ```

1. For **Configure Tag Settings**, review the tags for this module and modify them as necessary. By default, this module uses tags defined in the main solution stack.

1. Choose **Next**.

1. On the **Review** page, verify all the parameters that you provided. If they are correct, choose **Deploy Module**.

1. The status of the network module shows as **Enabling in progress**. The deployment of this module takes approximately five minutes. After the deployment is complete, the status of the network module shows as **Enabled**.
