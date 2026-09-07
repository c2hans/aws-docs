---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow.html
---

# Streamline Amazon Lex bot development and deployment by using an automated workflow
<a name="streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow"></a>

*Balaji Panneerselvam, Attila Dancso, Pavan Dusanapudi, Anand Jumnani, and James O'Hara, Amazon Web Services*

## Summary
<a name="streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow-summary"></a>

Developing and deploying Amazon Lex conversational bots can be challenging when you’re trying to manage multiple features, developers, and environments. An automated workflow using infrastructure as code (IaC) principles can help streamline the process. This pattern can help improve the productivity of Amazon Lex developers and enable efficient bot lifecycle management in the following ways:
+ **Enable concurrent development of multiple features** - With an automated workflow, developers can work on different features in parallel in separate branches. Changes can then be merged and deployed without blocking other work.
+ **Use the Amazon Lex console UI** - Developers can use the user-friendly Amazon Lex console to build and test bots. The bots are then described in infrastructure code for deployment.
+ **Promote bots across environments** - The workflow automates promoting bot versions from lower environments like development and test up to production. This approach reduces the risk and overhead of manual promotions.
+ **Maintain version control** - Managing bot definitions in Git rather than solely through the Amazon Lex service provides you with version control and an audit trail. Changes are tracked to individual developers, unlike when only using the AWS Management Console or APIs to modify bots stored in AWS.

By automating the Amazon Lex bot release process, teams can deliver features faster with reduced risk and effort. Bots remain under version control rather than isolated in the Amazon Lex console.

## Prerequisites and limitations
<a name="streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow-prereqs"></a>

**Prerequisites **
+ The workflow involves multiple AWS accounts for different environments (development, production, and DevOps), which requires account management and cross-account access configurations.
+ Python 3.9 available in your deployment environment or pipeline.
+ Git [installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and configured on a local workstation for source control.
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) and configured to authenticate by using the command line or Python.

**Limitations **
+ **Repository access** – The workflow assumes that the continuous integration and continuous delivery (CI/CD) pipeline has the necessary permissions to commit changes to the source code repository.
+ **Initial bot version** – The tooling requires that an initial version of the bot is deployed by using AWS CloudFormation templates. You must create the first iteration of the bot and commit it to the repo before the automated workflow can take over.
+ **Merge conflicts** – Although the workflow aims to enable concurrent development, there is still a possibility of merge conflicts when integrating changes from different branches. Resolving conflicts in bot configurations might require manual intervention.

**Product versions**
+ [Python 3.9](https://www.python.org/downloads/) or above
+ [AWS CDK v2 2.124.0](https://docs.aws.amazon.com/cdk/api/versions.html) or above
+ [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/pythonsdk/)1.28 or above

## Architecture
<a name="streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow-architecture"></a>

The following diagram displays the high-level architecture and key components of the solution.

![Workflow to automate development and deployment of Amazon Lex bots.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3c7f9d16-9708-43c4-afa6-9d804d6b9dad/images/cdc73e82-a777-4e88-8bf8-a73c9bacb47f.png)

Key components include the following:
+ **Lex bot repo** – A Git repository that stores the IaC definitions for the Amazon Lex bots.
+ **DevOps** – An AWS account dedicated to housing the CI/CD pipelines and related resources for the development and deployment process.
+ **Pipelines** – The AWS CodePipeline instances that automate various stages of the bot development and deployment lifecycle, such as creating a new bot, exporting a bot's definition, importing a bot definition, and deleting a bot.
+ **Ticket bots and main bot** – The Amazon Lex bot resources, where the ticket bots are feature-specific bots developed by individual teams or developers and the main bot is the baseline bot that integrates all the features.

The architecture diagram illustrates the following workflow:

1. **Baseline main bot** – The starting point of the workflow is to baseline the main bot in the development (Dev) environment. The main bot serves as the foundation for future development and feature additions.

1. **Create ticket bot** – When a new feature or change is required, a ticket bot is created. The ticket bot is essentially a copy or branch of the main bot that developers can work on without affecting the main version.

1. **Export ticket bot** - After work on the ticket bot is complete, it's exported from the Amazon Lex service. Then, the branch that contains the ticket bot is rebased from the main branch. This step ensures that any changes made to the main bot while the ticket bot was in development are incorporated, reducing potential conflicts.

1. **Import rebased ticket bot and validate** – The rebased ticket bot is imported back into the development environment and validated to ensure it functions correctly with the latest changes from the main branch. If validation is successful, a pull request (PR) is created to merge the ticket bot changes into the main branch.

1. **Delete ticket bot** – After the changes have been successfully merged into the main branch, the ticket bot is no longer needed. The ticket bot can be deleted to keep the environment clean and manageable.

1. **Deploy main bot into development environment and test** – The updated main bot, now including the new features or changes, is deployed to the development environment. Here, it undergoes thorough testing to ensure all functionalities work as expected.

1. **Deploy main bot into production environment** – After testing in the development environment is complete and successful, the main bot is deployed to the production environment. This step is the final stage of the workflow, where the new features become available to end users.

**Automation and scale**

The automated workflow allows developers to work on different features in parallel, each in separate branches. This facilitates concurrent development, enabling teams to collaborate effectively and deliver features faster. With branches isolated from each other, changes can be merged and deployed without blocking or interfering with other ongoing work.

The workflow automates the deployment and promotion of bot versions across different environments, such as development, testing, and production.

Storing bot definitions in a version control system such as Git provides a comprehensive audit trail and enables efficient collaboration. Changes are tracked to individual developers, ensuring transparency and accountability throughout the development lifecycle. This approach also facilitates code reviews, enabling teams to identify and address issues before deploying to production.

By using AWS CodePipeline and other AWS services, the automated workflow can scale to accommodate increasing workloads and team sizes.

## Tools
<a name="streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is an open-source software development framework for defining AWS Cloud infrastructure in code by using familiar programming languages and provisioning it through CloudFormation. The sample implementation in this pattern uses Python.
+ [AWS CDK Command Line Interface (AWS CDK CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) - The AWS CDK Toolkit is the primary tool for interacting with your AWS CDK app. It executes your app, interrogates the application model you defined, and produces and deploys the CloudFormation templates generated by the CDK.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions. This pattern uses CloudFormation for deploying the Amazon Lex bot configurations and related resources using infrastructure as code.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy. This pattern uses CodeBuild for building and packaging the deployment artifacts.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously. This pattern uses CodePipeline to orchestrate the continuous delivery pipeline.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact withAWS services through commands in your command line shell.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html) is an AWS service for building conversational interfaces (bots) for applications using voice and text.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.

**Other tools**
+ [Git](https://git-scm.com/docs) is an open source distributed version control system.

**Code repository**

The code for this pattern is available in the GitHub [management-framework-sample-for-amazon-lex](https://github.com/aws-samples/management-framework-sample-for-amazon-lex) repository. The code repo contains the following folders and files:
+ `prerequisite` folder – Contains CloudFormation stack definitions (using the AWS CDK) for setting up the required resources and environments.
+ `prerequisite/lexmgmtworkflow` folder – Main directory for the Lex Management Workflow project, including stack definitions and Python code.
+ `prerequisite/tests` – Contains unit tests.
+ `src` folder – Source code directory, including Amazon Lex bot management wrapper and utilities.
+ `src/dialogue_lambda` – Source code directory of the dialogue hook Lambda function that intercepts and processes user inputs during a conversation with an Amazon Lex bot.

## Best practices
<a name="streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow-best-practices"></a>
+ **Separation of concerns**
  + Maintain a clear separation of responsibilities between the DevOps, development, and production environments.
  + Use separate AWS accounts for each environment to enforce proper isolation and security boundaries.
  + Use cross-account roles and least-privilege access principles to ensure controlled access between environments.
+ **Infrastructure as code**
  + Regularly review and update the infrastructure code to align with best practices and evolving requirements.
  + Establish a clear branching and merging strategy for the source code repository
+ **Testing and validation**
  + Implement automated testing at various stages of the pipeline to catch issues early in the development cycle.
  + Use the Amazon Lex console or automated testing frameworks to validate bot configurations and functionality before promoting to higher environments.
  + Consider implementing manual approval gates for deployments to production or critical environments.
+ **Monitoring and logging **
  + Set up monitoring and logging mechanisms for the pipelines, deployments, and bot interactions.
  + Monitor pipeline events, deployment statuses, and bot performance metrics to identify and address issues promptly.
  + Use AWS services such as Amazon CloudWatch, AWS CloudTrail, and AWS X-Ray for centralized logging and monitoring.
  + Regularly review and analyze the performance, efficiency, and effectiveness of the automated workflow.
+ **Security and compliance**
  + Implement secure coding practices and follow AWS security best practices for Amazon Lex bot development and deployment.
  + Regularly review and update IAM roles, policies, and permissions to align with the principle of least privilege.
  + Consider integrating security scanning and compliance checks into the pipelines.

## Epics
<a name="streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow-epics"></a>

### Set up IaC for Amazon Lex bot management
<a name="set-up-iac-for-lex2-bot-management"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the local CDK environment. | 1. To clone this pattern’s repo and navigate to the `prerequisite` directory, run the following command:<pre>git clone https://github.com/aws-samples/management-framework-sample-for-amazon-lex.git<br /><br />cd management-framework-sample-for-amazon-lex</pre><br />2. To install and activate the Python virtual environment, run the following command that installs the CDK’s dependencies locally in the project folder, instead of globally:<pre>pip install virtualenv<br />python<version> -m venv .venv<br />source .venv/bin/activate<br />python -m pip install -r requirements.txt</pre> | AWS DevOps |
| Create a cross-account role in the `devops` environment. | The `devops` account is responsible for hosting and managing the CI/CD pipelines. To enable the CI/CD pipelines to interact with the `dev` and `prod` environments, run the following commands to create a cross-account role in the `devops` account.<pre>cdk bootstrap --profile=devops<br /><br />cdk deploy LexMgmtDevopsRoleStack -c dev-account-id=2222222222222 -c prod-account-id=333333333333 --profile=devops</pre> | AWS DevOps |
| Create a cross-account role in the `dev` environment. | Create an IAM role in the `dev` account with the necessary permissions to allow the `devops` account to assume this role. The CI/CD pipeline uses this role to perform actions in the `dev` account, such as deploying and managing Amazon Lex bot resources.<br />To create the IAM role, run the following commands:<pre>cdk bootstrap --profile=dev<br /><br />cdk deploy LexMgmtCrossaccountRoleStack -c devops-account-id=1111111111111 --profile=dev</pre> | AWS DevOps |
| Create a cross-account role in the `prod` environment. | Create an IAM role in the `prod` account with the necessary permissions to allow the `devops` account to assume this role. The CI/CD pipeline uses this role to perform actions in the `prod` account, such as deploying and managing Amazon Lex bot resources.<pre>cdk bootstrap --profile=prod<br /><br />cdk deploy LexMgmtCrossaccountRoleStack -c devops-account-id=1111111111111 --profile=prod</pre> | AWS DevOps |
| Create pipelines in the `devops` environment. | To manage the development workflow for Amazon Lex bots, run the following command to set up pipelines in the `devops` environment . <pre>cdk deploy LexMgmtWorkflowStack -c devops-account-id=1111111111111 -c dev-account-id=2222222222222 -c prod-account-id=333333333333 --profile=devops</pre> | AWS DevOps |

### Establish the baseline for the main bot
<a name="establish-the-baseline-for-the-main-bot"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Define the initial version of the main bot. | To define the initial version of the main bot, [trigger](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts.html#concepts-triggers) the `BaselineBotPipeline` pipeline.<br />The pipeline deploys the basic bot definition that’s defined in the CloudFormation template, exports the main bot definition as .json files. and stores the main bot code in a version control system. | AWS DevOps |

### Implement the feature development workflow
<a name="implement-the-feature-development-workflow"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the ticket bot to develop and test a feature. | `TicketBot` is a new bot instance that’s imported from the existing main bot definition in the feature branch. This approach ensures that the new bot has all the current functionality and configurations from the main bot.<br />To define the initial version of the ticket bot, trigger the `CreateTicketBotPipeline` pipeline.<br />The pipeline creates a new feature branch in the version control system and creates a new ticket bot instance based on the main bot. | Lex Bot Developer |
| Develop and test the ticket bot feature.  | To develop and test the feature, sign in to the AWS Management Console and open the Amazon Lex console at [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/). For more information, see [Testing a bot using the console](https://docs.aws.amazon.com/lexv2/latest/dg/test-bot.html) in the Amazon Lex documentation.<br />With the `TicketBot` instance, you can now add, modify, or extend the bot's functionality to implement the new feature. For example, you can create or modify intents, utterances, slots, and dialog flows. For more information, see [Adding intents](https://docs.aws.amazon.com/lexv2/latest/dg/add-intents.html) in the Amazon Lex documentation. | Lex Bot Developer |
| Export the ticket bot definition. | The exported bot definition is essentially a representation of the bot's configuration and functionality in a JSON format.<br />To export the ticket bot definition, trigger the `ExportTicketBotPipeline` pipeline.<br />The pipeline exports the ticket bot definition as .json files and stores the ticket bot code in a feature branch in the version control system. | Lex Bot Developer |
| Rebase the feature branch from the latest main branch. | During the development of a new feature, the main branch might have received other changes from different developers or teams. <br />To incorporate these changes into the feature branch, perform a Git `rebase` operation. This operation essentially replays the commits from the feature branch on top of the latest commits from the main branch, ensuring that the feature branch includes all the latest changes | Lex Bot Developer |
| Import and validate the rebased ticket bot. | After you rebase the feature branch, you must import it into the ticket bot instance. This import updates the existing ticket bot with the latest changes from the rebased branch.<br />To import the rebased ticket bot, trigger the `ImportTicketBotPipeline` pipeline.<br />The pipeline imports the ticket bot definition .json files in the feature branch in the version control system into the `TicketBot` instance. | Lex Bot Developer |
| Validate the rebased bot definition. | After you import the rebased bot definition, it's crucial to validate its functionality. You want to make sure that the new feature works as expected and doesn't conflict with existing functionality. <br />This validation typically involves testing the bot with various input scenarios, checking the responses, and verifying that the bot behaves as intended. You can perform validation in either of the following ways:+ Test the bot manually by using the Amazon Lex console.<br />+ Use an automated approach by using testing frameworks and tools that can simulate user interactions and assert expected responses. | Lex Bot Developer |
| Merge the feature branch into the main branch. | After you develop and test the new feature in the isolated `TicketBot` instance, do the following:1. Commit the changes to the corresponding feature branch in the version control system.<br />2. To merge the feature branch into the main branch, create a pull request (PR). This PR serves as a request to review and incorporate the changes into the main codebase. | Lex Bot Developer, Repository Adminstrator |
| Delete the feature branch and the ticket bot.  | After a feature branch is merged successfully into the main branch, delete the feature branch and the ticket bot from the source code repo. <br />To delete the feature branch and the ticket bot, trigger the `DeleteTicketBotPipeline` pipeline.<br />The pipeline removes temporary bot resources that were created during the development process (for example, the ticket bot). This action helps to maintain a clean repo and prevent confusion or conflicts with future feature branches.  | Lex Bot Developer |

### Maintain the main bot
<a name="maintain-the-main-bot"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Import the latest main bot definition into the `dev` environment. | To import the latest main bot definition in the main branch into the `dev` environment, trigger the `DeployBotDevPipeline` pipeline.<br />The pipeline also creates a git tag on approval. | AWS DevOps |
| Import the latest main bot definition into the `prod` environment. | To import the latest bot definition in the main branch into the `prod` environment, provide the tag reference from the previous task as a parameter and trigger the `DeployBotProdPipeline` pipeline.<br />The pipeline imports the latest bot definition from a specific tag into the `prod` environment. | AWS DevOps |

## Troubleshooting
<a name="streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| When you deploy Amazon Lex bots to different AWS accounts, the tooling services must have the necessary permissions to access resources in those accounts. | To grant cross-account access, use IAM roles and policies. Create IAM roles in the target accounts and attach policies to the roles that grant the required permissions. Then, assume these roles from the account where the Amazon Lex bot is deployed.<br />For more information, see [IAM permissions required to import](https://docs.aws.amazon.com/lexv2/latest/dg/import.html#import-permissions) and [IAM permissions required to export bots in Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/export.html#export-permissions) in the Amazon Lex documentation. |

## Related resources
<a name="streamline-amazon-lex-bot-development-and-deployment-using-an-automated-workflow-resources"></a>
+ [Importing bots in Amazon Lex V2](https://docs.aws.amazon.com/lexv2/latest/dg/import.html)
+ [Start a pipeline in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-about-starting.html)
+ [Working with Amazon Lex V2 bots](https://docs.aws.amazon.com/lexv2/latest/dg/building-bots.html)
