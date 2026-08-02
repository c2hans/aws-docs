---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_appsec_deploy_software_programmatically.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC11-BP06 Deploy software programmatically
<a name="sec_appsec_deploy_software_programmatically"></a>

Perform software deployments programmatically where possible. This approach reduces the likelihood that a deployment fails or an unexpected issue is introduced due to human error.

**Desired outcome: **Keeping people away from data is a key principle of building securely in the AWS Cloud. This principle includes how you deploy your software.

 The benefits of not relying on people to deploy software is the greater confidence that what you tested is what gets deployed, and that the deployment is performed consistently every time. The software should not need to be changed to function in different environments. Using the principles of twelve-factor application development, specifically the externalizing of configuration, allows you to deploy the same code to multiple environments without requiring changes. Cryptographically signing software packages is a good way to verify that nothing has changed between environments. The overall outcome of this approach is to reduce risk in your change process and improve the consistency of software releases.

**Common anti-patterns: **
+  Manually deploying software into production.
+  Manually performing changes to software to cater to different environments.

**Benefits of establishing this best practice: **
+  Increased confidence in the software release process.
+  Reduced risk of a failed change impacting business functionality.
+  Increased release cadence due to lower change risk.
+  Automatic rollback capability for unexpected events during deployment.
+  Ability to cryptographically prove that the software that was tested is the software deployed.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Build your AWS account structure to remove persistent human access from environments and use CI/CD tools to perform deployments. Architect your applications so that environment-specific configuration data is obtained from an external source, such as [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html). Sign packages after they have been tested, and validate these signatures during deployment. Configure your CI/CD pipelines to push application code and use canaries to confirm successful deployment. Use tools such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or [AWS CDK](https://aws.amazon.com/cdk/) to define your infrastructure, then use [AWS CodeBuild](https://aws.amazon.com/codebuild/) and [AWS CodePipeline](https://aws.amazon.com/codepipeline/) to perform CI/CD operations.

### Implementation steps
<a name="implementation-steps"></a>
+  Build well-defined CI/CD pipelines to streamline the deployment process.
+  Using [AWS CodeBuild](https://aws.amazon.com/codebuild/) and [AWS Code Pipeline](https://aws.amazon.com/codepipeline/) to provide CI/CD capability makes it simple to integrate security testing into your pipelines.
+  Follow the guidance on separation of environments in the [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) whitepaper.
+  Verify no persistent human access to environments where production workloads are running.
+  Architect your applications to support the externalization of configuration data.
+  Consider deploying using a blue/green deployment model.
+  Implement canaries to validate the successful deployment of software.
+  Use cryptographic tools such as [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) or [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) to sign and verify the software packages that you are deploying.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [SEC11-BP02 Automate testing throughout the development and release lifecycle](sec_appsec_automate_testing_throughout_lifecycle.md)

 **Related documents:**
+  [AWS CI/CD Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/ef1c179d-8097-4f34-8dc3-0e9eb381b6eb/en-US/)
+  [Accelerate deployments on AWS with effective governance](https://aws.amazon.com/blogs/architecture/accelerate-deployments-on-aws-with-effective-governance/)
+  [Automating safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/)
+  [Code signing using AWS Certificate Manager Private CA and AWS Key Management Service asymmetric keys](https://aws.amazon.com/blogs/security/code-signing-aws-certificate-manager-private-ca-aws-key-management-service-asymmetric-keys/)
+  [Code Signing, a Trust and Integrity Control for AWS Lambda](https://aws.amazon.com/blogs/aws/new-code-signing-a-trust-and-integrity-control-for-aws-lambda/)

 **Related videos:**
+  [Hands-off: Automating continuous delivery pipelines at Amazon](https://www.youtube.com/watch?v=ngnMj1zbMPY)

 **Related examples:**
+  [Blue/Green deployments with AWS Fargate](https://catalog.us-east-1.prod.workshops.aws/workshops/954a35ee-c878-4c22-93ce-b30b25918d89/en-US)
