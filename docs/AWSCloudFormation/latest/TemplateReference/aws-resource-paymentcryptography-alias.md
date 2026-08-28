---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-paymentcryptography-alias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PaymentCryptography::Alias
<a name="aws-resource-paymentcryptography-alias"></a>

Creates an *alias*, or a friendly name, for an AWS Payment Cryptography key. You can use an alias to identify a key in the console and when you call cryptographic operations such as [EncryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptData.html) or [DecryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DecryptData.html).

You can associate the alias with any key in the same AWS Region. Each alias is associated with only one key at a time, but a key can have multiple aliases. You can't create an alias without a key. The alias must be unique in the account and AWS Region, but you can create another alias with the same name in a different AWS Region.

To change the key that's associated with the alias, call [UpdateAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html). To delete the alias, call [DeleteAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html). These operations don't affect the underlying key. To get the alias that you created, call [ListAliases](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html).

**Cross-account use**: This operation can't be used across different AWS accounts.

 **Related operations:**
+  [DeleteAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html)
+  [GetAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html)
+  [ListAliases](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html)
+  [UpdateAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html)

## Syntax
<a name="aws-resource-paymentcryptography-alias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-paymentcryptography-alias-syntax.json"></a>

```
{
  "Type" : "AWS::PaymentCryptography::Alias",
  "Properties" : {
      "[AliasName](#cfn-paymentcryptography-alias-aliasname)" : {{String}},
      "[KeyArn](#cfn-paymentcryptography-alias-keyarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-paymentcryptography-alias-syntax.yaml"></a>

```
Type: AWS::PaymentCryptography::Alias
Properties:
  [AliasName](#cfn-paymentcryptography-alias-aliasname): {{String}}
  [KeyArn](#cfn-paymentcryptography-alias-keyarn): {{String}}
```

## Properties
<a name="aws-resource-paymentcryptography-alias-properties"></a>

`AliasName`  <a name="cfn-paymentcryptography-alias-aliasname"></a>
A friendly name that you can use to refer to a key. The value must begin with `alias/`.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
*Required*: Yes
*Type*: String
*Pattern*: `^alias/[a-zA-Z0-9/_-]+$`
*Minimum*: `7`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KeyArn`  <a name="cfn-paymentcryptography-alias-keyarn"></a>
The `KeyARN` of the key associated with the alias.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}$`
*Minimum*: `70`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-paymentcryptography-alias-return-values"></a>

### Ref
<a name="aws-resource-paymentcryptography-alias-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
