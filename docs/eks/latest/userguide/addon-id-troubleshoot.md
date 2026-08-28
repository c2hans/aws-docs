---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/addon-id-troubleshoot.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Troubleshoot Pod Identities for EKS add-ons
<a name="addon-id-troubleshoot"></a>

If your add-ons are encountering errors while attempting AWS API, SDK, or CLI operations, confirm the following:
+ The Pod Identity Agent is installed in your cluster.
  + For information about how to install the Pod Identity Agent, see [Set up the Amazon EKS Pod Identity Agent](pod-id-agent-setup.md).
+ The Add-on has a valid Pod Identity association.
  + Use the AWS CLI to retrieve the associations for the service account name used by the add-on.

    ```
    aws eks list-pod-identity-associations --cluster-name <cluster-name>
    ```
+ The IAM role has the required trust policy for Pod Identities.
  + Use the AWS CLI to retrieve the trust policy for an add-on.

    ```
    aws iam get-role --role-name <role-name> --query Role.AssumeRolePolicyDocument
    ```
+ The IAM role has the necessary permissions for the add-on.
  + Use AWS CloudTrail to review `AccessDenied` or `UnauthorizedOperation` events.
+ The service account name in the pod identity association matches the service account name used by the add-on.
  + For information about the available add-ons, see [AWS add-ons](workloads-add-ons-available-eks.md).
+ Check configuration of MutatingWebhookConfiguration named `pod-identity-webhook`
  +  `admissionReviewVersions` of the webhook needs to be `v1beta1` and doesn’t work with `v1`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
