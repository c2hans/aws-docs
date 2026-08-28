---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-dataflowendpointgroup-endpointdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::DataflowEndpointGroup EndpointDetails
<a name="aws-properties-groundstation-dataflowendpointgroup-endpointdetails"></a>

 The security details and endpoint information.

## Syntax
<a name="aws-properties-groundstation-dataflowendpointgroup-endpointdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-dataflowendpointgroup-endpointdetails-syntax.json"></a>

```
{
  "[AwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroup-endpointdetails-awsgroundstationagentendpoint)" : {{AwsGroundStationAgentEndpoint}},
  "[Endpoint](#cfn-groundstation-dataflowendpointgroup-endpointdetails-endpoint)" : {{DataflowEndpoint}},
  "[SecurityDetails](#cfn-groundstation-dataflowendpointgroup-endpointdetails-securitydetails)" : {{SecurityDetails}}
}
```

### YAML
<a name="aws-properties-groundstation-dataflowendpointgroup-endpointdetails-syntax.yaml"></a>

```
  [AwsGroundStationAgentEndpoint](#cfn-groundstation-dataflowendpointgroup-endpointdetails-awsgroundstationagentendpoint): {{
    AwsGroundStationAgentEndpoint}}
  [Endpoint](#cfn-groundstation-dataflowendpointgroup-endpointdetails-endpoint): {{
    DataflowEndpoint}}
  [SecurityDetails](#cfn-groundstation-dataflowendpointgroup-endpointdetails-securitydetails): {{
    SecurityDetails}}
```

## Properties
<a name="aws-properties-groundstation-dataflowendpointgroup-endpointdetails-properties"></a>

`AwsGroundStationAgentEndpoint`  <a name="cfn-groundstation-dataflowendpointgroup-endpointdetails-awsgroundstationagentendpoint"></a>
An agent endpoint.
*Required*: No
*Type*: [AwsGroundStationAgentEndpoint](aws-properties-groundstation-dataflowendpointgroup-awsgroundstationagentendpoint.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Endpoint`  <a name="cfn-groundstation-dataflowendpointgroup-endpointdetails-endpoint"></a>
 Information about the endpoint such as name and the endpoint address.
*Required*: No
*Type*: [DataflowEndpoint](aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityDetails`  <a name="cfn-groundstation-dataflowendpointgroup-endpointdetails-securitydetails"></a>
 The role ARN, and IDs for security groups and subnets.
*Required*: No
*Type*: [SecurityDetails](aws-properties-groundstation-dataflowendpointgroup-securitydetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-properties-groundstation-dataflowendpointgroup-endpointdetails--examples"></a>

### Create a EndpointDetails
<a name="aws-properties-groundstation-dataflowendpointgroup-endpointdetails--examples--Create_a_EndpointDetails"></a>

The following example creates Ground Station `EndpointDetails`

#### JSON
<a name="aws-properties-groundstation-dataflowendpointgroup-endpointdetails--examples--Create_a_EndpointDetails--json"></a>

```
{
  "EndpointDetails": [
    {
      "SecurityDetails": {
        "SubnetIds": [
          "subnet-6782e71e"
        ],
        "SecurityGroupIds": [
          "sg-6979fe18"
        ],
        "RoleArn": "arn:aws:iam::012345678910:role/groundstation-service-role-AWSServiceRoleForAmazonGroundStation-EXAMPLEBQ4PI"
      },
      "Endpoint": {
        "Name": "myEndpoint",
        "Address": {
          "Name": "172.10.0.2",
          "Port": 44720
        },
        "Mtu": 1500
      }
    }
  }
}
```

#### YAML
<a name="aws-properties-groundstation-dataflowendpointgroup-endpointdetails--examples--Create_a_EndpointDetails--yaml"></a>

```
EndpointDetails:
  - SecurityDetails:
      SubnetIds:
        - subnet-12345678
      SecurityGroupIds:
        - sg-87654321
      RoleArn: arn:aws:iam::012345678910:role/groundstation-service-role-AWSServiceRoleForAmazonGroundStation-EXAMPLEABCDE
Endpoint:
  Name: myEndpoint
  Address:
    Name: 172.10.0.2
    Port: 44720
  Mtu: 1500
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
