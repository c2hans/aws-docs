---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-enterprise-data-mesh-amazon-data-zone.html
---

# Build an enterprise data mesh with Amazon DataZone, AWS CDK, and AWS CloudFormation
<a name="build-enterprise-data-mesh-amazon-data-zone"></a>

*Dhrubajyoti Mukherjee, Ravi Kumar, Weizhou Sun, and Adjoa Taylor, Amazon Web Services*

## Summary
<a name="build-enterprise-data-mesh-amazon-data-zone-summary"></a>

On Amazon Web Services (AWS), customers understand that data is the key to accelerating innovation and driving business value for their enterprise. To manage this massive data, you can adopt a decentralized architecture such as data mesh. A data mesh architecture facilitates product thinking, a mindset that takes customers, goals, and the market into account. Data mesh also helps to establish a federated governance model that provides fast, secure access to your data.

[Strategies for building a data mesh-based enterprise solution on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/introduction.html) discusses how you can use the Data Mesh Strategy Framework to formulate and implement a data mesh strategy for your organization. By using the Data Mesh Strategy Framework, you can optimize the organization of teams and their interactions to accelerate your data mesh journey.

This document provides guidance on how to build an enterprise data mesh with [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html). Amazon DataZone is a data management service for cataloging, discovering, sharing, and governing data stored across AWS, on premises, and third-party sources. The pattern includes code artifacts that help you deploy the data mesh‒based data solution infrastructure using AWS Cloud Development Kit (AWS CDK) and AWS CloudFormation. This pattern is intended for cloud architects and DevOps engineers.

For information about the objectives of this pattern and the solution scope, see the [Additional information](#build-enterprise-data-mesh-amazon-data-zone-additional) section.

## Prerequisites and limitations
<a name="build-enterprise-data-mesh-amazon-data-zone-prereqs"></a>

**Prerequisites**
+ A minimum of two active AWS accounts: one for the central governance account and another for the member account
+ AWS administrator credentials for the central governance account in your development environment
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) to manage your AWS services from the command line
+ Node.js and Node Package Manager (npm) [installed](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) to manage AWS CDK applications
+ AWS CDK Toolkit [installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install) globally in your development environment by using npm, to synthesize and deploy AWS CDK applications

  ```
  npm install -g aws-cdk
  ```
+ Python version 3.12 installed in your development environment
+ TypeScript installed in your development environment or installed globally by using npm compiler:

  ```
  npm install -g typescript
  ```
+ Docker installed in your development environment
+ A version control system such as Git to maintain the source code of the solution (recommended)
+ An integrated development environment (IDE) or text editor with support for Python and TypeScript (strongly recommended)

**Limitations**
+ The solution has been tested only on machines that are running Linux or macOS.
+ In the current version, the solution doesn’t support the integration of Amazon DataZone and AWS IAM Identity Center by default. However, you can configure it to support this integration.

**Product versions**
+ Python version 3.12

## Architecture
<a name="build-enterprise-data-mesh-amazon-data-zone-architecture"></a>

The following diagram shows a data mesh reference architecture. The architecture is based on Amazon DataZone and uses Amazon Simple Storage Service (Amazon S3) and AWS Glue Data Catalog as data sources. The AWS services that you use with Amazon DataZone in your data mesh implementation might differ, based on your organization's requirements.

![Five step workflow for members accounts and central governance account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/79056dd9-e669-4302-afb8-21e3e0e8a136/images/eacbffca-4f25-405a-a7c8-f89d0fee5682.png)

1. In the producer accounts, raw data is either fit for consumption in its current form or it’s transformed for consumption by using AWS Glue. The technical metadata for the data is stored in Amazon S3 and is evaluated using a AWS Glue data crawler. The data quality is measured by using [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html). The source database in the Data Catalog is registered as an asset in the Amazon DataZone catalog. The Amazon DataZone catalog is hosted in the central governance account using Amazon DataZone data source jobs.

1. The central governance account hosts the Amazon DataZone domain and the Amazon DataZone data portal. The AWS accounts of the data producers and consumers are associated with the Amazon DataZone domain. The Amazon DataZone projects of the data producers and consumers are organized under the corresponding Amazon DataZone domain units.

1. End users of the data assets log into the Amazon DataZone data portal by using their AWS Identity and Access Management (IAM) credentials or single sign-on (with integration through IAM Identity Center). They search, filter, and view asset information (for example, data quality information or business and technical metadata) in the Amazon DataZone data catalog.

1. After an end user finds the data asset that they want, they use the Amazon DataZone subscription feature to request access. The data owner on the producer team receives a notification and evaluates the subscription request in the Amazon DataZone data portal. The data owner approves or rejects the subscription request based on its validity.

1. After the subscription request is granted and fulfilled, the asset is accessed in the consumer account for the following activities:
   + AI/ML model development by using Amazon SageMaker AI
   + Analytics and reporting by using Amazon Athena and Amazon Quick

## Tools
<a name="build-enterprise-data-mesh-amazon-data-zone-tools"></a>

**AWS services**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon Simple Storage Service (Amazon S3) by using standard SQL.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html) is a data management service that helps you catalog, discover, share, and govern data stored across AWS, on premises, and in third-party sources.
+ [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a cloud-scale business intelligence (BI) service that helps you visualize, analyze, and report your data in a single dashboard.
+ [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/?id=docs_gateway) is a managed machine learning (ML) service that helps you build and train ML models and then deploy them into a production-ready hosted environment.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code repository**

The solution is available in the GitHub [data-mesh-datazone-cdk-cloudformation](https://github.com/aws-samples/data-mesh-datazone-cdk-cloudformation) repository.

## Epics
<a name="build-enterprise-data-mesh-amazon-data-zone-epics"></a>

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the repository, run the following command in your local development environment (Linux or macOS):<pre>git clone https://github.com/aws-samples/data-mesh-datazone-cdk-cloudformation</pre> | Cloud architect, DevOps engineer |
| Create the environment. | To create the Python virtual environment, run the following commands:<pre> python3 -m venv .venv<br /> source .venv/bin/activate<br /> pip install -r requirements.txt</pre> | Cloud architect, DevOps engineer |
| Bootstrap the account. | To bootstrap the central governance account by using AWS CDK, run the following command:<pre>cdk bootstrap aws://<GOVERNANCE_ACCOUNT_ID>/<AWS_REGION></pre><br />Sign in to the AWS Management Console, open the central governance account console, and get the Amazon Resource Name (ARN) of the AWS CDK execution role. | Cloud architect, DevOps engineer |
| Construct the `DzDataMeshMemberStackSet.yaml` file. | To construct the `DzDataMeshMemberStackSet.yaml` file, from the root directory of the repository, initiate the following bash script:<pre>./lib/scripts/create_dz_data_mesh_member_stack_set.sh</pre> | Cloud architect, DevOps engineer |
| Confirm template creation. | Ensure that the CloudFormation template file is created at the `lib/cfn-templates/DzDataMeshMemberStackSet.yaml` location. | Cloud architect, DevOps engineer |

### Deploy resources in the central governance account
<a name="deploy-resources-in-the-central-governance-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify the configuration. | In the `config/Config.ts` file, modify the following parameters:<pre>DZ_APPLICATION_NAME - Name of the application.<br />DZ_STAGE_NAME - Name of the stage. <br />DZ_DOMAIN_NAME - Name of the Amazon DataZone domain<br />DZ_DOMAIN_DESCRIPTION - Description of the Amazon DataZone domain<br />DZ_DOMAIN_TAG - Tag of the Amazon DataZone domain<br />DZ_ADMIN_PROJECT_NAME - Name of the Amazon DataZone project for administrators<br />DZ_ADMIN_PROJECT_DESCRIPTION - Description of the Amazon DataZone project for administrators<br />CDK_EXEC_ROLE_ARN - ARN of the cdk execution role<br />DZ_ADMIN_ROLE_ARN - ARN of the administrator role</pre><br />Keep the remaining parameters empty. | Cloud architect, DevOps engineer |
| Update the Amazon DataZone glossary configuration. | To update the Amazon DataZone glossary configuration in the `lib/utils/glossary_config.json` file, use the following example configuration:<pre>{<br />    "GlossaryName": "PII Data",<br />    "GlossaryDescription": "If data source contains PII attributes",<br />    "GlossaryTerms": [{<br />            "Name": "Yes",<br />            "ShortDescription": "Yes",<br />            "LongDescription": "Yes Glossary Term"<br />        },<br />        {<br />            "Name": "No",<br />            "ShortDescription": "No",<br />            "LongDescription": "No Glossary Term"<br />        }<br />    ]<br />}</pre> | Cloud architect, DevOps engineer |
| Update the Amazon DataZone metadata form configuration. | To update the Amazon DataZone metadata form configuration in the `lib/utils/metadata_form_config.json file`, use the following example configuration:<pre>{<br />    "FormName": "ScheduleDataRefresh",<br />    "FormDescription": "Form for data refresh schedule",<br />    "FormSmithyModel": "@amazon.datazone#displayname(defaultName: \"Data Refresh Schedule\")\nstructure ScheduleDataRefresh {\n    @documentation(\"Schedule of Data Refresh\")\n    @required\n    @amazon.datazone#searchable\n    @amazon.datazone#displayname(defaultName: \"Data Refresh Schedule\")\n    data_refresh_schedule: String\n}"<br />}</pre> | Cloud architect, DevOps engineer |
| Export the AWS credentials. | To export AWS credentials to your development environment for the IAM role with administrative permissions, use the following format:<pre>export AWS_ACCESS_KEY_ID=<br />export AWS_SECRET_ACCESS_KEY=<br />export AWS_SESSION_TOKEN=</pre> | Cloud architect, DevOps engineer |
| Synthesize the template. | To synthesize the CloudFormation template, run the following command:<pre>npx cdk synth</pre> | Cloud architect, DevOps engineer |
| Deploy the solution. | To deploy the solution, run the following command:<pre>npx cdk deploy --all</pre> | Cloud architect, DevOps engineer |

### Configure new member accounts
<a name="configure-new-member-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the template. | Deploy the CloudFormation template located at `lib/cfn-templates/DzDataMeshCfnStackSetExecutionRole.yaml` in the member account with the following input parameters:<br /> + `GovernanceAccountID` ‒ Account ID of the governance account<br />+ `DataZoneKMSKeyID` ‒ ID of the AWS Key Management Service (AWS KMS) key that encrypts the Amazon DataZone metadata<br />+ `NotificationQueueName` ‒ Name of the Amazon SQS notification queue in the governance account | Cloud architect, DevOps engineer |
| Update the ARNs. | To update the list of CloudFormation StackSet execution role ARNs for the member accounts, use the following code:<pre>DZ_MEMBER_STACK_SET_EXEC_ROLE_LIST  - List of Stack set execution role arns for the member accounts.</pre> | Cloud architect, DevOps engineer |
| Synthesize and deploy. | To synthesize the CloudFormation template and deploy the solution, run the following commands:<pre>npx cdk synth<br />npx cdk deploy --all</pre> | Cloud architect, DevOps engineer |
| Associate the member account. | To associate the member account with the central governance account, do the following:1. Sign in to the console of the central governance account, and open the Amazon DataZone console at [https://console.aws.amazon.com/datazone/](https://console.aws.amazon.com/datazone/).<br />2. Choose the domain that you created.<br />3. Scroll to the **Associated accounts** tab, and choose **Request Association**.<br />4. Provide the AWS account ID, and choose **AWSRAMPermissionDataZonePortalReadWrite** as **RAM policy**.<br />5. Choose **Request Association**.<br />6. Wait until you receive an email notification that your account is successfully bootstrapped. | Cloud architect, DevOps engineer |
| Update the parameters. | To update the member account‒specific parameters in the config file at `config/Config.ts`, use the following format:<pre>export const DZ_MEMBER_ACCOUNT_CONFIG: memberAccountConfig = {<br />  '123456789012' : {<br />    PROJECT_NAME: 'TEST-PROJECT-123456789012',<br />    PROJECT_DESCRIPTION: 'TEST-PROJECT-123456789012',<br />    PROJECT_EMAIL: 'user@xyz.com'<br />  }<br />}</pre> | Cloud architect, DevOps engineer |
| Synthesize and deploy the template. | To synthesize the CloudFormation template and deploy the solution, run the following commands:<pre>npx cdk synth<br />npx cdk deploy --all</pre> | Cloud architect, DevOps engineer |
| Add member accounts. | To create and configure additional member accounts in the data solution, repeat the previous steps for each member account.<br />This solution doesn’t differentiate between data producers and consumers. | Cloud architect, DevOps engineer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Disassociate the member accounts. | To disassociate the accounts, do the following:1. Sign in to the console and open the Amazon DataZone console.<br />2. Choose **View Domains**.<br />3. Select the domain that you created.<br />4. Choose the **Account associations** tab.<br />5. Select the member account that you want to disassociate.<br />6. Choose **Disassociate**, and enter `disassociate` to confirm.<br />7. Repeat steps 3-6 for all member accounts. | Cloud architect, DevOps engineer |
| Delete the stack instances. | To delete the CloudFormation stack instances, do the following:1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation/](https://console.aws.amazon.com/cloudformation/).<br />2. In the navigation pane, choose **StackSets**.<br />3. Choose the stack set named **StackSet-DataZone-DataMesh-Member**, and choose the **Stack instances** tab.<br />4. Copy the AWS account ID  of the member account that you want to remove from membership. <br />5. Choose **Actions**, choose **Delete stacks from StackSet**, and keep the default options.<br />6. In the **Account numbers** field, enter the account ID. <br />7. In the **Specify regions** dropdown list, choose the AWS Region. <br />8. Choose **Next**, and then choose **Submit**. <br />9. On the **Operations** tab, confirm that the operation has succeeded. The stack deletion might take some time.<br />10. Repeat steps 2-9 for all member accounts. | Cloud architect, DevOps engineer |
| Destroy all resources. | To destroy resources, implement the following steps in your local development environment (Linux or macOS):1. Navigate to the root directory of your repository. <br />2. Export the AWS credentials for the IAM role that you used to create the AWS CDK stack. <br />3. To destroy the cloud resources, run the following command:<pre>npx cdk destroy --all</pre> | Cloud architect, DevOps engineer |

## Related resources
<a name="build-enterprise-data-mesh-amazon-data-zone-resources"></a>
+ [Amazon DataZone quickstart with AWS Glue data](https://docs.aws.amazon.com/datazone/latest/userguide/quickstart-glue.html)
+ [Tutorial: Create your first AWS CDK app](https://docs.aws.amazon.com/cdk/v2/guide/hello_world.html)
+ [Getting started with CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html)
+ [Strategies for building a data mesh-based enterprise solution on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/introduction.html)

## Additional information
<a name="build-enterprise-data-mesh-amazon-data-zone-additional"></a>

**Objectives**

Implementing this pattern achieves the following:
+ **Decentralized ownership of data** ‒ Shift data ownership from a central team to teams that represent the source systems, business units, or use cases of your organization.
+ **Product thinking** ‒ Introduce a product-based mindset that includes customers, the market, and other factors when considering the data assets in your organization.
+ **Federated governance** ‒ Improve security guardrails, controls, and compliance across your organization's data products.
+ **Multi-account and multiple-project support** ‒ Support efficient, secure data sharing and collaboration across the business units or projects of your organization.
+ **Centralized monitoring and notifications** ‒ Monitor the cloud resources of your data mesh by using Amazon CloudWatch, and notify users when a new member account is associated.
+ **Scalability and extensibility** ‒ Add new use cases into the data mesh as your organization evolves.

**Solution scope**

When you use this solution, you can start small and scale as you progress in your data mesh journey. Often, when a member account adopts the data solution, it contains account configurations specific to the organization, project, or business unit. This solution accommodates these diverse AWS account configurations by supporting the following features:
+ AWS Glue Data Catalog as the data source for Amazon DataZone
+ Management of the Amazon DataZone data domain and the related data portal
+ Management of adding member accounts in the data mesh‒based data solution
+ Management of Amazon DataZone projects and environments
+ Management of Amazon DataZone glossaries and metadata forms
+ Management of IAM roles that correspond to the data mesh‒based data solution users
+ Notification of data mesh‒based data solution users
+ Monitoring of the provisioned cloud infrastructure

  This solution uses AWS CDK and CloudFormation to deploy the cloud infrastructure. It uses CloudFormation to do the following:
  + Define and deploy cloud resources at a lower level of abstraction.
  + Deploy cloud resources from the AWS Management Console. By using this approach, you can deploy infrastructure without a development environment.

  The data mesh solution uses AWS CDK to define resources at higher abstraction level. As a result, the solution provides a decoupled, modular, and scalable approach by choosing the relevant tool to deploy the cloud resources.

**Next steps**

You can reach out to AWS[ experts](https://aws.amazon.com/professional-services) for guidance on building data mesh  with Amazon DataZone.

The modular nature of this solution supports building data management solutions with different architectures, such as data fabric and data lakes. In addition, based on the requirements of your organization, you can extend the solution to other Amazon DataZone data sources.
