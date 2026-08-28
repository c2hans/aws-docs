---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingPrincipalObject.html
---

# ThingPrincipalObject
<a name="API_ThingPrincipalObject"></a>

An object that represents the principal and the type of relation it has with the thing.

## Contents
<a name="API_ThingPrincipalObject_Contents"></a>

 ** principal **   <a name="iot-Type-ThingPrincipalObject-principal"></a>
The principal of the thing principal object.
Type: String
Required: Yes

 ** thingPrincipalType **   <a name="iot-Type-ThingPrincipalObject-thingPrincipalType"></a>
The type of the relation you want to specify when you attach a principal to a thing. The value defaults to `NON_EXCLUSIVE_THING`.
+  `EXCLUSIVE_THING` - Attaches the specified principal to the specified thing, exclusively. The thing will be the only thing that’s attached to the principal.
+  `NON_EXCLUSIVE_THING` - Attaches the specified principal to the specified thing. Multiple things can be attached to the principal.
Type: String
Valid Values: `EXCLUSIVE_THING | NON_EXCLUSIVE_THING`
Required: No

## See Also
<a name="API_ThingPrincipalObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingPrincipalObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingPrincipalObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingPrincipalObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
