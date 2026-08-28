---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UpdateDeploymentGroup.html
---

# UpdateDeploymentGroup
<a name="API_UpdateDeploymentGroup"></a>

Changes information about a deployment group.

## Request Syntax
<a name="API_UpdateDeploymentGroup_RequestSyntax"></a>

```
{
   "alarmConfiguration": {
      "alarms": [
         {
            "name": "{{string}}"
         }
      ],
      "enabled": {{boolean}},
      "ignorePollAlarmFailure": {{boolean}}
   },
   "applicationName": "{{string}}",
   "autoRollbackConfiguration": {
      "enabled": {{boolean}},
      "events": [ "{{string}}" ]
   },
   "autoScalingGroups": [ "{{string}}" ],
   "blueGreenDeploymentConfiguration": {
      "deploymentReadyOption": {
         "actionOnTimeout": "{{string}}",
         "waitTimeInMinutes": {{number}}
      },
      "greenFleetProvisioningOption": {
         "action": "{{string}}"
      },
      "terminateBlueInstancesOnDeploymentSuccess": {
         "action": "{{string}}",
         "terminationWaitTimeInMinutes": {{number}}
      }
   },
   "currentDeploymentGroupName": "{{string}}",
   "deploymentConfigName": "{{string}}",
   "deploymentStyle": {
      "deploymentOption": "{{string}}",
      "deploymentType": "{{string}}"
   },
   "ec2TagFilters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ec2TagSet": {
      "ec2TagSetList": [
         [
            {
               "Key": "{{string}}",
               "Type": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      ]
   },
   "ecsServices": [
      {
         "clusterName": "{{string}}",
         "serviceName": "{{string}}"
      }
   ],
   "loadBalancerInfo": {
      "elbInfoList": [
         {
            "name": "{{string}}"
         }
      ],
      "targetGroupInfoList": [
         {
            "name": "{{string}}"
         }
      ],
      "targetGroupPairInfoList": [
         {
            "prodTrafficRoute": {
               "listenerArns": [ "{{string}}" ]
            },
            "targetGroups": [
               {
                  "name": "{{string}}"
               }
            ],
            "testTrafficRoute": {
               "listenerArns": [ "{{string}}" ]
            }
         }
      ]
   },
   "newDeploymentGroupName": "{{string}}",
   "onPremisesInstanceTagFilters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "onPremisesTagSet": {
      "onPremisesTagSetList": [
         [
            {
               "Key": "{{string}}",
               "Type": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      ]
   },
   "outdatedInstancesStrategy": "{{string}}",
   "serviceRoleArn": "{{string}}",
   "terminationHookEnabled": {{boolean}},
   "triggerConfigurations": [
      {
         "triggerEvents": [ "{{string}}" ],
         "triggerName": "{{string}}",
         "triggerTargetArn": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateDeploymentGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [alarmConfiguration](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-alarmConfiguration"></a>
Information to add or change about Amazon CloudWatch alarms when the deployment group is updated.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** [applicationName](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-applicationName"></a>
The application name that corresponds to the deployment group to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [autoRollbackConfiguration](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-autoRollbackConfiguration"></a>
Information for an automatic rollback configuration that is added or changed when a deployment group is updated.
Type: [AutoRollbackConfiguration](API_AutoRollbackConfiguration.md) object
Required: No

 ** [autoScalingGroups](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-autoScalingGroups"></a>
The replacement list of Auto Scaling groups to be included in the deployment group, if you want to change them.
+ To keep the Auto Scaling groups, enter their names or do not specify this parameter.
+ To remove Auto Scaling groups, specify a non-null empty list of Auto Scaling group names to detach all CodeDeploy-managed Auto Scaling lifecycle hooks. For examples, see [Amazon EC2 instances in an Amazon EC2 Auto Scaling group fail to launch and receive the error "Heartbeat Timeout"](https://docs.aws.amazon.com/codedeploy/latest/userguide/troubleshooting-auto-scaling.html#troubleshooting-auto-scaling-heartbeat) in the * AWS CodeDeploy User Guide*.
Type: Array of strings
Required: No

 ** [blueGreenDeploymentConfiguration](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-blueGreenDeploymentConfiguration"></a>
Information about blue/green deployment options for a deployment group.
Type: [BlueGreenDeploymentConfiguration](API_BlueGreenDeploymentConfiguration.md) object
Required: No

 ** [currentDeploymentGroupName](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-currentDeploymentGroupName"></a>
The current name of the deployment group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [deploymentConfigName](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-deploymentConfigName"></a>
The replacement deployment configuration name to use, if you want to change it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [deploymentStyle](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-deploymentStyle"></a>
Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.
Type: [DeploymentStyle](API_DeploymentStyle.md) object
Required: No

 ** [ec2TagFilters](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-ec2TagFilters"></a>
The replacement set of Amazon EC2 tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.
Type: Array of [EC2TagFilter](API_EC2TagFilter.md) objects
Required: No

 ** [ec2TagSet](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-ec2TagSet"></a>
Information about groups of tags applied to on-premises instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups.
Type: [EC2TagSet](API_EC2TagSet.md) object
Required: No

 ** [ecsServices](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-ecsServices"></a>
 The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format `<clustername>:<servicename>`.
Type: Array of [ECSService](API_ECSService.md) objects
Required: No

 ** [loadBalancerInfo](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-loadBalancerInfo"></a>
Information about the load balancer used in a deployment.
Type: [LoadBalancerInfo](API_LoadBalancerInfo.md) object
Required: No

 ** [newDeploymentGroupName](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-newDeploymentGroupName"></a>
The new name of the deployment group, if you want to change it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [onPremisesInstanceTagFilters](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-onPremisesInstanceTagFilters"></a>
The replacement set of on-premises instance tags on which to filter, if you want to change them. To keep the existing tags, enter their names. To remove tags, do not enter any tag names.
Type: Array of [TagFilter](API_TagFilter.md) objects
Required: No

 ** [onPremisesTagSet](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-onPremisesTagSet"></a>
Information about an on-premises instance tag set. The deployment group includes only on-premises instances identified by all the tag groups.
Type: [OnPremisesTagSet](API_OnPremisesTagSet.md) object
Required: No

 ** [outdatedInstancesStrategy](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-outdatedInstancesStrategy"></a>
Indicates what happens when new Amazon EC2 instances are launched mid-deployment and do not receive the deployed application revision.
If this option is set to `UPDATE` or is unspecified, CodeDeploy initiates one or more 'auto-update outdated instances' deployments to apply the deployed application revision to the new Amazon EC2 instances.
If this option is set to `IGNORE`, CodeDeploy does not initiate a deployment to update the new Amazon EC2 instances. This may result in instances having different revisions.
Type: String
Valid Values: `UPDATE | IGNORE`
Required: No

 ** [serviceRoleArn](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-serviceRoleArn"></a>
A replacement ARN for the service role, if you want to change it.
Type: String
Required: No

 ** [terminationHookEnabled](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-terminationHookEnabled"></a>
This parameter only applies if you are using CodeDeploy with Amazon EC2 Auto Scaling. For more information, see [Integrating CodeDeploy with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html) in the * AWS CodeDeploy User Guide*.
Set `terminationHookEnabled` to `true` to have CodeDeploy install a termination hook into your Auto Scaling group when you update a deployment group. When this hook is installed, CodeDeploy will perform termination deployments.
For information about termination deployments, see [Enabling termination deployments during Auto Scaling scale-in events](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable) in the * AWS CodeDeploy User Guide*.
For more information about Auto Scaling scale-in events, see the [Scale in](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html#as-lifecycle-scale-in) topic in the *Amazon EC2 Auto Scaling User Guide*.
Type: Boolean
Required: No

 ** [triggerConfigurations](#API_UpdateDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-request-triggerConfigurations"></a>
Information about triggers to change when the deployment group is updated. For examples, see [Edit a Trigger in a CodeDeploy Deployment Group](https://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-notify-edit.html) in the * AWS CodeDeploy User Guide*.
Type: Array of [TriggerConfig](API_TriggerConfig.md) objects
Required: No

## Response Syntax
<a name="API_UpdateDeploymentGroup_ResponseSyntax"></a>

```
{
   "hooksNotCleanedUp": [
      {
         "hook": "string",
         "name": "string",
         "terminationHook": "string"
      }
   ]
}
```

## Response Elements
<a name="API_UpdateDeploymentGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [hooksNotCleanedUp](#API_UpdateDeploymentGroup_ResponseSyntax) **   <a name="CodeDeploy-UpdateDeploymentGroup-response-hooksNotCleanedUp"></a>
If the output contains no data, and the corresponding deployment group contained at least one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling lifecycle event hooks from the AWS account. If the output contains data, AWS CodeDeploy could not remove some Auto Scaling lifecycle event hooks from the AWS account.
Type: Array of [AutoScalingGroup](API_AutoScalingGroup.md) objects

## Errors
<a name="API_UpdateDeploymentGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlarmsLimitExceededException **
The maximum number of alarms for a deployment group (10) was exceeded.
HTTP Status Code: 400

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** DeploymentConfigDoesNotExistException **
The deployment configuration does not exist with the user or AWS account.
HTTP Status Code: 400

 ** DeploymentGroupAlreadyExistsException **
A deployment group with the specified name with the user or AWS account already exists.
HTTP Status Code: 400

 ** DeploymentGroupDoesNotExistException **
The named deployment group with the user or AWS account does not exist.
HTTP Status Code: 400

 ** DeploymentGroupNameRequiredException **
The deployment group name was not specified.
HTTP Status Code: 400

 ** ECSServiceMappingLimitExceededException **
 The Amazon ECS service is associated with more than one deployment groups. An Amazon ECS service can be associated with only one deployment group.
HTTP Status Code: 400

 ** InvalidAlarmConfigException **
The format of the alarm configuration is invalid. Possible causes include:
+ The alarm list is null.
+ The alarm object is null.
+ The alarm name is empty or null or exceeds the limit of 255 characters.
+ Two alarms with the same name have been specified.
+ The alarm configuration is enabled, but the alarm list is empty.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidAutoRollbackConfigException **
The automatic rollback configuration was specified in an invalid format. For example, automatic rollback is enabled, but an invalid triggering event type or no event types were listed.
HTTP Status Code: 400

 ** InvalidAutoScalingGroupException **
The Auto Scaling group was specified in an invalid format or does not exist.
HTTP Status Code: 400

 ** InvalidBlueGreenDeploymentConfigurationException **
The configuration for the blue/green deployment group was provided in an invalid format. For information about deployment configuration format, see [CreateDeploymentConfig](API_CreateDeploymentConfig.md).
HTTP Status Code: 400

 ** InvalidDeploymentConfigNameException **
The deployment configuration name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentGroupNameException **
The deployment group name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentStyleException **
An invalid deployment style was specified. Valid deployment types include "IN\_PLACE" and "BLUE\_GREEN." Valid deployment options include "WITH\_TRAFFIC\_CONTROL" and "WITHOUT\_TRAFFIC\_CONTROL."
HTTP Status Code: 400

 ** InvalidEC2TagCombinationException **
A call was submitted that specified both Ec2TagFilters and Ec2TagSet, but only one of these data types can be used in a single call.
HTTP Status Code: 400

 ** InvalidEC2TagException **
The tag was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidECSServiceException **
 The Amazon ECS service identifier is not valid.
HTTP Status Code: 400

 ** InvalidInputException **
The input was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidLoadBalancerInfoException **
An invalid load balancer name, or no load balancer name, was specified.
HTTP Status Code: 400

 ** InvalidOnPremisesTagCombinationException **
A call was submitted that specified both OnPremisesTagFilters and OnPremisesTagSet, but only one of these data types can be used in a single call.
HTTP Status Code: 400

 ** InvalidRoleException **
The service role ARN was specified in an invalid format. Or, if an Auto Scaling group was specified, the specified service role does not grant the appropriate permissions to Amazon EC2 Auto Scaling.
HTTP Status Code: 400

 ** InvalidTagException **
The tag was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidTargetGroupPairException **
 A target group pair associated with this deployment is not valid.
HTTP Status Code: 400

 ** InvalidTrafficRoutingConfigurationException **
 The configuration that specifies how traffic is routed during a deployment is invalid.
HTTP Status Code: 400

 ** InvalidTriggerConfigException **
The trigger was specified in an invalid format.
HTTP Status Code: 400

 ** LifecycleHookLimitExceededException **
The limit for lifecycle hooks was exceeded.
HTTP Status Code: 400

 ** TagSetListLimitExceededException **
The number of tag groups included in the tag set list exceeded the maximum allowed limit of 3.
HTTP Status Code: 400

 ** ThrottlingException **
An API function was called too frequently.
HTTP Status Code: 400

 ** TriggerTargetsLimitExceededException **
The maximum allowed number of triggers was exceeded.
HTTP Status Code: 400

## Examples
<a name="API_UpdateDeploymentGroup_Examples"></a>

### Example
<a name="API_UpdateDeploymentGroup_Example_1"></a>

This example illustrates one usage of UpdateDeploymentGroup.

#### Sample Request
<a name="API_UpdateDeploymentGroup_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 167
X-Amz-Target: CodeDeploy_20141006.UpdateDeploymentGroup
X-Amz-Date: 20160707T025726Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "alarmConfiguration": {
        "alarms": [
            {
                "name": "project-def-alarm"
            }
        ],
        "enabled": true,
        "ignorePollAlarmFailure": false
    },
    "applicationName": "TestApp-us-east-1",
    "autoRollbackConfiguration": {
        "enabled": true,
        "events": [
            "DEPLOYMENT_FAILURE"
        ]
    },
    "newDeploymentGroupName": "dep-group-def-765",
    "currentDeploymentGroupName": "dep-group-def-456",
    "triggerConfigurations": [
        {
            "triggerEvents": [
                "DeploymentFailure"
            ],
            "triggerName": "Trigger-group-us-east-1-deploy-fail",
            "triggerTargetArn": "arn:aws:sns:us-east-1:80398EXAMPLE:us-east-deploy-fail"
        }
    ]
}
```

#### Sample Response
<a name="API_UpdateDeploymentGroup_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 1bd3a202-88e9-11e5-a087-ab26ee53e16e
Content-Type: application/x-amz-json-1.1
Content-Length: 24

{
	"hooksNotCleanedUp": []
}
```

## See Also
<a name="API_UpdateDeploymentGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/UpdateDeploymentGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/UpdateDeploymentGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/UpdateDeploymentGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/UpdateDeploymentGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/UpdateDeploymentGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/UpdateDeploymentGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/UpdateDeploymentGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/UpdateDeploymentGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/UpdateDeploymentGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/UpdateDeploymentGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
