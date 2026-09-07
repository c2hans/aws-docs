---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/modernize-carddemo-mainframe-app.html
---

# Modernize the CardDemo mainframe application by using AWS Transform
<a name="modernize-carddemo-mainframe-app"></a>

*Santosh Kumar Singh and Cheryl du Preez, Amazon Web Services*

## Summary
<a name="modernize-carddemo-mainframe-app-summary"></a>

[AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) is designed to accelerate the modernization of mainframe applications. It uses generative AI to streamline the mainframe modernization process. It automates complex tasks, such as: legacy code analysis, mainframe documentation, business rules extraction, monolithic applications decomposition into business domain, and code refactoring. It accelerates modernization projects by automating complex tasks, such as application analysis and migration sequence planning. When decomposing monolithic applications, AWS Transform intelligently sequences the mainframe application transformation, which helps you to  transform business functions in parallel. AWS Transform can accelerate decision making and enhance operational agility and migration efficiency.

This pattern offers step-by-step instructions to help you test the mainframe modernization capabilities of AWS Transform by using [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo), which is a sample open source mainframe application.

## Prerequisites and limitations
<a name="modernize-carddemo-mainframe-app-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS IAM Identity Center, [enabled](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html)
+ [Permissions](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_id-based-policy-examples.html#id-based-policy-examples-admin-enable-transform) that allow administrators to enable AWS Transform
+ [Permissions](https://docs.aws.amazon.com/transform/latest/userguide/security_iam_id-based-policy-examples.html#id-based-policy-examples-admin-connector) that allow administrators to accept Amazon Simple Storage Service (Amazon S3) connection requests for the AWS Transform web application

** Limitations**
+ AWS Transform is available only in some AWS Regions. For a complete list of supported Regions, see [Supported Regions for AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/regions.html).
+ AWS Transform supports code analysis, document generation, business rules extraction, decomposition, and refactoring from Common Business-Oriented Language (COBOL) to Java. For more information, see [Capabilities and key features](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe.html#transform-app-mainframe-features) and [Supported file types for transformation of mainframe applications](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe.html#transform-app-mainframe-supported-files).
+ There is a service quota for mainframe transformation capabilities in AWS Transform. For more information, see [Quotas for AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-limits.html).
+ In order to collaborate on a shared workspace, all users must be registered users of the same instance of AWS IAM Identity Center that is associated with your instance of the AWS Transform web application.
+ The Amazon S3 bucket and AWS Transform must be in the same AWS account and Region.

## Architecture
<a name="modernize-carddemo-mainframe-app-architecture"></a>

The following diagram shows the architecture that you set up in this pattern.

![Using AWS Transform to modernize a mainframe application that is stored in an Amazon S3 bucket.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/0e539474-b733-452d-b0fb-6b3f4cbd5075/images/75be6d78-5b43-448c-ad07-bf74b9ae14ad.png)

The diagram shows the following workflow:

1. AWS Transform uses a connector to access the CardDemo mainframe application, which is stored in an Amazon S3 bucket.

1. AWS Transform uses AWS IAM Identity Center to manage user access and authentication. The system implements multiple layers of security controls for authentication, authorization, encryption, and access management to help protect code and artifacts during processing. Users interact with the AWS Transform agent through a chat interface. You can provide instructions to the AI agent for specific tasks in English. For more information, see [Human in the loop (HITL)](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe.html#transform-app-mainframe-hitl) in the AWS Transform documentation.

1. The AI agent interprets the user's instructions, creates a job plan, divides the job into executable tasks, and actions it autonomously. Users can review and approve the transformation. Transformation tasks include the following:
   + **Code analysis** – AWS Transform analyzes the code in each file for details such as file name, file type, lines of code, and their paths. The agent analyzes the source code, runs classifications, creates dependency mappings, and identifies any missing artifacts. It also identifies duplicate components.
   + **Document generation** – AWS Transform generates documentation for the mainframe application. By analyzing the code, it can automatically create detailed documentation of the application programs, including descriptions of the business logic, flows, integrations, and dependencies present in your legacy systems.
   + **Business logic extraction**– AWS Transform analyzes COBOL programs to document their core business logic, to help you understand the fundamental business logic.
   + **Code decomposition** – AWS Transform decomposes the code into domains that account for dependencies between programs and components. Grouping related files and programs within the same domain improves organization and helps preserve the application's logical structure when breaking it down into smaller components.
   + **Migration wave planning** – Based on the domains you created during the decomposition phase, AWS Transform generates a migration wave plan with recommended modernization order.
   + **Code refactoring** – AWS Transform refactors the code in all or selected domain files into Java code. The goal of this step is to preserve the critical business logic of the application while refactoring it to a modernized, cloud-optimized Java application.

1. AWS Transform stores the refactored code, generated documents, associated artifacts, and runtime libraries in your Amazon S3 bucket. You can do the following:
   + Access the runtime folder in your Amazon S3 bucket.
   + Build and deploy the application by following the [Build and deploy your modernized application post-refactoring](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow-build-deploy.html) in the AWS Transform documentation.
   + Through the chat interface, request and download a sample AWS CloudFormation, AWS Cloud Development Kit (AWS CDK), or Hashicorp Terraform template. These templates can help you deploy the AWS resources that are necessary to support the refactored application.
   + Use [Reforge](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-refactor-code-reforge) to improve the quality of refactored code by using large language models (LLMs). The refactoring engine preserves the functional equivalence of COBOL while transforming it into Java code. Reforge is an optional step that is available after the transformation. This step uses LLMs to restructure the code to closely resemble native Java, which can improve readability and maintainability. Reforge also adds human-readable comments to help you understand the code, and it implements modern coding patterns and best practices.

## Tools
<a name="modernize-carddemo-mainframe-app-tools"></a>

**AWS services**
+ [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) uses agentic AI to help you accelerate the modernization of legacy workloads, such as .NET, mainframe, and VMware workloads.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to your AWS accounts and cloud applications.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code repository**

You can use the open source AWS [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo) mainframe application as a sample application to get started with mainframe modernization.

## Best practices
<a name="modernize-carddemo-mainframe-app-best-practices"></a>
+ **Start small** – Begin with small, less complex code (15,000–20,000 lines of code) to get an understanding of how AWS Transform analyzes and transforms mainframe applications.
+ **Combine with human expertise** – Use AWS Transform as an accelerator while applying human expertise for optimal results.
+ **Review and test thoroughly** – Always review the transformed code carefully and run comprehensive tests to validate the functional equivalency after transformation.
+ **Provide feedback** – To provide feedback and suggestions for improvement, use the **Send feedback** button in the AWS Management Console or create a case with [AWS Support](https://support.console.aws.amazon.com/). For more information, see [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html). Your input is valuable for service enhancements and future development.

## Epics
<a name="modernize-carddemo-mainframe-app-epics"></a>

### Prepare the mainframe application
<a name="prepare-the-mainframe-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a bucket. | Create an Amazon S3 bucket in the same AWS account and Region where AWS Transform is enabled. You use this bucket to store the mainframe application code, and AWS Transform uses this bucket to store the generated documents, refactored code and other files associated with the transformation. For instructions, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation. | General AWS |
| Prepare the sample mainframe application. | 1. Enter the following command to clone the [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo) repository to your local workstation:<br />`git clone https://github.com/aws-samples/aws-mainframe-modernization-carddemo.git`<br />2. Create a new folder named `carddemo`.<br />3. Copy the `app` folder, which contains the mainframe source code, from the cloned repository into the `carddemo` folder.<br />4. Compress the `cardemo` folder into a ZIP file.<br />5. Upload the ZIP file to the Amazon S3 bucket that you created. For instructions, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the Amazon S3 documentation. | App developer, DevOps engineer |

### Configure IAM Identity Center and AWS Transform
<a name="configure-sso-and-trn"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add users to IAM Identity Center. | Add your prospective users to IAM Identity Center. Follow the instructions in [Adding users in IAM Identity Center](https://docs.aws.amazon.com/transform/latest/userguide/transform-user-management.html#transform-add-idc-users) in the AWS Transform documentation. | AWS administrator |
| Enable AWS Transform and add users. | 1. Enable AWS Transform. Follow the instructions in [Enable AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html#transform-enable).<br />2. Add users to AWS Transform. Follow the instructions in [Adding users to AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-user-management.html#transform-add-transform-users). | AWS administrator |
| Configure user access to the AWS Transform web application. | Each user must accept the invitation to access the AWS Transform web application. Follow the instructions in [Accepting the invitation](https://docs.aws.amazon.com/transform/latest/userguide/transform-user-onboarding.html#transform-user-invitation) in the AWS Transform documentation. | App developer, App owner |
| Log in to the AWS Transform web application. | Follow the instructions in [Signing in to AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-user-onboarding.html#transform-user-signin). | App developer, App owner |
| Set up a workspace. | Set up a workspace where users can collaborate in the AWS Transform web application. Follow the instructions in [Start your project](https://docs.aws.amazon.com/transform/latest/userguide/transform-environment.html#start-workflow) in the AWS Transform documentation. | AWS administrator |

### Transform the mainframe application
<a name="transform-the-mainframe-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a transformation job. | Create a transformation job to modernize the CardDemo mainframe application. For instructions, see [Create and start a job](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-start-job) in the AWS Transform documentation. When you are asked to set the objectives in the AWS Transform chat interface, choose **Perform mainframe modernization (IBM z/OS to AWS)** and then choose **Analyze code, Generate technical documentation, Business logic, Decompose code, Plan Migration sequence and Transform code to Java**. | App developer, App owner |
| Set up the connector. | Establish a connector to the Amazon S3 bucket that contains the CardDemo mainframe application. This connector allows AWS Transform to access resources in the bucket and perform consecutive transformation functions. For instructions, see [Set up a connector](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-setup-connector) in the AWS Transform documentation. | AWS administrator |
| Perform code analysis. | 1. On the **Specify asset location** page, enter the Amazon S3 bucket path for the `carddemo` ZIP file that you uploaded.<br />2. Choose **Approve and send to AWS Transform**. It starts analyzing the code.<br />3. Monitor the status on the **Worklog** tab.<br />4. When the analysis is complete, under **Analyze code** in the left navigation pane, choose **View code analysis results**.<br />5. (Optional) Choose **Download** to download the complete asset list, missing source code, and dependency file.For more information, see [Code analysis](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-code-analysis) in the AWS Transform documentation. | App developer, App owner |
| Generate technical documentation. | 1. In the left navigation pane, under **Generate technical documentation**, choose **Select files and configure settings**.<br />2. Expand **COBOL** or **JCL**, and then select one or multiple files.<br />3. Choose the documentation detail level:**Summary** – Provides a high-level overview of each file in the scope. Also, gives a one-line summary of each file.**Detailed functional specification** – Provides comprehensive details for each file in the mainframe application transformation scope. Some details include logic and flow, identified business rules, data flow, dependencies, input and output processing, and various transaction details.<br />4. Choose **Send to AWS Transform**.<br />5. Monitor the progress in the **Worklog** tab.Document generation time varies from minutes to hours, depending on the number of files and lines of code.<br />6. When complete, choose **Review documentation results**.<br />7. Access the generated document through the web application or download it. The generated documentation is also stored in the Amazon S3 bucket.<br />8. Explore the generated documentation by asking specific questions in the chat interface. For example, you can say "Tell me the features of CBACT01C."For more information, see [Generate technical documentation](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-generate-documentation) in the AWS Transform documentation. | App developer, App owner |
| Extract the business logic. | 1. In the left navigation pane, expand **Extract business logic**, and then choose** Select files for business logic extraction**.<br />2. Expand **COBOL** or **JCL**, and then select one or multiple files.<br />3. Choose **Send to AWS Transform**.<br />4. Monitor the progress in the **Worklog** tab.Business logic extraction time varies from minutes to hours, depending on the number of files and lines of code.<br />5. When extraction is complete, choose **Review business logic extraction results**.<br />6. Select a COBOL or JCL file, and then choose **View**.<br />7. Change the scope in **Flow diagram and functional rules** to review different levels of the flow charts, including the supporting code.<br />8. (Optional) Review the generated business logic, which is stored in JSON format in your Amazon S3 bucket.For more information, see [Extract business logic](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-extract-business-logic) in the AWS Transform documentation. | App developer, App owner |
| Decompose the code. | 1. In the left navigation pane, expand **Decompose code**, and then choose **Decompose into domains**.<br />2. In the **Actions** list, choose **Create domain**.<br />3. Enter a name for the new domain, such as `Bill payment`.<br />4. (Optional) Provide a description.<br />5. In the **Find files** search bar, search for `CB00`, and then select the file.<br />6. Choose **Mark as seed**.<br />7. Verify that the seed flag changes from **No** to **Yes**.<br />8. Choose **Create**.<br />9. Choose **Save**.<br />10. Choose **Decompose**.<br />11. Review the decomposition output by choosing the domain name.<br />12. When the decomposition is complete, choose **Send to AWS Transform**.For more information about decomposition and seeds, see [Decomposition](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-decomposition) in the AWS Transform documentation. | App developer, App owner |
| Plan the migration waves. | Plan the migration waves for the CardDemo application. Follow the instructions in [Migration wave planning](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-wave-planning) in the AWS Transform documentation to review and edit the wave plan. | App developer, App owner |
| Refactor the code. | 1. Refactor the CardDemo mainframe application into Java code in all or selected domain files. Follow the instructions in [Refactor code](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-refactor-code) in the AWS Transform documentation.<br />2. After the refactoring process is complete, build and deploy the modernized Java application. Follow the instructions in [Build and deploy your modernized application post-refactoring](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow-build-deploy.html#transform-app-mainframe-workflow-build-deploy-retrieve) in the AWS Transform documentation. | App developer, App owner |
| (Optional) Use Reforge to improve the Java code. | 1. Create a new job, and then enter an objective of `Reforge the code`.<br />2. Enter the of a project that has been modernized through AWS Transform. This project should be in your Amazon S3 bucket.<br />3. Enter the Java class list that specifies which service classes to reforge.<br />4. Review the generated output in the Amazon S3 bucket.For more information, see [Reforge](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-refactor-code-reforge) in the AWS Transform documentation. | App developer, App owner |
| Streamline the deployment. | AWS Transform can provide infrastructure as code (IaC) templates for CloudFormation, AWS CDK, or Terraform. These templates help you deploy core components, including compute, database, storage, and security resources.1. In the AWS Transform chat interface, request the templates by entering `Share the mainframe refactor <service> templates`, where `<service>` is one of the supported IaC services.<br />2. Deploy the template by using your preferred service. For example, see the following resources:[Create a stack from the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (CloudFormation documentation)[Deploy AWS CDK applications](https://docs.aws.amazon.com/cdk/v2/guide/deploy.html) (AWS CDK documentation)[Build infrastructure](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/aws-build) (Terraform documentation)<br />For more information, see [Deployment capabilities](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-features-deployment) in the AWS Transform documentation. | App developer, App owner |

## Troubleshooting
<a name="modernize-carddemo-mainframe-app-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| You are unable to view the source code or generated document in the AWS Transform web application. | Add a policy to the CORS permission for the Amazon S3 bucket to allow AWS Transform as an origin. For more information, see [S3 bucket CORS permissions](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html#transform-app-mainframe-workflow-setup-connector-s3) in the AWS Transform documentation. |

## Related resources
<a name="modernize-carddemo-mainframe-app-resources"></a>

**AWS documentation**
+ [Transformation of mainframe applications](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html) (AWS Transform documentation)

**Other AWS resources**
+ [Accelerate Your Mainframe Modernization Journey using AI Agents with AWS Transform](https://aws.amazon.com/blogs/migration-and-modernization/accelerate-your-mainframe-modernization-journey-using-ai-agents-with-aws-transform/) (AWS blog post)
+ [AWS Transform FAQs](https://aws.amazon.com/transform/faq/)
+ [AWS IAM Identity Center FAQs](https://aws.amazon.com/iam/identity-center/faqs/)

**Videos and tutorials**
+ [Introduction to Amazon Q Developer: Transform](https://explore.skillbuilder.aws/learn/courses/21893/aws-flash-introduction-to-amazon-q-developer-transform) (AWS Skill Builder)
+ [AWS re:Invent 2024 - Modernize mainframe applications faster using Amazon Q Developer](https://www.youtube.com/watch?v=pSi0XtYfY4o) (YouTube)
+ [AWS re:Invent 2024 - Automating migration and modernization to accelerate transformation](https://www.youtube.com/watch?v=9FjxnEoH5wg) (YouTube)
+ [AWS re:Invent 2024 - Toyota drives innovation & enhances operational efficiency with gen AI](https://www.youtube.com/watch?v=_NXc1MJenw4) (YouTube)

**Note**
AWS Transform was previously known as *Amazon Q Developer transform for mainframe*.
