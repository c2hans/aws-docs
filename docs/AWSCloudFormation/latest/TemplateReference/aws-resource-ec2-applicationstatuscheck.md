---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-applicationstatuscheck.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ApplicationStatusCheck
<a name="aws-resource-ec2-applicationstatuscheck"></a>

Creates an application status check for monitoring the health of applications running on your instances. You can configure the protocol, port, path, and thresholds for the health check. The following rules apply:
+ You can create a maximum of 50 application status checks for each account.
+ You must associate the check with instances or tags using `AssociateApplicationStatusCheck` before health checks start.
+ You must set the `Timeout` value to less than the `Interval` value.
+ You must start the `Path` with a forward slash (`/`). Default: `/`.
+ You can specify `Aggregation` as `included` or `excluded`. If you do not specify a value, it defaults to `included`, which means the check contributes to the instance-level application status.
+ You can use the following default values: `Interval` is 60 seconds, `Timeout` is 6 seconds, `FailureThreshold` is 2, `SuccessThreshold` is 2, `StatusCodeMatcher` is `200`, `InitializationGracePeriodSeconds` is 300 seconds.
+ You can tag the application status check during creation. For more information, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

## Syntax
<a name="aws-resource-ec2-applicationstatuscheck-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-applicationstatuscheck-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::ApplicationStatusCheck",
  "Properties" : {
      "[Aggregation](#cfn-ec2-applicationstatuscheck-aggregation)" : {{String}},
      "[DeviceIndex](#cfn-ec2-applicationstatuscheck-deviceindex)" : {{Integer}},
      "[FailureThreshold](#cfn-ec2-applicationstatuscheck-failurethreshold)" : {{Integer}},
      "[HealthCheckPaths](#cfn-ec2-applicationstatuscheck-healthcheckpaths)" : {{[ HealthCheckPath, ... ]}},
      "[InitializationGracePeriodSeconds](#cfn-ec2-applicationstatuscheck-initializationgraceperiodseconds)" : {{Integer}},
      "[Interval](#cfn-ec2-applicationstatuscheck-interval)" : {{Integer}},
      "[IpScope](#cfn-ec2-applicationstatuscheck-ipscope)" : {{String}},
      "[IpVersion](#cfn-ec2-applicationstatuscheck-ipversion)" : {{String}},
      "[Path](#cfn-ec2-applicationstatuscheck-path)" : {{String}},
      "[Port](#cfn-ec2-applicationstatuscheck-port)" : {{Integer}},
      "[Protocol](#cfn-ec2-applicationstatuscheck-protocol)" : {{String}},
      "[StatusCodeMatcher](#cfn-ec2-applicationstatuscheck-statuscodematcher)" : {{String}},
      "[SuccessThreshold](#cfn-ec2-applicationstatuscheck-successthreshold)" : {{Integer}},
      "[Tags](#cfn-ec2-applicationstatuscheck-tags)" : {{[ Tag, ... ]}},
      "[Timeout](#cfn-ec2-applicationstatuscheck-timeout)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-ec2-applicationstatuscheck-syntax.yaml"></a>

```
Type: AWS::EC2::ApplicationStatusCheck
Properties:
  [Aggregation](#cfn-ec2-applicationstatuscheck-aggregation): {{String}}
  [DeviceIndex](#cfn-ec2-applicationstatuscheck-deviceindex): {{Integer}}
  [FailureThreshold](#cfn-ec2-applicationstatuscheck-failurethreshold): {{Integer}}
  [HealthCheckPaths](#cfn-ec2-applicationstatuscheck-healthcheckpaths): {{
    - HealthCheckPath}}
  [InitializationGracePeriodSeconds](#cfn-ec2-applicationstatuscheck-initializationgraceperiodseconds): {{Integer}}
  [Interval](#cfn-ec2-applicationstatuscheck-interval): {{Integer}}
  [IpScope](#cfn-ec2-applicationstatuscheck-ipscope): {{String}}
  [IpVersion](#cfn-ec2-applicationstatuscheck-ipversion): {{String}}
  [Path](#cfn-ec2-applicationstatuscheck-path): {{String}}
  [Port](#cfn-ec2-applicationstatuscheck-port): {{Integer}}
  [Protocol](#cfn-ec2-applicationstatuscheck-protocol): {{String}}
  [StatusCodeMatcher](#cfn-ec2-applicationstatuscheck-statuscodematcher): {{String}}
  [SuccessThreshold](#cfn-ec2-applicationstatuscheck-successthreshold): {{Integer}}
  [Tags](#cfn-ec2-applicationstatuscheck-tags): {{
    - Tag}}
  [Timeout](#cfn-ec2-applicationstatuscheck-timeout): {{Integer}}
```

## Properties
<a name="aws-resource-ec2-applicationstatuscheck-properties"></a>

`Aggregation`  <a name="cfn-ec2-applicationstatuscheck-aggregation"></a>
The aggregation setting for the application status check. When set to `included`, the result of this check contributes to the instance-level application status. When set to `excluded`, the check runs independently and does not affect the instance-level status.
*Required*: No
*Type*: String
*Allowed values*: `included | excluded`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceIndex`  <a name="cfn-ec2-applicationstatuscheck-deviceindex"></a>
The index of the network device used for the health check. The value is greater than or equal to 0.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FailureThreshold`  <a name="cfn-ec2-applicationstatuscheck-failurethreshold"></a>
The number of consecutive failed health checks before the application status is considered impaired. The value must be greater than 0.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HealthCheckPaths`  <a name="cfn-ec2-applicationstatuscheck-healthcheckpaths"></a>
The health check paths for the application status check.
*Required*: No
*Type*: Array of [HealthCheckPath](aws-properties-ec2-applicationstatuscheck-healthcheckpath.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InitializationGracePeriodSeconds`  <a name="cfn-ec2-applicationstatuscheck-initializationgraceperiodseconds"></a>
The number of seconds to wait before starting health checks after an instance is launched. Valid values: 1 to 600.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interval`  <a name="cfn-ec2-applicationstatuscheck-interval"></a>
The interval, in seconds, between health checks. Valid value: 60.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpScope`  <a name="cfn-ec2-applicationstatuscheck-ipscope"></a>
The IP scope used for the health check.
*Required*: No
*Type*: String
*Allowed values*: `private`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpVersion`  <a name="cfn-ec2-applicationstatuscheck-ipversion"></a>
The IP version used for the health check.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-ec2-applicationstatuscheck-path"></a>
The URL path used for the health check HTTP request.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-ec2-applicationstatuscheck-port"></a>
The port used for the health check.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-ec2-applicationstatuscheck-protocol"></a>
The protocol used for the health check.
*Required*: Yes
*Type*: String
*Allowed values*: `http | https`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusCodeMatcher`  <a name="cfn-ec2-applicationstatuscheck-statuscodematcher"></a>
The comma-separated list of individual HTTP status codes or ranges that indicate a successful health check response.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuccessThreshold`  <a name="cfn-ec2-applicationstatuscheck-successthreshold"></a>
The number of consecutive successful health checks before the application status is considered healthy. The value must be greater than 0.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-applicationstatuscheck-tags"></a>
The tags assigned to the application status check.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-applicationstatuscheck-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-ec2-applicationstatuscheck-timeout"></a>
The amount of time, in seconds, to wait for a health check response. Valid values: 1 to 30.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-applicationstatuscheck-return-values"></a>

### Ref
<a name="aws-resource-ec2-applicationstatuscheck-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-applicationstatuscheck-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-applicationstatuscheck-return-values-fn--getatt-fn--getatt"></a>

`ApplicationStatusCheckId`  <a name="ApplicationStatusCheckId-fn::getatt"></a>
The ID of the application status check.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time when the application status check was created.
