---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/test-failures-eks.html
---

# AWS FIS experiment failures while testing Kubernetes pods running in your Amazon Elastic Kubernetes Service clusters
<a name="test-failures-eks"></a>

The following are common Amazon Elastic Kubernetes Service (Amazon EKS) failures encountered while testing Kubernetes pods running in your Amazon EKS clusters:
+ Incorrect configuration of IAM roles for AWS FIS experiments or the Kubernetes service account.
  + **Failure messages:**
    + `Error resolving targets. Kubernetes API returned ApiException with error code 401`.
    + `Error resolving targets. Kubernetes API returned ApiException with error code 403`.
    + `Unable to inject AWS FIS Pod: Kubernetes API returned status code 403. Check Amazon EKS logs for more details`.
  + **Remediation:** Verify the following.
    + Ensure that you have followed the instruction in [Use the AWS FIS`aws:eks:pod` actions](https://docs.aws.amazon.com/fis/latest/userguide/eks-pod-actions.html).
    + Ensure that you have created and configured a Kubernetes Service Account with the necessary RBAC permissions and the correct namespace.
    + Ensure that you have mapped the provided IAM role (see the output of the CloudFormation stack of the test) to the Kubernetes user.
+ Unable to start AWS FIS Pod: Max failed sidecar containers reached. This usually happens when the memory is not sufficient to run the AWS FIS sidecar container.
  + **Failure message:** `Unable to heartbeat FIS Pod: Max failed sidecar containers reached`.
  + **Remediation:** One option to avoid this error is to reduce the target load percentage to be aligned with the available memory or CPU.
+ Alarm assertion failed at the beginning of the experiment. This error occurs because the related alarm has no datapoint.
  + **Failure message:** `Assertion failed for the following alarms`. Lists all the alarms for which the assertion has failed.
  + **Remediation:** Ensure that Container Insights are correctly installed for the alarms and the alarm is not turned on (in `ALARM` state).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
