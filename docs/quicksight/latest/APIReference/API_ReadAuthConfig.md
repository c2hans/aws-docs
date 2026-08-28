---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReadAuthConfig.html
---

# ReadAuthConfig
<a name="API_ReadAuthConfig"></a>

Read-only authentication configuration containing non-sensitive authentication details for action connectors.

## Contents
<a name="API_ReadAuthConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AuthenticationMetadata **   <a name="QS-Type-ReadAuthConfig-AuthenticationMetadata"></a>
The authentication metadata containing configuration details specific to the authentication type.
Type: [ReadAuthenticationMetadata](API_ReadAuthenticationMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** AuthenticationType **   <a name="QS-Type-ReadAuthConfig-AuthenticationType"></a>
The type of authentication being used (BASIC, API\_KEY, OAUTH2\_CLIENT\_CREDENTIALS, or OAUTH2\_AUTHORIZATION\_CODE).
Type: String
Valid Values: `BASIC | API_KEY | OAUTH2_CLIENT_CREDENTIALS | NONE | IAM | OAUTH2_AUTHORIZATION_CODE`
Required: Yes

## See Also
<a name="API_ReadAuthConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReadAuthConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReadAuthConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReadAuthConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
