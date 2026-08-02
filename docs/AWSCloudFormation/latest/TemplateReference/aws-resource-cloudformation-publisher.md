---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-publisher.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::Publisher
<a name="aws-resource-cloudformation-publisher"></a>

The `AWS::CloudFormation::Publisher` resource registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users.

For information on requirements for registering as a public extension publisher, see [Publishing extensions to make them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.htm) in the *CloudFormation Command Line Interface (CLI) User Guide*.

## Syntax
<a name="aws-resource-cloudformation-publisher-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-publisher-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::Publisher",
  "Properties" : {
      "[AcceptTermsAndConditions](#cfn-cloudformation-publisher-accepttermsandconditions)" : {{Boolean}},
      "[ConnectionArn](#cfn-cloudformation-publisher-connectionarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-publisher-syntax.yaml"></a>

```
Type: AWS::CloudFormation::Publisher
Properties:
  [AcceptTermsAndConditions](#cfn-cloudformation-publisher-accepttermsandconditions): {{Boolean}}
  [ConnectionArn](#cfn-cloudformation-publisher-connectionarn): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-publisher-properties"></a>

`AcceptTermsAndConditions`  <a name="cfn-cloudformation-publisher-accepttermsandconditions"></a>
Whether you accept the [Terms and Conditions](https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf) for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry.
The default is `false`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectionArn`  <a name="cfn-cloudformation-publisher-connectionarn"></a>
If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.
For more information, see [Prerequisite: Registering your account to publish CloudFormation extensions](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs) in the *AWS CloudFormation Command Line Interface (CLI) User Guide*.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(-[w]+)*:.+:.+:[0-9]{12}:.+`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudformation-publisher-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-publisher-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the publisher ID. For example:

 `{ "Ref": "2a33349e7e606a8ad2e30e3c84521f012345678" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-publisher-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-publisher-return-values-fn--getatt-fn--getatt"></a>

`IdentityProvider`  <a name="IdentityProvider-fn::getatt"></a>
The type of account used as the identity provider when registering this publisher with CloudFormation.

`PublisherId`  <a name="PublisherId-fn::getatt"></a>
The ID of the extension publisher.

`PublisherProfile`  <a name="PublisherProfile-fn::getatt"></a>
The URL to the publisher's profile with the identity provider.

`PublisherStatus`  <a name="PublisherStatus-fn::getatt"></a>
Whether the publisher is verified. Currently, all registered publishers are verified.
