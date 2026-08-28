---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/prerequisites-for-modernizing-sas-9-to-sas-viya.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Prerequisites for modernizing SAS 9 to SAS Viya
<a name="prerequisites-for-modernizing-sas-9-to-sas-viya"></a>

 The SAS Viya software uses containers to deploy to a Kubernetes cluster. Additionally, the deployment is declarative and is based on a custom manifest that you create by using Kustomize.

 Knowledge of the following is needed to deploy, update, and manage the SAS Viya software:
+  Kubectl commands to perform operations, such as `kubectl apply`, `kubectl taint`, `kubectl label`, and `kubectl logs`
+  Experience with Amazon Elastic Kubernetes Service (Amazon EKS)
+  Depending on the deployment, experience with Kubernetes operator, Docker, or Ansible

 Optionally, SAS also provides a content assessment tool that helps you migrate your environment to SAS Viya. The [content assessment tool](https://blogs.sas.com/content/sgf/2021/07/23/how-to-use-the-sas-9-content-assessment-tool/) provides the inventory of what is in your SAS 9 environment and additionally provides you with details specifically around if your current code will transition to SAS Viya.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
