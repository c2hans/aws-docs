---
source_url: https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-list.html
---

# Discovering resources with AWS Cloud Control API
<a name="resource-operations-list"></a>

Use the `list-resources` command to discover the resources currently provisioned in your AWS account and AWS Region. This includes all resources of the specified resource type, regardless of whether they were provisioned through Cloud Control API, directly through the underlying service, or other mechanism (such as being part of an AWS CloudFormation stack).

The information returned for each resource includes:
+ The resource's primary identifier.
+ Optionally, it may include the *part or all* resource's properties, detailing the current state of the resource. For more information, see [Viewing resource type schemas](resource-types.md#resource-types-schemas).

The follow example returns a list of `AWS::Logs::LogGroup` resources.

```
$ aws cloudcontrol list-resources --type-name AWS::Logs::LogGroup
```

Cloud Control API returns a list of the resources in your account of the specified resource type. For the example , `list-resources` returns the primary identifier and resource properties of all `AWS::Logs::LogGroup` resources in your account, regardless of whether they were provisioned by Cloud Control API. The returned information resembles the following, depending on the resources in your account.

```
{
  "TypeName": "AWS::Logs::LogGroup",
  "ResourceDescriptions":
  [
    {
      "Identifier": "CloudControlExample",
      "Properties": '{"RetentionInDays":180, "LogGroupName": "CloudControlExample", "Arn": "arn:aws:logs:us-west-2:123456789012:log-group:CloudControlExample:*"}'
    },
    {
      "Identifier": "AnotherLogGroupResourceExample",
      "Properties": '{"RetentionInDays":90, "LogGroupName": "AnotherLogGroupResourceExample", "Arn": "arn:aws:logs:us-west-2:123456789012:log-group:AnotherLogGroupResourceExample:*"}'
    }
  ]
}
```

The follow example requests a list of `AWS::Kinesis::Stream` resources.

```
$ aws cloudcontrol list-resources --type-name AWS::Kinesis::Stream
```

For Kinesis streams, Cloud Control API returns the primary identifier of each stream, along with a *subset* of the resource properties. In this case, just a single property, `Name`. You could then use a stream's primary identifier with `get-resource` to request the resource's full current state.

```
{
    "TypeName": "AWS::Kinesis::Stream",
    "ResourceDescriptions": [
        {
            "Identifier": "MyKinesisStream",
            "Properties": '{"Name": "MyKinesisStream"}'
        },
        {
            "Identifier": "AnotherStream",
            "Properties": '{"Name": "AnotherStream"}'
        }
    ]
}
```

## Resources that require additional information
<a name="resource-operations-list-containers"></a>

Certain resources require that you provide additional information about the resources that you want to list as part of your request. In these cases, you must use the `ResourceModel` parameter to specify these properties.

The table below lists these resources, and the properties you to specify in the `ResourceModel` parameter during list requests.

| Resources | Required properties |
| --- | --- |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html) | `RestApiId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html) | `RestApiId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html) | `TypeArn` or `TypeName` |
|  [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html)  | `DomainName` |
|  [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html)  | `DomainName` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupmember.html) | `TransitGatewayMulticastDomainId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html) | `TransitGatewayMulticastDomainId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html) | `Cluster`, `Service`, and `ID` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html) | `ClusterName` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html) | `ClusterName` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html) | `LoadBalancerArn` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html) | `ListenerArn` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html) |  +  `SchemaDefinition`, `Schema/RegistryName`, and `Schema/SchemaName` <br />+  `SchemaDefinition` and `Schema/SchemaArn`   |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversionmetadata.html) | `SchemaVersionId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html) |  +  /`AccessPolicyResource`/`Portal` <br />+  /`AccessPolicyResource`/`Project`   |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html) | `ProjectId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html) | `PortalId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html) | `IndexId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html) | `IndexId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html) | `FlowArn` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html) | `FlowArn` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html) | `FlowArn` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html) | `FlowArn` |
|  [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html)  | `PackagingGroupId` |
|  [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html)  | `PackagingGroupId` |
|  [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html)  |  +  `FirewallArn` <br />+  `FirewallName`   |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-analysis.html) | `AwsAccountId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dashboard.html) | `AwsAccountId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html) | `AwsAccountId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-datasource.html) | `AwsAccountId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-template.html) | `AwsAccountId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-theme.html) | `AwsAccountId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html) | `DBProxyName` |
|  [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-accesspoint.html)  | `Bucket` |
|  [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3outposts-bucket.html)  | `OutpostId` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html) | `InstanceArn`, `PermissionSetArn`, `PrincipalId`, `PrincipalType`, `TargetId`, and `TargetType` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html) | `InstanceArn` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html) | `InstanceArn` |
| [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html) | `Scope` |
