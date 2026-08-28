---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-kubernetes-operator-uninstall.html
---

# Uninstalling the Flink Kubernetes operator for Amazon EMR on EKS
<a name="jobruns-flink-kubernetes-operator-uninstall"></a>

Follow these steps to uninstall the Flink Kubernetes operator.

1. Delete the operator.

   ```
   helm uninstall flink-kubernetes-operator -n <NAMESPACE>
   ```

1. Delete Kubernetes resources that Helm doesn’t uninstall.

   ```
   kubectl delete serviceaccounts, roles, rolebindings -l emr-containers.amazonaws.com/component=flink.operator --namespace <namespace>
   kubectl delete crd flinkdeployments.flink.apache.org flinksessionjobs.flink.apache.org
   ```

1. (Optional) Delete the cert-manager.

   ```
   kubectl delete -f https://github.com/jetstack/cert-manager/releases/download/v1.12.0/cert-manager.yaml
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
