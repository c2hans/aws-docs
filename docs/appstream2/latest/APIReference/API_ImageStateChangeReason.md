---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ImageStateChangeReason.html
---

# ImageStateChangeReason
<a name="API_ImageStateChangeReason"></a>

Describes the reason why the last image state change occurred.

## Contents
<a name="API_ImageStateChangeReason_Contents"></a>

 ** Code **   <a name="WorkSpacesApplications-Type-ImageStateChangeReason-Code"></a>
The state change reason code.
Type: String
Valid Values: `INTERNAL_ERROR | IMAGE_BUILDER_NOT_AVAILABLE | IMAGE_COPY_FAILURE | IMAGE_UPDATE_FAILURE | IMAGE_IMPORT_FAILURE`
Required: No

 ** Message **   <a name="WorkSpacesApplications-Type-ImageStateChangeReason-Message"></a>
The state change reason message.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ImageStateChangeReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ImageStateChangeReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ImageStateChangeReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ImageStateChangeReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
