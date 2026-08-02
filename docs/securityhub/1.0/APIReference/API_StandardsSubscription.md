---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StandardsSubscription.html
---

# StandardsSubscription
<a name="API_StandardsSubscription"></a>

A resource that represents your subscription to a supported standard.

## Contents
<a name="API_StandardsSubscription_Contents"></a>

 ** StandardsArn **   <a name="securityhub-Type-StandardsSubscription-StandardsArn"></a>
The ARN of the standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** StandardsInput **   <a name="securityhub-Type-StandardsSubscription-StandardsInput"></a>
A key-value pair of input for the standard.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: Yes

 ** StandardsStatus **   <a name="securityhub-Type-StandardsSubscription-StandardsStatus"></a>
The status of your subscription to the standard. Possible values are:
+  `PENDING` - The standard is in the process of being enabled. Or the standard is already enabled and AWS Security Hub CSPM is adding new controls to the standard.
+  `READY` - The standard is enabled.
+  `INCOMPLETE` - The standard could not be enabled completely. One or more errors (`StandardsStatusReason`) occurred when AWS Security Hub CSPM attempted to enable the standard.
+  `DELETING` - The standard is in the process of being disabled.
+  `FAILED` - The standard could not be disabled. One or more errors (`StandardsStatusReason`) occurred when AWS Security Hub CSPM attempted to disable the standard.
Type: String
Valid Values: `PENDING | READY | FAILED | DELETING | INCOMPLETE`
Required: Yes

 ** StandardsSubscriptionArn **   <a name="securityhub-Type-StandardsSubscription-StandardsSubscriptionArn"></a>
The ARN of the resource that represents your subscription to the standard.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Provider **   <a name="securityhub-Type-StandardsSubscription-Provider"></a>
The cloud provider whose resources the standard evaluates. For example, `AWS` or `Azure`.
Type: String
Valid Values: `AWS | Azure`
Required: No

 ** StandardsControlsUpdatable **   <a name="securityhub-Type-StandardsSubscription-StandardsControlsUpdatable"></a>
Specifies whether you can retrieve information about and configure individual controls that apply to the standard. Possible values are:
+  `READY_FOR_UPDATES` - Controls in the standard can be retrieved and configured.
+  `NOT_READY_FOR_UPDATES` - Controls in the standard cannot be retrieved or configured.
Type: String
Valid Values: `READY_FOR_UPDATES | NOT_READY_FOR_UPDATES`
Required: No

 ** StandardsStatusReason **   <a name="securityhub-Type-StandardsSubscription-StandardsStatusReason"></a>
The reason for the current status.
Type: [StandardsStatusReason](API_StandardsStatusReason.md) object
Required: No

## See Also
<a name="API_StandardsSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StandardsSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StandardsSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StandardsSubscription)
