---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/replatform-to-ec2.html
---

# Replatform to EC2
<a name="replatform-to-ec2"></a>

The Cloud Migration Factory on AWS solution allows groups of EC2 instances to be launched automatically from configurations defined in its datastore; deploying EC2 instances with EBS volumes attached. This provides the ability to provision new EC2 instances, allowing Replatform through AWS CloudFormation, and Rehost of on-premise servers with AWS MGN within a single CMF user interface. Before you can use this functionality the datastore must contain the definition of the servers. Once this has been addressed the servers should be linked to a wave. When the decision is taken to launch the EC2 instances, the user can initiate the following actions against the wave:
+ EC2 Input Validation
+ EC2 Generate CF Template
+ EC2 Deployment

## Prerequisites
<a name="prerequisites-1"></a>

Permissions to add the Replatform attribute access.

## Script Execution Platform Selection
<a name="script-execution-platform-selection"></a>

Before deploying automation scripts, determine which compute platform best suits your needs:
+  **Traditional Automation Server**: Best for scenarios requiring complex dependencies, multiple programming languages, or specific OS requirements
+  **SSM Automation Document**: Recommended for standard Python-based automation scripts where access to on-premises environment is not needed

## Initial configuration
<a name="initial-configuration"></a>

Configuration of the new EC2 instances is performed through the creation of new server items using either the user interface or through the import of a CSV intake form containing the server items. These definitions are converted to AWS CloudFormation templates stored in an S3 bucket within the same AWS account that the AWS CMF instance is deployed.

### User interface definition
<a name="user-interface-definition-1"></a>

When defining a server in the AWS Cloud Migration Factory datastore for use with the Replatform to EC2 functionality the server needs to be configured with a **Migration Strategy** of **Replatform**. Once **Replatform** is selected then the additional attributes required for this functionality will be shown on the screen. The following attributes are required to be populated for the functionality to work:

#### Required attributes
<a name="required-attributes"></a>

 **AMI Id** - ID of the Amazon Machine Image used to launch the EC2 instance.

 **Availability Zone** - AZ that the EC2 instance will be deployed to.

 **Root Volume Size** - Size in GB of the root volume for the instance.

 **Instance Type** - EC2 instance type to be used.

 **Security Group Ids** - List of security groups assigned to the instance.

 **Subnet Ids** - Subnet ID to assign this EC2 instance to.

 **Tenancy** - Currently the only supported option for the Replatform to EC2 integration is **Shared** any other option will be replaced with **Shared** when the template is generated.

#### Optional Attributes
<a name="optional-attributes"></a>

 **Enable Detailed Monitoring** - Check to enable detailed monitoring.

 **Additional Volume Names** - List of Additional EBS volume names. Each item in the list needs to map to the same line as the **Size** and **Type** lists.

 **Additional Volume Sizes** - List of additional EBS volume sizes. Each item in the list needs to map to the same line as the **Names** and **Type** lists.

 **Additional Volume Types** - List of additional EBS volume types. Each item in the list must map to the same line as the **Names** and **Size** lists, if not specified then defaults to **gp2** for all volumes.

 **EBS KMS Key Id for Volume Encryption** - If EBS volumes will be encrypted then specify the **Key ID**, **Key ARN**, **Key Alias**, or **Alias ARN**.

 **Enable EBS Optimized** - Select to turn on **EBS Optimized**.

 **Root Volume Name** - Select from the options provided, if not specified then the ID will be used.

 **Root Volume Type** - Provide the EBS type of the volume to be created, if not specified then defaults to **gp2**.

### Intake form definition
<a name="intake-form-definition-1"></a>

Intake forms can contain the details to create or update multiple types of record with the datastore in a single row of the csv file, this enables the import of related data. In the following example, the wave, application and server records will be created and related to each other automatically during the import.

Example: Intake form

| Column name | Example data | Required | Notes |
| --- | --- | --- | --- |
| wave\_name |  `wave1`  | Yes |  |
| app\_name |  `app1`  | Yes |  |
| aws\_accountid |  `1234567890`  | Yes |  |
| server\_name |  `Server1`  | Yes |  |
| server\_fqdn |  `Server1`  | Yes |  |
| server\_os\_family |  `linux`  | Yes |  |
| server\_os\_version |  `Amazon`  | Yes |  |
| server\_tier |  `Web`  | No |  |
| server\_environment |  `Dev`  | No |  |
| subnet\_IDs |  `subnet-xxxxxxx`  | Yes |  |
| securitygroup\_ID |  `sg-yyyyyyyyyy`  | Yes |  |
| instanceType |  `m5.large`  | Yes |  |
| iamRole |  `ec2customrole`  | No |  |
| tenancy |  `Shared`  | Yes |  |
| r\_type |  `Replatform`  | Yes |  |
| root\_vol\_size |  `50`  | Yes |  |
| ami\_id |  `ami-zzzzzzzzzz`  | Yes |  |
| availabilityzone |  `us-west-2a`  | Yes |  |
| root\_vol\_type |  `gp2`  | No |  |
| add\_vols\_size |  `40:100`  | No |  |
| add\_vols\_type |  `gp2:gp3`  | No |  |
| ebs\_optimized |  `false`  | No |  |
| ebs\_kmskey\_id |  `1111-1111-1111-1111`  | No |  |
| detailed\_monitoring |  `true`  | No |  |
| root\_vol\_name |  `Server1_root_volume`  | No |  |
| add\_vols\_name |  `Server1_root_volumeA: Server1_root_volumeB`  | No |  |

To import the intake form, follow the same process as any other data imports into the Cloud Migration Factory on AWS solution.

## Deployment actions
<a name="deployment-actions"></a>

### EC2 input validation
<a name="ec2-input-validation"></a>

After defining the instance parameters, you must first run the wave action: **Replatform**>**EC2**>**EC2 Input Validation**. This action verifies that all the correct parameters have been provided for each server in order to create a valid CloudFormation template.

**Note**
This validation does not currently verify that the input parameters are valid, only that they are present in each server definition. You must verify the correct values before creating the template otherwise the deployment of the template will fail.

### EC2 generate CloudFormation template
<a name="ec2-generate-cloud-formation-template"></a>

Once the definitions for all servers included in a wave have been verified the CloudFormation template can be generated. To do this, run the wave action: **Replatform**>**EC2**>**EC2 Generate CF Template**. This action creates a CloudFormation template for each application in the wave, where the servers in the application have a **Migration Strategy** of **Replatform**; any servers with other migration strategies defined will not be included in the template.

Once run, the templates for each application will be stored in the S3 bucket: ** -gfbuild-cftemplates **, which was automatically created when the Cloud Migration Factory on AWS solution was deployed. The folder structure of this bucket is as follows:
+ [Target AWS Account ID]
+ [Wave Name]
  +  **CFN\_Template\_** ** \\\_ ** ** 0yaml **

Each time the generate action is run a new version of the template is stored in the S3 bucket. The S3 URIs for the templates will be provided in the notification, these templates can be reviewed or edited as required before deployment.

The CloudFormation templates generate the following CloudFormation resource types currently:
+ AWS::EC2::Instance
+ AWS::EC2::Volume
+ AWS::EC2::VolumeAttachment

### EC2 deployment
<a name="ec2-deployment"></a>

Once you’re ready to deploy the new EC2 instances, you can initiate the **EC2 Deployment** action can be initiated through the wave action **Replatform**>**EC2**>**EC2 Deployment**. This action will use the latest version of the CloudFormation template for each application in the wave, and deploy these templates into the target accounts selected, through AWS CloudFormation.
