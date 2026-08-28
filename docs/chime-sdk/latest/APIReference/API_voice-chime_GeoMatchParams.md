---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GeoMatchParams.html
---

# GeoMatchParams
<a name="API_voice-chime_GeoMatchParams"></a>

The country and area code for a proxy phone number in a proxy phone session.

## Contents
<a name="API_voice-chime_GeoMatchParams_Contents"></a>

 ** AreaCode **   <a name="chimesdk-Type-voice-chime_GeoMatchParams-AreaCode"></a>
The area code.
Type: String
Pattern: `^$|^[0-9]{3,3}$`
Required: Yes

 ** Country **   <a name="chimesdk-Type-voice-chime_GeoMatchParams-Country"></a>
The country.
Type: String
Pattern: `^$|^[A-Z]{2,2}$`
Required: Yes

## See Also
<a name="API_voice-chime_GeoMatchParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/GeoMatchParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/GeoMatchParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/GeoMatchParams)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
