---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceState.html
---

# ServiceState
<a name="API_ServiceState"></a>

A structure that contains information about the current state of a service, including its latest change events such as deployments and other state-changing activities.

## Contents
<a name="API_ServiceState_Contents"></a>

 ** LatestChangeEvents **   <a name="applicationsignals-Type-ServiceState-LatestChangeEvents"></a>
An array containing the most recent change events for this service, such as deployments, with information about when they occurred and who initiated them.
Type: Array of [ChangeEvent](API_ChangeEvent.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** Service **   <a name="applicationsignals-Type-ServiceState-Service"></a>
The key attributes that identify this service, including Type, Name, and Environment information.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: Yes

 ** AttributeFilters **   <a name="applicationsignals-Type-ServiceState-AttributeFilters"></a>
The attribute filters that were applied when retrieving this service state information.
Type: Array of [AttributeFilter](API_AttributeFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_ServiceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
