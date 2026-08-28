---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-vas-uninstall-operator.html
---

# Uninstall the Amazon EMR on EKS vertical autoscaling operator
<a name="jobruns-vas-uninstall-operator"></a>

If you want to remove the vertical autoscaling operator from your Amazon EKS cluster, use the `cleanup` command with the Operator SDK CLI as shown in the following example. This also deletes upstream dependencies that installed with the operator, such as the Vertical Pod Autoscaler.

```
operator-sdk cleanup emr-dynamic-sizing
```

If there are any running jobs on the cluster when you delete the operator, those jobs continue to run without vertical autoscaling. If you submit jobs on the cluster after you delete the operator, Amazon EMR on EKS will ignore any vertical autoscaling-related parameters that you may have defined during [configuration](jobruns-vas-configure.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
