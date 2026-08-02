---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

Known issue resolution provides instructions to mitigate known errors. If these instructions don’t address your issue, see the [Contact AWS Support](contact-aws-support.md) section for instructions on opening an AWS Support case for this solution.

## Known issue resolution
<a name="known-issue-resolution"></a>

During the deployment of Workload Discovery on AWS and in the post-deployment phase, several common configuration errors can occur:

**Note**
To help make it easier to troubleshoot, we recommend disabling the rollback on failure feature in the AWS CloudFormation template. You can also find additional troubleshooting help in the Workload Discovery on AWS [post-deployment configuration documentation](https://aws-solutions.github.io/workload-discovery-on-aws/workload-discovery-on-aws/2.0/index.html).

### Config Delivery Channel Error
<a name="config-delivery-channel-error"></a>

 **Issue:** The following error occurs when deploying the main AWS CloudFormation template:

```
Failed to put delivery channel '<stack-name>-DiscoveryImport-<ID-string>-DeliveryChannel-<ID-string>' because the maximum number of delivery channels: 1 is reached. (Service: AmazonConfig; Status Code: 400; Error Code: MaxNumberOfDeliveryChannelsExceededException; Request ID: 4edc54bc-8c85-4925-b99d-7ef9c73215b3; Proxy: null)
```

 **Reason:** Solution is being deployed to a region that already has AWS Config enabled.

 **Resolution: **Follow the instructions in the [pre-requisites section](https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/prerequisites.html#verify-your-aws-config-details-in-your-account) and deploy the solution with the CloudFormation parameter **AlreadyHaveConfigSetup** set to `Yes`.

### Search Resolver Stack Deployment Times Out When Deploying To Existing VPC
<a name="search-resolver-stack-deployment-times-out-existing-vpc"></a>

 **Issue:** Nested stack that provisions a custom resource to create an index in the OpenSearch cluster times out with the following error:

```
Embedded stack arn:aws:cloudformation:<region>::stack/<stack-name>-SearchResolversStack-<ID-string>/<guid> was not successfullycreated: Stack creation time exceeded the specified timeout
```

 **Reason:** The private subnets provided as CloudFormation parameters do not have the ability to route to S3 (custom resources must write the result of their execution to an S3 bucket using a presigned URL). There are generally two reasons for this:

1. The private subnets do not have NAT gateways associated with them so there is no access to the internet.

1. The private subnet is using VPC endpoints instead of a NAT gateway and the S3 gateway endpoint is not configured correctly.

 **Resolution:**

1. Provision NAT gateways in the VPC to allow tasks running in private subnets to access the internet, either using CloudFormation or the AWS CLI as per the [documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-api-cli).

1. Ensure that the route tables for the subnets have been updated for the S3 VPC endpoint as per the [documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3).

### Resources Not Discovered After Account Has Been Imported
<a name="resources-not-discovered-after-account-imported"></a>

 **Issue:** Accounts have been imported through the Web UI but no resources appear to be discovered after the discovery process has run.

#### Global resources template not deployed
<a name="global-resource-template-not-deployed"></a>

 **Reason:** When the **CrossAccountDiscovery** CloudFormation parameter is set to `SELF_MANAGED`, the global resources CloudFormation template has not been deployed.

 **Resolution:** Deploy the global resources template in the required accounts, as per the [documentation](https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/import-a-region.html#deploy-the-aws-cloudformation-templates).

#### StackSet deployment error
<a name="stackset-deployment-error-org-mode"></a>

 **Reason:** When the **CrossAccountDiscovery** CloudFormation parameter is set to `AWS_ORGANIZATIONS`: one or more accounts is not discovered and the **Role Status** column has **Not Deployed** entries. This means there has been a problem with the automated deployment of the global resources template using StackSets.

 **Resolution:** Go to the **WdGlobalResources** StackSet in the region that Workload Discovery has been deployed to and check the errors in the stack instances that have failed to deploy:

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. From the navigation menu, select **StackSets**.

1. Select the **Service-managed** tab.

1. In the search bar, search for `WdGlobalResources`.

1. Choose `WdGlobalResources` from the search results.

1. Select the **Stack Instances** tab.

1. Inspect the **Detailed status** column for any errors.

#### Discovery ECS task out of memory
<a name="discovery-ecs-task-out-of-memory"></a>

 **Reason:** The discovery process ECS task is running out of memory. This can happen when importing a large number of accounts or resources. The **Last Discovered** column in the UI will display **Not Discovered** or have a value larger than the one specified in the **DiscoveryTaskFrequency** CloudFormation parameter (the default value is 15 minutes). There will be an out of memory error in the ECS console. To verify, follow these steps:

1. Sign in to the [Amazon Elastic Container Service console](https://console.aws.amazon.com/ecs/home).

1. Select the cluster named workload-discovery-cluster.

1. Choose the Tasks tab.

1. Select the Stopped button in the Desired task status panel.

1. In the **Last Status** column check for the error message `OutOfMemoryError: Container killed due to memory usage`.

 **Resolution:** Update the **Memory** CloudFormation parameter to a larger value: start with double and keep increasing until the error stops.

**Note**
Only certain combination of CPU units and memory values are valid so you may have to update the **CpuUnits** CloudFormation parameter as well. The full list of combinations is listed in the [ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-cpu-memory-error.html).

### Gremlin Lambda times out when connecting to AWS Neptune
<a name="gremlin-lambda-times-out"></a>

 **Issue:** GraphQL queries backed by the `<stack-name>-GremlinResol-GremlinAppSyncFunction-<ID-string>` lambda function timeout when attempting to connect to the AWS Neptune database.

 **Reason:** The VPC that the database is running has a custom DNS configuration.

 **Resolution:** Update the security group associated with the `<stack-name>-GremlinResol-GremlinAppSyncFunction-<ID-string>` lambda function to open port 53 for the UDP protocol.

### Unable to access Elastic Container Registry
<a name="unable-to-access-elastic-container-registry"></a>

 **Issue:** When the scheduled Amazon ECS task on Fargate is launched, the task fails with the following error:

```
ResourceInitializationError: unable to pull secrets or registry auth: execution resource retrieval failed: unable to retrieve ecr registry auth
```

 **Reason:** The ECS task is is running in a VPC that does not have a route to the to the ECR API endpoint.

 **Resolution:** Add a VPC endpoint for the `com.amazonaws.<region>.ecr.api` route as per [the ECR documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html#ecr-setting-up-vpc-create).

### Unable to pull container from Elastic Container Registry
<a name="cannot-pull-container-from-registry"></a>

 **Issue:** When the scheduled Amazon ECS task on Fargate is launched, the task fails with the following error:

```
CannotPullContainerFromRegistry: There is a connection issue between the task and Amazon ECR. Check your task network configuration
```

 **Reason:** The ECS task is is running in a VPC that does not have a route to the ECR Docker endpoint.

 **Resolution:** Add a VPC endpoint for the ``com.amazonaws.<region>.ecr.dkr` route as per [the ECR documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html#ecr-setting-up-vpc-create).

### Only Non-AWS Config Resources Are Being Discovered In Specific Accounts
<a name="only-aws-config-resources-being-discovered-in-specific-accounts"></a>

 **Issue:** The only resource types that the solution discovers are the ones listed in the table on the [Supported resources](https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/supported-resources-1.html) section.

#### Regional resources template not deployed
<a name="regional-resource-template-not-deployed"></a>

 **Reason: ** When the **CrossAccountDiscovery** CloudFormation parameter is set to `SELF_MANAGED`, the regional resources CloudFormation template has not been deployed in the regions of each account to be discovered.

 **Resolution:** Deploy the regional resources templates in the required accounts, as per the [documentation](https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/import-a-region.html#deploy-the-aws-cloudformation-templates).

#### Regional resources template deployed incorrectly
<a name="regional-resource-template-deployed-incorrectly"></a>

 **Reason:** When the **CrossAccountDiscovery** CloudFormation parameter is set to `SELF_MANAGED`, the regional resources CloudFormation template has been deployed in the regions of a number of accounts that did not have Config enabled but the CloudFormation parameter **AlreadyHaveConfigSetup** was erroneously set to `Yes`.

 **Resolution:** Delete the previous deployed regional resources stack (AWS Config will be in an inconsistent state otherwise) and re-deploy with the CloudFormation parameter **AlreadyHaveConfigSetup** set to `No`.

#### Config not enabled in required regions
<a name="aws-org-config-not-enabled-in-regions"></a>

 **Reason:** When the **CrossAccountDiscovery** CloudFormation parameter is set to `AWS_ORGANIZATIONS`, AWS Config is not enabled in the regions of each account to be discovered. In `AWS_ORGANIZATIONS` mode, you are responsible for enabling Config as per your organization’s policies.

 **Resolution:** Enable AWS Config in the regions of each account to be discovered.
