---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyTargetGroupAttributes.html
---

# ModifyTargetGroupAttributes
<a name="API_ModifyTargetGroupAttributes"></a>

Modifies the specified attributes of the specified target group.

## Request Parameters
<a name="API_ModifyTargetGroupAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Attributes.member.N**
The target group attributes.
Type: Array of [TargetGroupAttribute](API_TargetGroupAttribute.md) objects
Required: Yes

 ** TargetGroupArn **
The Amazon Resource Name (ARN) of the target group.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyTargetGroupAttributes_ResponseElements"></a>

The following element is returned by the service.

 **Attributes.member.N**
Information about the target group attributes.
Type: Array of [TargetGroupAttribute](API_TargetGroupAttribute.md) objects

## Errors
<a name="API_ModifyTargetGroupAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ModifyTargetGroupAttributes_Examples"></a>

### Modify the deregistration delay timeout
<a name="API_ModifyTargetGroupAttributes_Example_1"></a>

This example sets the deregistration delay timeout for the specified target group to the specified value.

#### Sample Request
<a name="API_ModifyTargetGroupAttributes_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyTargetGroupAttributes
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Attributes.member.1.Key=deregistration_delay.timeout_seconds
&Attributes.member.1.Value=600
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyTargetGroupAttributes_Example_1_Response"></a>

```
<ModifyTargetGroupAttributesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <ModifyTargetGroupAttributesResult>
    <Attributes>
      <member>
        <Value>600</Value>
        <Key>deregistration_delay.timeout_seconds</Key>
      </member>
    </Attributes>
  </ModifyTargetGroupAttributesResult>
  <ResponseMetadata>
    <RequestId>bb8c272b-f455-11e5-a53c-67205c0d10fd</RequestId>
  </ResponseMetadata>
</ModifyTargetGroupAttributesResponse>
```

## See Also
<a name="API_ModifyTargetGroupAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ModifyTargetGroupAttributes)
