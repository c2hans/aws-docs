---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-s3accesspointattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::S3AccessPointAttachment
<a name="aws-resource-fsx-s3accesspointattachment"></a>

An S3 access point attached to an Amazon FSx volume.

## Syntax
<a name="aws-resource-fsx-s3accesspointattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fsx-s3accesspointattachment-syntax.json"></a>

```
{
  "Type" : "AWS::FSx::S3AccessPointAttachment",
  "Properties" : {
      "[Name](#cfn-fsx-s3accesspointattachment-name)" : {{String}},
      "[OntapConfiguration](#cfn-fsx-s3accesspointattachment-ontapconfiguration)" : {{S3AccessPointOntapConfiguration}},
      "[OpenZFSConfiguration](#cfn-fsx-s3accesspointattachment-openzfsconfiguration)" : {{S3AccessPointOpenZFSConfiguration}},
      "[S3AccessPoint](#cfn-fsx-s3accesspointattachment-s3accesspoint)" : {{S3AccessPoint}},
      "[Type](#cfn-fsx-s3accesspointattachment-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-fsx-s3accesspointattachment-syntax.yaml"></a>

```
Type: AWS::FSx::S3AccessPointAttachment
Properties:
  [Name](#cfn-fsx-s3accesspointattachment-name): {{String}}
  [OntapConfiguration](#cfn-fsx-s3accesspointattachment-ontapconfiguration): {{
    S3AccessPointOntapConfiguration}}
  [OpenZFSConfiguration](#cfn-fsx-s3accesspointattachment-openzfsconfiguration): {{
    S3AccessPointOpenZFSConfiguration}}
  [S3AccessPoint](#cfn-fsx-s3accesspointattachment-s3accesspoint): {{
    S3AccessPoint}}
  [Type](#cfn-fsx-s3accesspointattachment-type): {{String}}
```

## Properties
<a name="aws-resource-fsx-s3accesspointattachment-properties"></a>

`Name`  <a name="cfn-fsx-s3accesspointattachment-name"></a>
The name of the S3 access point attachment; also used for the name of the S3 access point.
*Required*: Yes
*Type*: String
*Pattern*: `^(?=[a-z0-9])[a-z0-9-]{1,48}[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OntapConfiguration`  <a name="cfn-fsx-s3accesspointattachment-ontapconfiguration"></a>
The ONTAP configuration of the S3 access point attachment.
*Required*: No
*Type*: [S3AccessPointOntapConfiguration](aws-properties-fsx-s3accesspointattachment-s3accesspointontapconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OpenZFSConfiguration`  <a name="cfn-fsx-s3accesspointattachment-openzfsconfiguration"></a>
The OpenZFSConfiguration of the S3 access point attachment.
*Required*: No
*Type*: [S3AccessPointOpenZFSConfiguration](aws-properties-fsx-s3accesspointattachment-s3accesspointopenzfsconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3AccessPoint`  <a name="cfn-fsx-s3accesspointattachment-s3accesspoint"></a>
The S3 access point configuration of the S3 access point attachment.
*Required*: No
*Type*: [S3AccessPoint](aws-properties-fsx-s3accesspointattachment-s3accesspoint.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-fsx-s3accesspointattachment-type"></a>
The type of Amazon FSx volume that the S3 access point is attached to.
*Required*: Yes
*Type*: String
*Allowed values*: `OPENZFS | ONTAP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-fsx-s3accesspointattachment-return-values"></a>

### Ref
<a name="aws-resource-fsx-s3accesspointattachment-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fsx-s3accesspointattachment-return-values-fn--getatt"></a>

####
<a name="aws-resource-fsx-s3accesspointattachment-return-values-fn--getatt-fn--getatt"></a>

`Lifecycle`  <a name="Lifecycle-fn::getatt"></a>
The lifecycle status of the S3 access point attachment. The lifecycle can have the following values:
+ AVAILABLE - the S3 access point attachment is available for use
+ CREATING - Amazon FSx is creating the S3 access point and attachment
+ DELETING - Amazon FSx is deleting the S3 access point and attachment
+ FAILED - The S3 access point attachment is in a failed state. Delete and detach the S3 access point attachment, and create a new one.
+ MISCONFIGURED - The S3 access point attachment has a configuration issue that prevents it from serving requests. Amazon FSx periodically checks for this condition and automatically returns the access point to AVAILABLE when the issue is resolved.
+ UPDATING - Amazon FSx is updating the S3 access point attachment

`S3AccessPoint.Alias`  <a name="S3AccessPoint.Alias-fn::getatt"></a>
A DNS alias that is associated with the file system. You can use a DNS alias to access a file system using user-defined DNS names, in addition to the default DNS name that Amazon FSx assigns to the file system. For more information, see [DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) in the *FSx for Windows File Server User Guide*.

`S3AccessPoint.ResourceARN`  <a name="S3AccessPoint.ResourceARN-fn::getatt"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.
