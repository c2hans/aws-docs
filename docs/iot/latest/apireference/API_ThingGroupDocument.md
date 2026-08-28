---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingGroupDocument.html
---

# ThingGroupDocument
<a name="API_ThingGroupDocument"></a>

The thing group search index document.

## Contents
<a name="API_ThingGroupDocument_Contents"></a>

 ** attributes **   <a name="iot-Type-ThingGroupDocument-attributes"></a>
The thing group attributes.
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_.,@/:#-]+`
Value Length Constraints: Maximum length of 800.
Value Pattern: `[a-zA-Z0-9_.,@/:#=\[\]-]*`
Required: No

 ** parentGroupNames **   <a name="iot-Type-ThingGroupDocument-parentGroupNames"></a>
Parent group names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** thingGroupDescription **   <a name="iot-Type-ThingGroupDocument-thingGroupDescription"></a>
The thing group description.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[\p{Graph}\x20]*`
Required: No

 ** thingGroupId **   <a name="iot-Type-ThingGroupDocument-thingGroupId"></a>
The thing group ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** thingGroupName **   <a name="iot-Type-ThingGroupDocument-thingGroupName"></a>
The thing group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

## See Also
<a name="API_ThingGroupDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingGroupDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingGroupDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingGroupDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
