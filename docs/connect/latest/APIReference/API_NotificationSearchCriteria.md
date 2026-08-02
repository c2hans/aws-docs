---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_NotificationSearchCriteria.html
---

# NotificationSearchCriteria
<a name="API_NotificationSearchCriteria"></a>

The search criteria to be used to return notifications.

## Contents
<a name="API_NotificationSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-NotificationSearchCriteria-AndConditions"></a>
A list of conditions that must all be satisfied.
Type: Array of [NotificationSearchCriteria](#API_NotificationSearchCriteria) objects
Required: No

 ** OrConditions **   <a name="connect-Type-NotificationSearchCriteria-OrConditions"></a>
A list of conditions to be met, where at least one condition must be satisfied.
Type: Array of [NotificationSearchCriteria](#API_NotificationSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-NotificationSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_NotificationSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/NotificationSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/NotificationSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/NotificationSearchCriteria)
