---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ResponderErrorMaskingForHttpCode.html
---

# ResponderErrorMaskingForHttpCode
<a name="API_ResponderErrorMaskingForHttpCode"></a>

Describes the masking for HTTP error codes.

## Contents
<a name="API_ResponderErrorMaskingForHttpCode_Contents"></a>

 ** action **   <a name="rtbfabric-Type-ResponderErrorMaskingForHttpCode-action"></a>
The action for the error..
Type: String
Valid Values: `NO_BID | PASSTHROUGH`
Required: Yes

 ** httpCode **   <a name="rtbfabric-Type-ResponderErrorMaskingForHttpCode-httpCode"></a>
The HTTP error code.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `DEFAULT|4XX|5XX|\d{3}`
Required: Yes

 ** loggingTypes **   <a name="rtbfabric-Type-ResponderErrorMaskingForHttpCode-loggingTypes"></a>
The error log type.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `NONE | METRIC | RESPONSE`
Required: Yes

 ** responseLoggingPercentage **   <a name="rtbfabric-Type-ResponderErrorMaskingForHttpCode-responseLoggingPercentage"></a>
The percentage of response logging.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_ResponderErrorMaskingForHttpCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ResponderErrorMaskingForHttpCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ResponderErrorMaskingForHttpCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ResponderErrorMaskingForHttpCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
