---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-aws-resource-inventory.html
---

# Automatically inventory AWS resources across multiple accounts and Regions
<a name="automate-aws-resource-inventory"></a>

*Matej Macek, Amazon Web Services*

## Summary
<a name="automate-aws-resource-inventory-summary"></a>

This pattern outlines an automated approach to maintaining a comprehensive inventory of AWS resources across multiple accounts and AWS Regions. It is designed to help infrastructure and security engineers improve their resource management practices. It uses AWS Config to track resource changes, Amazon Athena for querying, and Amazon Quick Sight for interactive dashboards. You implement this solution by deploying an AWS CloudFormation stack.

This solution is similar to the one presented in [Visualizing AWS Config data using Amazon Athena and Amazon Quick Sight](https://aws.amazon.com/blogs/mt/visualizing-aws-config-data-using-amazon-athena-and-amazon-quicksight/) (AWS blog post). This pattern expands on that solution to address the following common requirements and provide the following key benefits:
+ **Compliance-focused** – This approach can help you meet regulatory requirements such as [PCI DSS](https://www.pcisecuritystandards.org/), [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), [ISO/IEC 27001](https://www.iso.org/standard/27001), [HIPAA](https://www.hhs.gov/programs/hipaa/index.html), [GDPR](https://gdpr.eu/), and others that mandate accurate asset inventories.
+ **Customization framework** – It provides a foundation for creating Quick Sight dashboards for various AWS resources, so that you can customize the solution to your specific requirements.
+ **User-driven enhancements** – This approach incorporates feedback from real-world use cases and addresses requests for a more comprehensive solution.

Infrastructure, security, and finance teams often face visibility and collaboration challenges in dynamic, multi-account or multi-Region environments. This solution is designed to address those challenges and significantly reduce the time and effort required to create and maintain a resource inventory. The result is a centralized view of resources that helps you improve resource allocation decisions, identify and mitigate risks, optimize costs, and improve overall visibility and collaboration. This approach bridges the gap between conceptual solutions and real-world implementation needs for security, compliance, and operational purposes.

## Prerequisites and limitations
<a name="automate-aws-resource-inventory-prereqs"></a>

**Prerequisites**
+ The following active AWS accounts:
  + *Management account* - A centralized account for billing, creating accounts, and controlling access across the organization
  + *Audit account* – A centralized hub for security monitoring, compliance checks, and drift notifications
  + *Log archive account* – A centralized account for storing and analyzing the collected data
+ In the audit account, an AWS Config [aggregator](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html) that collects and aggregates configuration data from your target accounts and Regions
+ In the log archive account, set up the following:
  + An Amazon Simple Storage Service (Amazon S3) [bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) where you store the data from the AWS Config aggregator
  + An Amazon Quick [subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html)
  + An [authorized connection](https://docs.aws.amazon.com/quicksight/latest/user/athena.html) between Quick Sight and Amazon Athena
  + [Permissions](https://docs.aws.amazon.com/athena/latest/ug/s3-permissions.html) to access the Amazon S3 bucket through an Athena query
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ Permissions to deploy a CloudFormation stack that provisions the following resources:
  + An AWS Lambda function
  + An Amazon S3 notification configuration
  + Athena database, tables, and views
  + Quick Sight datasets and data sources
+ Permissions to run automations in AWS Systems Manager
+ Permissions to access Quick

**Limitations**
+ The solution relies on AWS Config. AWS Config usually records configuration changes to your resources right after a change is detected, or at the frequency that you specify. However, this is on a best-effort basis and can take longer at times.
+ This solution tracks only [resource types that AWS Config supports](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html).
+ The solution does not track resource inventory across other cloud providers or on-premises environments.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page in the AWS documentation, and choose the link for the service.

## Architecture
<a name="automate-aws-resource-inventory-architecture"></a>

The following diagram shows a streamlined process for collecting, organizing, analyzing, and visualizing configuration and compliance data across multiple accounts in an AWS organization.

![Collecting and visualizing configuration and compliance data across an organization.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/67a9667a-da19-4dcb-a2fe-62bc94a0541b/images/c9245de1-ac85-4a9e-a0c0-dbcc27a8bb5d.png)

The diagram shows the following workflow:

1. On a periodic schedule, the AWS Config aggregator collects configuration and compliance data about the resources in the target accounts and Regions and then delivers the data to the Amazon S3 bucket in the log archive account.

1. Adding new AWS Config data to the Amazon S3 bucket invokes an AWS Lambda function.

1. The Lambda function partitions the data by configuring keys with values that correspond to the Region and date of each snapshot file. This helps AWS Glue efficiently query and process the configuration and compliance data.

1. Amazon Athena uses an AWS Glue [schema](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html) to run SQL queries against the data stored in the Amazon S3 bucket. It utilizes the schema metadata from AWS Glue to understand the structure of the data.

1. [Views](https://docs.aws.amazon.com/athena/latest/ug/views.html) in Athena define and extract the target datasets.

1. [Dashboards](https://docs.aws.amazon.com/quicksight/latest/user/using-dashboards.html) in Quick Sight help you to visualize and analyze the datasets.

## Tools
<a name="automate-aws-resource-inventory-tools"></a>

**AWS services**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that helps you analyze data directly in Amazon S3 by using standard SQL.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the resources in your AWS account and how they’re configured. It helps you identify how resources are related to one another and how their configurations have changed over time. An AWS Config [aggregator](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html) collects AWS Config configuration and compliance data from multiple AWS accounts and Regions.
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a fully managed extract, transform, and load (ETL) service. It helps you reliably categorize, clean, enrich, and move data between data stores and data streams. This pattern uses an AWS Glue [Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro) and [Schema registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html).
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [Amazon Quick Sight](https://docs.aws.amazon.com/quicksuite/latest/userguide/quick-bi.html) is a business intelligence (BI) service that helps you transform raw data into meaningful insights through interactive visualizations, dashboards, and reports. Quick Sight is a core component of Amazon Quick.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your applications and infrastructure running in the AWS Cloud. It simplifies application and resource management, shortens the time to detect and resolve operational problems, and helps you manage your AWS resources securely at scale. [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) simplifies common maintenance, deployment, and remediation tasks for many AWS services.

**Code repository**

The AWS CloudFormation template for this pattern is available in the [AWS Config visualization](https://github.com/aws-samples/aws-management-and-governance-samples/blob/master/AWSConfig/AWS-Config-Visualization/README.md) GitHub repository. This CloudFormation template deploys an AWS Systems Manager automation runbook that sets up AWS Config for use with Amazon Athena. This automation prepares AWS Glue to connect with the designated Amazon S3 bucket, creates views in Amazon Athena, and configures Quick Sight for dashboard visualization.

## Best practices
<a name="automate-aws-resource-inventory-best-practices"></a>
+ We recommend that you follow the best practices in [Set up and govern a secure, multi-account AWS environment with AWS Control Tower](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/welcome.html) on AWS Prescriptive Guidance.
+ We recommend that you create an AWS Config aggregator that collects configuration and compliance data for the entire AWS organization. For more information, see [Multi-Account Multi-Region Data Aggregation](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html) in the AWS Config documentation.
+ Before deploying this solution, we recommend that you review the current pricing information for [Amazon S3](https://aws.amazon.com/s3/pricing/), [AWS Config](https://aws.amazon.com/config/pricing/), [Athena](https://aws.amazon.com/athena/pricing/), and [Quick](https://aws.amazon.com/quicksight/pricing/).

## Epics
<a name="automate-aws-resource-inventory-epics"></a>

### Deploy the CloudFormation stack
<a name="deploy-the-cfnshort-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the CloudFormation template. | Download the [Config-QuickSight-Visualization-SSM-Automation.yaml](https://github.com/aws-samples/aws-management-and-governance-samples/blob/master/AWSConfig/AWS-Config-Visualization/cft/Config-QuickSight-Visualization-SSM-Automation.yaml) CloudFormation template. | AWS administrator, Cloud administrator, DevOps engineer |
| Modify the CloudFormation template. | Complete this step only if you're using [AWS Control Tower](https://aws.amazon.com/controltower/) and AWS Config is managed by AWS Control Tower. You need to modify the CloudFormation template.1. Sign in to the management account.<br />2. Open the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2).<br />3. Navigate to the **Settings** page. This page displays details about the organization, including the organization ID.<br />4. Copy the organization ID.<br />5. In your preferred text editor, open the **Config-QuickSight-Visualization-SSM-Automation.yaml** file.<br />6. Find the following line:<br />`return re.match('^AWSLogs/(\d+)/Config/([\w-]+)/(\d+)/(\d+)/(\d+)/ConfigSnapshot/[^\\\]+$', object_key)`<br />7. Replace this line with the following, where `<ORGANIZATION_ID>` is the ID that you previously copied:<br />`return re.match('^<ORGANIZATION_ID>/AWSLogs/(\d+)/Config/([\w-]+)/(\d+)/(\d+)/(\d+)/ConfigSnapshot/[^\\\]+$', object_key)`<br />8. Save and close the **Config-QuickSight-Visualization-SSM-Automation.yaml** file. | DevOps engineer, AWS administrator |
| Create a CloudFormation stack. | Follow the instructions in [Create a stack from the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html). Note the following:1. Choose **Upload a template file**, and then choose the YAML file you downloaded.<br />2. For **Stack name**, enter `Config-QuickSight-Visualization-SSM-Automation`.<br />3. Choose **Submit**. | AWS administrator, Cloud administrator, DevOps engineer |

### Run the automation in Systems Manager
<a name="run-the-automation-in-sys"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Find your Quick user name. | 1. Open the [Quick console](https://quicksight.aws.amazon.com/).<br />2. Open the profile menu.<br />3. Make note of the user name. You need this value later. | AWS administrator, Cloud administrator, DevOps engineer |
| Find the delivery channel name and Amazon S3 bucket name. | 1. In the AWS CLI, enter the following command:<pre>aws configservice describe-delivery-channels</pre><br />2. Make note of the Amazon S3 bucket name and the name of your the [AWS Config delivery channel](https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html). You need these values later. | AWS administrator, Cloud administrator, DevOps engineer |
| Run the automation in Systems Manager. | 1. Open the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/).<br />2. In the navigation pane, choose **Documents**.<br />3. Choose **Owned by me**.<br />4. Choose **Config-QuickSight-Visualization**.<br />5. Choose **Execute automation**.<br />6. In the **Input parameters** section, enter your values for the following parameters:`ConfigDeliveryChannelName` – Enter the name of your AWS Config [delivery channel](https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html). This parameter is required.`ConfigS3BucketLocation` – Enter the name of the Amazon S3 bucket where you store AWS Config configuration data. This parameter is required.`QuickSightUserName` – Enter a user name that has administrative access to Quick. This parameter is required.`AutomationAssumeRole` – The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. This parameter is optional. Leave this parameter blank.`DeleteConfigVisualization` – Choose `false`.<br />7. Choose **Execute**. | AWS administrator, Cloud administrator, DevOps engineer |

### Visualize data in Quick Sight
<a name="visualize-data-in-qsight"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Refresh data. | To schedule dataset refreshes according to your specific requirements, follow the instructions in [Refreshing SPICE data](https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html). | AWS administrator, DevOps engineer, Cloud administrator |
| Create an analysis. | To create a dashboard in Quick Sight that helps you visualize the resources, follow the instructions in [Starting an analysis in Quick Sight](https://docs.aws.amazon.com/quicksuite/latest/userguide/creating-an-analysis.html). | Quick Suite administrator |
| Create a dashboard. | 1. After you finish modifying your Quick Sight analysis, follow the instructions in [Publishing dashboards](https://docs.aws.amazon.com/quicksight/latest/user/creating-a-dashboard.html) to create a dashboard. A *dashboard* is an analysis that you can share with other Quick users.<br />2. Follow the instructions in [Granting access to a dashboard](https://docs.aws.amazon.com/quicksight/latest/user/share-a-dashboard.html) to share the dashboard with your target Quick users. | Quick Suite administrator |

### (Optional) Clean up
<a name="optional-clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the resources created by the Systems Manager automation. | 1. Open the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/).<br />2. In the navigation pane, choose **Documents**.<br />3. Choose **Owned by me**.<br />4. Choose **Config-QuickSight-Visualization**.<br />5. Choose **Execute automation**.<br />6. In the **Input parameters** section, for the `DeleteConfigVisualization` parameter, enter `true`.<br />7. Choose **Execute**. | AWS administrator, Cloud administrator, DevOps engineer |
| Delete the CloudFormation stack. | To delete the resources in the `Config-QuickSight-Visualization-SSM-Automation` stack, follow the instructions in [Delete a stack from the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html). | AWS administrator, Cloud administrator, DevOps engineer |

## Troubleshooting
<a name="automate-aws-resource-inventory-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Amazon Quick is attempting to connect to the `us-east-1` AWS Region, but the creation of resources in that Region is not permitted. | A service control policy is restricting your subscription to Amazon Quick in this Region. In the service control policy, manually specify the target AWS Region. Replace `<REGION_ID>` with the appropriate Region identifier:<pre>https://<REGION_ID>.quicksight.aws.amazon.com/sn/start/dashboards</pre><br />The following is an example:<pre>https://eu-central-1.quicksight.aws.amazon.com/sn/start/dashboards</pre> |
| In Amazon Athena, you encounter the following message:<br />`Before you run your first query, you need to set up a query result location in Amazon S3.` | Make sure that you have prepared an Amazon S3 bucket where you will store the query results from Amazon Athena. Then follow the instructions in [Specify a query result location using the Amazon Athena console](https://docs.aws.amazon.com/athena/latest/ug/query-results-specify-location-console.html). |

## Related resources
<a name="automate-aws-resource-inventory-resources"></a>

**AWS documentation**
+ [AWS Config documentation](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
+ [Amazon Quick documentation](https://docs.aws.amazon.com/quicksuite/latest/userguide/what-is.html)

**AWS blog post**
+ [Automate AWS Config data visualization with AWS Systems Manager](https://aws.amazon.com/blogs/mt/automate-aws-config-data-visualization-with-aws-systems-manager/)
+ [How to record resource configuration changes periodically with AWS Config](https://aws.amazon.com/blogs/mt/how-to-record-resource-configuration-changes-periodically-with-aws-config/)

**Other resources**
+ [Amazon Quick Community Learning Center](https://community.amazonquicksight.com/c/learning-center/10/none)
+ [Amazon Quick Community Gallery](https://community.amazonquicksight.com/c/gallery/44)
