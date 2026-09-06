---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IAM::AccessKey
<a name="aws-resource-iam-accesskey"></a>

 Creates a new AWS secret access key and corresponding AWS access key ID for the specified user. The default status for new keys is `Active`.

 For information about quotas on the number of keys you can create, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.

**Important**
To ensure the security of your AWS account, the secret access key is accessible only during key and user creation. You must save the key (for example, in a text file) if you want to be able to access it again. If a secret key is lost, you can rotate access keys by increasing the value of the `serial` property.

## Syntax
<a name="aws-resource-iam-accesskey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iam-accesskey-syntax.json"></a>

```
{
  "Type" : "AWS::IAM::AccessKey",
  "Properties" : {
      "[Serial](#cfn-iam-accesskey-serial)" : {{Integer}},
      "[Status](#cfn-iam-accesskey-status)" : {{String}},
      "[UserName](#cfn-iam-accesskey-username)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iam-accesskey-syntax.yaml"></a>

```
Type: AWS::IAM::AccessKey
Properties:
  [Serial](#cfn-iam-accesskey-serial): {{Integer}}
  [Status](#cfn-iam-accesskey-status): {{String}}
  [UserName](#cfn-iam-accesskey-username): {{String}}
```

## Properties
<a name="aws-resource-iam-accesskey-properties"></a>

`Serial`  <a name="cfn-iam-accesskey-serial"></a>
This value is specific to CloudFormation and can only be *incremented*. Incrementing this value notifies CloudFormation that you want to rotate your access key. When you update your stack, CloudFormation will replace the existing access key with a new key.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Status`  <a name="cfn-iam-accesskey-status"></a>
The status of the access key. `Active` means that the key is valid for API calls, while `Inactive` means it is not.
*Required*: No
*Type*: String
*Allowed values*: `Active | Inactive | Expired`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserName`  <a name="cfn-iam-accesskey-username"></a>
The name of the IAM user that the new key will belong to.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
*Required*: Yes
*Type*: String
*Pattern*: `[\w+=,.@-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iam-accesskey-return-values"></a>

### Ref
<a name="aws-resource-iam-accesskey-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `AccessKeyId`. For example: `AKIAIOSFODNN7EXAMPLE`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-iam-accesskey-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iam-accesskey-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID for this access key.

`SecretAccessKey`  <a name="SecretAccessKey-fn::getatt"></a>
Returns the secret access key for the specified AWS::IAM::AccessKey resource. For example: wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY.

## See also
<a name="aws-resource-iam-accesskey--seealso"></a>
+ To view `AWS::IAM::AccessKey` template example snippets, see [Declaring an IAM Access Key Resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-iam-accesskey).
+ [CreateAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccessKey.html) in the *AWS Identity and Access Management API Reference*
