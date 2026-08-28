---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/trustedidentitypropagation-emr-serverless.html
---

# Connect your Studio JupyterLab notebooks to EMR Serverless with trusted identity propagation enabled
<a name="trustedidentitypropagation-emr-serverless"></a>

Amazon EMR Serverless provides a serverless option for running Apache Spark and Apache Hive applications without managing clusters. When integrated with trusted identity propagation, EMR Serverless automatically scales compute resources while maintaining your identity context for access control and auditing. This approach eliminates the operational overhead of cluster management while preserving the security benefits of identity-based access control. The following section provides information on how to connect your trusted identity propagation enabled Studio with the EMR Serverless.

To connect Studio to Amazon EMR Serverless with trusted identity propagation enabled, ensure you have completed the following setups:
+  [Setting up trusted identity propagation for Studio](trustedidentitypropagation-setup.md)
+  [Trusted identity propagation with EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-service-trusted-prop.html)
+  [Enable communications between Studio and EMR Serverless](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-serverless.html)

 **Connect to the EMR Serverless application**

For a full list of options on how to connect your JupyterLab notebook to EMR Serverless, see [Connect to an EMR Serverless application](https://docs.aws.amazon.com/sagemaker/latest/dg/connect-emr-serverless-application.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
