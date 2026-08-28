---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CommandPayload.html
---

# CommandPayload
<a name="API_CommandPayload"></a>

The command payload object that contains the instructions for the device to process.

## Contents
<a name="API_CommandPayload_Contents"></a>

 ** content **   <a name="iot-Type-CommandPayload-content"></a>
The static payload file for the command.
Type: Base64-encoded binary data object
Required: No

 ** contentType **   <a name="iot-Type-CommandPayload-contentType"></a>
The content type that specifies the format type of the payload file. This field must use a type/subtype format, such as `application/json`. For information about various content types, see [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types).
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_CommandPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CommandPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CommandPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CommandPayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
