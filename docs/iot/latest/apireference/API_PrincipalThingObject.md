---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_PrincipalThingObject.html
---

# PrincipalThingObject
<a name="API_PrincipalThingObject"></a>

An object that represents the thing and the type of relation it has with the principal.

## Contents
<a name="API_PrincipalThingObject_Contents"></a>

 ** thingName **   <a name="iot-Type-PrincipalThingObject-thingName"></a>
The name of the thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** thingPrincipalType **   <a name="iot-Type-PrincipalThingObject-thingPrincipalType"></a>
The type of the relation you want to specify when you attach a principal to a thing. The value defaults to `NON_EXCLUSIVE_THING`.
+  `EXCLUSIVE_THING` - Attaches the specified principal to the specified thing, exclusively. The thing will be the only thing that’s attached to the principal.
+  `NON_EXCLUSIVE_THING` - Attaches the specified principal to the specified thing. Multiple things can be attached to the principal.
Type: String
Valid Values: `EXCLUSIVE_THING | NON_EXCLUSIVE_THING`
Required: No

## See Also
<a name="API_PrincipalThingObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/PrincipalThingObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/PrincipalThingObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/PrincipalThingObject)
