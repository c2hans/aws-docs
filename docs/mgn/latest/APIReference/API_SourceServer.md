---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_SourceServer.html
---

# SourceServer
<a name="API_SourceServer"></a>

## Contents
<a name="API_SourceServer_Contents"></a>

 ** applicationID **   <a name="mgn-Type-SourceServer-applicationID"></a>
Source server application ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `app-[0-9a-zA-Z]{17}`
Required: No

 ** arn **   <a name="mgn-Type-SourceServer-arn"></a>
Source server ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** connectorAction **   <a name="mgn-Type-SourceServer-connectorAction"></a>
Source Server connector action.
Type: [SourceServerConnectorAction](API_SourceServerConnectorAction.md) object
Required: No

 ** dataReplicationInfo **   <a name="mgn-Type-SourceServer-dataReplicationInfo"></a>
Source server data replication info.
Type: [DataReplicationInfo](API_DataReplicationInfo.md) object
Required: No

 ** fqdnForActionFramework **   <a name="mgn-Type-SourceServer-fqdnForActionFramework"></a>
Source server fqdn for action framework.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** isArchived **   <a name="mgn-Type-SourceServer-isArchived"></a>
Source server archived status.
Type: Boolean
Required: No

 ** launchedInstance **   <a name="mgn-Type-SourceServer-launchedInstance"></a>
Source server launched instance.
Type: [LaunchedInstance](API_LaunchedInstance.md) object
Required: No

 ** lifeCycle **   <a name="mgn-Type-SourceServer-lifeCycle"></a>
Source server lifecycle state.
Type: [LifeCycle](API_LifeCycle.md) object
Required: No

 ** replicationType **   <a name="mgn-Type-SourceServer-replicationType"></a>
Source server replication type.
Type: String
Valid Values: `AGENT_BASED | SNAPSHOT_SHIPPING`
Required: No

 ** sourceProperties **   <a name="mgn-Type-SourceServer-sourceProperties"></a>
Source server properties.
Type: [SourceProperties](API_SourceProperties.md) object
Required: No

 ** sourceServerID **   <a name="mgn-Type-SourceServer-sourceServerID"></a>
Source server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

 ** tags **   <a name="mgn-Type-SourceServer-tags"></a>
Source server Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** userProvidedID **   <a name="mgn-Type-SourceServer-userProvidedID"></a>
Source server user provided ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`
Required: No

 ** vcenterClientID **   <a name="mgn-Type-SourceServer-vcenterClientID"></a>
Source server vCenter client id.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `vcc-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_SourceServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/SourceServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/SourceServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/SourceServer)
