---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspacesPool.html
---

# WorkspacesPool
<a name="API_WorkspacesPool"></a>

Describes a pool of WorkSpaces.

## Contents
<a name="API_WorkspacesPool_Contents"></a>

 ** BundleId **   <a name="WorkSpaces-Type-WorkspacesPool-BundleId"></a>
The identifier of the bundle used by the pool.
Type: String
Pattern: `^wsb-[0-9a-z]{8,63}$`
Required: Yes

 ** CapacityStatus **   <a name="WorkSpaces-Type-WorkspacesPool-CapacityStatus"></a>
The capacity status for the pool
Type: [CapacityStatus](API_CapacityStatus.md) object
Required: Yes

 ** CreatedAt **   <a name="WorkSpaces-Type-WorkspacesPool-CreatedAt"></a>
The time the pool was created.
Type: Timestamp
Required: Yes

 ** DirectoryId **   <a name="WorkSpaces-Type-WorkspacesPool-DirectoryId"></a>
The identifier of the directory used by the pool.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** PoolArn **   <a name="WorkSpaces-Type-WorkspacesPool-PoolArn"></a>
The Amazon Resource Name (ARN) for the pool.
Type: String
Pattern: `^arn:aws[a-z-]{0,7}:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** PoolId **   <a name="WorkSpaces-Type-WorkspacesPool-PoolId"></a>
The identifier of a pool.
Type: String
Pattern: `^wspool-[0-9a-z]{9}$`
Required: Yes

 ** PoolName **   <a name="WorkSpaces-Type-WorkspacesPool-PoolName"></a>
The name of the pool.
Type: String
Pattern: `^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$`
Required: Yes

 ** RunningMode **   <a name="WorkSpaces-Type-WorkspacesPool-RunningMode"></a>
The running mode of the pool.
Type: String
Valid Values: `AUTO_STOP | ALWAYS_ON`
Required: Yes

 ** State **   <a name="WorkSpaces-Type-WorkspacesPool-State"></a>
The current state of the pool.
Type: String
Valid Values: `CREATING | DELETING | RUNNING | STARTING | STOPPED | STOPPING | UPDATING`
Required: Yes

 ** ApplicationSettings **   <a name="WorkSpaces-Type-WorkspacesPool-ApplicationSettings"></a>
The persistent application settings for users of the pool.
Type: [ApplicationSettingsResponse](API_ApplicationSettingsResponse.md) object
Required: No

 ** Description **   <a name="WorkSpaces-Type-WorkspacesPool-Description"></a>
The description of the pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9_./() -]+$`
Required: No

 ** Errors **   <a name="WorkSpaces-Type-WorkspacesPool-Errors"></a>
The pool errors.
Type: Array of [WorkspacesPoolError](API_WorkspacesPoolError.md) objects
Required: No

 ** TimeoutSettings **   <a name="WorkSpaces-Type-WorkspacesPool-TimeoutSettings"></a>
The amount of time that a pool session remains active after users disconnect. If they try to reconnect to the pool session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new pool instance.
Type: [TimeoutSettings](API_TimeoutSettings.md) object
Required: No

## See Also
<a name="API_WorkspacesPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspacesPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspacesPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspacesPool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
