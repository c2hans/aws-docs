---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ParentEntityUpdateRequest.html
---

# ParentEntityUpdateRequest
<a name="API_ParentEntityUpdateRequest"></a>

The parent entity update request.

## Contents
<a name="API_ParentEntityUpdateRequest_Contents"></a>

 ** updateType **   <a name="tm-Type-ParentEntityUpdateRequest-updateType"></a>
The type of the update.
Type: String
Valid Values: `UPDATE | DELETE`
Required: Yes

 ** parentEntityId **   <a name="tm-Type-ParentEntityUpdateRequest-parentEntityId"></a>
The ID of the parent entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$ROOT|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_ParentEntityUpdateRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ParentEntityUpdateRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ParentEntityUpdateRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ParentEntityUpdateRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
