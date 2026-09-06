---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Step.html
---

# Step
<a name="API_Step"></a>

Step signifies the criteria to be used for routing to an agent

## Contents
<a name="API_Step_Contents"></a>

 ** Expiry **   <a name="connect-Type-Step-Expiry"></a>
An object to specify the expiration of a routing step.
Type: [Expiry](API_Expiry.md) object
Required: No

 ** Expression **   <a name="connect-Type-Step-Expression"></a>
A tagged union to specify expression for a routing step.
Type: [Expression](API_Expression.md) object
Required: No

 ** Status **   <a name="connect-Type-Step-Status"></a>
Represents status of the Routing step.
Type: String
Valid Values: `ACTIVE | INACTIVE | JOINED | EXPIRED`
Required: No

## See Also
<a name="API_Step_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Step)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Step)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Step)
