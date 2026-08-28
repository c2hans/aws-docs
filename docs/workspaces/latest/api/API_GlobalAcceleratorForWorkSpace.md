---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_GlobalAcceleratorForWorkSpace.html
---

# GlobalAcceleratorForWorkSpace
<a name="API_GlobalAcceleratorForWorkSpace"></a>

Describes the Global Accelerator for WorkSpaces.

## Contents
<a name="API_GlobalAcceleratorForWorkSpace_Contents"></a>

 ** Mode **   <a name="WorkSpaces-Type-GlobalAcceleratorForWorkSpace-Mode"></a>
Indicates if Global Accelerator for WorkSpaces is enabled, disabled, or the same mode as the associated directory.
Type: String
Valid Values: `ENABLED_AUTO | DISABLED | INHERITED`
Required: Yes

 ** PreferredProtocol **   <a name="WorkSpaces-Type-GlobalAcceleratorForWorkSpace-PreferredProtocol"></a>
Indicates the preferred protocol for Global Accelerator.
Type: String
Valid Values: `TCP | NONE | INHERITED`
Required: No

## See Also
<a name="API_GlobalAcceleratorForWorkSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/GlobalAcceleratorForWorkSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/GlobalAcceleratorForWorkSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/GlobalAcceleratorForWorkSpace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
