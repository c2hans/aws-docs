---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/sec_appsec_regularly_assess_security_properties_of_pipelines.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC11-BP07 Regularly assess security properties of the pipelines
<a name="sec_appsec_regularly_assess_security_properties_of_pipelines"></a>

 Apply the principles of the Well-Architected Security Pillar to your pipelines, with particular attention to the separation of permissions. Regularly assess the security properties of your pipeline infrastructure. Effectively managing the security *of* the pipelines allows you to deliver the security of the software that passes *through* the pipelines.

**Desired outcome: **The pipelines used to build and deploy your software should follow the same recommended practices as any other workload in your environment. The tests that are implemented in the pipelines should not be editable by the builders who are using them. The pipelines should only have the permissions needed for the deployments they are doing and should implement safeguards to avoid deploying to the wrong environments. Pipelines should not rely on long-term credentials, and should be configured to emit state so that the integrity of the build environments can be validated.

**Common anti-patterns:**
+  Security tests that can be bypassed by builders.
+  Overly broad permissions for deployment pipelines.
+  Pipelines not being configured to validate inputs.
+  Not regularly reviewing the permissions associated with your CI/CD infrastructure.
+  Use of long-term or hardcoded credentials.

**Benefits of establishing this best practice:**
+  Greater confidence in the integrity of the software that is built and deployed through the pipelines.
+  Ability to stop a deployment when there is suspicious activity.

** Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Starting with managed CI/CD services that support IAM roles reduces the risk of credential leakage. Applying the Security Pillar principles to your CI/CD pipeline infrastructure can help you determine where security improvements can be made. Following the [AWS Deployment Pipelines Reference Architecture](https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/) is a good starting point for building your CI/CD environments. Regularly reviewing the pipeline implementation and analyzing logs for unexpected behavior can help you understand the usage patterns of the pipelines being used to deploy software.

### Implementation steps
<a name="implementation-steps"></a>
+  Start with the [AWS Deployment Pipelines Reference Architecture](https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/).
+  Consider using [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to programmatically generate least privilege IAM policies for the pipelines.
+  Integrate your pipelines with monitoring and alerting so that you are notified of unexpected or abnormal activity, for AWS managed services [Amazon EventBridge](https://aws.amazon.com/eventbridge/) allows you to route data to targets such as [AWS Lambda](https://aws.amazon.com/lambda/) or [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS).

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Deployment Pipelines Reference Architecture](https://aws.amazon.com/blogs/aws/new_deployment_pipelines_reference_architecture_and_-reference_implementations/)
+  [Monitoring AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/monitoring.html)
+  [Security best practices for AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-best-practices.html)

 **Related examples:**
+  [DevOps monitoring dashboard](https://github.com/aws-solutions/aws-devops-monitoring-dashboard) (GitHub)
