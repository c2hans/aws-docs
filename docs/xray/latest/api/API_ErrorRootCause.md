---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_ErrorRootCause.html
---

# ErrorRootCause
<a name="API_ErrorRootCause"></a>

The root cause of a trace summary error.

## Contents
<a name="API_ErrorRootCause_Contents"></a>

 ** ClientImpacting **   <a name="xray-Type-ErrorRootCause-ClientImpacting"></a>
A flag that denotes that the root cause impacts the trace client.
Type: Boolean
Required: No

 ** Services **   <a name="xray-Type-ErrorRootCause-Services"></a>
A list of services corresponding to an error. A service identifies a segment and it contains a name, account ID, type, and inferred flag.
Type: Array of [ErrorRootCauseService](API_ErrorRootCauseService.md) objects
Required: No

## See Also
<a name="API_ErrorRootCause_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/ErrorRootCause)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/ErrorRootCause)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/ErrorRootCause)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
