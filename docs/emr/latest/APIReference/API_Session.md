---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_Session.html
---

# Session
<a name="API_Session"></a>

Detailed information about a Spark Connect session.

## Contents
<a name="API_Session_Contents"></a>

 ** Arn **   <a name="EMR-Type-Session-Arn"></a>
The Amazon Resource Name (ARN) of the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** ClusterId **   <a name="EMR-Type-Session-ClusterId"></a>
The ID of the cluster that the session belongs to.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** Id **   <a name="EMR-Type-Session-Id"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** State **   <a name="EMR-Type-Session-State"></a>
The current state of the session. Valid values are `SUBMITTED`, `STARTING`, `STARTED`, `IDLE`, `BUSY`, `TERMINATING`, `TERMINATED`, and `FAILED`.
Type: String
Valid Values: `SUBMITTED | STARTING | STARTED | IDLE | BUSY | TERMINATING | TERMINATED | FAILED`
Required: Yes

 ** AccountId **   <a name="EMR-Type-Session-AccountId"></a>
The AWS account ID that owns the session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** CreatedAt **   <a name="EMR-Type-Session-CreatedAt"></a>
The date and time that the session was created.
Type: Timestamp
Required: No

 ** EndedAt **   <a name="EMR-Type-Session-EndedAt"></a>
The date and time that the session was terminated or failed.
Type: Timestamp
Required: No

 ** EngineConfigurations **   <a name="EMR-Type-Session-EngineConfigurations"></a>
The configuration overrides for the session. Only runtime configuration overrides are supported.
Type: Array of [Configuration](API_Configuration.md) objects
Required: No

 ** ExecutionRoleArn **   <a name="EMR-Type-Session-ExecutionRoleArn"></a>
The execution role ARN for the session. Amazon EMR uses this role to access AWS resources on your behalf during session execution.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
Required: No

 ** IdleSince **   <a name="EMR-Type-Session-IdleSince"></a>
The date and time that the session last entered the `IDLE` state.
Type: Timestamp
Required: No

 ** MonitoringConfiguration **   <a name="EMR-Type-Session-MonitoringConfiguration"></a>
The monitoring configuration for the session.
Type: [SessionMonitoringConfiguration](API_SessionMonitoringConfiguration.md) object
Required: No

 ** Name **   <a name="EMR-Type-Session-Name"></a>
The name of the session, if one was provided at creation time.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ReleaseLabel **   <a name="EMR-Type-Session-ReleaseLabel"></a>
The Amazon EMR release label of the cluster that the session is running on.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ServerUrl **   <a name="EMR-Type-Session-ServerUrl"></a>
The Spark Connect server URL for the session. Use this URL with the `Credentials` returned by `GetSessionEndpoint` to connect directly to the session over VPC peering.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** SessionIdleTimeoutInMinutes **   <a name="EMR-Type-Session-SessionIdleTimeoutInMinutes"></a>
The idle timeout, in minutes. If the session is idle for this duration, Amazon EMR automatically terminates it.
Type: Long
Required: No

 ** StartedAt **   <a name="EMR-Type-Session-StartedAt"></a>
The date and time that the session entered the `STARTED` state.
Type: Timestamp
Required: No

 ** StateChangeReason **   <a name="EMR-Type-Session-StateChangeReason"></a>
A human-readable message describing the most recent state change.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Tags **   <a name="EMR-Type-Session-Tags"></a>
The tags associated with the session.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** UpdatedAt **   <a name="EMR-Type-Session-UpdatedAt"></a>
The date and time that the session was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Session_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Session)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Session)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Session)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
