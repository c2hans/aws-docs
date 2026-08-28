---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationfsxontap-customsecretconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationFSxONTAP CustomSecretConfig
<a name="aws-properties-datasync-locationfsxontap-customsecretconfig"></a>

Specifies configuration information for a customer-managed Secrets Manager secret where a storage location credentials is stored in Secrets Manager as plain text (for authentication token, secret key, or password) or as binary (for Kerberos keytab). This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret.

**Note**
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.

## Syntax
<a name="aws-properties-datasync-locationfsxontap-customsecretconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationfsxontap-customsecretconfig-syntax.json"></a>

```
{
  "[SecretAccessRoleArn](#cfn-datasync-locationfsxontap-customsecretconfig-secretaccessrolearn)" : {{String}},
  "[SecretArn](#cfn-datasync-locationfsxontap-customsecretconfig-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationfsxontap-customsecretconfig-syntax.yaml"></a>

```
  [SecretAccessRoleArn](#cfn-datasync-locationfsxontap-customsecretconfig-secretaccessrolearn): {{String}}
  [SecretArn](#cfn-datasync-locationfsxontap-customsecretconfig-secretarn): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationfsxontap-customsecretconfig-properties"></a>

`SecretAccessRoleArn`  <a name="cfn-datasync-locationfsxontap-customsecretconfig-secretaccessrolearn"></a>
Specifies the ARN for the AWS Identity and Access Management role that DataSync uses to access the secret specified for `SecretArn`.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*|)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-datasync-locationfsxontap-customsecretconfig-secretarn"></a>
Specifies the ARN for an AWS Secrets Manager secret.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):secretsmanager:[a-z-0-9]+:[0-9]{12}:secret:.*|)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
