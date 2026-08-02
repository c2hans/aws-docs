---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressTlsProtocolExpression.html
---

# IngressTlsProtocolExpression
<a name="API_IngressTlsProtocolExpression"></a>

The structure for a TLS related condition matching on the incoming mail.

## Contents
<a name="API_IngressTlsProtocolExpression_Contents"></a>

 ** Evaluate **   <a name="sesmailmanager-Type-IngressTlsProtocolExpression-Evaluate"></a>
The left hand side argument of a TLS condition expression.
Type: [IngressTlsProtocolToEvaluate](API_IngressTlsProtocolToEvaluate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Operator **   <a name="sesmailmanager-Type-IngressTlsProtocolExpression-Operator"></a>
The matching operator for a TLS condition expression.
Type: String
Valid Values: `MINIMUM_TLS_VERSION | IS`
Required: Yes

 ** Value **   <a name="sesmailmanager-Type-IngressTlsProtocolExpression-Value"></a>
The right hand side argument of a TLS condition expression.
Type: String
Valid Values: `TLS1_2 | TLS1_3`
Required: Yes

## See Also
<a name="API_IngressTlsProtocolExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressTlsProtocolExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressTlsProtocolExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressTlsProtocolExpression)
