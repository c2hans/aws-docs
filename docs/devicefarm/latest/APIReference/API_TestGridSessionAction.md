---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridSessionAction.html
---

# TestGridSessionAction
<a name="API_TestGridSessionAction"></a>

An action taken by a [TestGridSession](API_TestGridSession.md) browser instance.

## Contents
<a name="API_TestGridSessionAction_Contents"></a>

 ** action **   <a name="devicefarm-Type-TestGridSessionAction-action"></a>
The action taken by the session.
Type: String
Required: No

 ** duration **   <a name="devicefarm-Type-TestGridSessionAction-duration"></a>
The time, in milliseconds, that the action took to complete in the browser.
Type: Long
Required: No

 ** requestMethod **   <a name="devicefarm-Type-TestGridSessionAction-requestMethod"></a>
HTTP method that the browser used to make the request.
Type: String
Required: No

 ** started **   <a name="devicefarm-Type-TestGridSessionAction-started"></a>
The time that the session invoked the action.
Type: Timestamp
Required: No

 ** statusCode **   <a name="devicefarm-Type-TestGridSessionAction-statusCode"></a>
HTTP status code returned to the browser when the action was taken.
Type: String
Required: No

## See Also
<a name="API_TestGridSessionAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/TestGridSessionAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/TestGridSessionAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/TestGridSessionAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
