---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns.html
---

# Create Infoblox objects using AWS CloudFormation custom resources and Amazon SNS
<a name="create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns"></a>

*Tim Sutton, Amazon Web Services*

## Summary
<a name="create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns-summary"></a>

**Notice**: AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

Infoblox Domain Name System (DNS), Dynamic Host Configuration Protocol (DHCP), and IP address management ([Infoblox DDI](https://www.infoblox.com/products/ddi/)) enables you to centralize and efficiently control a complex hybrid environment. With Infoblox DDI, you can discover and record all network assets in one authoritative IP address management (IPAM) database, in addition to managing DNS on premises and on the Amazon Web Services (AWS) Cloud by using the same appliances.

This pattern describes how to use an AWS CloudFormation custom resource to create Infoblox objects (for example, DNS records or IPAM objects) by calling the Infoblox WAPI API. For more information about the Infoblox WAPI, see the [WAPI documentation](https://www.infoblox.com/wp-content/uploads/infoblox-deployment-infoblox-rest-api.pdf) in the Infoblox documentation.

By using this pattern’s approach, you can obtain a unified view of DNS records and IPAM configurations for your AWS and on-premises environments, in addition to removing manual processes that create records and provision your networks. You can use this pattern’s approach for the following use cases:
+ Adding an A record after creating an Amazon Elastic Compute Cloud (Amazon EC2) instance
+ Adding a CNAME record after creating an Application Load Balancer
+ Adding a network object after creating a virtual private cloud (VPC)
+ Providing the next network range and using that range to create subnets

You can also extend this pattern and use other Infoblox device features such as adding different DNS record types or configuring Infoblox vDiscovery.

The pattern uses a hub-and-spoke design in which the hub requires connectivity to the Infoblox appliance on the AWS Cloud or on premises and uses AWS Lambda to call the Infoblox API. The spoke is in the same or a different account in the same organization in AWS Organizations, and calls the Lambda function by using an AWS CloudFormation custom resource.

## Prerequisites and limitations
<a name="create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns-prereqs"></a>

**Prerequisites **
+ An existing Infoblox appliance or grid, installed on the AWS Cloud, on premises, or both, and configured with an admin user that can administer IPAM and DNS actions. For more information about this, see [About admin accounts](https://docs.infoblox.com/display/nios86/About+Admin+Accounts) in the Infoblox documentation.
+ An existing DNS authoritative zone that you want to add records on the Infoblox appliance. For more information about this, see [Configuring authoritative zones](https://docs.infoblox.com/display/nios86/Configuring+Authoritative+Zones) in the Infoblox documentation.
+ Two active AWS accounts in AWS Organizations. One account is the hub account and the other account is the spoke account.
+ The hub and spoke accounts must be in the same AWS Region.
+ The hub account’s VPC must connect to the Infoblox appliance; for example, by using AWS Transit Gateway or VPC peering.
+ [AWS Serverless Application Model (AWS SAM),](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) locally installed and configured with AWS Cloud9 or AWS CloudShell.
+ The `Infoblox-Hub.zip` and `ClientTest.yaml` files (attached), downloaded to the local environment that contains AWS SAM.

**Limitations **
+ The AWS CloudFormation custom resource’s service token must be from the same Region where the stack is created. We recommend that you use a hub account in each Region, instead of creating an Amazon Simple Notification Service (Amazon SNS) topic in one Region and calling the Lambda function in another Region.

**Product versions**
+ Infoblox WAPI version 2.7

## Architecture
<a name="create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns-architecture"></a>

The following diagrams shows this pattern’s workflow.

![Creating Infoblox objects using AWS CloudFormation custom resources and Amazon SNS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8d609d3f-6f5e-4084-849f-ca191db8055e/images/3594a064-e103-4211-84b7-da67c41ebb15.png)

The diagram shows the following components for this pattern’s solution:

1. AWS CloudFormation custom resources enable you to write custom provisioning logic in templates that AWS CloudFormation runs when you create, update, or delete stacks. When you create a stack, AWS CloudFormation sends a `create` request to an SNS topic that's monitored by an application running on an EC2 instance.

1. The Amazon SNS notification from the AWS CloudFormation custom resource is encrypted through a specific AWS Key Management Service (AWS KMS) key and access is restricted to accounts in your organization in Organizations. The SNS topic initiates the Lambda resource that calls the Infoblox WAPI API.

1. Amazon SNS invokes the following Lambda functions that take the Infoblox WAPI URL, the user name, and password AWS Secrets Manager Amazon Resource Names (ARNs) as environment variables:
   + `dnsapi.lambda_handler` – Receives the `DNSName`, `DNSType`, and `DNSValue` values from the AWS CloudFormation custom resource and uses these to create DNS A records and CNAMES.
   + `ipaddr.lambda_handler` – Receives the `VPCCIDR`, `Type`, `SubnetPrefix`, and `Network Name` values from the AWS CloudFormation custom resource and uses these to add the network data into the Infoblox IPAM database or provide the custom resource with the next available network that can be used to create new subnets.
   + `describeprefixes.lambda_handler` – Calls the `describe_managed_prefix_lists` AWS API by using the `"com.amazonaws."+Region+".s3"` filter to retrieve the required `prefix ID`.
**Important**
These Lambda functions are written in Python and are similar to each other but call different APIs.

1. You can deploy the Infoblox grid as physical, virtual, or cloud-based network appliances.  It can be deployed on-premises or as a virtual appliance using a range of hypervisors, including VMware ESXi, Microsoft Hyper-V, Linux KVM, and Xen. You can also deploy the Infoblox grid on the AWS Cloud with an Amazon Machine Image (AMI).

1. The diagram shows a hybrid solution for the Infoblox grid that provides DNS and IPAM to resources on the AWS Cloud and on premises.

**Technology stack  **
+ AWS CloudFormation
+ IAM
+ AWS KMS
+ AWS Lambda
+ AWS SAM
+ AWS Secrets Manager
+ Amazon SNS
+ Amazon VPC

## Tools
<a name="create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns-tools"></a>
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
+ [AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) is an open-source framework that helps you build serverless applications in the AWS Cloud.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Code**

You can use the `ClientTest.yaml` sample AWS CloudFormation template (attached) to test the Infoblox hub. You can customize the AWS CloudFormation template to include the custom resources from the following table.

|  |
| --- |
| Create an A record using the Infoblox spoke custom resource | Return values: `infobloxref ` – Infoblox referencesExample resource:

```
ARECORDCustomResource:

  Type: "Custom::InfobloxAPI"

  Properties:

    ServiceToken: !Sub  arn:aws:sns:${AWS::Region}:${HubAccountID}:RunInfobloxDNSFunction

    DNSName: 'arecordtest.company.com'

    DNSType: 'ARecord'

    DNSValue: '10.0.0.1'
``` |
| --- |--- |
| Create a CNAME record using the Infoblox spoke custom resource | **Return values**: <br />`infobloxref ` – Infoblox references<br />**Example resource**:<pre>CNAMECustomResource:<br /><br />  Type: "Custom::InfobloxAPI"<br /><br />  Properties:<br /><br />    ServiceToken: !Sub arn:aws:sns:${AWS::Region}:${HubAccountID}:RunInfoblox    <br /><br />    DNSFunction<br /><br />    DNSName: 'cnametest.company.com'<br /><br />    DNSType: 'cname' <br /><br />    DNSValue: 'aws.amazon.com'</pre> |
| Create a network object using the Infoblox spoke custom resource | **Return values:**<br />`infobloxref ` – Infoblox references<br />`network` – Network range (the same as `VPCCIDR`)<br />**Example resource:**<pre>VPCCustomResource:<br /><br />  Type: 'Custom::InfobloxAPI'<br /><br />  Properties:<br /><br />    ServiceToken: !Sub  arn:aws:sns:${AWS::Region}:${HubAccountID}:RunInfobloxNextSubnetFunction<br /><br />    VPCCIDR: !Ref VpcCIDR<br /><br />    Type: VPC<br /><br />    NetworkName: My-VPC</pre> |
| Retrieve the next available subnet using the Infoblox spoke custom resource | **Return values:**<br />`infobloxref` – Infoblox references<br />`network ` – The subnet's network range<br />**Example resource:**<pre>Subnet1CustomResource:<br /><br />  Type: 'Custom::InfobloxAPI'<br /><br />  DependsOn: VPCCustomResource<br /><br />  Properties:<br /><br />    ServiceToken: !Sub  arn:aws:sns:${AWS::Region}:${HubAccountID}:RunInfobloxNextSubnetFunction<br /><br />    VPCCIDR: !Ref VpcCIDR<br /><br />    Type: Subnet<br /><br />    SubnetPrefix: !Ref SubnetPrefix<br /><br />NetworkName: My-Subnet</pre> |

## Epics
<a name="create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns-epics"></a>

### Create and configure the hub account’s VPC
<a name="create-and-configure-the-hub-accountrsquor-s-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC with a connection to the Infoblox appliance. | Sign in to the AWS Management Console for your hub account and create a VPC by following the steps in the [Amazon VPC on the AWS Cloud Quick Start reference deployment](https://aws-quickstart.github.io/quickstart-aws-vpc/) from AWS Quick Starts.The VPC must have HTTPS connectivity to the Infoblox appliance and we recommend that you use a private subnet for this connection. | Network administrator, System administrator |
| (Optional) Create the VPC endpoints for private subnets.  | VPC endpoints provide connectivity to public services for your private subnets. The following endpoints are required:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns.html)<br />For more information about creating endpoints for private subnets, see [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) in the Amazon VPC documentation. | Network administrator, Systems administrator |

### Deploy the Infoblox hub
<a name="deploy-the-infoblox-hub"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Build the AWS SAM template. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns.html) | Developer, System administrator |
| Deploy the AWS SAM template. | The `sam deploy` command takes the required parameters and saves them into the `samconfig.toml` file, stores the AWS CloudFormation template and Lambda functions in an S3 bucket, and then deploys the AWS CloudFormation template into your hub account.  <br />The following sample code shows how to deploy the AWS SAM template:<pre>$ sam deploy --guided<br /><br />Configuring SAM deploy<br />======================<br />        Looking for config file [samconfig.toml] :  Found<br />        Reading default arguments  :  Success<br />        Setting default arguments for 'sam deploy'<br />        =========================================<br />        Stack Name [Infoblox-Hub]:<br />        AWS Region [eu-west-1]:<br />        Parameter InfobloxUsername:<br />        Parameter InfobloxPassword:<br />        Parameter InfobloxIPAddress [xxx.xxx.xx.xxx]:<br />        Parameter AWSOrganisationID [o-xxxxxxxxx]:<br />        Parameter VPCID [vpc-xxxxxxxxx]:<br />        Parameter VPCCIDR [xxx.xxx.xxx.xxx/16]:<br />        Parameter VPCSubnetID1 [subnet-xxx]:<br />        Parameter VPCSubnetID2 [subnet-xxx]:<br />        Parameter VPCSubnetID3 [subnet-xxx]:<br />        Parameter VPCSubnetID4 []: <br />        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy<br />        Confirm changes before deploy [Y/n]: y<br />        #SAM needs permission to be able to create roles to connect to the resources in your template<br />Allow SAM CLI IAM role creation [Y/n]: n<br />Capabilities [['CAPABILITY_NAMED_IAM']]:<br />        Save arguments to configuration file [Y/n]: y<br />        SAM configuration file [samconfig.toml]:<br />        SAM configuration environment [default]: </pre>You must use the `--guided` option each time because the Infoblox sign-in credentials are not stored in the `samconfig.toml` file. | Developer, System administrator |

## Related resources
<a name="create-infoblox-objects-using-aws-cloudformation-custom-resources-and-amazon-sns-resources"></a>
+ [Getting started with WAPIs using Postman](https://blogs.infoblox.com/community/getting-started-with-wapis-using-postman/) (Infoblox Blog)
+ [Provisioning vNIOS for AWS Using the BYOL Model](https://docs.infoblox.com/display/NAIG/Provisioning+vNIOS+for+AWS+Using+the+BYOL+Model) (Infoblox documentation)
+ [quickstart-aws-vpc](https://github.com/aws-quickstart/quickstart-aws-vpc) (GitHub repo)
+ [describe\_managed\_prefix\_lists](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_managed_prefix_lists) (AWS SDK for Python documentation)

## Attachments
<a name="attachments-8d609d3f-6f5e-4084-849f-ca191db8055e"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/8d609d3f-6f5e-4084-849f-ca191db8055e/attachments/attachment.zip)
