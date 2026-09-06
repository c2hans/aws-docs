---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Session.html
---

# Session
<a name="API_Session"></a>

Information about a session, including the session state, configuration, and timestamps.

## Contents
<a name="API_Session_Contents"></a>

 ** applicationId **   <a name="emrserverless-Type-Session-applicationId"></a>
The ID of the application that the session belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** arn **   <a name="emrserverless-Type-Session-arn"></a>
The Amazon Resource Name (ARN) of the session.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+\/sessions\/[0-9a-zA-Z]+`
Required: Yes

 ** createdAt **   <a name="emrserverless-Type-Session-createdAt"></a>
The date and time that the session was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="emrserverless-Type-Session-createdBy"></a>
The IAM principal that created the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+`
Required: Yes

 ** executionRoleArn **   <a name="emrserverless-Type-Session-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the execution role for the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::([0-9]{12}):(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

 ** releaseLabel **   <a name="emrserverless-Type-Session-releaseLabel"></a>
The Amazon EMR release label associated with the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/-]+`
Required: Yes

 ** sessionId **   <a name="emrserverless-Type-Session-sessionId"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** state **   <a name="emrserverless-Type-Session-state"></a>
The state of the session.
Type: String
Valid Values: `SUBMITTED | STARTING | STARTED | IDLE | BUSY | FAILED | TERMINATING | TERMINATED`
Required: Yes

 ** stateDetails **   <a name="emrserverless-Type-Session-stateDetails"></a>
Additional details about the current state of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** updatedAt **   <a name="emrserverless-Type-Session-updatedAt"></a>
The date and time that the session was last updated.
Type: Timestamp
Required: Yes

 ** billedResourceUtilization **   <a name="emrserverless-Type-Session-billedResourceUtilization"></a>
The aggregate vCPU, memory, and storage that AWS has billed for the session. The billed resources include a 1-minute minimum usage for workers, plus additional storage over 20 GB per worker. Note that billed resources do not include usage for idle pre-initialized workers.
Type: [ResourceUtilization](API_ResourceUtilization.md) object
Required: No

 ** configurationOverrides **   <a name="emrserverless-Type-Session-configurationOverrides"></a>
The configuration overrides for the session, including runtime configuration properties.
Type: [SessionConfigurationOverrides](API_SessionConfigurationOverrides.md) object
Required: No

 ** endedAt **   <a name="emrserverless-Type-Session-endedAt"></a>
The date and time that the session was terminated or failed.
Type: Timestamp
Required: No

 ** idleSince **   <a name="emrserverless-Type-Session-idleSince"></a>
The date and time that the session became idle.
Type: Timestamp
Required: No

 ** idleTimeoutMinutes **   <a name="emrserverless-Type-Session-idleTimeoutMinutes"></a>
The idle timeout in minutes for the session. After the session remains idle for this duration, it is automatically terminated.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000.
Required: No

 ** name **   <a name="emrserverless-Type-Session-name"></a>
The optional name of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** networkConfiguration **   <a name="emrserverless-Type-Session-networkConfiguration"></a>
The network configuration for customer VPC connectivity for the session.
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object
Required: No

 ** startedAt **   <a name="emrserverless-Type-Session-startedAt"></a>
The date and time that the session moved to a running state.
Type: Timestamp
Required: No

 ** tags **   <a name="emrserverless-Type-Session-tags"></a>
The tags assigned to the session.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[A-Za-z0-9 /_.:=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 /_.:=+@-]*`
Required: No

 ** totalExecutionDurationSeconds **   <a name="emrserverless-Type-Session-totalExecutionDurationSeconds"></a>
The total execution duration of the session in seconds.
Type: Long
Required: No

 ** totalResourceUtilization **   <a name="emrserverless-Type-Session-totalResourceUtilization"></a>
The aggregate vCPU, memory, and storage resources used from the time the session starts to execute, until the time the session terminates, rounded up to the nearest second.
Type: [TotalResourceUtilization](API_TotalResourceUtilization.md) object
Required: No

## See Also
<a name="API_Session_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/Session)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/Session)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/Session)
