---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/cdk-deployment.html
---

# CDK deployment
<a name="cdk-deployment"></a>

 In addition to the CloudFormation template, you can also use the CDK project this solution was built on to integrate it into your environment. Review the following considerations to make an informed decision whether to use the CDK deployment model over the default CloudFormation template.
+  With CDK, you can selectively choose which modules and elements needs to be deployed for each new stack you create. While the base module is always deployed, API module, demo website, and auto session revocation are optional and each of the listed components can be turned on or off. However, the CloudFormation template has all the components (except auto session revocation module) integrated within the template, and cannot be turned off.
+  Auto session revocation module is only available when deployed through CDK as an optional module.
+  CDK deployment model makes it easier to manage the configuration inputs when running multiple stacks.

 If you decide that the CDK deployment model is more suitable for your workloads, use the following procedure to launch this solution in your environment.

## Prerequisites
<a name="prerequisites-2"></a>
+  [AWS Command Line Interface](https://aws.amazon.com/cli/)
+  Node.js 12.x or later
+  AWS CDK 2.24.1

## Deployment procedure
<a name="deployment-procedure"></a>

 If you are deploying the solution for the first time using the CDK toolkit, run **cdk bootstrap** to setup the required CDK resources in your AWS account. For more details on using the CDK bootstrapping process, refer to [Bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html).

**Note**
If you're planning on using multiple regions, the bootstrapping process must be done for each AWS region. In case you have gone through the process of installing CDK bootstrap tooling in a given account and region, you can ignore this step.

1.  Clone the solution source code from the repository.

   ```
   git clone https://github.com/aws-solutions/secure-media-delivery-at-the-edge.git
   ```

1.  Install the dependencies of the project to make it ready to use. To do so, run the below commands in the folder where you cloned the source code to.

    **On Linux**

   ```
   cd source
   ```

   ```
   ./install_dependencies.sh
   ```

    **On Windows**

   ```
   cd source
   ```

   ```
   ./install_dependencies.ps1
   ```

1.  Run the built-in wizard which will prompt you with questions about the modules to deploy and the number of parameters which determine the operations of the functional components chosen to be deployed.

   ```
   npm run wizard
   ```

    For more details about the meaning and usage of parameters prompted in the wizard, refer to the [Design considerations](cloudfront-prerequisites.md) and [Session revocation](session-revocation-guide.md) sections.

    The wizard will then generate a configuration in the `solution.context.json` file that is located in the same CDK project directory. This config file stores all the inputs provided through the wizard and can be modified any time you want to choose certain parameters and redeploy the stack.

1.  Deploy the solution in your account.

   ```
   npx cdk deploy --all
   ```

1.  After CDK deployment finishes, follow the steps from 2 to 4 as described in the [Deployment process overview](deploy-the-solution.md#deployment-process-overview) section for CloudFormation.

**Note**
 When running from your local environment, the determination of the target account and region will be based on the AWS profile in use as specified in the config and credentials file. If you want to deploy the stack in multiple accounts and regions, you must define the appropriate profiles associated with the account and right default region that you need. For more information refer to [Specifying credentials and region](https://docs.aws.amazon.com/cdk/v2/guide/cli.html#cli-environment).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
