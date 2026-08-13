---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-certificateprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::CertificateProvider
<a name="aws-resource-iot-certificateprovider"></a>

Creates a certificate provider. AWS IoT Core certificate provider lets you customize how to sign a certificate signing request (CSR) in fleet provisioning. For more information, see [Self-managed certificate signing using AWS IoT Corecertificate provider](https://docs.aws.amazon.com/iot/latest/developerguide/provisioning-cert-provider.html) from the *AWS IoT Core Developer Guide*.

## Syntax
<a name="aws-resource-iot-certificateprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-certificateprovider-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::CertificateProvider",
  "Properties" : {
      "[AccountDefaultForOperations](#cfn-iot-certificateprovider-accountdefaultforoperations)" : {{[ String, ... ]}},
      "[CertificateProviderName](#cfn-iot-certificateprovider-certificateprovidername)" : {{String}},
      "[LambdaFunctionArn](#cfn-iot-certificateprovider-lambdafunctionarn)" : {{String}},
      "[Tags](#cfn-iot-certificateprovider-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iot-certificateprovider-syntax.yaml"></a>

```
Type: AWS::IoT::CertificateProvider
Properties:
  [AccountDefaultForOperations](#cfn-iot-certificateprovider-accountdefaultforoperations): {{
    - String}}
  [CertificateProviderName](#cfn-iot-certificateprovider-certificateprovidername): {{String}}
  [LambdaFunctionArn](#cfn-iot-certificateprovider-lambdafunctionarn): {{String}}
  [Tags](#cfn-iot-certificateprovider-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iot-certificateprovider-properties"></a>

`AccountDefaultForOperations`  <a name="cfn-iot-certificateprovider-accountdefaultforoperations"></a>
A list of the operations that the certificate provider will use to generate certificates. Valid value: `CreateCertificateFromCsr`.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateProviderName`  <a name="cfn-iot-certificateprovider-certificateprovidername"></a>
The name of the certificate provider.
*Required*: No
*Type*: String
*Pattern*: `[\w=,@-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LambdaFunctionArn`  <a name="cfn-iot-certificateprovider-lambdafunctionarn"></a>
The ARN of the Lambda function.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `170`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iot-certificateprovider-tags"></a>
Metadata that can be used to manage the certificate provider.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-certificateprovider-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iot-certificateprovider-return-values"></a>

### Ref
<a name="aws-resource-iot-certificateprovider-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the certificate provider. For example:

 `{ "Ref": "MyCertificateProvider" }`

A value similar to the following is returned:

 `a1234567b89c012d3e4fg567hij8k9l01mno1p23q45678901rs234567890t1u2`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iot-certificateprovider-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iot-certificateprovider-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) for the certificate. For example:
 `{ "Fn::GetAtt": ["MyCertificateProvider", "Arn"] }`
A value similar to the following is returned:
 `arn:aws:iot:ap-southeast-2:123456789012:certprovider/my-certificate-provider`
