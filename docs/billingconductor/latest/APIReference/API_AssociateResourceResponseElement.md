---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AssociateResourceResponseElement.html
---

# AssociateResourceResponseElement
<a name="API_AssociateResourceResponseElement"></a>

A resource association result for a percentage custom line item.

## Contents
<a name="API_AssociateResourceResponseElement_Contents"></a>

 ** Arn **   <a name="billingconductor-Type-AssociateResourceResponseElement-Arn"></a>
The resource ARN that was associated to the custom line item.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:(customlineitem|billinggroup)/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** Error **   <a name="billingconductor-Type-AssociateResourceResponseElement-Error"></a>
An `AssociateResourceError` that will populate if the resource association fails.
Type: [AssociateResourceError](API_AssociateResourceError.md) object
Required: No

## See Also
<a name="API_AssociateResourceResponseElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/AssociateResourceResponseElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/AssociateResourceResponseElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/AssociateResourceResponseElement)
