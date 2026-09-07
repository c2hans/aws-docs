---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/improve-operational-performance-by-enabling-amazon-devops-guru-across-multiple-aws-regions-accounts-and-ous-with-the-aws-cdk.html
---

# Improve operational performance by enabling Amazon DevOps Guru across multiple AWS Regions, accounts, and OUs with the AWS CDK
<a name="improve-operational-performance-by-enabling-amazon-devops-guru-across-multiple-aws-regions-accounts-and-ous-with-the-aws-cdk"></a>

*Dr. Rahul Sharad Gaikwad, Amazon Web Services*

## Summary
<a name="improve-operational-performance-by-enabling-amazon-devops-guru-across-multiple-aws-regions-accounts-and-ous-with-the-aws-cdk-summary"></a>

This pattern demonstrates the steps to enable the Amazon DevOps Guru service across multiple Amazon Web Services (AWS) Regions, accounts, and organizational units (OUs) by using the AWS Cloud Development Kit (AWS CDK) in TypeScript. You can use AWS CDK stacks to deploy AWS CloudFormation StackSets from the administrator (primary) AWS account to enable Amazon DevOps Guru across multiple accounts, instead of logging into each account and enabling DevOps Guru individually for each account.

Amazon DevOps Guru provides artificial intelligence operations (AIOps) features to help you improve the availability of your applications and resolve operational issues faster. DevOps Guru reduces your manual effort by applying machine learning (ML) powered recommendations, without requiring any ML expertise. DevOps Guru analyzes your resources and operational data. If it detects any anomalies, it provides metrics, events, and recommendations to help you address the issue.

This pattern describes three deployment options for enabling Amazon DevOps Guru:
+ For all stack resources across multiple accounts and Regions
+ For all stack resources across OUs
+ For specific stack resources across multiple accounts and Regions

## Prerequisites and limitations
<a name="improve-operational-performance-by-enabling-amazon-devops-guru-across-multiple-aws-regions-accounts-and-ous-with-the-aws-cdk-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI), installed and configured. (See [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the AWS CLI documentation.)
+ AWS CDK Toolkit, installed and configured. (See [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) in the AWS CDK documentation.)
+ Node Package Manager (npm), installed and configured for the AWS CDK in TypeScript. (See [Downloading and installing Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) in the npm documentation.)
+ Python3 installed and configured, for running a Python script to inject traffic into the sample serverless application. (See [Python Setup and Usage](https://docs.python.org/3/using/index.html) in the Python documentation.)
+ Pip, installed and configured to install the Python requests library. (See the [pip installation instructions](https://pypi.org/project/pip/) on the PyPl website.)

**Product versions**
+ AWS CDK Toolkit version 1.107.0 or later
+ npm version 7.9.0 or later
+ Node.js version 15.3.0 or later

## Architecture
<a name="improve-operational-performance-by-enabling-amazon-devops-guru-across-multiple-aws-regions-accounts-and-ous-with-the-aws-cdk-architecture"></a>

**Technologies**

The architecture for this pattern includes the following services:
+ [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/)
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
+ [AWS Lambda](https://aws.amazon.com/lambda/)
+ [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)

**AWS CDK stacks**

The pattern uses the following AWS CDK stacks:
+ `CdkStackSetAdminRole` – Creates an AWS Identity and Access management (IAM) administrator role to establish a trust relationship between the administrator and target accounts.
+ `CdkStackSetExecRole` – Creates an IAM role to trust the administrator account.
+ `CdkDevopsGuruStackMultiAccReg` – Enables DevOps Guru across multiple AWS Regions and accounts for all stacks, and sets up Amazon Simple Notification Service (Amazon SNS) notifications.
+ `CdkDevopsGuruStackMultiAccRegSpecStacks` – Enables DevOps Guru across multiple AWS Regions and accounts for specific stacks, and sets up Amazon SNS notifications.
+ `CdkDevopsguruStackOrgUnit` – Enables DevOps Guru across OUs, and sets up Amazon SNS notifications.
+ `CdkInfrastructureStack` – Deploys sample serverless application components such as API Gateway, Lambda, and DynamoDB in the administrator account to demonstrate fault injection and insights generation.

**Sample application architecture**

The following diagram illustrates the architecture of a sample serverless application that has been deployed across multiple accounts and Regions. The pattern uses the administrator account to deploy all the AWS CDK stacks. It also uses the administrator account as one of the target accounts for setting up DevOps Guru.

1. When DevOps Guru is enabled, it first baselines each resource’s behavior and then ingests operational data from CloudWatch vended metrics.

1. If it detects an anomaly, it correlates it with the events from CloudTrail, and generates an insight.

1. The insight provides a correlated sequence of events along with prescribed recommendations to enable the operator to identify the culprit resource.

1. Amazon SNS sends notification messages to the operator.

![A sample serverless application that has been deployed across multiple accounts and Regions.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6075ca48-862a-4aa0-93c6-10bad8195a5c/images/beeb0992-aaa8-4f08-b983-685b6b8b8d5e.png)

**Automation and scale**

The [GitHub repository](https://github.com/aws-samples/amazon-devopsguru-cdk-samples.git) provided with this pattern uses the AWS CDK as an infrastructure as code (IaC) tool to create the configuration for this architecture. AWS CDK helps you orchestrate resources and enable DevOps Guru across multiple AWS accounts, Regions, and OUs.

## Tools
<a name="improve-operational-performance-by-enabling-amazon-devops-guru-across-multiple-aws-regions-accounts-and-ous-with-the-aws-cdk-tools"></a>

**AWS services**
+ [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) – AWS Cloud Development Kit (AWS CDK) helps you define your cloud infrastructure as code in one of five supported programming languages: TypeScript, JavaScript, Python, Java, and C\#.
+ [AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)– AWS Command Line Interface (AWS CLI) is a unified tool that provides a consistent command-line interface for interacting with AWS services and resources.

**Code**

The source code for this pattern is available on GitHub, in the [Amazon DevOps Guru CDK Samples](https://github.com/aws-samples/amazon-devopsguru-cdk-samples.git) repository. The AWS CDK code is written in TypeScript. To clone and use the repository, follow the instructions in the next section.

**Important**
Some of the stories in this pattern include AWS CDK and AWS CLI command examples that are formatted for Unix, Linux, and macOS. For Windows, replace the backslash (\\) continuation character at the end of each line with a caret (^).

## Epics
<a name="improve-operational-performance-by-enabling-amazon-devops-guru-across-multiple-aws-regions-accounts-and-ous-with-the-aws-cdk-epics"></a>

### Prepare the AWS resources for deployment
<a name="prepare-the-aws-resources-for-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure AWS named profiles. | Set up your AWS named profiles as follows to deploy stacks in a multi-account environment.<br />For the administrator account:<pre>$aws configure --profile administrator<br />AWS Access Key ID [****]: <your-administrator-access-key-ID><br />AWS Secret Access Key [****]: <your-administrator-secret-access-key><br />Default region name [None]: <your-administrator-region><br />Default output format [None]: json</pre><br />For the target account:<pre>$aws configure --profile target<br />AWS Access Key ID [****: <your-target-access-key-ID><br />AWS Secret Access Key [****]: <your-target-secret-access-key><br />Default region name [None]: <your-target-region><br />Default output format [None]: json</pre><br />For more information, see [Using named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles) in the AWS CLI documentation. | DevOps engineer |
| Verify AWS profile configurations. | (Optional) You can verify your AWS profile configurations in the `credentials` and `config` files by following the instructions in [Set and view configuration settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-methods) in the AWS CLI documentation. | DevOps engineer |
| Verify the AWS CDK version. | Verify the version of the AWS CDK Toolkit by running the following command:<pre>$cdk --version</pre><br />This pattern requires version 1.107.0 or later. If you have an earlier version of the AWS CDK, follow the instructions in the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) to update it. | DevOps engineer |
| Clone the project code. | Clone the GitHub repository for this pattern by using the command:<pre>$git clone https://github.com/aws-samples/amazon-devopsguru-cdk-samples.git</pre> | DevOps engineer |
| Install package dependencies and compile the TypeScript files. | Install the package dependencies and compile the TypeScript files by running the following commands:<pre>$cd amazon-devopsguru-cdk-samples<br />$npm install<br />$npm fund</pre><br />These commands install all the packages from the sample repository.If you get any errors about missing packages, use one of the following commands:<pre>$npm ci</pre><br />—or—<pre>$npm install -g @aws-cdk/<package-name></pre><br />You can find the list of package names and versions in the `Dependencies` section of the `/amazon-devopsguru-cdk-samples/package.json` file. For more information, see [npm ci](https://docs.npmjs.com/cli/v7/commands/npm-ci) and [npm install](https://docs.npmjs.com/cli/v7/commands/npm-install) in the npm documentation. | DevOps engineer |

### Build (synthesize) the AWS CDK stacks
<a name="build-synthesize-the-aws-cdk-stacks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure an email address for Amazon SNS notifications. | Follow these steps to provide an email address for Amazon SNS notifications:1. Edit the files `/amazon-devopsguru-cdk-samples/lib/cdk-devopsguru-multi-acc-reg-stack.ts` and `/amazon-devopsguru-cdk-samples/lib/cdk-devopsguru-org-uni-stack.ts`.<br />2. In the `DevOpsGuruTopic`, `Subscription` section, update the `Endpoint` parameter with your email address.<br />3. Save and close the files. | DevOps engineer |
| Build the project code. | Build the project code and synthesize the stacks by running the command:<pre>npm run build && cdk synth </pre><br />You should see output similar to the following: <pre>$npm run build && cdk synth<br />> cdk-devopsguru@0.1.0 build<br />> tsc<br />Successfully synthesized to ~/amazon-devopsguru-cdk-samples/cdk.out<br />Supply a stack id (CdkDevopsGuruStackMultiAccReg,CdkDevopsGuruStackMultiAccRegSpecStacks, CdkDevopsguruStackOrgUnit, CdkInfrastructureStack, CdkStackSetAdminRole, CdkStackSetExecRole) to display its template.</pre><br />For more information and steps, see [Your first AWS CDK app](https://docs.aws.amazon.com/cdk/latest/guide/hello_world.html) in the AWS CDK documentation. | DevOps engineer |
| List the AWS CDK stacks. | Run the following command to list all AWS CDK stacks:<pre>$cdk list</pre><br />The command displays the following list:<pre>CdkDevopsGuruStackMultiAccReg<br />CdkDevopsGuruStackMultiAccRegSpecStacks<br />CdkDevopsguruStackOrgUnit<br />CdkInfrastructureStack<br />CdkStackSetAdminRole<br />CdkStackSetExecRole</pre> | DevOps engineer |

### Option 1 - Enable DevOps Guru for all stack resources across multiple accounts
<a name="option-1---enable-devops-guru-for-all-stack-resources-across-multiple-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the AWS CDK stacks for creating IAM roles. | This pattern uses [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to perform stack operations across multiple accounts. If you are creating your first stack set, you must create the following IAM roles to get the required permissions set up in your AWS accounts:+ `AWSCloudFormationStackSetAdministrationRole`<br />+ `AWSCloudFormationStackSetExecutionRole`The roles must have these exact names.1. Create the IAM `AWSCloudFormationStackSetAdministrationRole` role in the administrator (primary) account by running the following CLI command:<pre>$cdk deploy CdkStackSetAdminRole --profile administrator</pre><br />2. Create the IAM `AWSCloudFormationStackSetExecutionRole` role in all target accounts where you want to run the stack instances. To create this role, run these CLI commands:<pre>$cdk deploy CdkStackSetExecRole \<br />  --parameters AdministratorAccountId=<administrator-account-ID> \<br />  --profile administrator  <br /><br />$cdk deploy CdkStackSetExecRole \<br />  --parameters AdministratorAccountId=<administrator-account-ID> \<br />  --profile target</pre><br />For more information, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) in the AWS CloudFormation documentation. | DevOps engineer |
| Deploy the AWS CDK stack for enabling DevOps Guru across multiple accounts. | The AWS CDK `CdkDevopsGuruStackMultiAccReg` stack creates stack sets to deploy stack instances across multiple accounts and Regions. To deploy the stack, run the following CLI command with the specified parameters:<pre>$cdk deploy CdkDevopsGuruStackMultiAccReg \<br />  --profile administrator \<br />  --parameters AdministratorAccountId=<administrator-account-ID> \<br />  --parameters TargetAccountId=<target-account-ID> \<br />  --parameters RegionIds="<region-1>,<region-2>"</pre><br />Currently Amazon DevOps Guru is available in the AWS Regions listed in the [DevOps Guru FAQ](https://aws.amazon.com/devops-guru/faqs/). | DevOps engineer |

### Option 2 - Enable DevOps Guru for all stack resources across OUs
<a name="option-2---enable-devops-guru-for-all-stack-resources-across-ous"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Extract OU IDs. | On the [AWS Organizations](https://console.aws.amazon.com/organizations/v2/home/accounts) console, identify the IDs of the organizational units where you want to enable DevOps Guru. | DevOps engineer |
| Enable service-managed permissions for OUs. | If you're using AWS Organizations for account management, you must grant service-managed permissions to enable DevOps Guru. Instead of creating the IAM roles manually, use [organization-based trusted access and service-linked roles (SLRs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-enable-trusted-access.html)). | DevOps engineer |
| Deploy the AWS CDK stack for enabling DevOps Guru across OUs. | The AWS CDK `CdkDevopsguruStackOrgUnit` stack enables DevOps Guru service across OUs. To deploy the stack, run the following command with the specified parameters:<pre>$cdk deploy CdkDevopsguruStackOrgUnit \<br />  --profile administrator \ <br />  --parameters RegionIds="<region-1>,<region-2>" \<br />  --parameters OrganizationalUnitIds="<OU-1>,<OU-2>"</pre> | DevOps engineer |

### Option 3 - Enable DevOps Guru for specific stack resources across multiple accounts
<a name="option-3---enable-devops-guru-for-specific-stack-resources-across-multiple-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the AWS CDK stacks for creating IAM roles. | If you haven't already created the required IAM roles shown in the first option, do that first:1. Create the IAM `AWSCloudFormationStackSetAdministrationRole` role in the administrator (primary) account by running the following CLI command:<pre>$cdk deploy CdkStackSetAdminRole --profile administrator</pre><br />2. Create the IAM `AWSCloudFormationStackSetExecutionRole` role in all target accounts where you want to run the stack instances. To create this role, run the CLI commands:<pre>$cdk deploy CdkStackSetExecRole \<br />  --parameters AdministratorAccountId=<administrator-account-ID> \<br />  --profile administrator  <br /><br />$cdk deploy CdkStackSetExecRole \<br />  --parameters AdministratorAccountId=<administrator-account-ID> \<br />  --profile target</pre><br />For more information, see [Grant self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html) in the AWS CloudFormation documentation. | DevOps engineer |
| Delete existing stacks. | If you already used the first option to enable DevOps Guru for all stack resources, you can delete the old stack by using the following command:<pre>$cdk destroy CdkDevopsGuruStackMultiAccReg --profile administrator </pre><br />Or, you can change the` RegionIds` parameter when you redeploy the stack to avoid a *Stacks already exist* error. | DevOps engineer |
| Update the AWS CDK stack with a stack list.  | 1. Edit the file `/amazon-devopsguru-cdk-samples/lib/cdk-devopsguru-multi-acc-reg-spec-stack.ts`.<br />2. Under `Resources`, `CloudFormation`, `StackNames`, list the stacks for which you want to enable DevOps Guru. For demonstration purposes, the parameter specifies the `CdkInfrastructureStack` stack, but you can edit this entry based on your requirements.<br />3. Save and close the file.<br />4. To synthesize and update the stack template, run:<pre> $cdk synth</pre> | Data engineer |
| Deploy the AWS CDK stack for enabling DevOps Guru for specific stack resources across multiple accounts. | The AWS CDK `CdkDevopsGuruStackMultiAccRegSpecStacks` stack enables DevOps Guru for specific stack resources across multiple accounts. To deploy the stack, run the following command:<pre>$cdk deploy CdkDevopsGuruStackMultiAccRegSpecStacks \<br />  --profile administrator  \<br />  --parameters AdministratorAccountId=<administrator-account-ID> \<br />  --parameters TargetAccountId=<target-account-ID> \<br />  --parameters RegionIds="<region-1>,<region-2>"</pre>If you previously deployed this stack for option 1, change the `RegionIds` parameter (making sure to choose from [available Regions](https://aws.amazon.com/devops-guru/faqs/)) to avoid a *Stacks already exist* error. | DevOps engineer |

### Deploy the AWS CDK infrastructure stack
<a name="deploy-the-aws-cdk-infrastructure-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the sample serverless infrastructure stack. | The AWS CDK `CdkInfrastructureStack` stack deploys serverless components such as API Gateway, Lambda, and a DynamoDB table to demonstrate DevOps Guru insights. To deploy the stack, run the following command: <pre>$cdk deploy CdkInfrastructureStack --profile administrator</pre> | DevOps engineer |
| Insert sample records in DynamoDB. | Run the following command to populate the DynamoDB table with sample records. Provide the correct path for the `populate-shops-dynamodb-table.json` script.<pre>$aws dynamodb batch-write-item \<br />  --request-items file://scripts/populate-shops-dynamodb-table.json \<br />  --profile administrator</pre><br />The command displays the following output:<pre>{<br />    "UnprocessedItems": {}<br />}</pre> | DevOps engineer |
| Verify inserted records in DynamoDB. | To verify that the DynamoDB table includes the sample records from the `populate-shops-dynamodb-table.json` file, access the URL for the `ListRestApiEndpointMonitorOperator` API, which is published as an output of the AWS CDK stack. You can also find this URL in the **Outputs** tab of the AWS CloudFormation console for the `CdkInfrastructureStack` stack. The AWS CDK output would look similar to the following:<pre>CdkInfrastructureStack.CreateRestApiMonitorOperatorEndpointD1D00045 = https://oure17c5vob.execute-api.<your-region>.amazonaws.com/prod/<br /><br />CdkInfrastructureStack.ListRestApiMonitorOperatorEndpointABBDB8D8 = https://cdff8icfrn4.execute-api.<your-region>.amazonaws.com/prod/</pre> | DevOps engineer |
| Wait for resources to complete baselining. | This serverless stack has a few resources. We recommend that you wait for 2 hours before you carry out the next steps. If you deployed this stack in a production environment, it might take up to 24 hours to complete baselining, depending on the number of resources you selected to monitor in DevOps Guru. | DevOps engineer |

### Generate DevOps Guru insights
<a name="generate-devops-guru-insights"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the AWS CDK infrastructure stack. | To try out DevOps Guru insights, you can make some configuration changes to reproduce a typical operational issue.1. Edit the file `/amazon-devopsguru-cdk-samples/lib/infrastructure-stack.ts`.<br />2. In the `DDB Table` section, change the read capacity for the DynamoDB table from 5 to 1.<br />3. Save and close the file.<br />4. Run the following commands to synthesize and deploy the updated AWS CDK infrastructure stack:<pre>$cdk synth<br />$cdk deploy CdkInfrastructureStack --profile administrator</pre> | DevOps engineer |
| Inject HTTP requests on the API. | Inject ingress traffic in the form of HTTP requests on the `ListRestApiMonitorOperatorEndpointxxxx` API:1. Edit the Python script `/amazon-devopsguru-cdk-samples/scripts/sendAPIRequest.py`.<br />2. Update the `url` variable with the API link for `ListRestApiMonitorOperatorEndpointxxxx`. You can find this URL in the output of the AWS CDK **deploy** command or on the AWS Cloudformation console, in the **Outputs** tab for the stack.<br />3. Save and close the file.<br />4. Run the Python script by using the command:<pre>$python sendAPIRequest.py</pre><br />5. Make sure that you get a 200 status code.<br />6. You might need to run the script through multiple (preferably four) terminals to inject traffic at a high rate.<br />7. After the script runs approximately 10 minutes in a loop, you can see an operational insight on the [DevOps Guru console](https://console.aws.amazon.com/devops-guru/). | DevOps engineer |
| Review DevOps Guru insights. | Under standard conditions, the DevOps Guru dashboard displays zero in the ongoing insights counter. If it detects an anomaly, it raises an alert in the form of an insight. In the navigation pane, choose **Insights** to see the details of the anomaly, including an overview, aggregated metrics, relevant events, and recommendations. For more information about reviewing insights, see the [Gaining operational insights with AIOps using Amazon DevOps Guru](https://aws.amazon.com/blogs/devops/gaining-operational-insights-with-aiops-using-amazon-devops-guru/) blog post. | DevOps engineer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up and delete resources. | After you walk through this pattern, you should remove the resources you created to avoid incurring any further charges. Run these commands:<pre>$cdk destroy CdkDevopsGuruStackMultiAccReg --profile administrator<br />$cdk destroy CdkDevopsguruStackOrgUnit --profile administrator<br />$cdk destroy CdkDevopsGuruStackMultiAccRegSpecStacks --profile administrator<br />$cdk destroy CdkInfrastructureStack --profile administrator<br />$cdk destroy CdkStackSetAdminRole --profile administrator<br />$cdk destroy CdkStackSetExecRole --profile administrator<br />$cdk destroy CdkStackSetExecRole --profile target</pre> | DevOps engineer |

## Related resources
<a name="improve-operational-performance-by-enabling-amazon-devops-guru-across-multiple-aws-regions-accounts-and-ous-with-the-aws-cdk-resources"></a>
+ [Gaining operational insights with AIOps using Amazon DevOps Guru](https://aws.amazon.com/blogs/devops/gaining-operational-insights-with-aiops-using-amazon-devops-guru/)
+ [Easily configure Amazon DevOps Guru across multiple accounts and Regions using AWS CloudFormation StackSets](https://aws.amazon.com/blogs/devops/configure-devops-guru-multiple-accounts-regions-using-cfn-stacksets/)
+ [DevOps Guru Workshop](https://aiops-using-devops-guru.workshop.aws/)
