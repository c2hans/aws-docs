---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-eksaccessentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment EksAccessEntry
<a name="aws-properties-batch-computeenvironment-eksaccessentry"></a>

Configures whether AWS Batch manages an Amazon EKS access entry on the cluster for the compute environment. For information on how the fields interact with the cluster's `authenticationMode` and with other compute environments that share the cluster, see [Amazon EKS access entry authentication](https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html) in the *AWS Batch User Guide*.

**Note**
Setting `desiredState=ENABLED` on a single compute environment does not guarantee that AWS Batch creates an access entry, and setting `desiredState=DISABLED` on a single compute environment does not guarantee that AWS Batch deletes one. AWS Batch compares the `desiredState` across all compute environments that target the same cluster. The AWS Batch-managed access entry is created only when all compute environments have `desiredState=ENABLED`, and deleted only when all have `desiredState=DISABLED`. If you have multiple compute environments on the same cluster, set `desiredState` consistently across all of them to avoid uncertainty. For more information, see [Reconciling desiredState across compute environments](https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html#eks-access-entries-reconciliation) in the *AWS Batch User Guide*.

## Syntax
<a name="aws-properties-batch-computeenvironment-eksaccessentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-eksaccessentry-syntax.json"></a>

```
{
  "[DesiredState](#cfn-batch-computeenvironment-eksaccessentry-desiredstate)" : {{String}},
  "[Status](#cfn-batch-computeenvironment-eksaccessentry-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-eksaccessentry-syntax.yaml"></a>

```
  [DesiredState](#cfn-batch-computeenvironment-eksaccessentry-desiredstate): {{String}}
  [Status](#cfn-batch-computeenvironment-eksaccessentry-status): {{String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-eksaccessentry-properties"></a>

`DesiredState`  <a name="cfn-batch-computeenvironment-eksaccessentry-desiredstate"></a>
The desired access entry state for the compute environment. When omitted in a AWS CloudFormation template, AWS Batch applies `INHERIT_FROM_CLUSTER` as the default value. Valid values:
ENABLED
AWS Batch manages an access entry on the cluster for the compute environment.
DISABLED
AWS Batch deletes the AWS Batch-managed access entry for the cluster. This value is rejected if the cluster's `authenticationMode` is `API`, because such a cluster doesn't support the `aws-auth` ConfigMap.
INHERIT\_FROM\_CLUSTER
AWS Batch defers to the cluster's current access entry `status`. On a cluster whose authentication mode is `API`, AWS Batch creates and manages an access entry. On a cluster whose authentication mode is `API_AND_CONFIG_MAP` or `CONFIG_MAP`, AWS Batch neither adds nor removes an access entry.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED | INHERIT_FROM_CLUSTER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-batch-computeenvironment-eksaccessentry-status"></a>
The observed state of the access entry on the cluster. `ACTIVE` means that an access entry for the compute environment exists on the cluster and takes precedence over the `aws-auth` ConfigMap. `INACTIVE` means that no AWS Batch-managed access entry is present.
This field is read-only and only appears in the [DescribeComputeEnvironments](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeComputeEnvironments.html) response.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | INACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
