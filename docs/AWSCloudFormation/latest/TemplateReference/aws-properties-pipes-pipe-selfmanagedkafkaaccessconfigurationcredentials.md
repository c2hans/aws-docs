---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe SelfManagedKafkaAccessConfigurationCredentials
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials"></a>

The AWS Secrets Manager secret that stores your stream credentials.

## Syntax
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-syntax.json"></a>

```
{
  "[BasicAuth](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-basicauth)" : {{String}},
  "[ClientCertificateTlsAuth](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-clientcertificatetlsauth)" : {{String}},
  "[SaslScram256Auth](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram256auth)" : {{String}},
  "[SaslScram512Auth](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram512auth)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-syntax.yaml"></a>

```
  [BasicAuth](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-basicauth): {{String}}
  [ClientCertificateTlsAuth](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-clientcertificatetlsauth): {{String}}
  [SaslScram256Auth](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram256auth): {{String}}
  [SaslScram512Auth](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram512auth): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-properties"></a>

`BasicAuth`  <a name="cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-basicauth"></a>
The ARN of the Secrets Manager secret.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):secret:.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientCertificateTlsAuth`  <a name="cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-clientcertificatetlsauth"></a>
The ARN of the Secrets Manager secret.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):secret:.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SaslScram256Auth`  <a name="cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram256auth"></a>
The ARN of the Secrets Manager secret.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):secret:.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SaslScram512Auth`  <a name="cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials-saslscram512auth"></a>
The ARN of the Secrets Manager secret.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):secret:.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
