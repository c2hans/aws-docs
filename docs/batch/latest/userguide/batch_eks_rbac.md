---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/batch_eks_rbac.html
---

# RBAC permissions or bindings aren't configured properly
<a name="batch_eks_rbac"></a>

If you experience any RBAC permissions or binding issues, verify that the `aws-batch` Kubernetes role can access the Kubernetes namespace:

```
$ kubectl get namespace {{namespace}} --as=aws-batch
```

```
$ kubectl auth can-i get ns --as=aws-batch
```

You can also use the **kubectl describe** command to view the authorizations for a cluster role or Kubernetes namespace.

```
$ kubectl describe clusterrole {{aws-batch-cluster-role}}
```

The following is example output.

```
Name:         aws-batch-cluster-role
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources                                      Non-Resource URLs  Resource Names  Verbs
  ---------                                      -----------------  --------------  -----
  configmaps                                     []                 []              [get list watch]
  nodes                                          []                 []              [get list watch]
  pods                                           []                 []              [get list watch]
  daemonsets.apps                                []                 []              [get list watch]
  deployments.apps                               []                 []              [get list watch]
  replicasets.apps                               []                 []              [get list watch]
  statefulsets.apps                              []                 []              [get list watch]
  clusterrolebindings.rbac.authorization.k8s.io  []                 []              [get list]
  clusterroles.rbac.authorization.k8s.io         []                 []              [get list]
  namespaces                                     []                 []              [get]
  events                                         []                 []              [list]
```

```
$ kubectl describe role {{aws-batch-compute-environment-role}} -n {{my-aws-batch-namespace}}
```

The following is example output.

```
Name:         aws-batch-compute-environment-role
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources                               Non-Resource URLs  Resource Names  Verbs
  ---------                               -----------------  --------------  -----
  pods                                    []                 []              [create get list watch delete patch]
  serviceaccounts                         []                 []              [get list]
  rolebindings.rbac.authorization.k8s.io  []                 []              [get list]
  roles.rbac.authorization.k8s.io         []                 []              [get list]
```

To resolve this issue, re-apply the RBAC permissions and `rolebinding` commands. For more information, see [Step 2: Prepare your Amazon EKS cluster for AWS Batch](getting-started-eks.md#getting-started-eks-step-1).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
