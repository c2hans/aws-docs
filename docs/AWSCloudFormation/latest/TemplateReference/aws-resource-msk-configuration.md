---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-msk-configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Configuration
<a name="aws-resource-msk-configuration"></a>

Creates a new MSK configuration. To see an example of how to use this operation, first save the following text to a file and name the file `config-file.txt`.

```
auto.create.topics.enable = true

zookeeper.connection.timeout.ms = 1000

log.roll.ms = 604800000
```

Now run the following Python 3.6 script in the folder where you saved `config-file.txt`. This script uses the properties specified in `config-file.txt` to create a configuration named `SalesClusterConfiguration`. This configuration can work with Apache Kafka versions 1.1.1 and 2.1.0.

```
import boto3

client = boto3.client('kafka')

config_file = open('config-file.txt', 'r')

server_properties = config_file.read()

response = client.create_configuration(
    Name='SalesClusterConfiguration',
    Description='The configuration to use on all sales clusters.',
    KafkaVersions=['1.1.1', '2.1.0'],
    ServerProperties=server_properties
)

print(response)
```

## Syntax
<a name="aws-resource-msk-configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-msk-configuration-syntax.json"></a>

```
{
  "Type" : "AWS::MSK::Configuration",
  "Properties" : {
      "[Description](#cfn-msk-configuration-description)" : {{String}},
      "[KafkaVersionsList](#cfn-msk-configuration-kafkaversionslist)" : {{[ String, ... ]}},
      "[LatestRevision](#cfn-msk-configuration-latestrevision)" : {{LatestRevision}},
      "[Name](#cfn-msk-configuration-name)" : {{String}},
      "[ServerProperties](#cfn-msk-configuration-serverproperties)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-msk-configuration-syntax.yaml"></a>

```
Type: AWS::MSK::Configuration
Properties:
  [Description](#cfn-msk-configuration-description): {{String}}
  [KafkaVersionsList](#cfn-msk-configuration-kafkaversionslist): {{
    - String}}
  [LatestRevision](#cfn-msk-configuration-latestrevision): {{
    LatestRevision}}
  [Name](#cfn-msk-configuration-name): {{String}}
  [ServerProperties](#cfn-msk-configuration-serverproperties): {{String}}
```

## Properties
<a name="aws-resource-msk-configuration-properties"></a>

`Description`  <a name="cfn-msk-configuration-description"></a>
The description of the configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KafkaVersionsList`  <a name="cfn-msk-configuration-kafkaversionslist"></a>
The [versions of Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/supported-kafka-versions.html) with which you can use this MSK configuration.
When you update the `KafkaVersionsList` property, CloudFormation recreates a new configuration with the updated property before deleting the old configuration. Such an update requires a [resource replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement). To successfully update `KafkaVersionsList`, you must also update the `Name` property in the same operation.
If your configuration is attached with any clusters created using the AWS Management Console or AWS CLI, you'll need to manually delete the old configuration from the console after the update completes.
For more information, see [Can’t update KafkaVersionsList in MSK configuration](https://docs.aws.amazon.com/msk/latest/developerguide/troubleshooting.html#troubleshoot-kafkaversionslist-cfn-update-failure) in the *Amazon MSK Developer Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LatestRevision`  <a name="cfn-msk-configuration-latestrevision"></a>
Latest revision of the MSK configuration.
*Required*: No
*Type*: [LatestRevision](aws-properties-msk-configuration-latestrevision.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-msk-configuration-name"></a>
The name of the configuration. Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$".
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerProperties`  <a name="cfn-msk-configuration-serverproperties"></a>
Contents of the `server.properties` file. When using the console, the SDK, or the AWS CLI, the contents of `server.properties` can be in plaintext.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-msk-configuration-return-values"></a>

### Ref
<a name="aws-resource-msk-configuration-return-values-ref"></a>

When you provide the logical ID of this resource to the `Ref` intrinsic function, it returns the MSK configuration.

### Fn::GetAtt
<a name="aws-resource-msk-configuration-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-msk-configuration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the configuration.

`LatestRevision.CreationTime`  <a name="LatestRevision.CreationTime-fn::getatt"></a>
The time when the configuration revision was created.

`LatestRevision.Description`  <a name="LatestRevision.Description-fn::getatt"></a>
The description of the configuration revision.

`LatestRevision.Revision`  <a name="LatestRevision.Revision-fn::getatt"></a>
The revision number.
