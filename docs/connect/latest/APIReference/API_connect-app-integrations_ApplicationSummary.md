---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-app-integrations_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_connect-app-integrations_ApplicationSummary"></a>

Summary information about the Application.

## Contents
<a name="API_connect-app-integrations_ApplicationSummary_Contents"></a>

 ** ApplicationType **   <a name="connect-Type-connect-app-integrations_ApplicationSummary-ApplicationType"></a>
The type of application.
Type: String
Valid Values: `STANDARD | SERVICE | MCP_SERVER`
Required: No

 ** Arn **   <a name="connect-Type-connect-app-integrations_ApplicationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the Application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** CreatedTime **   <a name="connect-Type-connect-app-integrations_ApplicationSummary-CreatedTime"></a>
The time when the application was created.
Type: Timestamp
Required: No

 ** Id **   <a name="connect-Type-connect-app-integrations_ApplicationSummary-Id"></a>
A unique identifier for the Application.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** IsService **   <a name="connect-Type-connect-app-integrations_ApplicationSummary-IsService"></a>
 *This member has been deprecated.*
Indicates whether the application is a service.
Type: Boolean
Required: No

 ** LastModifiedTime **   <a name="connect-Type-connect-app-integrations_ApplicationSummary-LastModifiedTime"></a>
The time when the application was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-connect-app-integrations_ApplicationSummary-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\/\._ \-]+$`
Required: No

 ** Namespace **   <a name="connect-Type-connect-app-integrations_ApplicationSummary-Namespace"></a>
The namespace of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 211.
Pattern: `^[a-zA-Z0-9\/\._\-]+$`
Required: No

## See Also
<a name="API_connect-app-integrations_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/ApplicationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
