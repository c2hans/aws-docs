---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/spark-operator-uninstall.html
---

# Uninstalling the Spark operator for Amazon EMR on EKS
<a name="spark-operator-uninstall"></a>

Use the following steps to uninstall the Spark operator.

1. Delete the Spark operator using the correct namespace. For this example, the namespace is `spark-operator-demo`.

   ```
   helm uninstall spark-operator-demo -n spark-operator
   ```

1. Delete the Spark operator service account:

   ```
   kubectl delete sa emr-containers-sa-spark-operator -n spark-operator
   ```

1. Delete the Spark operator `CustomResourceDefinitions` (CRDs):

   ```
   kubectl delete crd sparkapplications.sparkoperator.k8s.io
   kubectl delete crd scheduledsparkapplications.sparkoperator.k8s.io
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
