---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/deployment.html
---

# Deploying the PoC environment
<a name="deployment"></a>

Many users prefer to thoroughly test all communication channels and migration steps in advance. Testing migration from isolated networks could be a challenge. To address that need, AWS provides two options:
+ An [AWS CloudFormation template](https://github.com/aws-samples/amazon-mgn-private-endpoint/blob/main/CloudFormation-for-MGN-private-deployments/MGN_Private_EP_v2_ticket.yaml) that prepares all required resources on AWS. The template builds a proof of concept (PoC) environment that emulates the components of the data center environment and sets up the AWS infrastructure. It includes isolated source and target VPCs, subnets, and VPC endpoints.
+ A dedicated workshop ([Migrate the Well-Architected Way](https://catalog.workshops.aws/well-architected-migration/)) with detailed, step-by-step instructions to create your test environment (see the step [Create VPC endpoints](https://catalog.workshops.aws/well-architected-migration/en-US/2-migration/1-initial-credentials-setup/3-vpc-endpoints)).

Alternatively, you can deploy your PoC environment by following the steps in the next sections.

## Manual deployment
<a name="manual"></a>

The following list outlines the major steps for manual deployments in your environment. For more information, see [Connect to AWS Transform MGN data and control planes over a private network](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/connect-to-application-migration-service-data-and-control-planes-over-a-private-network.html?did=pg_card&trk=pg_card).

1. Create the source VPC and staging area VPC with a private subnet.

1. Create the following VPC endpoints in the staging area subnet:
   + MGN, and enable the private DNS name (shared by the replication server and source server).
   + Amazon EC2, and enable the private DNS name (shared by the replication server and source server).
   + Amazon S3 (private DNS name not supported). Interface endpoints are supported across Direct Connect, AWS VPN, and VPC peering. Therefore, this is required for source servers only (and could be located on premises) to connect to the MGN control plane over a private network.
**Note**
The **ssm **and **ssmmessages **endpoints are optional and currently created to connect the source server through the AWS Systems Manager Session Manager.
   + Amazon S3 gateway endpoint in the staging area subnet. This is required by the replication server to connect to Amazon S3. You must update the routes for the staging area subnet.

1. Create an inbound resolver endpoint in the staging area VPC to allow resolution of the private DNS record (for VPC interface endpoints) from the source VPC.

1. Update the source VPC DHCP options with the inbound resolver endpoint of the staging area VPC as DNS server IP.

1. Enable peering between the source and staging VPCs, and update both VPC route tables.

1. Create a security group in the source and staging VPCs to allow the following ports.

<table>
<tbody>
</tbody>
</table>

1. Initialize MGN in the staging area AWS Region by updating the staging area subnet details and enabling communication over private IP.

1. Create an AWS Identity and Access Management (IAM) role for installing MGN Agent. Attach managed policies and generate access keys and a secrets key.

1. Create an IAM profile to connect Amazon EC2 via the Session Manager.

1. Install an Agent on the source machines.

## Automate agent deployments with Cloud Migration Factory
<a name="automated"></a>

The [Cloud Migration Factory on AWS](https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/) automates the deployment of the MGN Agent for the private networks scenario, with additional command line parameters. When you deploy this solution (see options for [automated deployment](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/deployment.html)), you can use these [scripts](https://github.com/aws-samples/amazon-mgn-private-endpoint/blob/main/CMF-scripts-for-MGN-private-deployments/Archive-endpoint-cmfv3__1_.zip) and one of the following options:
+ Manually run these [scripts](https://github.com/aws-samples/amazon-mgn-private-endpoint/blob/main/CMF-scripts-for-MGN-private-deployments/Archive-endpoint-cmfv3__1_.zip) from the command line, as described in the [Run automations from command prompt](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/run-automations-from-command-prompt.html) section of the [Cloud Migration Factory User Guide](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/welcome.html)
+ Add the [scripts](https://github.com/aws-samples/amazon-mgn-private-endpoint/blob/main/CMF-scripts-for-MGN-private-deployments/Archive-endpoint-cmfv3__1_.zip) to Migration Factory by following the instructions in the [Scripts management](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/scripts-management.html) section for full integration with Cloud Migration Factory

These scripts automate the following:
+ MGN Agent installation on a Windows server using private endpoints
+ MGN Agent installation on Linux servers using private endpoints
