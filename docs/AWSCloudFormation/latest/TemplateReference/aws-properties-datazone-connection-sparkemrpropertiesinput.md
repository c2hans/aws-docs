---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-sparkemrpropertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection SparkEmrPropertiesInput
<a name="aws-properties-datazone-connection-sparkemrpropertiesinput"></a>

The Spark EMR properties.

## Syntax
<a name="aws-properties-datazone-connection-sparkemrpropertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-sparkemrpropertiesinput-syntax.json"></a>

```
{
  "[ComputeArn](#cfn-datazone-connection-sparkemrpropertiesinput-computearn)" : {{String}},
  "[InstanceProfileArn](#cfn-datazone-connection-sparkemrpropertiesinput-instanceprofilearn)" : {{String}},
  "[JavaVirtualEnv](#cfn-datazone-connection-sparkemrpropertiesinput-javavirtualenv)" : {{String}},
  "[LogUri](#cfn-datazone-connection-sparkemrpropertiesinput-loguri)" : {{String}},
  "[ManagedEndpointArn](#cfn-datazone-connection-sparkemrpropertiesinput-managedendpointarn)" : {{String}},
  "[PythonVirtualEnv](#cfn-datazone-connection-sparkemrpropertiesinput-pythonvirtualenv)" : {{String}},
  "[RuntimeRole](#cfn-datazone-connection-sparkemrpropertiesinput-runtimerole)" : {{String}},
  "[TrustedCertificatesS3Uri](#cfn-datazone-connection-sparkemrpropertiesinput-trustedcertificatess3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-sparkemrpropertiesinput-syntax.yaml"></a>

```
  [ComputeArn](#cfn-datazone-connection-sparkemrpropertiesinput-computearn): {{String}}
  [InstanceProfileArn](#cfn-datazone-connection-sparkemrpropertiesinput-instanceprofilearn): {{String}}
  [JavaVirtualEnv](#cfn-datazone-connection-sparkemrpropertiesinput-javavirtualenv): {{String}}
  [LogUri](#cfn-datazone-connection-sparkemrpropertiesinput-loguri): {{String}}
  [ManagedEndpointArn](#cfn-datazone-connection-sparkemrpropertiesinput-managedendpointarn): {{String}}
  [PythonVirtualEnv](#cfn-datazone-connection-sparkemrpropertiesinput-pythonvirtualenv): {{String}}
  [RuntimeRole](#cfn-datazone-connection-sparkemrpropertiesinput-runtimerole): {{String}}
  [TrustedCertificatesS3Uri](#cfn-datazone-connection-sparkemrpropertiesinput-trustedcertificatess3uri): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-sparkemrpropertiesinput-properties"></a>

`ComputeArn`  <a name="cfn-datazone-connection-sparkemrpropertiesinput-computearn"></a>
The compute ARN of Spark EMR.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:(elasticmapreduce|emr-serverless|emr-containers):.*`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceProfileArn`  <a name="cfn-datazone-connection-sparkemrpropertiesinput-instanceprofilearn"></a>
The instance profile ARN of Spark EMR.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JavaVirtualEnv`  <a name="cfn-datazone-connection-sparkemrpropertiesinput-javavirtualenv"></a>
The java virtual env of the Spark EMR.
*Required*: No
*Type*: String
*Pattern*: `^[\S]*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogUri`  <a name="cfn-datazone-connection-sparkemrpropertiesinput-loguri"></a>
The log URI of the Spark EMR.
*Required*: No
*Type*: String
*Pattern*: `^s3://.+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedEndpointArn`  <a name="cfn-datazone-connection-sparkemrpropertiesinput-managedendpointarn"></a>
The managed endpoint ARN of the EMR on EKS cluster.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PythonVirtualEnv`  <a name="cfn-datazone-connection-sparkemrpropertiesinput-pythonvirtualenv"></a>
The Python virtual env of the Spark EMR.
*Required*: No
*Type*: String
*Pattern*: `^[\S]*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeRole`  <a name="cfn-datazone-connection-sparkemrpropertiesinput-runtimerole"></a>
The runtime role of the Spark EMR.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrustedCertificatesS3Uri`  <a name="cfn-datazone-connection-sparkemrpropertiesinput-trustedcertificatess3uri"></a>
The certificates S3 URI of the Spark EMR.
*Required*: No
*Type*: String
*Pattern*: `^s3://.+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
