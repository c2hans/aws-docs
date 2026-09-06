---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ResourceChangeDetail.html
---

# ResourceChangeDetail
<a name="API_ResourceChangeDetail"></a>

Information about a change to a resource attribute.

## Contents
<a name="API_ResourceChangeDetail_Contents"></a>

 ** CausingEntity **   <a name="servicecatalog-Type-ResourceChangeDetail-CausingEntity"></a>
The ID of the entity that caused the change.
Type: String
Required: No

 ** Evaluation **   <a name="servicecatalog-Type-ResourceChangeDetail-Evaluation"></a>
For static evaluations, the value of the resource attribute will change and the new value is known. For dynamic evaluations, the value might change, and any new value will be determined when the plan is updated.
Type: String
Valid Values: `STATIC | DYNAMIC`
Required: No

 ** Target **   <a name="servicecatalog-Type-ResourceChangeDetail-Target"></a>
Information about the resource attribute to be modified.
Type: [ResourceTargetDefinition](API_ResourceTargetDefinition.md) object
Required: No

## See Also
<a name="API_ResourceChangeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ResourceChangeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ResourceChangeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ResourceChangeDetail)
