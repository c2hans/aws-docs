---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetRulePriorities.html
---

# SetRulePriorities
<a name="API_SetRulePriorities"></a>

Sets the priorities of the specified rules.

You can reorder the rules as long as there are no priority conflicts in the new order. Any existing rules that you do not specify retain their current priority.

## Request Parameters
<a name="API_SetRulePriorities_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **RulePriorities.member.N**
The rule priorities.
Type: Array of [RulePriorityPair](API_RulePriorityPair.md) objects
Required: Yes

## Response Elements
<a name="API_SetRulePriorities_ResponseElements"></a>

The following element is returned by the service.

 **Rules.member.N**
Information about the rules.
Type: Array of [Rule](API_Rule.md) objects

## Errors
<a name="API_SetRulePriorities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermitted **
This operation is not allowed.
HTTP Status Code: 400

 ** PriorityInUse **
The specified priority is in use.
HTTP Status Code: 400

 ** RuleNotFound **
The specified rule does not exist.
HTTP Status Code: 400

## Examples
<a name="API_SetRulePriorities_Examples"></a>

### Set the rule priority
<a name="API_SetRulePriorities_Example_1"></a>

This example sets the priority of the specified rule.

#### Sample Request
<a name="API_SetRulePriorities_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=SetRulePriorities
&RulePriorities.member.1.RuleArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3
&RulePriorities.member.1.Priority=5
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_SetRulePriorities_Example_1_Response"></a>

```
<SetRulePrioritiesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <SetRulePrioritiesResult>
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
        <Priority>5</Priority>
        <Actions>
          <member>
            <Type>forward</Type>
            <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
          </member>
        </Actions>
        <RuleArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3</RuleArn>
      </member>
    </Rules>
  </SetRulePrioritiesResult>
  <ResponseMetadata>
    <RequestId>4d7a8036-f3a7-11e5-9c02-8fd20490d5a6</RequestId>
  </ResponseMetadata>
</SetRulePrioritiesResponse>
```

## See Also
<a name="API_SetRulePriorities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/SetRulePriorities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/SetRulePriorities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/SetRulePriorities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/SetRulePriorities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/SetRulePriorities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/SetRulePriorities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/SetRulePriorities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/SetRulePriorities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/SetRulePriorities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/SetRulePriorities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
