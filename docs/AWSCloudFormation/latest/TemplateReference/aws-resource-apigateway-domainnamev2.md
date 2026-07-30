---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-domainnamev2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::DomainNameV2
<a name="aws-resource-apigateway-domainnamev2"></a>

The `AWS::ApiGateway::DomainNameV2` resource specifies a custom domain name for your private APIs in API Gateway. You can use a private custom domain name to provide a URL for your private API that's more intuitive and easier to recall.

## Syntax
<a name="aws-resource-apigateway-domainnamev2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apigateway-domainnamev2-syntax.json"></a>

```
{
  "Type" : "AWS::ApiGateway::DomainNameV2",
  "Properties" : {
      "[CertificateArn](#cfn-apigateway-domainnamev2-certificatearn)" : {{String}},
      "[DomainName](#cfn-apigateway-domainnamev2-domainname)" : {{String}},
      "[EndpointAccessMode](#cfn-apigateway-domainnamev2-endpointaccessmode)" : {{String}},
      "[EndpointConfiguration](#cfn-apigateway-domainnamev2-endpointconfiguration)" : {{EndpointConfiguration}},
      "[Policy](#cfn-apigateway-domainnamev2-policy)" : {{Json}},
      "[RoutingMode](#cfn-apigateway-domainnamev2-routingmode)" : {{String}},
      "[SecurityPolicy](#cfn-apigateway-domainnamev2-securitypolicy)" : {{String}},
      "[Tags](#cfn-apigateway-domainnamev2-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-apigateway-domainnamev2-syntax.yaml"></a>

```
Type: AWS::ApiGateway::DomainNameV2
Properties:
  [CertificateArn](#cfn-apigateway-domainnamev2-certificatearn): {{String}}
  [DomainName](#cfn-apigateway-domainnamev2-domainname): {{String}}
  [EndpointAccessMode](#cfn-apigateway-domainnamev2-endpointaccessmode): {{String}}
  [EndpointConfiguration](#cfn-apigateway-domainnamev2-endpointconfiguration): {{
    EndpointConfiguration}}
  [Policy](#cfn-apigateway-domainnamev2-policy): {{Json}}
  [RoutingMode](#cfn-apigateway-domainnamev2-routingmode): {{String}}
  [SecurityPolicy](#cfn-apigateway-domainnamev2-securitypolicy): {{String}}
  [Tags](#cfn-apigateway-domainnamev2-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-apigateway-domainnamev2-properties"></a>

`CertificateArn`  <a name="cfn-apigateway-domainnamev2-certificatearn"></a>
 The reference to an AWS-managed certificate that will be used by the private endpoint for this domain name. AWS Certificate Manager is the only supported source.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-apigateway-domainnamev2-domainname"></a>
Represents a custom domain name as a user-friendly host name of an API (RestApi).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointAccessMode`  <a name="cfn-apigateway-domainnamev2-endpointaccessmode"></a>
The endpoint access mode for your DomainName.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointConfiguration`  <a name="cfn-apigateway-domainnamev2-endpointconfiguration"></a>
The endpoint configuration to indicate the types of endpoints an API (RestApi) or its custom domain name (DomainName) has and the IP address types that can invoke it.
*Required*: No
*Type*: [EndpointConfiguration](aws-properties-apigateway-domainnamev2-endpointconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-apigateway-domainnamev2-policy"></a>
 A stringified JSON policy document that applies to the `execute-api` service for this DomainName regardless of the caller and Method configuration. You can use `Fn::ToJsonString` to enter your `policy`. For more information, see [Fn::ToJsonString](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ToJsonString.html).
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoutingMode`  <a name="cfn-apigateway-domainnamev2-routingmode"></a>
The routing mode for this domain name. The routing mode determines how API Gateway sends traffic from your custom domain name to your private APIs.
*Required*: No
*Type*: String
*Allowed values*: `BASE_PATH_MAPPING_ONLY | ROUTING_RULE_THEN_BASE_PATH_MAPPING | ROUTING_RULE_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityPolicy`  <a name="cfn-apigateway-domainnamev2-securitypolicy"></a>
The Transport Layer Security (TLS) version \+ cipher suite for this DomainName.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-apigateway-domainnamev2-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-apigateway-domainnamev2-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-apigateway-domainnamev2-return-values"></a>

### Ref
<a name="aws-resource-apigateway-domainnamev2-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the domain name ARN.

### Fn::GetAtt
<a name="aws-resource-apigateway-domainnamev2-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-apigateway-domainnamev2-return-values-fn--getatt-fn--getatt"></a>

`DomainNameArn`  <a name="DomainNameArn-fn::getatt"></a>
The ARN of the domain name.

`DomainNameId`  <a name="DomainNameId-fn::getatt"></a>
The domain name ID.

## Examples
<a name="aws-resource-apigateway-domainnamev2--examples"></a>

**Topics**
+ [Private custom domain name example](#aws-resource-apigateway-domainnamev2--examples--Private_custom_domain_name_example)
+ [Private custom domain name example with routing mode](#aws-resource-apigateway-domainnamev2--examples--Private_custom_domain_name_example_with_routing_mode)

### Private custom domain name example
<a name="aws-resource-apigateway-domainnamev2--examples--Private_custom_domain_name_example"></a>

The following example creates a `DomainNameV2` resource named `MyDomainName`.

#### JSON
<a name="aws-resource-apigateway-domainnamev2--examples--Private_custom_domain_name_example--json"></a>

```
{
    "MyDomainName": {
        "Type": "AWS::ApiGateway::DomainNameV2",
        "Properties": {
            "DomainName": "private.example.com",
            "CertificateArn": "arn:aws:acm:us-west-2:123456789:certificate/abcd-000-1234-0000-000000abcd",
            "EndpointConfiguration": {
                "Types": [
                    "PRIVATE"
                ]
            },
            "SecurityPolicy": "TLS_1_2",
            "Policy": "{\n\"Version\": \"2012-10-17\",		 	 	 \n\"Statement\": [\n{\n\"Effect\": \"Allow\",\n\"Principal\": \"*\",\n\"Action\": \"execute-api:Invoke\",\n\"Resource\": [\n\"execute-api:/*\"\n]\n},\n {\n\"Effect\": \"Deny\",\n\"Principal\": \"*\",\n\"Action\": \"execute-api:Invoke\",\n\"Resource\": [\n\"execute-api:/*\"\n],\n\"Condition\" : {\n\"StringNotEquals\": {\n\"aws:SourceVpce\": \"vpce-abcd1234efg\"\n}\n}\n}\n]\n}"
        }
    }
}
```

#### YAML
<a name="aws-resource-apigateway-domainnamev2--examples--Private_custom_domain_name_example--yaml"></a>

```
MyDomainName:
  Type: AWS::ApiGateway::DomainNameV2
  Properties:
    DomainName: private.example.com
    CertificateArn: arn:aws:acm:us-west-2:123456789:certificate/abcd-000-1234-0000-000000abcd
    EndpointConfiguration:
      Types:
        - PRIVATE
    SecurityPolicy: TLS_1_2
    Policy:
        Statement:
            - Action: 'execute-api:Invoke'
              Effect: Allow
              Principal: '*'
              Resource: 'execute-api:/*'
            - Action: 'execute-api:Invoke'
              Condition:
                StringNotEquals:
                  'aws:SourceVpce': !Ref EndpointID
              Effect: Deny
              Principal: '*'
              Resource: 'execute-api:/*'
        Version: 2012-10-17
```

### Private custom domain name example with routing mode
<a name="aws-resource-apigateway-domainnamev2--examples--Private_custom_domain_name_example_with_routing_mode"></a>

The following example creates a `DomainNameV2` resource named `MyDomainName` with a RoutingMode of `ROUTING_RULE_ONLY`.

#### JSON
<a name="aws-resource-apigateway-domainnamev2--examples--Private_custom_domain_name_example_with_routing_mode--json"></a>

```
{
  "MyDomainName": {
    "Type": "AWS::ApiGateway::DomainNameV2",
    "Properties": {
      "DomainName": "private.example.com",
      "CertificateArn": "arn:aws:acm:us-west-2:123456789:certificate/abcd-000-1234-0000-000000abcd",
      "EndpointConfiguration": {
        "Types": [
          "PRIVATE"
        ]
      },
      "SecurityPolicy": "TLS_1_2",
      "Policy": "{\n\"Version\": \"2012-10-17\",		 	 	 \n\"Statement\": [\n{\n\"Effect\": \"Allow\",\n\"Principal\": \"*\",\n\"Action\": \"execute-api:Invoke\",\n\"Resource\": [\n\"execute-api:/*\"\n]\n},\n {\n\"Effect\": \"Deny\",\n\"Principal\": \"*\",\n\"Action\": \"execute-api:Invoke\",\n\"Resource\": [\n\"execute-api:/*\"\n],\n\"Condition\" : {\n\"StringNotEquals\": {\n\"aws:SourceVpce\": \"vpce-abcd1234efg\"\n}\n}\n}\n]\n}",
      "RoutingMode": "ROUTING_RULE_ONLY"
    }
  }
}
```

#### YAML
<a name="aws-resource-apigateway-domainnamev2--examples--Private_custom_domain_name_example_with_routing_mode--yaml"></a>

```
MyDomainName:
    Type: AWS::ApiGateway::DomainNameV2
    Properties:
      DomainName: private.example.com
      CertificateArn: arn:aws:acm:us-west-2:123456789:certificate/abcd-000-1234-0000-000000abcd
      EndpointConfiguration:
        Types:
          - PRIVATE
      SecurityPolicy: "TLS_1_2"
      Policy:
        Statement:
            - Action: 'execute-api:Invoke'
              Effect: Allow
              Principal: '*'
              Resource: 'execute-api:/*'
            - Action: 'execute-api:Invoke'
              Condition:
                StringNotEquals:
                  'aws:SourceVpce': !Ref EndpointID
              Effect: Deny
              Principal: '*'
              Resource: 'execute-api:/*'
        Version: 2012-10-17
      RoutingMode: ROUTING_RULE_ONLY
```
