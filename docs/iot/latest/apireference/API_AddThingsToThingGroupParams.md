---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AddThingsToThingGroupParams.html
---

# AddThingsToThingGroupParams
<a name="API_AddThingsToThingGroupParams"></a>

Parameters used when defining a mitigation action that move a set of things to a thing group.

## Contents
<a name="API_AddThingsToThingGroupParams_Contents"></a>

 ** thingGroupNames **   <a name="iot-Type-AddThingsToThingGroupParams-thingGroupNames"></a>
The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you can't add a thing to more than one group in the same hierarchy.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** overrideDynamicGroups **   <a name="iot-Type-AddThingsToThingGroupParams-overrideDynamicGroups"></a>
Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic thing groups.
Type: Boolean
Required: No

## See Also
<a name="API_AddThingsToThingGroupParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AddThingsToThingGroupParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AddThingsToThingGroupParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AddThingsToThingGroupParams)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
