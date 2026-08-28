---
source_url: https://docs.aws.amazon.com/eks/latest/eksctl/iam-identity-mappings.html
---

# Manage IAM users and roles
<a name="iam-identity-mappings"></a>

**Note**
AWS suggests migraitng to [EKS Pod Identity Associations](pod-identity-associations.md) from the `aws-auth` ConfigMap.

EKS clusters use IAM users and roles to control access to the cluster. The rules are implemented in a config map

## Edit ConfigMap with a CLI Command
<a name="_edit_configmap_with_a_cli_command"></a>

called `aws-auth`. `eksctl` provides commands to read and edit this config map.

 **Get all identity mappings:**

```
eksctl get iamidentitymapping --cluster <clusterName> --region=<region>
```

 **Get all identity mappings matching an arn:**

```
eksctl get iamidentitymapping --cluster <clusterName> --region=<region> --arn arn:aws:iam::123456:role/testing-role
```

 **Create an identity mapping:**

```
 eksctl create iamidentitymapping --cluster  <clusterName> --region=<region> --arn arn:aws:iam::123456:role/testing --group system:masters --username admin
```

 **Delete an identity mapping:**

```
eksctl delete iamidentitymapping --cluster  <clusterName> --region=<region> --arn arn:aws:iam::123456:role/testing
```

**Note**
Above command deletes a single mapping FIFO unless `--all` is given in which case it removes all matching. Will warn if more mappings matching this role are found.

 **Create an account mapping:**

```
 eksctl create iamidentitymapping --cluster  <clusterName> --region=<region> --account user-account
```

 **Delete an account mapping:**

```
 eksctl delete iamidentitymapping --cluster  <clusterName> --region=<region> --account user-account
```

## Edit ConfigMap using a ClusterConfig file
<a name="_edit_configmap_using_a_clusterconfig_file"></a>

The identity mappings can also be specified in ClusterConfig:

```
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: cluster-with-iamidentitymappings
  region: us-east-1

iamIdentityMappings:
  - arn: arn:aws:iam::000000000000:role/myAdminRole
    groups:
      - system:masters
    username: admin
    noDuplicateARNs: true # prevents shadowing of ARNs

  - arn: arn:aws:iam::000000000000:user/myUser
    username: myUser
    noDuplicateARNs: true # prevents shadowing of ARNs

  - serviceName: emr-containers
    namespace: emr # serviceName requires namespace

  - account: "000000000000" # account must be configured with no other options

nodeGroups:
  - name: ng-1
    instanceType: m5.large
    desiredCapacity: 1
```

```
 eksctl create iamidentitymapping -f cluster-with-iamidentitymappings.yaml
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
