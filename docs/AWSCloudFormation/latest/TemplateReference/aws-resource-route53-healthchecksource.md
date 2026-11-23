---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthchecksource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HealthCheckSource

The `AWS::Route53::HealthCheckSource` resource creates a health check source that Amazon Route 53 uses to check the health of private endpoints, such as internal load balancers. Your endpoints don't need to be reachable from the internet. A health check source is a set of network interfaces that Route 53 creates in your VPC. Route 53 sends the health check requests from these network interfaces. To create a health check source, you specify the VPC, subnets, and security groups that Route 53 uses for the network interfaces.

After you create a health check source, reference its ID in the `HealthCheckSourceId` property of `HealthCheckConfig` when you create an `AWS::Route53::HealthCheck` resource with an `EndpointType` of `PRIVATE`. For more information, see [HealthCheckConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthcheck-healthcheckconfig.html).

A health check source must specify a VPC. It must also specify one subnet in each Availability Zone where Route 53 runs private-endpoint health checks. Most Regions require three subnets. Regions that have only two such Availability Zones, such as US West (N. California), require two. Each subnet must specify one or more security groups in the same VPC. These security groups must allow outbound traffic to the endpoints that you want to check. Route 53 creates network interfaces in each subnet and sends health check requests from all of them.

Route 53 creates the health check source asynchronously. CloudFormation waits until the `HealthCheckSourceStatus` is `CREATE_COMPLETED` before it marks the resource as created, so resources that depend on the health check source, such as private-endpoint health checks, are created only after the source is ready to use. If the status becomes `CREATE_FAILED`, the stack operation fails and the error message includes the `StatusReasonCode` and `StatusReason` that Route 53 returned.

To create a health check source, the principal that CloudFormation uses must have permission to create the service-linked role for Route 53 private-endpoint health checks (`iam:CreateServiceLinkedRole`). Otherwise, the create request fails with `AccessDenied`.

**Important**
You can't change `HealthCheckSourceConfig` after you create a health check source. If you change it in a template, CloudFormation replaces the health check source with a new one that has a new ID and ARN. Only `Tags` can be updated without interruption.

## Syntax
<a name="aws-resource-route53-healthchecksource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53-healthchecksource-syntax.json"></a>

```json
{
  "Type" : "AWS::Route53::HealthCheckSource",
  "Properties" : {
      "[HealthCheckSourceConfig](#cfn-route53-healthchecksource-healthchecksourceconfig)" : {{HealthCheckSourceConfig}},
      "[Tags](#cfn-route53-healthchecksource-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53-healthchecksource-syntax.yaml"></a>

```yaml
Type: AWS::Route53::HealthCheckSource
Properties:
  [HealthCheckSourceConfig](#cfn-route53-healthchecksource-healthchecksourceconfig): {{
    HealthCheckSourceConfig}}
  [Tags](#cfn-route53-healthchecksource-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53-healthchecksource-properties"></a>

`HealthCheckSourceConfig`  <a name="cfn-route53-healthchecksource-healthchecksourceconfig"></a>
The virtual private cloud (VPC), subnets, and security groups for the health check source.
*Required*: Yes
*Type*: [HealthCheckSourceConfig](aws-properties-route53-healthchecksource-healthchecksourceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-route53-healthchecksource-tags"></a>
A complex type that contains a list of the tags that you want to apply to the health check source when you create it.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53-healthchecksource-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53-healthchecksource-return-values"></a>

### Ref
<a name="aws-resource-route53-healthchecksource-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the health check source, such as `arn:aws:route53:::healthchecksource/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53-healthchecksource-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53-healthchecksource-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the health check source, such as `arn:aws:route53:::healthchecksource/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`. This is the same value that `Ref` returns.

`HealthCheckSourceId`  <a name="HealthCheckSourceId-fn::getatt"></a>
The ID of the health check source. Route 53 assigns this ID when it creates the source.

`HealthCheckSourceStatus`  <a name="HealthCheckSourceStatus-fn::getatt"></a>
The current status of the health check source. The health check source status can have one of the following values:
+ `CREATE_PENDING` - Route 53 accepted the request to create the source and hasn't started creating it. You can't use the source in a health check until its status is `CREATE_COMPLETED`.
+ `CREATE_IN_PROGRESS` - Route 53 is creating the source. You can't use the source in a health check until its status is `CREATE_COMPLETED`.
+ `CREATE_COMPLETED` - The source is ready to use.
+ `CREATE_FAILED` - Route 53 couldn't create the source. `StatusReasonCode` and `StatusReason` explain why.
+ `DELETE_PENDING` - Route 53 accepted the request to delete the source and hasn't started deleting it.
+ `DELETE_IN_PROGRESS` - Route 53 is deleting the source.
+ `DELETE_COMPLETED` - Route 53 has deleted the source. You can't retrieve a health check source in this status: `GetHealthCheckSource` returns `NoSuchHealthCheckSource`.
+ `DELETE_FAILED` - Route 53 couldn't delete the source. `StatusReasonCode` and `StatusReason` explain why.
If the status is `CREATE_FAILED`, fix the cause that `StatusReasonCode` indicates, and then either retry `CreateHealthCheckSource` with the same `CallerReference` and settings, or delete the source and create a new one. If the status is `DELETE_FAILED`, retry the `DeleteHealthCheckSource` request.

## Examples
<a name="aws-resource-route53-healthchecksource--examples"></a>

### Example: Create a health check source and a private endpoint health check
<a name="aws-resource-route53-healthchecksource--examples--Example:_Create_a_health_check_source_and_a_private_endpoint_health_check"></a>

The following example creates a health check source with one subnet in each of three Availability Zones, and then creates a private-endpoint health check that uses the source to send HTTP requests to a private IP address in the VPC.

#### JSON
<a name="aws-resource-route53-healthchecksource--examples--Example:_Create_a_health_check_source_and_a_private_endpoint_health_check--json"></a>

```json
{
   "MyHealthCheckSource": {
      "Type": "AWS::Route53::HealthCheckSource",
      "Properties": {
         "HealthCheckSourceConfig": {
            "VpcId": "vpc-1234567890abcdef0",
            "SubnetConfigurationList": [
               {
                  "SubnetId": "subnet-1234567890abcdef0",
                  "AvailabilityZoneId": "use1-az1",
                  "SecurityGroupIdList": [ "sg-1234567890abcdef0" ]
               },
               {
                  "SubnetId": "subnet-1234567890abcdef1",
                  "AvailabilityZoneId": "use1-az2",
                  "SecurityGroupIdList": [ "sg-1234567890abcdef0" ]
               },
               {
                  "SubnetId": "subnet-1234567890abcdef2",
                  "AvailabilityZoneId": "use1-az4",
                  "SecurityGroupIdList": [ "sg-1234567890abcdef0" ]
               }
            ]
         },
         "Tags": [
            {
               "Key": "Name",
               "Value": "my-health-check-source"
            }
         ]
      }
   },
   "MyPrivateHealthCheck": {
      "Type": "AWS::Route53::HealthCheck",
      "Properties": {
         "HealthCheckConfig": {
            "Type": "HTTP",
            "EndpointType": "PRIVATE",
            "HealthCheckSourceId": { "Fn::GetAtt": [ "MyHealthCheckSource", "HealthCheckSourceId" ] },
            "IPAddress": "10.0.1.25",
            "Port": 80,
            "ResourcePath": "/health",
            "RequestInterval": 30,
            "FailureThreshold": 3
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-route53-healthchecksource--examples--Example:_Create_a_health_check_source_and_a_private_endpoint_health_check--yaml"></a>

```yaml
MyHealthCheckSource:
  Type: 'AWS::Route53::HealthCheckSource'
  Properties:
    HealthCheckSourceConfig:
      VpcId: vpc-1234567890abcdef0
      SubnetConfigurationList:
        - SubnetId: subnet-1234567890abcdef0
          AvailabilityZoneId: use1-az1
          SecurityGroupIdList:
            - sg-1234567890abcdef0
        - SubnetId: subnet-1234567890abcdef1
          AvailabilityZoneId: use1-az2
          SecurityGroupIdList:
            - sg-1234567890abcdef0
        - SubnetId: subnet-1234567890abcdef2
          AvailabilityZoneId: use1-az4
          SecurityGroupIdList:
            - sg-1234567890abcdef0
    Tags:
      - Key: Name
        Value: my-health-check-source
MyPrivateHealthCheck:
  Type: 'AWS::Route53::HealthCheck'
  Properties:
    HealthCheckConfig:
      Type: HTTP
      EndpointType: PRIVATE
      HealthCheckSourceId:
        Fn::GetAtt: [ MyHealthCheckSource, HealthCheckSourceId ]
      IPAddress: 10.0.1.25
      Port: 80
      ResourcePath: /health
      RequestInterval: 30
      FailureThreshold: 3
```

## See also
<a name="aws-resource-route53-healthchecksource--seealso"></a>
+ [CreateHealthCheckSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHealthCheckSource.html) in the *Amazon Route 53 API Reference*
+ [HealthCheckSource](https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckSource.html) in the *Amazon Route 53 API Reference*
