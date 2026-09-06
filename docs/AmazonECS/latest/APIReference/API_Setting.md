---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Setting.html
---

# Setting
<a name="API_Setting"></a>

The current account setting for a resource.

## Contents
<a name="API_Setting_Contents"></a>

 ** name **   <a name="ECS-Type-Setting-name"></a>
The Amazon ECS resource name.
Type: String
Valid Values: `serviceLongArnFormat | taskLongArnFormat | containerInstanceLongArnFormat | awsvpcTrunking | containerInsights | fargateFIPSMode | tagResourceAuthorization | fargateTaskRetirementWaitPeriod | guardDutyActivate | defaultLogDriverMode | fargateEventWindows`
Required: No

 ** principalArn **   <a name="ECS-Type-Setting-principalArn"></a>
The ARN of the principal. It can be a user, role, or the root user. If this field is omitted, the authenticated user is assumed.
Type: String
Required: No

 ** type **   <a name="ECS-Type-Setting-type"></a>
Indicates whether AWS manages the account setting, or if the user manages it.
 `aws_managed` account settings are read-only, as AWS manages such on the customer's behalf. Currently, the `guardDutyActivate` account setting is the only one AWS manages.
Type: String
Valid Values: `user | aws_managed`
Required: No

 ** value **   <a name="ECS-Type-Setting-value"></a>
Determines whether the account setting is on or off for the specified resource.
Type: String
Required: No

## See Also
<a name="API_Setting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Setting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Setting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Setting)
