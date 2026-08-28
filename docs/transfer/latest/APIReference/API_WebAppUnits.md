---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_WebAppUnits.html
---

# WebAppUnits
<a name="API_WebAppUnits"></a>

Contains an integer value that represents the value for number of concurrent connections or the user sessions on your web app.

## Contents
<a name="API_WebAppUnits_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Provisioned **   <a name="TransferFamily-Type-WebAppUnits-Provisioned"></a>
An integer that represents the number of units for your desired number of concurrent connections, or the number of user sessions on your web app at the same time.
Each increment allows an additional 250 concurrent sessions: a value of `1` sets the number of concurrent sessions to 250; `2` sets a value of 500, and so on.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_WebAppUnits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/WebAppUnits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/WebAppUnits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/WebAppUnits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
