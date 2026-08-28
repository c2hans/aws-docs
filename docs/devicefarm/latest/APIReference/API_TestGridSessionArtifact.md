---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridSessionArtifact.html
---

# TestGridSessionArtifact
<a name="API_TestGridSessionArtifact"></a>

Artifacts are video and other files that are produced in the process of running a browser in an automated context.

**Note**
Video elements might be broken up into multiple artifacts as they grow in size during creation.

## Contents
<a name="API_TestGridSessionArtifact_Contents"></a>

 ** filename **   <a name="devicefarm-Type-TestGridSessionArtifact-filename"></a>
The file name of the artifact.
Type: String
Required: No

 ** type **   <a name="devicefarm-Type-TestGridSessionArtifact-type"></a>
The kind of artifact.
Type: String
Valid Values: `UNKNOWN | VIDEO | SELENIUM_LOG`
Required: No

 ** url **   <a name="devicefarm-Type-TestGridSessionArtifact-url"></a>
A semi-stable URL to the content of the object.
Type: String
Required: No

## See Also
<a name="API_TestGridSessionArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/TestGridSessionArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/TestGridSessionArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/TestGridSessionArtifact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
