---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/deploying-vmware-cloud-on-aws-sddc.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Deploying VMware Cloud on AWS SDDC
<a name="deploying-vmware-cloud-on-aws-sddc"></a>

 To start the deployment process, sign in to Cloud Services Portal (CSP).

1.  Log in to the VMC Console at [https://vmc.vmware.com](https://vmc.vmware.com).

1.  Choose **VMware Cloud on AWS Service** from the services listed.
![A screenshot of the My Services screen. Choose VMware Cloud on AWS Service.](http://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/images/my-services.png)

1.  Choose **Create SDDC**.
![A screenshot of the Welcome screen. Choose Create SDDC .](http://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/images/welcome2.png)

1.  Enter the SDDC properties:
   +  **AWS Region** — Choose the Region where you want to deploy the SDDC. This will be the same Region as the previously created VPC.
   +  **Deployment** — Choose **Multi-Host** or **Single-Host**. Single-Host configuration is limited to a 30-day lifespan. You can scale up to the minimum of 2-host without disruption before the 30-day period ends.
   +  **Host Type** — Select the host type: `i3` or `i3en`.
   +  **SDDC Name** — Enter the name of SDDC. This is a display name and doesn’t reflect the cluster or vCenter name.
   +  **Number of Hosts** — if you are deploying a multi-host cluster, specify the initial number of hosts in the SDDC. You can add or remove hosts later if needed.
   +  **Host Capacity and Total Capacity** — This will update to reflect the number of hosts selected.
   +  **Show Advanced Configuration** — (Optional) Select the size of the SDDC appliances.

    By default, a new SDDC is created with medium-sized NSX Edge and vCenter Server appliances. Large-sized appliances are recommended for deployments with more than 30 hosts or 3000 VMs or in any other situation where management cluster resources might be oversubscribed.

    The Large SDDC type is also required for the "Edge Scale Out" feature; should be noted that if a customer plans to leverage Traffic Groups (to scale out source-based routes via distinct Edges) that this is required at deployment time. It should also be noted that this setting cannot be changed after the SDDC has been deployed.

    If you create the SDDC with a medium appliance configuration and find that you need additional management cluster resources, you can upsize the configuration to large sized appliances.

1.  When you have finished, choose **Next**.
![A screenshot of the SDDC Properties screen. Enter the SDDC properties and choose NEXT Enter the SDDC properties and choose NEXT.](http://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/images/sddc-properties.png)

1.  Connect to your AWS account.
**Important**
After an AWS account has been associated with a VMware Organization as the seller of record, the AWS account number cannot be updated. There can be only one AWS seller of record per VMware Organization.
   +  **Connect to a new AWS account** — Select this option and follow the instructions on the page. The VMC Console shows the progress of the connection. Once completed, you can progress to the next step. The account needs to have sufficient permissions to run a CloudFormation Template in the customer account.

1.  Choose **NEXT**.
![A screenshot of the Connect to AWS screen. After you connect to your AWS account, choose NEXT .](http://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/images/connect-to-aws.png)

1.  Select your previously-configured VPC and subnet.
![A screenshot of the VPC and subnet screen. Select your previously-configured VPC and subnet. .](http://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/images/vpc-and-subnet.png)

1.  Choose **NEXT**.

1.  Enter the Management Subnet CIDR block for the SDDC.

1.  Choose **NEXT**.
![A screenshot of the Configure Network screen. Enter the Management Subnet CIDR block for the SDDC and choose NEXT.](http://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/images/configure-network.png)

**Important**
 This must be a [RFC1918](https://tools.ietf.org/html/rfc1918) private address space (`10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`) with CIDR block sizes of /16, /20, or /23. The management CIDR block cannot be changed after the SDDC is deployed. Choose a range of IP addresses that does not overlap with the AWS subnet you are connecting to. If you plan to connect the SDDC to an on-premises DC or another environment, the IP subnet must be unique within your enterprise network infrastructure. Choose a CIDR that will give you future scalability.
 Refer to the *SDDC management IP planning * entry in the *Design considerations* table, located in the [Infrastructure preparation and planning](account-requirements.md#infrastructure-preparation-and-planning) section of this document.

1.  Acknowledge that you understand and take responsibility for the costs you incur when you deploy an SDDC, then choose **DEPLOY SDDC** to create the SDDC.

![A screenshot of the View and Acknowledge screen. Select DEPLOY SDDC to create the SDDC.](http://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/images/review-acknowledge.png)

Charges begin when you click **DEPLOY SDDC**. You cannot pause or cancel the deployment process after it starts. You won't be able to use the SDDC until deployment is complete. Deployment typically takes about two hours.

![A screenshot showing a successfully deployed SDDC .](http://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/images/successful-deployment.png)
