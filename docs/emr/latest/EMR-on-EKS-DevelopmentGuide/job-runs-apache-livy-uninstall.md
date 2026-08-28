---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs-apache-livy-uninstall.html
---

# Uninstalling Apache Livy with Amazon EMR on EKS
<a name="job-runs-apache-livy-uninstall"></a>

Follow these steps to uninstall Apache Livy.

1. Delete the Livy setup using the names of your namespace and application name. In this example, the application name is `livy-demo` and the namespace is `livy-ns`.

   ```
   helm uninstall {{livy-demo}} -n {{livy-ns}}
   ```

1. When uninstalling, Amazon EMR on EKS deletes the Kubernetes service in Livy, the AWS load balancers, and the target groups that you created during installation. Deleting resources can take a few minutes. Make sure that the resources are deleted before installing Livy on the namespace again.

1. Delete the Spark namespace.

   ```
   kubectl delete namespace spark-ns
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
