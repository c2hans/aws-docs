---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ChangeInput.html
---

# ChangeInput
<a name="API_ChangeInput"></a>

Specifies a change to apply to a collaboration.

## Contents
<a name="API_ChangeInput_Contents"></a>

 ** specification **   <a name="API-Type-ChangeInput-specification"></a>
The specification details for the change. The structure depends on the specification type.
Type: [ChangeSpecification](API_ChangeSpecification.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** specificationType **   <a name="API-Type-ChangeInput-specificationType"></a>
The type of specification for the change. Currently supports `MEMBER` for member-related changes.
Type: String
Valid Values: `MEMBER | COLLABORATION`
Required: Yes

## See Also
<a name="API_ChangeInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ChangeInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ChangeInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ChangeInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
