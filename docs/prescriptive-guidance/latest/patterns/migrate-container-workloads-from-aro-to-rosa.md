---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-container-workloads-from-aro-to-rosa.html
---

# Migrate your container workloads from Azure Red Hat OpenShift (ARO) to Red Hat OpenShift Service on AWS (ROSA)
<a name="migrate-container-workloads-from-aro-to-rosa"></a>

*Naveen Ramasamy, Srikanth Rangavajhala, and Gireesh Sreekantan, Amazon Web Services*

## Summary
<a name="migrate-container-workloads-from-aro-to-rosa-summary"></a>

This pattern provides step-by-step instructions for migrating container workloads from Azure Red Hat OpenShift (ARO) to [Red Hat OpenShift Service on AWS (ROSA)](https://aws.amazon.com/rosa/). ROSA is a managed Kubernetes service provided by Red Hat in collaboration with AWS. It helps you deploy, manage, and scale your containerized applications by using the Kubernetes platform, and benefits from both Red Hat's expertise in Kubernetes and the AWS Cloud infrastructure.

Migrating container workloads from ARO, from other clouds, or from on premises to ROSA involves transferring applications, configurations, and data from one platform to another. This pattern helps ensure a smooth transition while optimizing for AWS Cloud services, security, and cost efficiency. It covers two methods for migrating your workloads to ROSA clusters: CI/CD and Migration Toolkit for Containers (MTC).

This pattern covers both methods. The method you choose depends on the complexity and certainty of your migration process. If you have full control over your application's state and can guarantee a consistent setup through a pipeline, we recommend that you use the CI/CD method. However, if your application state involves uncertainties, unforeseen changes, or a complex ecosystem, we recommend that you use MTC as a reliable and controlled path to migrate your application and its data to a new cluster. For a detailed comparison of the two methods, see the [Additional information](#migrate-container-workloads-from-aro-to-rosa-additional) section.

Benefits of migrating to ROSA:
+ ROSA seamlessly integrates with AWS as a native service. It is easily accessible through the AWS Management Console and billed through a single AWS account. It offers full compatibility with other AWS services and provides collaborative support from both AWS and Red Hat.
+ ROSA supports hybrid and multi-cloud deployments. It enables applications to run consistently across on-premises data centers and multiple cloud environments.
+ ROSA benefits from Red Hat's security focus, and provides features such as role-based access control (RBAC), image scanning, and vulnerability assessments to ensure a secure container environment.
+ ROSA is designed to scale applications easily and provides high availability options. It allows applications to grow as needed while maintaining reliability.
+ ROSA automates and simplifies the deployment of a Kubernetes cluster compared with manual setup and management methods. This accelerates the development and deployment process.
+ ROSA benefits from AWS Cloud services, and provides seamless integration with AWS offerings such as database services, storage solutions, and security services.

## Prerequisites and limitations
<a name="migrate-container-workloads-from-aro-to-rosa-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ Permissions configured for AWS services that ROSA relies on to deliver functionality. For more information, see [Prerequisites](https://docs.aws.amazon.com/rosa/latest/userguide/set-up.html) in the ROSA documentation.
+ ROSA enabled on the [ROSA console](https://console.aws.amazon.com/rosa). For instructions, see the [ROSA documentation](https://docs.aws.amazon.com/rosa/latest/userguide/set-up.html#enable-rosa).
+ The ROSA cluster installed and configured. For more information, see [Get started with ROSA](https://docs.aws.amazon.com/rosa/latest/userguide/getting-started.html)  in the ROSA documentation. To understand the different methods for setting up a ROSA cluster, see the AWS Prescriptive Guidance guide [ROSA implementation strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/).
+ Network connectivity established from the on-premises network to AWS through [AWS Direct Connect](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html) (preferred) or [AWS Virtual Private Network (Site-to-Site VPN)](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html).
+ An Amazon Elastic Compute Cloud (Amazon EC2) instance or another virtual server to install tools such as `aws client`, OpenShift CLI (`oc`) client, ROSA client, and Git binary.

Additional prerequisites for the CI/CD method:
+ Access to the on-premises Jenkins server with permissions to create a new pipeline, add stages, add OpenShift clusters, and perform builds.
+ Access to the Git repository where application source code is maintained, with permissions to create a new Git branch and perform commits to the new branch.

Additional prerequisites for the MTC method:
+ An Amazon Simple Storage Service (Amazon S3) bucket, which will be used as a replication repository.
+ Administrative access to the source ARO cluster. This is required to set up the MTC connection.

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="migrate-container-workloads-from-aro-to-rosa-architecture"></a>

ROSA provides three network deployment patterns: public, private, and [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html). PrivateLink enables Red Hat site reliability engineering (SRE) teams to manage the cluster by using a private subnet connected to the cluster’s PrivateLink endpoint in an existing VPC.

Choosing the PrivateLink option provides the most secure configuration. For that reason, we recommend it for sensitive workloads or strict compliance requirements. For information about the public and private network deployment options, see the [Red Hat OpenShift documentation](https://docs.openshift.com/rosa/architecture/rosa-architecture-models.html#rosa-hcp-architecture_rosa-architecture-models).

**Important**
You can create a PrivateLink cluster only at installation time. You cannot change a cluster to use PrivateLink after installation.

The following diagram illustrates the PrivateLink architecture for a ROSA cluster that uses Direct Connect to connect to the on-premises and ARO environments.

![ROSA cluster that uses AWS Direct Connect and AWS PrivateLink.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/527cedfb-ec21-42be-bf21-d4e4e4f9db51/images/eff9b017-6fc7-4874-b610-849a42071ef4.png)

**AWS permissions to ROSA**

For AWS permissions to ROSA, we recommend that you use AWS Security Token Service (AWS STS) with short-lived, dynamic tokens. This method uses least-privilege predefined roles and policies to grant ROSA minimal permissions to operate in the AWS account, and supports ROSA installation, control plane, and compute functionality.

**CI/CD pipeline redeployment**

CI/CD pipeline redeployment is the recommended method for users who have a mature CI/CD pipeline. When you choose this option, you can use any [DevOps deployment strategy ](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies.html)to gradually shift your application load to deployments on ROSA.

**Note**
This pattern assumes a common use case where you have an on-premises Git, JFrog Artifactory, and Jenkins pipeline. This approach requires that you establish network connectivity from your on-premises network to AWS through Direct Connect, and that you set up the ROSA cluster before you follow the instructions in the [Epics](#migrate-container-workloads-from-aro-to-rosa-epics) section. See the [Prerequisites](#migrate-container-workloads-from-aro-to-rosa-prereqs) section for details.

The following diagram shows the workflow for this method.

![Migrating containers from ARO to ROSA by using the CI/CD method.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/527cedfb-ec21-42be-bf21-d4e4e4f9db51/images/f658590e-fbd9-4297-a02c-0b516694d436.png)

**MTC method**

You can use the [Migration Toolkit for Containers (MTC)](https://docs.openshift.com/container-platform/4.13/migration_toolkit_for_containers/about-mtc.html)** **to migrate your containerized workloads between different Kubernetes environments, such as from ARO to ROSA. MTC simplifies the migration process by automating several key tasks and providing a comprehensive framework for managing the migration lifecycle.

The following diagram shows the workflow for this method.

![Migrating containers from ARO to ROSA by using the MTC method.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/527cedfb-ec21-42be-bf21-d4e4e4f9db51/images/979bbc7b-2e39-4dd1-b4f0-ea1032880a38.png)

## Tools
<a name="migrate-container-workloads-from-aro-to-rosa-tools"></a>

**AWS services**
+ [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) is an online data transfer and discovery service that helps you move files or object data to, from, and between AWS storage services.
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services while bypassing internet service providers in your network path.
+ [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) helps you create unidirectional, private connections from your virtual private clouds (VPCs) to services outside of the VPC.
+ [Red Hat OpenShift Service on AWS (ROSA)](https://docs.aws.amazon.com/rosa/latest/userguide/what-is-rosa.html) is a managed service that helps Red Hat OpenShift users to build, scale, and manage containerized applications on AWS.
+ [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) helps you request temporary, limited-privilege credentials for users.

**Other tools**
+ [Migration Toolkit for Containers (MTC)](https://docs.openshift.com/container-platform/4.13/migration_toolkit_for_containers/about-mtc.html) provides a console and API for migrating containerized applications from ARO to ROSA.

## Best practices
<a name="migrate-container-workloads-from-aro-to-rosa-best-practices"></a>
+ For [resilience](https://docs.aws.amazon.com/ROSA/latest/userguide/disaster-recovery-resiliency.html) and if you have security compliance workloads, set up a Multi-AZ ROSA cluster that uses PrivateLink. For more information, see the [ROSA documentation](https://docs.aws.amazon.com/rosa/latest/userguide/getting-started-classic-private-link.html).
**Note**
PrivateLink cannot be configured after installation.
+ The S3 bucket that you use for replication repository should not be public. Use the appropriate S3 bucket policies to restrict access.
+ If you choose the MTC method, use the **Stage** migration option to reduce the downtime window during cutover.
+ Review your service quotas before and after you provision the ROSA cluster. If necessary, request a quota increase according to your requirements. For more information, see the [Service Quotas documentation](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).
+ Review the [ROSA security guidelines](https://docs.aws.amazon.com/ROSA/latest/userguide/security.html) and implement security best practices.
+ We recommend that you remove the default cluster administrator after installation. For more information, see the [Red Hat OpenShift documentation](https://docs.openshift.com/container-platform/4.13/post_installation_configuration/cluster-tasks.html).
+ Use machine pool automatic scaling to scale down unused worker nodes in the ROSA cluster to optimize costs. For more information, see the [ROSA Workshop](https://catalog.workshops.aws/aws-openshift-workshop/en-US/5-nodes-storage/3-autoscale-machine-pool).
+ Use the Red Hat Cost Management service for OpenShift Container Platform to better understand and track costs for clouds and containers. For more information, see the [ROSA Workshop](https://catalog.workshops.aws/aws-openshift-workshop/en-US/10-cost-management).
+ Monitor and audit ROSA cluster infrastructure services and applications by using AWS services. For more information, see the [ROSA Workshop](https://catalog.workshops.aws/aws-openshift-workshop/en-US/8-observability).

## Epics
<a name="migrate-container-workloads-from-aro-to-rosa-epics"></a>

### Option 1: Use a CI/CD pipeline
<a name="option-1-use-a-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add the new ROSA cluster to Jenkins. | 1. On the Jenkins console, choose **Manage Jenkins**, **Configure System**.<br />2. On the **Manage Jenkins** page, in the **OpenShift Plug-in** section, choose **Add a new cluster**.<br />3. Provide required information such as the cluster name, API server URL, and token information to authenticate with ROSA. | AWS administrator, AWS systems administrator, AWS DevOps |
| Add the `oc` client to your Jenkins nodes. | 1. On the Jenkins console, choose **Manage Jenkins**, **Global Tool Configuration**.<br />2. In the **OpenShift Client Tools** section, install the OpenShift CLI (`oc`) client version that is the same as your ROSA cluster version. | AWS administrator, AWS systems administrator, AWS DevOps |
| Create a new Git branch. | Create a new branch in your Git repository for `rosa-dev`. This branch separates the code or configuration parameter changes for ROSA from your existing pipeline. | AWS DevOps |
| Tag images for ROSA. | In your build stage, use a different tag to identify the images that are built from the ROSA pipeline. | AWS administrator, AWS systems administrator, AWS DevOps |
| Create a pipeline. | Create a new Jenkins pipeline that's similar to your existing pipeline. For this pipeline, use the `rosa-dev` Git branch that you created earlier, and make sure to include the Git checkout, code scan, and build stages that are identical to your existing pipeline. | AWS administrator, AWS systems administrator, AWS DevOps |
| Add a ROSA deployment stage. | In the new pipeline, add a stage to deploy to the ROSA cluster and reference the ROSA cluster that you added to the Jenkins global configuration. | AWS administrator, AWS DevOps, AWS systems administrator |
| Start a new build. | In Jenkins, select your pipeline and choose **Build now**, or start a new build by committing a change to the `rosa-dev` branch in Git. | AWS administrator, AWS DevOps, AWS systems administrator |
| Verify the deployment. | Use the **oc** command or the [ROSA console](https://console.aws.amazon.com/rosa) to verify that the application has been deployed on your target ROSA cluster. | AWS administrator, AWS DevOps, AWS systems administrator |
| Copy data to the target cluster. | For stateful workloads, copy the data from the source cluster to the target cluster by using AWS DataSync or open source utilities such as **rsync**, or you can use the MTC method. For more information, see the [AWS DataSync documentation](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html). | AWS administrator, AWS DevOps, AWS systems administrator |
| Test your application. | 1. Retrieve the route URL for your application by using the **oc route** command or the [ROSA console](https://console.aws.amazon.com/rosa).<br />2. Test your application by using the route URL. | AWS administrator, AWS DevOps, AWS systems administrator |
| Cut over. | If your testing is successful, use the appropriate Amazon Route 53 policy to move the traffic from the ARO-hosted application to the ROSA-hosted application. When you complete this step, your application's workload will fully transition to the ROSA cluster. | AWS administrator, AWS systems administrator |

### Option 2: Use MTC
<a name="option-2-use-mtc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the MTC operator. | Install the MTC operator on both ARO and ROSA clusters:1. In the ARO or ROSA console, navigate to the **Operators**, **OperatorHub** page.<br />2. In the **Filter by** keyword box, find or type **MTC**.<br />3. Select the MTC operator to display additional information.<br />4. After you read the information about the operator, choose **Install**. | AWS administrator, AWS DevOps, AWS systems administrator |
| Configure network traffic to the replication repository. | If you're using a proxy server, configure it to allow network traffic between the replication repository and the clusters. The replication repository is an intermediate storage object that MTC uses to migrate data. The source and target clusters must have network access to the replication repository during migration. | AWS administrator, AWS DevOps, AWS systems administrator |
| Add the source cluster to MTC. | On the MTC web console, add the ARO source cluster. | AWS administrator, AWS DevOps, AWS systems administrator |
| Add Amazon S3 as your replication repository. | On the MTC web console, add the Amazon S3 bucket (see [Prerequisites](#migrate-container-workloads-from-aro-to-rosa-prereqs)) as the replication repository. | AWS administrator, AWS DevOps, AWS systems administrator |
| Create a migration plan. | On the MTC web console, create a migration plan and specify the data transfer type as **Copy**. This will instruct MTC to copy the data from the source (ARO) cluster to the S3 bucket, and from the bucket to the target (ROSA) cluster. | AWS administrator, AWS DevOps, AWS systems administrator |
| Run the migration plan. | Run the migration plan by using the **Stage** or **Cutover** option:+ Choose **Stage** to copy data to the target cluster without stopping your application. You can run multiple stage migrations to copy most of your data before cutover migration. This shortens the duration of cutover migration.<br />+ Choose **Cutover** to stop your application on the source cluster while moving the resources to the target cluster.<br />To prevent stopping the application, you can clear the** Halt transactions on the source cluster during migration **check box. | AWS administrator, AWS DevOps, AWS systems administrator |

## Troubleshooting
<a name="migrate-container-workloads-from-aro-to-rosa-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Connectivity issues | When you migrate your container workloads from ARO to ROSA, you might encounter connectivity issues that should be resolved to ensure a successful migration. To address these connectivity issues (listed in this table) during migration, meticulous planning, coordination with your network and security teams, and thorough testing are vital. Implementing a gradual migration strategy and verifying connectivity at each step will help minimize potential disruptions and ensure a smooth transition from ARO to ROSA. |
| Network configuration differences | ARO and ROSA might have variations in their network configurations, such as virtual network (VNet) settings, subnets, and network policies. For proper communication between services, make sure that the network settings align between the two platforms. |
| Security group and firewall rules | ROSA and ARO might have different default security group and firewall settings. Make sure to adjust and update these rules to permit necessary traffic to maintain connectivity among containers and services during migration.  |
| IP address and DNS changes | When you migrate workloads, IP addresses and DNS names might change. Reconfigure applications that rely on static IPs or specific DNS names.  |
| External service access | If your application depends on external services such as databases or APIs, you might have to update their connection settings to make sure they can communicate with the new services from ROSA. |
| Azure Private Link configuration | If you use Azure Private Link or private endpoint services in ARO, you will need to set up the equivalent functionality in ROSA to ensure private connectivity between resources. |
| Site-to-Site VPN or Direct Connect setup  | If there are existing Site-to-Site VPN or Direct Connect connections between your on-premises network and ARO, you will need to establish similar connections with ROSA for uninterrupted communication with your local resources. |
| Ingress and load balancer settings | Configurations for ingress controllers and load balancers might differ between ARO and ROSA. Reconfigure these settings to maintain external access to your services. |
| Certificate and TLS handling | If your applications use SSL certificates or TLS, make sure that the certificates are valid and configured correctly in ROSA. |
| Container registry access | If your containers are hosted in an external container registry, set up the proper authentication and access permissions for ROSA. |
| Monitoring and logging | Update monitoring and logging configurations to reflect the new infrastructure on ROSA so you can continue to monitor the health and performance of your containers effectively. |

## Related resources
<a name="migrate-container-workloads-from-aro-to-rosa-resources"></a>

**AWS**** references**
+ [What is Red Hat OpenShift Service on AWS?](https://docs.aws.amazon.com/ROSA/latest/userguide/what-is-rosa.html) (ROSA documentation)
+ [Get started with ROSA](https://docs.aws.amazon.com/ROSA/latest/userguide/getting-started.html) (ROSA documentation)
+ [Red Hat OpenShift Service on AWS implementation strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/red-hat-openshift-on-aws-implementation/) (AWS Prescriptive Guidance)
+ [Red Hat OpenShift Service on AWS Now GA](https://aws.amazon.com/blogs/aws/red-hat-openshift-service-on-aws-now-generally-availably/) (AWS blog post)
+ [ROSA Workshop](https://catalog.workshops.aws/aws-openshift-workshop/en-US/0-introduction)
+ [ROSA FAQ](https://aws.amazon.com/rosa/faqs/)
+ [ROSA Workshop FAQ](https://www.rosaworkshop.io/rosa/14-faq/)
+ [ROSA pricing](https://aws.amazon.com/rosa/pricing/)

**Red Hat OpenShift documentation**
+ [Installing a cluster quickly on AWS](https://docs.openshift.com/container-platform/4.13/installing/installing_aws/installing-aws-default.html)
+ [Installing a cluster on AWS in a restricted network](https://docs.openshift.com/container-platform/4.13/installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.html)
+ [Installing a cluster on AWS into an existing VPC](https://docs.openshift.com/container-platform/4.13/installing/installing_aws/installing-aws-vpc.html)
+ [Installing a cluster on user-provisioned infrastructure in AWS by using CloudFormation templates](https://docs.openshift.com/container-platform/4.13/installing/installing_aws/installing-aws-user-infra.html)
+ [Installing a cluster on AWS in a restricted network with user-provisioned infrastructure](https://docs.openshift.com/container-platform/4.13/installing/installing_aws/installing-restricted-networks-aws.html)
+ [Installing a cluster on AWS with customizations](https://docs.openshift.com/container-platform/4.13/installing/installing_aws/installing-aws-customizations.html)
+ [Getting started with the OpenShift CLI](https://docs.openshift.com/container-platform/4.13/cli_reference/openshift_cli/getting-started-cli.html)

## Additional information
<a name="migrate-container-workloads-from-aro-to-rosa-additional"></a>

**Choosing between MTC and CI/CD pipeline redeployment options**

Migrating applications from one OpenShift cluster to another requires careful consideration. Ideally, you would want a smooth transition by using a CI/CD pipeline to redeploy the application and handle the migration of persistent volume data. However, in practice, a running application on a cluster is susceptible to unforeseen changes over time. These changes can cause the application to gradually deviate from its original deployment state. MTC offers a solution for scenarios where the exact contents of a namespace are uncertain and a seamless migration of all application components to a new cluster is important.

Making the right choice requires evaluating your specific scenario and weighing the benefits of each approach. By doing so, you can ensure a successful and seamless migration that aligns with your needs and priorities. Here are additional guidelines for choosing between the two options.

**CI/CD pipeline redeployment**

The CI/CD pipeline method is the recommended approach if your application can be confidently redeployed by using a pipeline. This ensures that the migration is controlled, predictable, and aligned with your existing deployment practices. When you choose this method, you can use [blue/green deployment](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/bluegreen-deployments.html) or canary deployment strategies to gradually shift the load to deployments on ROSA. For this scenario, this pattern assumes that Jenkins is orchestrating application deployments from the on-premises environment.

Advantages:
+ You do not require administrative access to the source ARO cluster or need to deploy any operators on the source or destination cluster.
+ This approach helps you switch traffic gradually by using a DevOps strategy.

Disadvantages:
+ It requires more effort to test the functionality of your application.
+ If your application contains persistent data, it requires additional steps to copy the data by using AWS DataSync or other tools.

**MTC migration**

In the real world, running applications can undergo unanticipated changes that cause them to drift away from the initial deployment. Choose the MTC option when you're unsure about the current state of your application on the source cluster. For example, if your application ecosystem spans various components, configurations, and data storage volumes, we recommend that you choose MTC to ensure a complete migration that covers the application and its entire environment.

Advantages:
+ MTC provides complete backup and restore of the workload.
+ It will copy the persistent data from source to target while migrating the workload.
+ It does not require access to the source code repository.

Disadvantages:
+ You need administrative privileges to install the MTC operator on the source and destination clusters.
+ The DevOps team requires training to use the MTC tool and perform migrations.
