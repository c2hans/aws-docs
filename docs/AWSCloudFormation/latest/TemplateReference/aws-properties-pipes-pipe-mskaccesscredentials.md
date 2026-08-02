---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-mskaccesscredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe MSKAccessCredentials
<a name="aws-properties-pipes-pipe-mskaccesscredentials"></a>

The AWS Secrets Manager secret that stores your stream credentials.

## Syntax
<a name="aws-properties-pipes-pipe-mskaccesscredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-mskaccesscredentials-syntax.json"></a>

```
{
  "[ClientCertificateTlsAuth](#cfn-pipes-pipe-mskaccesscredentials-clientcertificatetlsauth)" : {{String}},
  "[SaslScram512Auth](#cfn-pipes-pipe-mskaccesscredentials-saslscram512auth)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-mskaccesscredentials-syntax.yaml"></a>

```
  [ClientCertificateTlsAuth](#cfn-pipes-pipe-mskaccesscredentials-clientcertificatetlsauth): {{String}}
  [SaslScram512Auth](#cfn-pipes-pipe-mskaccesscredentials-saslscram512auth): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-mskaccesscredentials-properties"></a>

`ClientCertificateTlsAuth`  <a name="cfn-pipes-pipe-mskaccesscredentials-clientcertificatetlsauth"></a>
The ARN of the Secrets Manager secret.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):secret:.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SaslScram512Auth`  <a name="cfn-pipes-pipe-mskaccesscredentials-saslscram512auth"></a>
The ARN of the Secrets Manager secret.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):secret:.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
