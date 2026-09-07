---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/visualize-iam-credential-reports-for-all-aws-accounts-using-amazon-quicksight.html
---

# Visualize IAM credential reports for all AWS accounts using Amazon Quick Sight
<a name="visualize-iam-credential-reports-for-all-aws-accounts-using-amazon-quicksight"></a>

*Parag Nagwekar and Arun Chandapillai, Amazon Web Services*

## Summary
<a name="visualize-iam-credential-reports-for-all-aws-accounts-using-amazon-quicksight-summary"></a>

|
|
| Warning: IAM users have long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. |
| --- |

You can use AWS Identity and Access Management (IAM) credential reports to help you meet the security, auditing, and compliance requirements of your organization. [Credential reports](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) provide a list of all the users in your AWS accounts and show the status of their credentials, such as passwords, access keys, and multi-factor authentication (MFA) devices. You can use credential reports for multiple AWS accounts managed by [AWS Organizations](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/core-concepts.html).

This pattern includes steps and code to help you create and share IAM credential reports for all the AWS accounts in your organization by using Amazon Quick Sight dashboards. You can share the dashboards with stakeholders in your organization. The reports can help your organization achieve the following targeted business outcomes:
+ Identify security incidents related to IAM users
+ Track real-time migration of IAM users to single sign-on (SSO) authentication
+ Track AWS Regions accessed by IAM users
+ Stay compliant
+ Share information with other stakeholders

## Prerequisites and limitations
<a name="visualize-iam-credential-reports-for-all-aws-accounts-using-amazon-quicksight-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An [organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) with member accounts
+ An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) with permissions to access accounts in Organizations
+ AWS Command Line Interface (AWS CLI) version 2, [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ A [subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html) to [Amazon Quick Enterprise edition](https://docs.aws.amazon.com/quicksight/latest/user/editions.html)

## Architecture
<a name="visualize-iam-credential-reports-for-all-aws-accounts-using-amazon-quicksight-architecture"></a>

**Technology stack**
+ Amazon Athena
+ Amazon EventBridge
+ Amazon Quick Sight
+ Amazon Simple Storage Service (Amazon S3)
+ AWS Glue
+ AWS Identity and Access Management (IAM)
+ AWS Lambda
+ AWS Organizations

**Target architecture**

The following diagram shows an architecture for setting up a workflow that captures IAM credential report data from multiple AWS accounts.

![The following screenshot illustrates the architecture diagram](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8724ff28-40f6-4c43-9c65-fbd18bbbfd0f/images/e780916a-4ab7-4fdc-8ecc-c837c7d90d13.png)

1. EventBridge invokes a Lambda function daily.

1. The Lambda function assumes an IAM role in every AWS account across the organization. Then, the function creates the IAM credentials report and stores the report data in a centralized S3 bucket. You must enable encryption and deactivate public access on the S3 bucket.

1. An AWS Glue crawler crawls the S3 bucket daily and updates the Athena table accordingly.

1. Quick Sight imports and analyzes the data from the credential report and builds a dashboard that can be visualized by and shared with stakeholders.

## Tools
<a name="visualize-iam-credential-reports-for-all-aws-accounts-using-amazon-quicksight-tools"></a>

**AWS services**
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is an interactive query service that makes it easy to analyze data in Amazon S3 by using standard SQL.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a cloud-scale business intelligence (BI) service that helps you visualize, analyze, and report your data in a single dashboard. Quick Sight is a core component within Amazon Quick, providing interactive data visualization, SPICE in-memory analytics, embedded analytics, and dashboard sharing.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.

**Code**

The code for this pattern is available in the GitHub [getiamcredsreport-allaccounts-org](https://github.com/aws-samples/getiamcredsreport-allaccounts-org) repository. You can use the code from this repository to create IAM credential reports across AWS accounts in Organizations and store them in a central location.

## Epics
<a name="visualize-iam-credential-reports-for-all-aws-accounts-using-amazon-quicksight-epics"></a>

### Set up the infrastructure
<a name="set-up-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Amazon Quick Enterprise edition. | 1. Activate the Amazon Quick Enterprise edition in your AWS account. For more information, see [Managing user access inside Amazon Quick ](https://docs.aws.amazon.com/quicksight/latest/user/managing-users.html)in the Quick documentation.<br />2. To grant dashboard permissions, get the Amazon Resource Name (ARN) of the Quick Sight users. | AWS administrator, AWS DevOps, Cloud administrator, Cloud architect |
| Integrate Amazon Quick Sight with Amazon S3 and Athena. | You must [authorize](https://docs.aws.amazon.com/quicksight/latest/user/troubleshoot-connect-to-datasources.html) Quick Sight to use Amazon S3 and Athena before you deploy the AWS CloudFormation stack. | AWS administrator, AWS DevOps, Cloud administrator, Cloud architect |

### Deploy the infrastructure
<a name="deploy-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the GitHub repository. | 1. Clone the GitHub [getiamcredsreport-allaccounts-org](https://github.com/aws-samples/getiamcredsreport-allaccounts-org) repository to your local machine by running the following command: `git clone https://github.com/aws-samples/getiamcredsreport-allaccounts-org` | AWS administrator |
| Deploy the infrastructure. | 1. Sign in to the AWS Management Console and open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. In the navigation pane, choose **Create stack**, and then choose **With new resources (standard)**.<br />3. On the **Identify resources** page, choose **Next**.<br />4. On the **Specify template** page, for **Template source**,** **select **Upload a template file**.<br />5. Choose **Choose file**, select the `Cloudformation-createcredrepo.yaml` file from your cloned GitHub repository, and then choose **Next**.<br />6. In **Parameters**, update `IAMRoleName` with** **your IAM role.** **This should be the IAM role that you want Lambda to assume in every account of the organization. This role creates the credential report. **Note**: The role doesn't have to be present in all accounts at this step of stack creation.<br />7. In **Parameters**, update `S3BucketName` with the name of the S3 bucket where Lambda can store the credentials for all accounts.<br />8. For **Stack name**, enter your stack name.<br />9. Choose **Submit**.<br />10. Note the Lambda function's role name. | AWS administrator |
| Create an IAM permission policy. | [Create an IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) for every AWS account across your organization with the following permissions:<pre>{<br />  "Version": "2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Effect": "Allow",<br />      "Action": [<br />        "iam:GenerateCredentialReport",<br />        "iam:GetCredentialReport"<br />        ],<br />      "Resource": "*"<br />    }<br />  ]<br />}</pre> | AWS DevOps, Cloud administrator, Cloud architect, Data engineer |
| Create an IAM role with a trust policy. | 1. [Create an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) for the AWS accounts and attach the permission policy that you created in the previous step.<br />2. Attach the following trust policy to the IAM role:<pre>{<br />   "Version": "2012-10-17",		 	 	 <br />   "Statement":[<br />      {<br />         "Effect":"Allow",<br />         "Principal":{<br />            "AWS":[<br />               "arn:aws:iam::<MasterAccountID>:role/<LambdaRole>"<br />            ]<br />         },<br />         "Action":"sts:AssumeRole"<br />      }<br />   ]<br />}</pre>Replace `arn:aws:iam::<MasterAccountID>:role/<LambdaRole>` with the ARN of the Lambda role that you noted previously.Organizations typically use automation to create IAM roles for their AWS accounts. We recommend that you use this automation, if available. Alternatively, you can use the `CreateRoleforOrg.py` script from** **the code repository. The script requires an existing administrative role or any other IAM role that has permission to create an IAM policy and role in every AWS account. | Cloud administrator, Cloud architect, AWS administrator |
| Configure Amazon Quick Sight to visualize the data. | 1. [Sign in to Quick ](https://docs.aws.amazon.com/quicksight/latest/user/signing-in.html)with your credentials.<br />2. [Create a dataset](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-athena.html) by using Athena (using the `iamcredreportdb` database and `"cfn_iamcredreport"` table), and then automatically [refresh the dataset](https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html).<br />3. [Create an analysis in Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/creating-an-analysis.html).<br />4. [Create a Quick Sight dashboard](https://docs.aws.amazon.com/quicksight/latest/user/example-analysis.html). | AWS DevOps, Cloud administrator, Cloud architect, Data engineer |

## Additional information
<a name="visualize-iam-credential-reports-for-all-aws-accounts-using-amazon-quicksight-additional"></a>

**Additional considerations**

Consider the following:
+ After you use CloudFormation to deploy the infrastructure, you can wait to get the reports created in Amazon S3 and analyzed by Athena until Lambda and AWS Glue run as per their schedules. Alternatively, you can run Lambda manually to get the reports in Amazon S3, and then run the AWS Glue crawler to get the Athena table that's created from the data.
+ Quick is a powerful tool for analyzing and visualizing data based on your business requirements. You can use [parameters](https://docs.aws.amazon.com/quicksight/latest/user/parameters-in-quicksight.html) in Quick to control widget data based on data fields that you choose. Also, you can use a Quick analysis to create parameters (for example, Account, Date, and User fields such as `partition_0`, `partition_1`, and `user` respectively) from your dataset to add controls for the parameters for Account, Date, and User.
+ To build your own Quick Sight dashboards, see [Quick Workshops](https://catalog.workshops.aws/quicksight/en-US) from the AWS Workshop Studio website.
+ To see sample Quick Sight dashboards, see the GitHub [getiamcredsreport-allaccounts-org](https://github.com/aws-samples/getiamcredsreport-allaccounts-org) code repository.

**Targeted business outcomes**

You can use this pattern to achieve the following targeted business outcomes:
+ **Identify security incidents related to IAM users **– Investigate every user across every AWS account in your organization by using a single pane of glass. You can track the trend of an IAM user’s most recently accessed individual AWS Regions and the services they used.
+ **Track real-time migration of IAM users to SSO authentication **– By using SSO, users can sign in once with a single credential and access multiple AWS accounts and applications. If you’re planning to migrate your IAM users to SSO, this pattern can help you transition to SSO and track all IAM user credential usage (such as access to the AWS Management Console or usage of access keys) across all AWS accounts.
+ **Track AWS Regions accessed by IAM users **– You can control IAM user access to Regions for various purposes, such as data sovereignty and cost control. You can also track use of Regions by any IAM user.
+ **Stay compliant **– By following the principle of least privilege, you can grant only the specific IAM permissions that are required to perform a specific task. Also, you can track access to AWS services, the AWS Management Console, and long-term credentials usage.
+ **Share information with other stakeholders **– You can share curated dashboards with other stakeholders, without granting them access to IAM credential reports or AWS accounts.
