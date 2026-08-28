---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::HealthLake::FHIRDatastore KmsEncryptionConfig
<a name="aws-properties-healthlake-fhirdatastore-kmsencryptionconfig"></a>

 The customer-managed-key(CMK) used when creating a Data Store. If a customer owned key is not specified, an Amazon owned key will be used for encryption.

## Syntax
<a name="aws-properties-healthlake-fhirdatastore-kmsencryptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-healthlake-fhirdatastore-kmsencryptionconfig-syntax.json"></a>

```
{
  "[CmkType](#cfn-healthlake-fhirdatastore-kmsencryptionconfig-cmktype)" : {{String}},
  "[KmsKeyId](#cfn-healthlake-fhirdatastore-kmsencryptionconfig-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-healthlake-fhirdatastore-kmsencryptionconfig-syntax.yaml"></a>

```
  [CmkType](#cfn-healthlake-fhirdatastore-kmsencryptionconfig-cmktype): {{String}}
  [KmsKeyId](#cfn-healthlake-fhirdatastore-kmsencryptionconfig-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-healthlake-fhirdatastore-kmsencryptionconfig-properties"></a>

`CmkType`  <a name="cfn-healthlake-fhirdatastore-kmsencryptionconfig-cmktype"></a>
 The type of customer-managed-key(CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and Amazon owned CMKs. For more information on CMK types, see [KmsEncryptionConfig](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html#HealthLake-Type-KmsEncryptionConfig-CmkType).
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOMER_MANAGED_KMS_KEY | AWS_OWNED_KMS_KEY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-healthlake-fhirdatastore-kmsencryptionconfig-kmskeyid"></a>
The Key Management Service (AWS KMS) encryption key id/alias used to encrypt the data store contents at rest.
*Required*: No
*Type*: String
*Pattern*: `(arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:kms:)?([a-z]{2}-[a-z]+(-[a-z]+)?-\d:)?(\d{12}:)?(((key/)?[a-zA-Z0-9-_]+)|(alias/[a-zA-Z0-9:/_-]+))`
*Minimum*: `1`
*Maximum*: `400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
