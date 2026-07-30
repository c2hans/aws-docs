---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ResourceTargetDefinition.html
---

# ResourceTargetDefinition
<a name="API_ResourceTargetDefinition"></a>

The field that CloudFormation will change, such as the name of a resource's property, and whether the resource will be recreated.

## Contents
<a name="API_ResourceTargetDefinition_Contents"></a>

 ** AfterValue **
The value of the property after the change is executed. Large values can be truncated.
Type: String
Required: No

 ** AfterValueFrom **
Indicates the source of the after value. Valid value:
+  `TEMPLATE` – The after value comes from the new template.
Only present for drift-aware change sets.
Type: String
Valid Values: `TEMPLATE`
Required: No

 ** Attribute **
Indicates which resource attribute is triggering this update, such as a change in the resource attribute's `Metadata`, `Properties`, or `Tags`.
Type: String
Valid Values: `Properties | Metadata | CreationPolicy | UpdatePolicy | DeletionPolicy | UpdateReplacePolicy | Tags`
Required: No

 ** AttributeChangeType **
The type of change to be made to the property if the change is executed.
+  `Add` The item will be added.
+  `Remove` The item will be removed.
+  `Modify` The item will be modified.
+  `SyncWithActual` The drift status of this item will be reset but the item will not be modified.
Type: String
Valid Values: `Add | Remove | Modify | SyncWithActual`
Required: No

 ** BeforeValue **
The value of the property before the change is executed. Large values can be truncated.
Type: String
Required: No

 ** BeforeValueFrom **
Indicates the source of the before value. Valid values:
+  `ACTUAL_STATE` – The before value represents current actual state.
+  `PREVIOUS_DEPLOYMENT_STATE` – The before value represents the previous CloudFormation deployment state.
Only present for drift-aware change sets.
Type: String
Valid Values: `PREVIOUS_DEPLOYMENT_STATE | ACTUAL_STATE`
Required: No

 ** Drift **
Detailed drift information for the resource property, including actual values, previous deployment values, and drift detection timestamps.
Type: [LiveResourceDrift](API_LiveResourceDrift.md) object
Required: No

 ** Name **
If the `Attribute` value is `Properties`, the name of the property. For all other attributes, the value is null.
Type: String
Required: No

 ** Path **
The property path of the property.
Type: String
Required: No

 ** RequiresRecreation **
If the `Attribute` value is `Properties`, indicates whether a change to this property causes the resource to be recreated. The value can be `Never`, `Always`, or `Conditionally`. To determine the conditions for a `Conditionally` recreation, see the update behavior for that property in the [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the * AWS CloudFormation User Guide*.
Type: String
Valid Values: `Never | Conditionally | Always`
Required: No

## See Also
<a name="API_ResourceTargetDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceTargetDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceTargetDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceTargetDefinition)
