---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateRule.html
---

# CreateRule
<a name="API_CreateRule"></a>

Creates a rule for the specified listener. The listener must be associated with an Application Load Balancer or a dual-stack Network Load Balancer.

Each rule consists of a priority, one or more actions, and one or more conditions. Rules are evaluated in priority order, from the lowest value to the highest value. When the conditions for a rule are met, its actions are performed. If the conditions for no rules are met, the actions for the default rule are performed. For more information, see [Listener rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules) in the *Application Load Balancers Guide* or [Listener rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html#listener-rules) in the *Network Load Balancers Guide*.

To view your current rules, use [DescribeRules](API_DescribeRules.md). To update a rule, use [ModifyRule](API_ModifyRule.md). To set the priorities of your rules, use [SetRulePriorities](API_SetRulePriorities.md). To delete a rule, use [DeleteRule](API_DeleteRule.md).

## Request Parameters
<a name="API_CreateRule_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Actions.member.N**
The actions.
Type: Array of [Action](API_Action.md) objects
Required: Yes

 **Conditions.member.N**
The conditions.
Type: Array of [RuleCondition](API_RuleCondition.md) objects
Required: Yes

 ** ListenerArn **
The Amazon Resource Name (ARN) of the listener.
Type: String
Required: Yes

 ** Priority **
The rule priority. A listener can't have multiple rules with the same priority.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50000.
Required: Yes

 **Tags.member.N**
The tags to assign to the rule.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

 **Transforms.member.N**
The transforms to apply to requests that match this rule. You can add one host header rewrite transform and one URL rewrite transform.
Type: Array of [RuleTransform](API_RuleTransform.md) objects
Required: No

## Response Elements
<a name="API_CreateRule_ResponseElements"></a>

The following element is returned by the service.

 **Rules.member.N**
Information about the rule.
Type: Array of [Rule](API_Rule.md) objects

## Errors
<a name="API_CreateRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IncompatibleProtocols **
The specified configuration is not valid with this protocol.
HTTP Status Code: 400

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** InvalidLoadBalancerAction **
The requested action is not valid.
HTTP Status Code: 400

 ** ListenerNotFound **
The specified listener does not exist.
HTTP Status Code: 400

 ** PriorityInUse **
The specified priority is in use.
HTTP Status Code: 400

 ** TargetGroupAssociationLimit **
You've reached the limit on the number of load balancers per target group.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

 ** TooManyActions **
You've reached the limit on the number of actions per rule.
HTTP Status Code: 400

 ** TooManyRegistrationsForTargetId **
You've reached the limit on the number of times a target can be registered with a load balancer.
HTTP Status Code: 400

 ** TooManyRules **
You've reached the limit on the number of rules per load balancer.
HTTP Status Code: 400

 ** TooManyTags **
You've reached the limit on the number of tags for this resource.
HTTP Status Code: 400

 ** TooManyTargetGroups **
You've reached the limit on the number of target groups for your AWS account.
HTTP Status Code: 400

 ** TooManyTargets **
You've reached the limit on the number of targets.
HTTP Status Code: 400

 ** TooManyUniqueTargetGroupsPerLoadBalancer **
You've reached the limit on the number of unique target groups per load balancer across all listeners. If a target group is used by multiple actions for a load balancer, it is counted as only one use.
HTTP Status Code: 400

 ** UnsupportedProtocol **
The specified protocol is not supported.
HTTP Status Code: 400

## Examples
<a name="API_CreateRule_Examples"></a>

### Create a rule that forwards to a target group if a condition is met
<a name="API_CreateRule_Example_1"></a>

This example creates a rule that forwards requests to the specified target group if the URL contains the specified pattern (for example, /img/\*).

#### Sample Request
<a name="API_CreateRule_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateRule
&ListenerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
&Priority=10
&Conditions.member.1.Field=path-pattern
&Conditions.member.1.Values.member.1=/img/*
&Actions.member.1.Type=forward
&Actions.member.1.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateRule_Example_1_Response"></a>

```
<CreateRuleResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <CreateRuleResult>
    <Rules>
      <member>
        <IsDefault>false</IsDefault>
        <Conditions>
          <member>
            <Field>path-pattern</Field>
            <Values>
              <member>/img/*</member>
            </Values>
          </member>
        </Conditions>
        <Priority>10</Priority>
        <Actions>
          <member>
            <Type>forward</Type>
            <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
          </member>
        </Actions>
        <RuleArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee</RuleArn>
      </member>
    </Rules>
  </CreateRuleResult>
  <ResponseMetadata>
    <RequestId>c5478c83-f397-11e5-bb98-57195a6eb84a</RequestId>
  </ResponseMetadata>
</CreateRuleResponse>
```

### Create a rule with a forward rule and an authenticate-oidc rule
<a name="API_CreateRule_Example_2"></a>

This example creates a rule that first authenticates the user and then forwards the request if the user is authenticated.

#### Sample Request
<a name="API_CreateRule_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateRule
&ListenerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
&Priority=10
&Actions.member.1.Type=authenticate-oidc
&Actions.member.1.AuthenticateOidcConfig.Issuer="https://idp-issuer.com"
&Actions.member.1.AuthenticateOidcConfig.AuthorizationEndpoint="https://authorization-endpoint.com"
&Actions.member.1.AuthenticateOidcConfig.TokenEndpoint="https://token-endpoint.com"
&Actions.member.1.AuthenticateOidcConfig.UserInfoEndpoint="https://user-info-endpoint.com"
&Actions.member.1.AuthenticateOidcConfig.ClientId="abcdefghijklmnopqrstuvwxyz123456789"
&Actions.member.1.AuthenticateOidcConfig.ClientSecret="123456789012345678901234567890"
&Actions.member.1.AuthenticateOidcConfig.SessionTimeout=3600
&Actions.member.1.AuthenticateOidcConfig.Scope="email"
&Actions.member.1.AuthenticateOidcConfig.OnUnauthenticatedRequest="authenticate"
&Actions.member.1.Order=1
&Actions.member.2.Type=forward
&Actions.member.2.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Actions.member.2.Order=2
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/CreateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/CreateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/CreateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/CreateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/CreateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/CreateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/CreateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/CreateRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/CreateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/CreateRule)
