---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbclusterendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBClusterEndpoint
<a name="aws-resource-rds-dbclusterendpoint"></a>

This data type represents the information you need to connect to an Amazon Aurora DB cluster. This data type is used as a response element in the following actions:
+  `CreateDBClusterEndpoint`
+  `DescribeDBClusterEndpoints`
+  `ModifyDBClusterEndpoint`
+  `DeleteDBClusterEndpoint`

For the data structure that represents Amazon RDS DB instance endpoints, see `Endpoint`.

## Syntax
<a name="aws-resource-rds-dbclusterendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-dbclusterendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::DBClusterEndpoint",
  "Properties" : {
      "[CustomEndpointType](#cfn-rds-dbclusterendpoint-customendpointtype)" : {{String}},
      "[DBClusterEndpointIdentifier](#cfn-rds-dbclusterendpoint-dbclusterendpointidentifier)" : {{String}},
      "[DBClusterIdentifier](#cfn-rds-dbclusterendpoint-dbclusteridentifier)" : {{String}},
      "[ExcludedMembers](#cfn-rds-dbclusterendpoint-excludedmembers)" : {{[ String, ... ]}},
      "[StaticMembers](#cfn-rds-dbclusterendpoint-staticmembers)" : {{[ String, ... ]}},
      "[Tags](#cfn-rds-dbclusterendpoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rds-dbclusterendpoint-syntax.yaml"></a>

```
Type: AWS::RDS::DBClusterEndpoint
Properties:
  [CustomEndpointType](#cfn-rds-dbclusterendpoint-customendpointtype): {{String}}
  [DBClusterEndpointIdentifier](#cfn-rds-dbclusterendpoint-dbclusterendpointidentifier): {{String}}
  [DBClusterIdentifier](#cfn-rds-dbclusterendpoint-dbclusteridentifier): {{String}}
  [ExcludedMembers](#cfn-rds-dbclusterendpoint-excludedmembers): {{
    - String}}
  [StaticMembers](#cfn-rds-dbclusterendpoint-staticmembers): {{
    - String}}
  [Tags](#cfn-rds-dbclusterendpoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rds-dbclusterendpoint-properties"></a>

`CustomEndpointType`  <a name="cfn-rds-dbclusterendpoint-customendpointtype"></a>
The type associated with a custom endpoint. One of: `READER`, `WRITER`, `ANY`.
*Required*: Yes
*Type*: String
*Allowed values*: `READER | WRITER | ANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DBClusterEndpointIdentifier`  <a name="cfn-rds-dbclusterendpoint-dbclusterendpointidentifier"></a>
The identifier associated with the endpoint. This parameter is stored as a lowercase string.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DBClusterIdentifier`  <a name="cfn-rds-dbclusterendpoint-dbclusteridentifier"></a>
The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExcludedMembers`  <a name="cfn-rds-dbclusterendpoint-excludedmembers"></a>
List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticMembers`  <a name="cfn-rds-dbclusterendpoint-staticmembers"></a>
List of DB instance identifiers that are part of the custom endpoint group.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-rds-dbclusterendpoint-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-rds-dbclusterendpoint-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rds-dbclusterendpoint-return-values"></a>

### Ref
<a name="aws-resource-rds-dbclusterendpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rds-dbclusterendpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-rds-dbclusterendpoint-return-values-fn--getatt-fn--getatt"></a>

`DBClusterEndpointArn`  <a name="DBClusterEndpointArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the endpoint.

`DBClusterEndpointResourceIdentifier`  <a name="DBClusterEndpointResourceIdentifier-fn::getatt"></a>
A unique system-generated identifier for an endpoint. It remains the same for the whole life of the endpoint.

`Endpoint`  <a name="Endpoint-fn::getatt"></a>
The DNS address of the endpoint.

`EndpointType`  <a name="EndpointType-fn::getatt"></a>
The type of the endpoint. One of: `READER`, `WRITER`, `CUSTOM`.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the endpoint. One of: `creating`, `available`, `deleting`, `inactive`, `modifying`. The `inactive` state applies to an endpoint that can't be used for a certain kind of cluster, such as a `writer` endpoint for a read-only secondary cluster in a global database.
