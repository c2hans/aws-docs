---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/deployment.html
---

# Deployment
<a name="deployment"></a>

 Before you deploy this solution, review the architecture and other considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 15 mins

## Prerequisites
<a name="prerequisites"></a>

### Install tools
<a name="install-tools"></a>

 Install the following tools.
+  The latest version of the [AWS CLI](https://aws.amazon.com/cli/) (2.2.37 or newer), installed and configured.
+  The latest version of the [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) (1.116.0 or newer).
+  Make 3.5.0 or newer. For Mac OS X, run brew install make; for Amazon Linux 2, run yum install make.
+  (Optional) [Docker](https://docs.docker.com/get-docker/) 19.0.0 or newer (required when `enableOpa` is set to `true`).
+  A CDK bootstrapped AWS account, refer to [Bootstrapping](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html) for more information.
+  Node.js version 14, refer to [Getting started](https://docs.npmjs.com/getting-started) for more information.

### Activate AWS Config and AWS Network Firewall
<a name="activate-aws-config-and-aws-network-firewall"></a>
+  Ensure AWS Config aggregator is configured and accessible to the solution. The Config aggregator can operate in the same account to which the solution will be deployed to, or can be accessed using the `crossAccountConfigReadOnlyRole` role when located in another account.
+  Create at least one Network Firewall rule group before installing this solution.

 Install AWS Certificate Manager (ACM) certificate
+  (Optional) The ACM certificate is required only when `enableOpa` is set to `true`. A certificate is required to import into ACM to allow the solution to activate transport layer security (TLS) in Application Load Balancer.

## Deployment overview
<a name="deployment-overview"></a>

 Deploying this architecture on AWS includes the following steps. For detailed instructions, follow the links for each step.

 [Step 1. Update solution configuration](#step-1.-update-solution-configuration)

 [Step 2. Build and deploy the stack](#step-2.-build-and-deploy-the-stack)

1.  (Optional) Cross-account support.

1.  (Optional) Deploy to existing VPC.

## Step 1. Update solution configuration
<a name="step-1.-update-solution-configuration"></a>

 The solution can be configured to suit different customer requirements for rule synchronization delay and specific cloud resources. All configuration items can be configured in the `cdk.context.json` file located in the `source` folder.

 The supported configuration and their default values are as follows:

**Note**
 None of the following properties are mandatory during configuration. If no customer value is provided, the default value of the configuration is used.

|  **Configuration**  |  **Description**  |  **Default value**  |  **Value type**  |
| --- | --- | --- | --- |
|  networkFirewallRuleGroupNamePattern  |  Allowed Network Firewall rule group pattern  |  default-anfwconfig-rule-\*  |  string  |
|  defaultAggregatorName  |  AWS Config aggregator name used by this solution, when creating a new rule group. If no aggregator is provided, defaultAggregator will be assigned to the rule group  |  org-replicator |  string  |
|  ruleResolutionInterval  |  The interval rules are resolved and applied into Network Firewall  |  10 mins  |  integer, min value 5, max value 60  |
|  failureNotificationTargetEmails  |  The email address for sending notifications. Once rule resolution failure happens, customer can add their email to the SNS topic manually later on  |  []  |  list of strings  |
|  apiGatewayType  |  The type of API gateway  |  private  |  edge \| private  |
|  enableOpa\*  |  (OPA specific configuration) Enable OPA cluster to validate rule and object mutation requests  |  FALSE  |  true \| false  |
|  certificateArn\*  |  (OPA specific configuration) ACM certification for the ALB  |  used when enableOpa is set to true  |   |
|  crossAccountConfigReadOnlyRole\*\*  |  AWS IAM read-only role in the account in which the AWS config is activated  |  NULL, target at solution installation account  |  string  |
|  crossAccount NetworkFirewall ReadWriteRole\*\*  |  AWS IAM read/write role account in which the AWS network firewall instance is setup  |  NULL, target at solution installation account  |  string  |

### Override default configuration values
<a name="override-default-configuration-values"></a>

 There are two ways to update the default values provided by the solution:

1.  Update the `cdk.context.json` file.

   1.  Go to the solution’s `source` folder.

   1.  Locate the `cdk.context.json` file.

   1.  Update the value of any supported configuration listed in the above table.

   1.  Follow the steps in [Build and deploy the stack](#step-2.-build-and-deploy-the-stack) section.

1.  Passing the parameter from command line.

   1.  Follow step 7.b in [Build and deploy the stack](#step-2.-build-and-deploy-the-stack) section.

## Step 2. Build and deploy the stack
<a name="step-2.-build-and-deploy-the-stack"></a>

1.  Clone the solution source code from its [GitHub repository](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/).

1.  Open the terminal and navigate to the folder created in step 1.

1.  Navigate to the `source` folder.

1.  Run the following command to install a global npm plugin to allow cross-account deployment:

   ```
   npm install -g cdk-assume-role-credential-plugin
   ```

1.  Run `npm run install:all`.

1.  Run `npm run all`.

1.  Run `cdk synth`.

   1.  (Optional for customize configuration value), run `cdk synth -c <Configuration> <Value>`

      For example, to override `ruleResolutionInterval`, run:

      ```
      cdk synth -c ruleResolutionInterval=5
      ```

       This would set the `ruleResolutionInterval` from default 10 minutes to five minutes.

1.  Run `cdk deploy`.

   1.  Ensure docker daemon is running (if OPA is activated).

    cdk boot strap is completed for the deployment account.

### (Optional) Activate cross-account access
<a name="optional-activate-cross-account-access"></a>

 This section is required only if the AWS Config and/or AWS Network Firewall instance is in a different account in which the solution is installed.

 **Activate cross-account access for AWS Config**

To allow cross-account access, create a trusted role in the hosting account in which AWS Config is going to be used.

1.  Update the solution’s configuration `crossAccountConfigReadOnlyRole` to `arn:aws:iam::<TARGET_ACCOUNT>:role/ConfigReadOnlyRole` where `TARGET_ACCOUNT` is the account AWS Config is running.

1.  Redeploy the solution. For details, refer to [Build and deploy the stack](#step-2.-build-and-deploy-the-stack).

1.  Deploy cross account role.

   1.  Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/home) of the TARGET\_ACCOUNT.

   1.  Select the button to launch the `deployment-prerequisties/cross-account-role-config-stack.yaml` AWS CloudFormation template.

   1.  Choose **Next**.

   1.  Update the stack name to Object-extension-AWS-config-role-stack.

   1.  Update **solutionInstalledAccount** to the target account.

   1.  Choose **Next**.

   1.  Choose **Create stack** to deploy the stack.

 The stack deploys the following resources to the target account.

1.  Cross-account trust IAM role `ConfigReadOnlyRole` in the target account.

1.  Trust relationship to the solution installation account.

 **Activate cross-account access for AWS Network Firewall**

 This solution also supports cross-account access for AWS Network Firewall.

1.  Update the solution’s configuration `crossAccount NetworkFirewall ReadWriteRole` to `arn:aws:iam::<TARGET_ACCOUNT>:role/NetworkFirewallReadWriteRole` where `TARGET_ACCOUNT` is the account AWS Config is running.

1.  Redeploy the solution. For details, refer to [Build and deploy the stack](#step-2.-build-and-deploy-the-stack).

1.  Deploy cross-account role.

   1.  Sign in to the [AWS Management Console](https://console.aws.amazon.com/console/home) of the TARGET\_ACCOUNT.

   1.  Select the button to launch the `deployment-prerequisties/cross-account-role-anfw-stack.yaml` AWS CloudFormation template.

   1.  Choose **Next**.

   1.  Update stack name to `Object-extension-AWS-network-firewall-role-stack`.

   1.  Update **solutionInstalledAccount** to the target account.

   1.  Choose **Next**.

   1.  Choose **Create stack** to deploy the stack.

### (Optional) Deploy to an existing VPC
<a name="optional-deploy-to-an-existing-vpc"></a>

 If your VPC is created outside your CDK app, you can use the configuration `importVpcDetails` to import your existing VPC to be used for this solution. The solution will leverage the CDK’s `Vpc.fromVpcAttributes` way to import VPCs. There are three requisites to import existing VPCs.
+  Every subnet group in the VPC must have a subnet in each availability zone (AZ) (for example, each AZ must have both a public and private subnet). Asymmetric VPCs are not supported.
+  Public subnet requires an NAT gateway so that services in private subnet can use a certain AWS service. For example, AWS Network Firewall.
+ All configuration parameters `vpcId`, `availabilityZones`, `publicSubnetIds`, `privateSubnetIds`, `vpcCidrBlock` must either be known at synthesis time, or they must come from deploy-time list parameters whose deploy-time lengths are known at synthesis time. The parameters must also match the target VPC exactly. For the usage of public and private subnets, refer to **[Network configuration](security.md#network-configuration)**.
+  Imported VPC must activate the following VPC endpoints:
  +  EC2
  +  EC2 Message
  +  Lambda
  +  SNS
  +  KMS
  +  CloudWatch
  +  AWS Config
  +  If `enableOpa` is set to `true`, Amazon ECR, ECR Docker, Elastic Load Balancer endpoints are required.

 Example: Using an existing VPC

 Update the configuration in `cdk.context.json`.

```
{
  "networkFirewallRuleGroupNamePattern": "anfwconfig-*",
  "defaultAggregatorName": "org-replicator",
  "apiGatewayType": "edge",
  "enableOpa": false,
  "importVpcDetails”: {
    "vpcId":"vpc-0d2c9296c3b26e396",
    "availabilityZones": ["ap-southeast-2a","ap-southeast-2b"],
    "publicSubnetIds": ["subnet-019358ac809ad81a2","subnet-0fea75ee8255c55d5"],
    "privateSubnetIds": ["subnet-09ec1f4a0336f6431","subnet-009dca942826cf5b1"],
    "vpcCidrBlock": "172.31.0.0/16"
  }
}
```

 To verify all the roles and roles’ access are set up correctly, refer to **[Interaction steps](interaction-steps.md)** to setup a rule bundle and rule, and to test the resolution.
