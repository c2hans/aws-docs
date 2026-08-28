---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_Status.html
---

# Status
<a name="API_Status"></a>

An object that represents the status of an entity, component, component type, or workspace.

## Contents
<a name="API_Status_Contents"></a>

 ** error **   <a name="tm-Type-Status-error"></a>
The error message.
Type: [ErrorDetails](API_ErrorDetails.md) object
Required: No

 ** state **   <a name="tm-Type-Status-state"></a>
The current state of the entity, component, component type, or workspace.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | ERROR`
Required: No

## See Also
<a name="API_Status_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/Status)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/Status)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/Status)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
