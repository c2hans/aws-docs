---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StreamUrlSummary.html
---

# StreamUrlSummary
<a name="API_StreamUrlSummary"></a>

Describes a stream URL. This is a summary view that omits the full configuration, such as launch arguments and display settings. To retrieve the complete configuration, call [GetStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamUrl.html).

## Contents
<a name="API_StreamUrlSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="gameliftstreams-Type-StreamUrlSummary-Arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream URL across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamurl/[stream group resource ID]/[stream URL resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`
Required: Yes

 ** ApplicationArn **   <a name="gameliftstreams-Type-StreamUrlSummary-ApplicationArn"></a>
The application that runs in the stream sessions.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`
Required: No

 ** CreatedAt **   <a name="gameliftstreams-Type-StreamUrlSummary-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp
Required: No

 ** Description **   <a name="gameliftstreams-Type-StreamUrlSummary-Description"></a>
The descriptive label for the stream URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`
Required: No

 ** ExpiresAt **   <a name="gameliftstreams-Type-StreamUrlSummary-ExpiresAt"></a>
The date and time when the stream URL expires and stops accepting new stream sessions. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp
Required: No

 ** RemainingUses **   <a name="gameliftstreams-Type-StreamUrlSummary-RemainingUses"></a>
The number of times the stream URL can still be used to start a stream session.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** SessionLengthSeconds **   <a name="gameliftstreams-Type-StreamUrlSummary-SessionLengthSeconds"></a>
The maximum length of time, in seconds, that a stream session started from this stream URL can run.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

 ** Status **   <a name="gameliftstreams-Type-StreamUrlSummary-Status"></a>
The current status of the stream URL. Possible statuses include the following:
+  `ACTIVE`: The stream URL is valid and can start stream sessions.
+  `EXPIRED`: The stream URL has passed its expiration time and can no longer start stream sessions.
+  `REVOKED`: The stream URL was revoked and can no longer start stream sessions.
+  `LIMIT_REACHED`: The stream URL has been used the maximum number of times and can no longer start stream sessions.
Type: String
Valid Values: `ACTIVE | EXPIRED | REVOKED | LIMIT_REACHED`
Required: No

 ** StatusReason **   <a name="gameliftstreams-Type-StreamUrlSummary-StatusReason"></a>
Additional information about why the stream URL is in its current status. Amazon GameLift Streams populates this value when the status is `REVOKED`. Possible values include the following:
+  `userRevoked`: You revoked the stream URL.
+  `revokedAndTerminatingSessions`: You revoked the stream URL and Amazon GameLift Streams is ending its running stream sessions.
+  `revokedAndSessionsTerminated`: You revoked the stream URL and its running stream sessions have ended.
+  `streamGroupDeleted`: The stream group was deleted, which revoked the stream URL.
+  `applicationDeleted`: The application was deleted, which revoked the stream URL.
Type: String
Valid Values: `userRevoked | revokedAndTerminatingSessions | revokedAndSessionsTerminated | streamGroupDeleted | applicationDeleted`
Required: No

 ** StreamGroupArn **   <a name="gameliftstreams-Type-StreamUrlSummary-StreamGroupArn"></a>
The stream group that runs the stream sessions.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`
Required: No

 ** StreamUrl **   <a name="gameliftstreams-Type-StreamUrlSummary-StreamUrl"></a>
The shareable stream URL. Distribute this URL to end users so that they can start and play a stream session in a hosted web player. Treat the stream URL as a secret. Anyone who has it can start a stream session until the stream URL expires, is revoked, or reaches its usage limit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** StreamUrlId **   <a name="gameliftstreams-Type-StreamUrlSummary-StreamUrlId"></a>
The unique identifier for the stream URL resource, for example `su-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** UsageLimit **   <a name="gameliftstreams-Type-StreamUrlSummary-UsageLimit"></a>
The maximum number of times the stream URL can start a stream session.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_StreamUrlSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/StreamUrlSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/StreamUrlSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/StreamUrlSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
