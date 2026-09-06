---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-targetdomain-dnsverification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::TargetDomain DnsVerification
<a name="aws-properties-securityagent-targetdomain-dnsverification"></a>

Contains DNS verification details for a target domain, including the DNS record to create for domain ownership verification.

## Syntax
<a name="aws-properties-securityagent-targetdomain-dnsverification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-targetdomain-dnsverification-syntax.json"></a>

```
{
  "[DnsRecordName](#cfn-securityagent-targetdomain-dnsverification-dnsrecordname)" : {{String}},
  "[DnsRecordType](#cfn-securityagent-targetdomain-dnsverification-dnsrecordtype)" : {{String}},
  "[Token](#cfn-securityagent-targetdomain-dnsverification-token)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-targetdomain-dnsverification-syntax.yaml"></a>

```
  [DnsRecordName](#cfn-securityagent-targetdomain-dnsverification-dnsrecordname): {{String}}
  [DnsRecordType](#cfn-securityagent-targetdomain-dnsverification-dnsrecordtype): {{String}}
  [Token](#cfn-securityagent-targetdomain-dnsverification-token): {{String}}
```

## Properties
<a name="aws-properties-securityagent-targetdomain-dnsverification-properties"></a>

`DnsRecordName`  <a name="cfn-securityagent-targetdomain-dnsverification-dnsrecordname"></a>
The name of the DNS record to create for verification.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsRecordType`  <a name="cfn-securityagent-targetdomain-dnsverification-dnsrecordtype"></a>
The type of DNS record to create. Currently, only TXT is supported.
*Required*: No
*Type*: String
*Allowed values*: `TXT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Token`  <a name="cfn-securityagent-targetdomain-dnsverification-token"></a>
The verification token to include in the DNS record value.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
