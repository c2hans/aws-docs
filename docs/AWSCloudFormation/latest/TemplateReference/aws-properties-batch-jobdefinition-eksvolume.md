---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-eksvolume.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EksVolume
<a name="aws-properties-batch-jobdefinition-eksvolume"></a>

Specifies an Amazon EKS volume for a job definition.

## Syntax
<a name="aws-properties-batch-jobdefinition-eksvolume-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-eksvolume-syntax.json"></a>

```
{
  "[EmptyDir](#cfn-batch-jobdefinition-eksvolume-emptydir)" : {{EksEmptyDir}},
  "[HostPath](#cfn-batch-jobdefinition-eksvolume-hostpath)" : {{EksHostPath}},
  "[Name](#cfn-batch-jobdefinition-eksvolume-name)" : {{String}},
  "[PersistentVolumeClaim](#cfn-batch-jobdefinition-eksvolume-persistentvolumeclaim)" : {{EksPersistentVolumeClaim}},
  "[Secret](#cfn-batch-jobdefinition-eksvolume-secret)" : {{EksSecret}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-eksvolume-syntax.yaml"></a>

```
  [EmptyDir](#cfn-batch-jobdefinition-eksvolume-emptydir): {{
    EksEmptyDir}}
  [HostPath](#cfn-batch-jobdefinition-eksvolume-hostpath): {{
    EksHostPath}}
  [Name](#cfn-batch-jobdefinition-eksvolume-name): {{String}}
  [PersistentVolumeClaim](#cfn-batch-jobdefinition-eksvolume-persistentvolumeclaim): {{
    EksPersistentVolumeClaim}}
  [Secret](#cfn-batch-jobdefinition-eksvolume-secret): {{
    EksSecret}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-eksvolume-properties"></a>

`EmptyDir`  <a name="cfn-batch-jobdefinition-eksvolume-emptydir"></a>
Specifies the configuration of a Kubernetes `emptyDir` volume. For more information, see [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) in the *Kubernetes documentation*.
*Required*: No
*Type*: [EksEmptyDir](aws-properties-batch-jobdefinition-eksemptydir.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostPath`  <a name="cfn-batch-jobdefinition-eksvolume-hostpath"></a>
Specifies the configuration of a Kubernetes `hostPath` volume. For more information, see [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) in the *Kubernetes documentation*.
*Required*: No
*Type*: [EksHostPath](aws-properties-batch-jobdefinition-ekshostpath.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-batch-jobdefinition-eksvolume-name"></a>
The name of the volume. The name must be allowed as a DNS subdomain name. For more information, see [DNS subdomain names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) in the *Kubernetes documentation*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PersistentVolumeClaim`  <a name="cfn-batch-jobdefinition-eksvolume-persistentvolumeclaim"></a>
Specifies the configuration of a Kubernetes `persistentVolumeClaim` bounded to a `persistentVolume`. For more information, see [ Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in the *Kubernetes documentation*.
*Required*: No
*Type*: [EksPersistentVolumeClaim](aws-properties-batch-jobdefinition-ekspersistentvolumeclaim.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Secret`  <a name="cfn-batch-jobdefinition-eksvolume-secret"></a>
Specifies the configuration of a Kubernetes `secret` volume. For more information, see [secret](https://kubernetes.io/docs/concepts/storage/volumes/#secret) in the *Kubernetes documentation*.
*Required*: No
*Type*: [EksSecret](aws-properties-batch-jobdefinition-ekssecret.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
