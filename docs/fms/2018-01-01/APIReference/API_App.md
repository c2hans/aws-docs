---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_App.html
---

# App
<a name="API_App"></a>

An individual AWS Firewall Manager application.

## Contents
<a name="API_App_Contents"></a>

 ** AppName **   <a name="fms-Type-App-AppName"></a>
The application's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** Port **   <a name="fms-Type-App-Port"></a>
The application's port number, for example `80`.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: Yes

 ** Protocol **   <a name="fms-Type-App-Protocol"></a>
The IP protocol name or number. The name can be one of `tcp`, `udp`, or `icmp`. For information on possible numbers, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## See Also
<a name="API_App_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/App)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/App)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/App)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
