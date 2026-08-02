---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

Known issue resolution provides instructions to mitigate known errors. If these instructions don’t address your issue, see the [Contact AWS Support](contact-aws-support.md) section for instructions on opening an AWS Support case for this solution.

## Known issue resolution
<a name="known-issue-resolution"></a>

### Failed to upload data in S3 bucket
<a name="failed-to-upload-data-in-s3-bucket"></a>

 **Issue:** Unable to Upload New Data

 **Reason:** For security purposes, data upload permissions to the bucket are restricted to users with the data-admin role. Standard admin users do not have upload privileges.

 **Resolution: **

1. Go to IAM console and find the role that ends with data-admin

1. Switch to the data-admin role in that account

1. Add the required data in S3 transformed bucket

1. Switch back to the main role

1. Run the crawler to index the new data

### Data Science Configuration Deployment Failure
<a name="data-science-configuration-deployment-failure"></a>

 **Issue:** The deployment failed while deploying basic\_datascience configuration

 **Reason:** To set up a data science environment in SageMaker Studio, a unique user profile is needed with a unique name. This profile will grant the user permission to access and launch SageMaker Studio resources.

 **Resolution:** User Profile Name Issues:
+ Modify the user profile name in datascience-team.yaml
+ Please change the <my-own-data-science-profile-name> to something custom that you can identify

```
     userProfiles:
              # The key/name of the user profile should be specified as follows:
              # If the Domain is in SSO auth mode, this should map to an SSO User ID.
              # If in IAM mode, this should map to Session Name portion of the aws:userid variable.
              "<my-own-data-science-profile-name>":
                # Required if the domain is in IAM AuthMode. This is the role
                # from which the user will launch the user profile in Studio.
                # The role's id will be combined with the userid
                # to grant the user access to launch the user profile.
                userRole:
                  id: generated-role-id:data-user
```

### Lake Formation Data Lake Deployment Issues
<a name="lake-formation-data-lake-deployment-issues"></a>

 **Issue:** The following error messages

```
Reading config from /Users/xxx/Documents/MDAA/config/lakeformation_datalake/datascience/datascience-team.yaml.
Error: ENOENT: no such file or directory
```

 **Reason:** LakeFormation expects a datascience.yaml to create datascience related configurations

 **Resolution:**

1. Create a folder named datascience inside lakeformation\_datalake folder

1. Create a file named datascience-team.yaml inside the folder

1. Please add the sample configuration values as below:

```
# List of roles which will be provided admin access to the team resources
dataAdminRoles:
- id: generated-role-id:data-admin

# List of roles which will be provided usage access to the team resources
# Can be either directly referenced Role Arns, Role Arns via SSM Params,
# or generated roles created using the MDAA roles module.
teamUserRoles:
- id: generated-role-id:data-user

# The role which will be used to execute Team SageMaker resources (Studio Domain Apps, SageMaker Jobs/Pipelines, etc)
teamExecutionRole:
id: generated-role-id:team-execution

# The team Studio Domain config
studioDomainConfig:
authMode: IAM
vpcId: "{{context:vpc_id}}"
subnetIds:
- "{{context:subnet_id}}"
notebookSharingPrefix: sagemaker/notebooks/

# List of Studio user profiles which will be created.
userProfiles:
# The key/name of the user profile should be specified as follows:
# If the Domain is in SSO auth mode, this should map to an SSO User ID.
# If in IAM mode, this should map to Session Name portion of the aws:userid variable.
"<my-own-data-science-profile-name>":
# Required if the domain is in IAM AuthMode. This is the role
# from which the user will launch the user profile in Studio.
# The role's id will be combined with the userid
# to grant the user access to launch the user profile.
userRole:
id: generated-role-id:data-user
```

### Failed to resolve context: vpc\_id
<a name="failed-to-resolve-context-vpc_id"></a>

 **Issue:** Encounters the following error message

```
Error: Failed to resolve context: vpc_id
at MdaaConfigRefValueTransformer.parseContext (/Users/xxx/Documents/MDAA/packages/utilities/mdaa-config/lib/config.ts:193:19)
at /Users/xxxx/Documents/MDAA/packages/utilities/mdaa-config/lib/config.ts:165:38
```

 **Reason:** vpc\_id and subnet\_id are needed to create a secure data environment within the vpc

 **Resolution:**

1. Go to `mdaa.yaml` file

1. Please check if you have vpc\_id configured in the file

1. The below values should go after organization in the config file.

1. Please run the deployment again after the values are changed

```
# TODO: Set an appropriate, unique organization name
# Failure to do so may result in global naming conflicts.
organization: trial-datalake-lk
context:
    vpc_id: vpc-00000090000
    subnet_id: subnet-09090909090
```

 **Issue:** Failure in deploying Generative AI Accelerator

Error Message:

```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
[100%] fail: docker build —tag cdkasset-7a1e3989751f91a191cd33edf97f22ef63c06ad34f01895a7af11a3e32e3a97a . exited with error code 1
```

 **Resolution:**
+ Ensure Docker is installed and running
+ Verify Docker daemon is active before deployment
+ Check Docker configuration settings

### Cross-Account Lake Formation Region Issues
<a name="cross-account-lake-formation-region-issues"></a>

 **Issue:** Lake Formation cross-account access fails when regions differ between accounts

 **Reason:** Lake Formation resource links and cross-account permissions require region alignment for proper functionality

 **Resolution:**

1. Ensure Lake Formation settings are configured in the same region across accounts

1. Verify resource links are created in the correct region

1. Check that IAM roles have permissions for the target region

1. Update Lake Formation resource shares to include the correct region

1. Redeploy affected modules after region alignment

### CLI and Configuration Errors
<a name="cli-and-configuration-errors"></a>

 **Issue:** MDAA fails during synth or deploy with error:

```
DuplicateAccountLevelModulesException {
  duplicates: [ [ 'default/default', 'qs-account' ] ],
  message: 'Found account-level modules that will be deployed more than once'
}
```

 **Reason:** Certain MDAA modules (such as `qs-account`, `data-catalog`) are designated as "account-level modules" - they should only be deployed once per AWS account/region combination. This error occurs when the same account-level module is configured in multiple environments that target the same AWS account.

 **Resolution:**

1. Review your `mdaa.yaml` to identify which environments share the same AWS account

1. Ensure account-level modules only appear once per account/region:
   + Define the module in only ONE environment per account, OR
   + Use different AWS accounts for different domains/environments

1. If you need the same functionality in multiple environments on the same account, the module only needs to be deployed once - other environments can reference the shared resources

 **Important Note:**

The `-e` (environment) and `-d` (domain) CLI flags do NOT bypass this validation. MDAA validates the entire configuration file for consistency before any synthesis or deployment begins, regardless of which subset you intend to deploy. This is by design to prevent configuration conflicts.

### VPC Endpoints Deployment with Bedrock Knowledge Base
<a name="vpc-endpoints-deployment-with-bedrock-knowledge-base"></a>

 **Issue:** VPC Endpoints fail to deploy when Bedrock Knowledge Base uses OpenSearch Serverless on different VPCs

 **Reason:** VPC endpoint configuration conflicts when Knowledge Base and OpenSearch Serverless are deployed in separate VPCs

 **Resolution:**

1. Ensure Bedrock Knowledge Base and OpenSearch Serverless are in the same VPC

1. If separate VPCs are required, configure VPC peering:
   + Create VPC peering connection between the VPCs
   + Update route tables to allow traffic between VPCs
   + Update security groups to allow necessary traffic

1. Verify VPC endpoint service names are correct for your region

1. Check that subnet configurations allow VPC endpoint creation

 **Alternative Approach:**
+ Deploy Knowledge Base and OpenSearch Serverless in the same VPC
+ Use private subnets for both services
+ Configure security groups to allow communication between services

 **Additional Notes:** \* Ensure you’re using the latest version for automatic resolution

### Lambda `python3.13` runtime rejected after upgrade to 1.7.0
<a name="lambda-python3-13-runtime-rejected-after-upgrade-to-1-7-0"></a>

 **Issue:** After upgrading to MDAA 1.7.0, CloudFormation deploys fail on Lambda functions with an error indicating that the `python3.13` runtime is not supported.

 **Reason:** MDAA 1.7.0 upgrades `aws-cdk-lib` from 2.192.0 to 2.258.0. This CDK version removed the `Runtime.PYTHON_3_13` enum value and replaced it with `Runtime.PYTHON_3_14`. Any MDAA config that specifies `python3.13` as a Lambda runtime fails at synth or deploy time.

 **Resolution:**

1. Search your MDAA configs for `python3.13` (Lambda function runtime, layer runtime, and DataOps Lambda runtime fields).

1. Replace with one of:
   +  `python3.13t` — the thread-based Python 3.13 runtime, which is still supported
   +  `python3.14` — the latest Python runtime
   + Another supported runtime for your use case

1. Redeploy with `npx @aws-mdaa/cli deploy -c ./mdaa.yaml`.

### AgentCore Runtime dataProtection config keys silently ignored
<a name="agentcore-runtime-dataprotection-config-keys-silently-ignored"></a>

 **Issue:** After upgrading to 1.7.0, AgentCore Runtime modules still deploy but the `dataProtection.enabled` or `dataProtection.identifiers` fields in the configuration appear to have no effect.

 **Reason:** MDAA 1.7.0 replaced the previous opt-in AgentCore data protection configuration (`dataProtection.enabled` and `dataProtection.identifiers`) with a mandatory built-in baseline. Data protection is now always applied to service-created runtime log groups (customer-managed KMS encryption and a comprehensive PII masking baseline). The identifier list cannot be narrowed. Existing configs using the old keys are silently ignored.

 **Resolution:**

1. Remove the deprecated `dataProtection.enabled` and `dataProtection.identifiers` fields from your AgentCore Runtime module configs.

1. If you need to mask additional AWS-managed data identifiers on top of the built-in set, use `dataProtection.additionalIdentifiers` (additive only).

1. Redeploy. On next deploy, existing AgentCore runtimes gain a new KMS key, a Data Protection policy, and a log-protection custom resource.

### DataZone `AlreadyExists` on concurrent `CfnOwner` creation
<a name="datazone-alreadyexists-on-concurrent-cfnowner-creation"></a>

 **Issue:** Deployments to a DataZone domain occasionally fail with `Transaction cancelled …​ ConditionalCheckFailed …​ AlreadyExists` on `AWS::DataZone::Owner` resources.

 **Reason:** Concurrent creation of `AWS::DataZone::Owner` resources targeting the same domain unit triggers DynamoDB transaction collisions.

 **Resolution:**
+ This is fixed in MDAA 1.7.0 by chaining `CfnOwner` resources on the same domain unit sequentially via CloudFormation `DependsOn`. If you are on 1.6.0 or earlier, retry the deployment or upgrade to 1.7.0 to eliminate the race. Owners on different domain units continue to be created in parallel.

### SageMaker Studio Domain `resource already exists` on mutable-settings update
<a name="sagemaker-studio-domain-resource-already-exists-on-mutable-settings-update"></a>

 **Issue:** Updates to a SageMaker Studio Domain fail with a `resource already exists` error even when the change is limited to mutable settings such as default user settings or domain settings.

 **Reason:** Prior to MDAA 1.7.0, the domain handler would attempt to create the domain instead of updating it when only mutable settings changed.

 **Resolution:**
+ This is fixed in MDAA 1.7.0. Upgrade to 1.7.0 and redeploy.
+ Note: changing immutable properties (`AuthMode`, `DomainName`, `KmsKeyId`, `VpcId`) still requires manual domain recreation.
