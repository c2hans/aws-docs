---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Connection.html
---

# Connection
<a name="API_Connection"></a>

Contains information about a connection.

## Contents
<a name="API_Connection_Contents"></a>

 ** AuthorizationType **   <a name="eventbridge-Type-Connection-AuthorizationType"></a>
The authorization type specified for the connection.
OAUTH tokens are refreshed when a 401 or 407 response is returned.
Type: String
Valid Values: `BASIC | OAUTH_CLIENT_CREDENTIALS | API_KEY`
Required: No

 ** ConnectionArn **   <a name="eventbridge-Type-Connection-ConnectionArn"></a>
The ARN of the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`
Required: No

 ** ConnectionState **   <a name="eventbridge-Type-Connection-ConnectionState"></a>
The state of the connection.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | AUTHORIZED | DEAUTHORIZED | AUTHORIZING | DEAUTHORIZING | ACTIVE | FAILED_CONNECTIVITY`
Required: No

 ** CreationTime **   <a name="eventbridge-Type-Connection-CreationTime"></a>
A time stamp for the time that the connection was created.
Type: Timestamp
Required: No

 ** LastAuthorizedTime **   <a name="eventbridge-Type-Connection-LastAuthorizedTime"></a>
A time stamp for the time that the connection was last authorized.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="eventbridge-Type-Connection-LastModifiedTime"></a>
A time stamp for the time that the connection was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="eventbridge-Type-Connection-Name"></a>
The name of the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** StateReason **   <a name="eventbridge-Type-Connection-StateReason"></a>
The reason that the connection is in the connection state.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

## See Also
<a name="API_Connection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/Connection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/Connection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/Connection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
