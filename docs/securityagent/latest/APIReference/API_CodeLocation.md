---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CodeLocation.html
---

# CodeLocation
<a name="API_CodeLocation"></a>

Represents a location in source code associated with a security finding.

## Contents
<a name="API_CodeLocation_Contents"></a>

 ** filePath **   <a name="securityagent-Type-CodeLocation-filePath"></a>
The absolute path to the file containing the code location.
Type: String
Required: Yes

 ** label **   <a name="securityagent-Type-CodeLocation-label"></a>
The role of this location in the vulnerability, such as source or sink.
Type: String
Required: No

 ** lineEnd **   <a name="securityagent-Type-CodeLocation-lineEnd"></a>
The ending line number of the code location.
Type: Integer
Required: No

 ** lineStart **   <a name="securityagent-Type-CodeLocation-lineStart"></a>
The starting line number of the code location.
Type: Integer
Required: No

## See Also
<a name="API_CodeLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CodeLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CodeLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CodeLocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
