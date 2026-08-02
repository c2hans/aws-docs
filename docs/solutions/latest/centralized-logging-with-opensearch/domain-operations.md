---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/domain-operations.html
---

# Domain Operations
<a name="domain-operations"></a>

Once logged into the Centralized Logging with OpenSearch console, you can import an Amazon OpenSearch Service domain.

 **Prerequisites**

1. Centralized Logging with OpenSearch supports Amazon OpenSearch Service, and engine version OpenSearch 1.3 or later.

1. Centralized Logging with OpenSearch supports OpenSearch clusters within VPC. If you don’t have an Amazon OpenSearch Service domain yet, you can create an Amazon OpenSearch Service domain within VPC. See [Launching your Amazon OpenSearch Service domains within a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html).

1. Centralized Logging with OpenSearch supports OpenSearch clusters with [fine-grained access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html) only. In the security configuration, the Access policy should look like the following image:

    **Sample access policy.**
![image27](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image27.png)

## Import an Amazon OpenSearch Service Domain
<a name="import-an-amazon-opensearch-service-domain"></a>

1. Sign in to the Centralized Logging with OpenSearch console.

1. In the left navigation panel, under **Domains**, choose **Import OpenSearch Domain**.

1. On the **Select domain** page, choose a domain from the dropdown list. The dropdown list will display only domains in the same Region as the solution.

1. Choose **Next**.

1. On the **Configure network** page, under **Network creation**, choose **Manual** and choose **Next**; or choose **Automatic**, and go to step 9.

1. Under **VPC**, choose a VPC from the list. By default, the solution creates a standalone VPC, and you can choose the one named `LogHubVpc/DefaultVPC`. You can also choose the same VPC as your Amazon OpenSearch Service domains.

1. Under **Log Processing Subnet Group**, select at least 2 subnets from the dropdown list. By default, the solution creates two private subnets. You can choose subnets named `LogHubVpc/DefaultVPC/privateSubnet1` and `LogHubVpc/DefaultVPC/privateSubnet2`.

1. Under **Log Processing Security Group**, select one from the dropdown list. By default, the solution creates one Security Group named `ProcessSecurityGroup`.

1. On the **Create tags** page, add tags if needed.

1. Choose **Import**.

## Set up VPC Peering
<a name="set-up-vpc-peering"></a>

By default, the solution creates a standalone VPC. You must create VPC Peering to allow the log processing layer to have access to your Amazon OpenSearch Service domains.

**Note**
Automatic mode will create VPC peering and configure route table automatically. You do not need to set up VPC peering again.

 **VPC peering connecting the solution and an OpenSearch VPC.**

![setup vpc peering](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/setup-vpc-peering.png)

Follow this section to create VPC peering, update your security group, and update route tables.

### Create VPC Peering Connection
<a name="create-vpc-peering-connection"></a>

1. Sign in to the Centralized Logging with OpenSearch console.

1. In the left navigation panel, under **Domains**, select **OpenSearch Domains**.

1. Find the domain that you imported and select the domain name.

1. Choose the **Network** tab.

1. Copy the VPC ID in both sections **OpenSearch domain network** and **Log processing network**. You will create a Peering Connection between these two VPCs.

1. Navigate to [VPC Console Peering Connections](https://console.aws.amazon.com/vpc/home#PeeringConnections).

1. Select the Create peering connection button.

1. On the **Create peering connection** page, enter a name.

1. For the Select a local VPC to peer with, VPC ID (Requester), select the VPC ID of the Log processing network.

1. For the Select another VPC to peer with, VPC ID (Accepter), select the VPC ID of the OpenSearch domain network.

1. Choose **Create peering connection**, and navigate to the peering connection detail page.

1. Choose the **Actions** button and choose **Accept request**.

### Update Route Tables
<a name="update-route-tables"></a>

1. Go to the Centralized Logging with OpenSearch console.

1. In the **OpenSearch domain network** section, choose the subnet under **Availability Zone and Subnets** to open the subnet console in a new tab.

1. Select the subnet, and choose the **Route table** tab.

1. Select the associated route table of the subnet to open the route table configuration page.

1. Select the **Routes** tab, and choose **Edit routes**.

1. Add a route 10.255.0.0/16 (the CIDR of Centralized Logging with OpenSearch, if you created the solution with existing VPC, change this value) pointing to the Peering Connection you created.

1. Go back to the Centralized Logging with OpenSearch console.

1. Choose the VPC ID under the **OpenSearch domain network** section.

1. Select the VPC ID on the VPC Console and find its **IPv4 CIDR**.

1. On the Centralized Logging with OpenSearch console, in the **Log processing network** section, choose the subnets under **Availability Zone and Subnets** to open the subnets in new tabs.

1. Repeat step 3, 4, 5, 6 to add an opposite route. Namely, configure the IPv4 CIDR of the OpenSearch VPC to point to the Peering Connection. You must repeat the steps for each subnet of the Log processing network.

### Update Security Group of OpenSearch Domain
<a name="update-security-group-of-opensearch-domain"></a>

1. On the Centralized Logging with OpenSearch console, under the **OpenSearch domain network** section, select the Security Group ID in **Security Groups** to open the Security Group in a new tab.

1. On the console, select **Edit inbound rules**.

1. Add the rule `ALLOW TCP/443 from 10.255.0.0/16` (the CIDR of Centralized Logging with OpenSearch, if you created Centralized Logging with OpenSearch with existing VPC, change this value).

1. Choose **Save rules**.

**Note**
If you prefer to use Transit Gateway rather than VPC peering for connectivity between OpenSearch domain VPC and the solution VPC, select manual network create option during domain import. After creation, you’ll need to configure your route tables to direct traffic through the Transit Gateway instead of VPC peering connection.

## Remove an Amazon OpenSearch Service domain
<a name="remove-an-amazon-opensearch-service-domain"></a>

If needed, you can remove the Amazon OpenSearch Service domains.

**Important**
Removing the domain from Centralized Logging with OpenSearch will NOT delete the Amazon OpenSearch Service domain in your AWS account. It will NOT impact any existing log analytics pipelines.

1. Sign in to the Centralized Logging with OpenSearch console.

1. In the navigation pane, under **Domains**, choose **OpenSearch Domains**.

1. Select the domain from the table.

1. Choose **Remove**.

1. In the confirmation dialog box, choose **Remove**.
