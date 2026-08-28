---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_RuntimeSessionData.html
---

# RuntimeSessionData
<a name="API_amazon-q-connect_RuntimeSessionData"></a>

The list of key-value pairs that are stored on the session.

## Contents
<a name="API_amazon-q-connect_RuntimeSessionData_Contents"></a>

 ** key **   <a name="connect-Type-amazon-q-connect_RuntimeSessionData-key"></a>
The key of the data stored on the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** value **   <a name="connect-Type-amazon-q-connect_RuntimeSessionData-value"></a>
The value of the data stored on the session.
Type: [RuntimeSessionDataValue](API_amazon-q-connect_RuntimeSessionDataValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_amazon-q-connect_RuntimeSessionData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/RuntimeSessionData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/RuntimeSessionData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/RuntimeSessionData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
