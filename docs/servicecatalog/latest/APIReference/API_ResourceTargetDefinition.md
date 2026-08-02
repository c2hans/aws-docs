---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ResourceTargetDefinition.html
---

# ResourceTargetDefinition
<a name="API_ResourceTargetDefinition"></a>

Information about a change to a resource attribute.

## Contents
<a name="API_ResourceTargetDefinition_Contents"></a>

 ** Attribute **   <a name="servicecatalog-Type-ResourceTargetDefinition-Attribute"></a>
The attribute to be changed.
Type: String
Valid Values: `PROPERTIES | METADATA | CREATIONPOLICY | UPDATEPOLICY | DELETIONPOLICY | TAGS`
Required: No

 ** Name **   <a name="servicecatalog-Type-ResourceTargetDefinition-Name"></a>
If the attribute is `Properties`, the value is the name of the property. Otherwise, the value is null.
Type: String
Required: No

 ** RequiresRecreation **   <a name="servicecatalog-Type-ResourceTargetDefinition-RequiresRecreation"></a>
If the attribute is `Properties`, indicates whether a change to this property causes the resource to be re-created.
Type: String
Valid Values: `NEVER | CONDITIONALLY | ALWAYS`
Required: No

## See Also
<a name="API_ResourceTargetDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ResourceTargetDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ResourceTargetDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ResourceTargetDefinition)
