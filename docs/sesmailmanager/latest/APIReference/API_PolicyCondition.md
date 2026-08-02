---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_PolicyCondition.html
---

# PolicyCondition
<a name="API_PolicyCondition"></a>

The email traffic filtering conditions which are contained in a traffic policy resource.

## Contents
<a name="API_PolicyCondition_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BooleanExpression **   <a name="sesmailmanager-Type-PolicyCondition-BooleanExpression"></a>
This represents a boolean type condition matching on the incoming mail. It performs the boolean operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
Type: [IngressBooleanExpression](API_IngressBooleanExpression.md) object
Required: No

 ** IpExpression **   <a name="sesmailmanager-Type-PolicyCondition-IpExpression"></a>
This represents an IP based condition matching on the incoming mail. It performs the operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
Type: [IngressIpv4Expression](API_IngressIpv4Expression.md) object
Required: No

 ** Ipv6Expression **   <a name="sesmailmanager-Type-PolicyCondition-Ipv6Expression"></a>
This represents an IPv6 based condition matching on the incoming mail. It performs the operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
Type: [IngressIpv6Expression](API_IngressIpv6Expression.md) object
Required: No

 ** StringExpression **   <a name="sesmailmanager-Type-PolicyCondition-StringExpression"></a>
This represents a string based condition matching on the incoming mail. It performs the string operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
Type: [IngressStringExpression](API_IngressStringExpression.md) object
Required: No

 ** TlsExpression **   <a name="sesmailmanager-Type-PolicyCondition-TlsExpression"></a>
This represents a TLS based condition matching on the incoming mail. It performs the operation configured in 'Operator' and evaluates the 'Protocol' object against the 'Value'.
Type: [IngressTlsProtocolExpression](API_IngressTlsProtocolExpression.md) object
Required: No

## See Also
<a name="API_PolicyCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/PolicyCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/PolicyCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/PolicyCondition)
