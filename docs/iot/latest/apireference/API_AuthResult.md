---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuthResult.html
---

# AuthResult
<a name="API_AuthResult"></a>

The authorizer result.

## Contents
<a name="API_AuthResult_Contents"></a>

 ** allowed **   <a name="iot-Type-AuthResult-allowed"></a>
The policies and statements that allowed the specified action.
Type: [Allowed](API_Allowed.md) object
Required: No

 ** authDecision **   <a name="iot-Type-AuthResult-authDecision"></a>
The final authorization decision of this scenario. Multiple statements are taken into account when determining the authorization decision. An explicit deny statement can override multiple allow statements.
Type: String
Valid Values: `ALLOWED | EXPLICIT_DENY | IMPLICIT_DENY`
Required: No

 ** authInfo **   <a name="iot-Type-AuthResult-authInfo"></a>
Authorization information.
Type: [AuthInfo](API_AuthInfo.md) object
Required: No

 ** denied **   <a name="iot-Type-AuthResult-denied"></a>
The policies and statements that denied the specified action.
Type: [Denied](API_Denied.md) object
Required: No

 ** missingContextValues **   <a name="iot-Type-AuthResult-missingContextValues"></a>
Contains any missing context values found while evaluating policy.
Type: Array of strings
Required: No

## See Also
<a name="API_AuthResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuthResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuthResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuthResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
