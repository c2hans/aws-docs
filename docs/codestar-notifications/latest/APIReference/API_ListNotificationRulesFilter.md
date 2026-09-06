---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListNotificationRulesFilter.html
---

# ListNotificationRulesFilter
<a name="API_ListNotificationRulesFilter"></a>

Information about a filter to apply to the list of returned notification rules. You can filter by event type, owner, resource, or target.

## Contents
<a name="API_ListNotificationRulesFilter_Contents"></a>

 ** Name **   <a name="codestarnotifications-Type-ListNotificationRulesFilter-Name"></a>
The name of the attribute you want to use to filter the returned notification rules.
Type: String
Valid Values: `EVENT_TYPE_ID | CREATED_BY | RESOURCE | TARGET_ADDRESS`
Required: Yes

 ** Value **   <a name="codestarnotifications-Type-ListNotificationRulesFilter-Value"></a>
The value of the attribute you want to use to filter the returned notification rules. For example, if you specify filtering by *RESOURCE* in Name, you might specify the ARN of a pipeline in AWS CodePipeline for the value.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

## See Also
<a name="API_ListNotificationRulesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/ListNotificationRulesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/ListNotificationRulesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/ListNotificationRulesFilter)
