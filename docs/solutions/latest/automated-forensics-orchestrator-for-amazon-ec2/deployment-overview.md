---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/deployment-overview.html
---

# Deployment overview
<a name="deployment-overview"></a>

Use the following steps to deploy this Guidance on AWS. For detailed instructions, follow the links for each step,

The Guidance is deployed in the following three AWS accounts:

1. Forensic AWS account - Core Guidance components to perform forensics orchestration

1. Security Hub AWS account - Configure events and custom actions to trigger forensic orchestration flow

1. Application AWS account - IAM roles needed to establish trust between Forensic AWS account and Application AWS account

Deploying this Guidance is a three-step process.

1. Forensic Orchestrator Guidance deployment in the *Forensic AWS Account.*

1. AWS Security Hub configuration to add custom actions to trigger forensics from AWS Security Hub in the *Security Hub AWS account.*

1.  *Application AWS Account* deployment to establish trust relationship with the Forensic AWS account.

**Note**
The Automated Forensics Orchestrator for Amazon EC2 and EKS can also be deployed in Security Hub AWS account. Use existing VPC steps to deploy AWS Security Hub configuration in Security Hub AWS account.

## Forensic Orchestrator Guidance deployment in Forensic AWS account
<a name="forensic-orchestrator-solution-deployment-in-forensic-aws-account"></a>

The following steps deploy the Forensics Orchestrator AWS Step Functions, AWS Lambda, and AWS SSM documents into the Forensic AWS account.

1. In your terminal, clone the Guidance’s source code from the [GitHub repository](https://github.com/aws-solutions-library-samples/automated-forensic-orchestrator-for-amazon-ec2).

   ```
   git clone link:https://github.com/aws-solutions-library-samples/automated-forensic-orchestrator-for-amazon-ec2.git
   ```

1. Navigate to the source code folder created in step 1.

   ```
   cd automated-forensic-orchestrator-for-amazon-ec2/source
   ```
**Note**
To deploy into existing VPC update `cdk.json` to configure **isExistingVPC** to `true` and add **vpcID** to **vpcConfigDetails** in `cdk.json`.

   ```
   "vpcConfigDetails": {
               "isExistingVPC": true,
               "vpcID": "vpc-1234567890"
               "enableVPCEndpoints": false,
               "enableVpcFlowLog": false
   }
   ```

1. Set AWS credentials to deploy into the AWS account.

   ```
   AWS_ACCESS_KEY_ID=<your_access_key_id>
   ```

```
export AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
```

```
export AWS_SESSION_TOKEN=<your_session_token>
```

```
export AWS_REGION=<Your Region - us-east-1>
```

1. Install the required NPM libraries.

   ```
   npm ci
   ```

1. Compile and build AWS Lambda functions.

   ```
   npm run build
   ```

1. Build the forensics AWS CloudFormation stack to be deployed in the forensic AWS account.

   ```
   cdk synth -c account=<Forensic AWS Account Number> -c region=<Region> -c sechubaccount=<Security Hub Aggregator Account Number> -c STACK_BUILD_TARGET_ACCT=forensicAccount
   ```

   1. Build the necessary CDK CFN templates for deploying forensic stack. Example:

      ```
      cdk synth -c account=1234567890 -c sechubaccount=0987654321 -c region=us-east-1 -c STACK_BUILD_TARGET_ACCT=forensicAccount
      ```

1. Deploy the forensics stack in the forensic AWS account.

   ```
   cdk deploy --all -c account=<Forensic AWS Account Number> -c region=<Region> --require-approval=never -c sechubaccount=<Security Hub Aggregator AWS Account Number> -c STACK_BUILD_TARGET_ACCT=forensicAccount
   ```

   Example command that deploys Forensic Guidances stack:

   ```
   cdk deploy --all -c sechubaccount=0987654321 -c STACK_BUILD_TARGET_ACCT=forensicAccount -c account=1234567890 -c region=us-east-1 --require-approval=never
   ```

## Security Hub aggregator account deployment in a new VPC
<a name="security-hub-aggregator-account-deployment-in-a-new-vpc"></a>

As described above, the Guidance has a dependency on Security Hub to initiate the forensics orchestration. To initiate the forensic Step Functions deployed in the forensic account from AWS Security Hub findings through custom actions present in AWS Security Hub account, deploy the following stack in Security Hub aggregator AWS account.

**Note**
If you are reusing the existing downloaded code delete the `cdk.out` folder.

1. Clone the Guidance source code from AWS Solutions Library Samples GitHub repository.

   ```
   git clone link:https://github.com/aws-solutions-library-samples/automated-forensic-orchestrator-for-amazon-ec2.git
   ```

1. Navigate to the cloned repository created in step 1.

1. Navigate to the source folder.

   ```
   cd automated-forensic-orchestrator-for-amazon-ec2/source
   ```
**Note**
To deploy into existing VPC update `cdk.json` to configure **isExistingVPC** to `true` and add **vpcID** to the vpcConfigDetails in the `cdk.json` file.

   ```
   "vpcConfigDetails": {
               "isExistingVPC": true,
               "vpcID": "vpc-1234567890"
               "enableVPCEndpoints": false,
               "enableVpcFlowLog": false
   }
   ```

1. Set AWS credentials to deploy into the AWS account.

   ```
   export AWS_ACCESS_KEY_ID=<your_access_key_id>
   ```

```
export AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
```

```
export AWS_SESSION_TOKEN=<your_session_token>
```

```
export AWS_REGION=<Your Region -us-east-1>
```

1. Install the required NPM libraries.

   ```
   npm ci
   ```

1. Compile and build AWS Lambda functions.

   ```
   npm run build
   ```

1. Build the forensics Security Hub AWS CloudFormation stack to be deployed in Security Hub aggregator account.

   ```
   cdk synth -c sechubaccount=<SecHub Account Number> -c forensicAccount=<ForensicAccount> -c forensicRegion=us-east-1 -c sechubregion=us-east-1 -c STACK_BUILD_TARGET_ACCT=securityHubAccount
   ```

   Example:

   ```
   cdk synth -c sechubaccount=0987654321 -c forensicAccount=1234567890 -c forensicRegion=us-east-1 -c sechubregion=us-east-1 -c STACK_BUILD_TARGET_ACCT=securityHubAccount
   ```

1. Deploy the forensics Security Hub stack in the Security Hub aggregator account.

   ```
   cdk deploy --all -c sechubaccount=0987654321 -c account=<Security Hub AWS AccountNumber> -c region=us-east-1 --require-approval=never -c forensicAccount=<Forensic AWS AccountNumber> -c STACK_BUILD_TARGET_ACCT=securityHubAccount -c sechubregion=us-east-1
   ```

   Example:

   ```
   cdk deploy --all -c sechubaccount=0987654321 -c account=0987654321 -c region=us-east-1 --require-approval=never -c forensicAccount=1234567890 -c STACK_BUILD_TARGET_ACCT=securityHubAccount -c sechubregion=us-east-1
   ```

## Application account deployment
<a name="application-account-deployment"></a>

1. Download the [cross-account-role.yml](https://github.com/aws-solutions-library-samples/automated-forensic-orchestrator-for-amazon-ec2/blob/main/source/deployment-prerequisties/cross-account-role.yml) file to your local hard drive.

1. Deploy the `/deployment-prerequisties/cross-account-role.yml` template file as an AWS CloudFormation stack in the application account, and pass the forensic account as input parameter. This will establish a trust relationship between the forensic components deployed in the forensic account and the application account.

   ```
   aws cloudformation deploy --template-file /deployment-prerequisties/cross-account-role.yml --stack-name app-stack --parameter-overrides solutionInstalledAccount=<Forensic Solution AWS Account Number> solutionAccountRegion=us-east-1 kmsKey=<ARN of the application account EBS volume encryption KMS key>
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Forensics Orchestrator for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
