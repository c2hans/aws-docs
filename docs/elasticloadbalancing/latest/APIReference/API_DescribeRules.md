---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeRules.html
---

# DescribeRules
<a name="API_DescribeRules"></a>

Describes the specified rules or the rules for the specified listener. You must specify either a listener or rules.

## Request Parameters
<a name="API_DescribeRules_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ListenerArn **
The Amazon Resource Name (ARN) of the listener.
Type: String
Required: No

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 ** PageSize **
The maximum number of results to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

 **RuleArns.member.N**
The Amazon Resource Names (ARN) of the rules.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeRules_ResponseElements"></a>

The following elements are returned by the service.

 ** NextMarker **
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.
Type: String

 **Rules.member.N**
Information about the rules.
Type: Array of [Rule](API_Rule.md) objects

## Errors
<a name="API_DescribeRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ListenerNotFound **
The specified listener does not exist.
HTTP Status Code: 400

 ** RuleNotFound **
The specified rule does not exist.
HTTP Status Code: 400

 ** UnsupportedProtocol **
The specified protocol is not supported.
HTTP Status Code: 400

## Examples
<a name="API_DescribeRules_Examples"></a>

### Describe a rule
<a name="API_DescribeRules_Example_1"></a>

This example describes the specified rule.

#### Sample Request
<a name="API_DescribeRules_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeRules
&RuleArns.member.1=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeRules_Example_1_Response"></a>

```
<DescribeRulesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeRulesResult>
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
            <TargetGroupArn>arn:aws:elasticloadbalancing:ua-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
          </member>
        </Actions>
        <RuleArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee</RuleArn>
      </member>
    </Rules>
  </DescribeRulesResult>
  <ResponseMetadata>
    <RequestId>74926cf3-f3a3-11e5-b543-9f2c3fbb9bee</RequestId>
  </ResponseMetadata>
</DescribeRulesResponse>
```

### Describe the rules for a listener
<a name="API_DescribeRules_Example_2"></a>

This example describes the rules for the specified listener. The output includes the default rule and any other rules that you've defined.

#### Sample Request
<a name="API_DescribeRules_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeRules
&ListenerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeRules_Example_2_Response"></a>

```
<DescribeRulesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeRulesResult>
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
      <member>
        <IsDefault>true</IsDefault>
        <Conditions />
        <Priority>default</Priority>
        <Actions>
          <member>
            <Type>forward</Type>
            <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
          </member>
        </Actions>
        <RuleArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/fd906cf3d7a9d36d</RuleArn>
      </member>
    </Rules>
  </DescribeRulesResult>
  <ResponseMetadata>
    <RequestId>d8581c8d-f3a3-11e5-8a24-ffe2bf8623ae</RequestId>
  </ResponseMetadata>
</DescribeRulesResponse>
```

## See Also
<a name="API_DescribeRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeRules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
