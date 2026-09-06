---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyListenerAttributes.html
---

# ModifyListenerAttributes
<a name="API_ModifyListenerAttributes"></a>

Modifies the specified attributes of the specified listener.

## Request Parameters
<a name="API_ModifyListenerAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Attributes.member.N**
The listener attributes.
Type: Array of [ListenerAttribute](API_ListenerAttribute.md) objects
Required: Yes

 ** ListenerArn **
The Amazon Resource Name (ARN) of the listener.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyListenerAttributes_ResponseElements"></a>

The following element is returned by the service.

 **Attributes.member.N**
Information about the listener attributes.
Type: Array of [ListenerAttribute](API_ListenerAttribute.md) objects

## Errors
<a name="API_ModifyListenerAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** ListenerNotFound **
The specified listener does not exist.
HTTP Status Code: 400

## See Also
<a name="API_ModifyListenerAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ModifyListenerAttributes)
