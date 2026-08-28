---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentBindingPropertiesValueProperties.html
---

# ComponentBindingPropertiesValueProperties
<a name="API_ComponentBindingPropertiesValueProperties"></a>

Represents the data binding configuration for a specific property using data stored in AWS. For AWS connected properties, you can bind a property to data stored in an Amazon S3 bucket, an Amplify DataStore model or an authenticated user attribute.

## Contents
<a name="API_ComponentBindingPropertiesValueProperties_Contents"></a>

 ** bucket **   <a name="amplifyuibuilder-Type-ComponentBindingPropertiesValueProperties-bucket"></a>
An Amazon S3 bucket.
Type: String
Required: No

 ** defaultValue **   <a name="amplifyuibuilder-Type-ComponentBindingPropertiesValueProperties-defaultValue"></a>
The default value to assign to the property.
Type: String
Required: No

 ** field **   <a name="amplifyuibuilder-Type-ComponentBindingPropertiesValueProperties-field"></a>
The field to bind the data to.
Type: String
Required: No

 ** key **   <a name="amplifyuibuilder-Type-ComponentBindingPropertiesValueProperties-key"></a>
The storage key for an Amazon S3 bucket.
Type: String
Required: No

 ** model **   <a name="amplifyuibuilder-Type-ComponentBindingPropertiesValueProperties-model"></a>
An Amplify DataStore model.
Type: String
Required: No

 ** predicates **   <a name="amplifyuibuilder-Type-ComponentBindingPropertiesValueProperties-predicates"></a>
A list of predicates for binding a component's properties to data.
Type: Array of [Predicate](API_Predicate.md) objects
Required: No

 ** slotName **   <a name="amplifyuibuilder-Type-ComponentBindingPropertiesValueProperties-slotName"></a>
The name of a component slot.
Type: String
Required: No

 ** userAttribute **   <a name="amplifyuibuilder-Type-ComponentBindingPropertiesValueProperties-userAttribute"></a>
An authenticated user attribute.
Type: String
Required: No

## See Also
<a name="API_ComponentBindingPropertiesValueProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ComponentBindingPropertiesValueProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ComponentBindingPropertiesValueProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ComponentBindingPropertiesValueProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
