---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/jobruns-flink-native-kubernetes-security-requirements.html
---

# Flink JobManager service account security requirements for Native Kubernetes
<a name="jobruns-flink-native-kubernetes-security-requirements"></a>

The Flink JobManager pod uses a Kubernetes service account to access the Kubernetes API server to create and watch TaskManager pods. The JobManager service account must have appropriate permissions to create/delete TaskManager pods and allow the TaskManager to watch leader ConfigMaps to retrieve the address of JobManager and ResourceManager in your cluster.

The following rules apply to this service account.

```
rules:
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - "*"
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - "*"
- apiGroups:
  - ""
  resources:
  - configmaps
  verbs:
  - "*"
- apiGroups:
  - "apps"
  resources:
  - deployments
  verbs:
  - "*"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
