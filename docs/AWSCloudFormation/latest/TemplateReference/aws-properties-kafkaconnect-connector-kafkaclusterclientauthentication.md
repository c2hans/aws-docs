---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector KafkaClusterClientAuthentication
<a name="aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication"></a>

The client authentication information used in order to authenticate with the Apache Kafka cluster.

## Syntax
<a name="aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication-syntax.json"></a>

```
{
  "[AuthenticationType](#cfn-kafkaconnect-connector-kafkaclusterclientauthentication-authenticationtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication-syntax.yaml"></a>

```
  [AuthenticationType](#cfn-kafkaconnect-connector-kafkaclusterclientauthentication-authenticationtype): {{String}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication-properties"></a>

`AuthenticationType`  <a name="cfn-kafkaconnect-connector-kafkaclusterclientauthentication-authenticationtype"></a>
The type of client authentication used to connect to the Apache Kafka cluster. Value NONE means that no client authentication is used.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | IAM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
