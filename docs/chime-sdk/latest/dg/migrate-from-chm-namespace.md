---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html
---

# Migrating from the Amazon Chime namespace
<a name="migrate-from-chm-namespace"></a>

The Amazon Chime SDK exposes APIs on a set of endpoints. Although you can make HTTPS requests directly to the endpoints, many customers use the AWS SDK in their applications to call the service APIs. The AWS SDK is available in different languages, and it simplifies API calling by encapsulating request signing and retry logic. The AWS SDK includes a namespace for each service endpoint.

When first launched, the Amazon Chime SDK shared a single endpoint with the Amazon Chime application. As a result, solutions used the `Chime` namespace in the AWS SDK to call the Amazon Chime application and the Amazon Chime SDK APIs.

The Amazon Chime SDK now provides dedicated endpoints for each sub-service, such as meetings and PSTN audio. Each endpoint is addressable through a dedicated namespace in the AWS SDK.

The following topics list the services, namespaces, and endpoints, and describe how to use them in code and with the AWS CLI.

**Topics**
+ [Endpoints, namespaces, and CLI commands](#endpoint-namespace-cli)
+ [Migration help for each service](#help-per-service)
+ [API mapping](#name-end-map)

## Endpoints, namespaces, and CLI commands
<a name="endpoint-namespace-cli"></a>

The following table lists the dedicated Amazon Chime SDK namespaces, endpoints, and CLI commands. The links take you to more information about each service.

| Endpoint | AWS SDK Namespace | AWS SDK CLI |
| --- | --- | --- |
| [identity-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) | ChimeSDKIdentity | [chime-sdk-identity](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-identity/index.html) |
| [media-pipelines-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Media_Pipelines.html) | ChimeSDKMediaPipelines | [chime-sdk-media-pipelines](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-media-pipelines/index.html) |
| [meetings-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Meetings.html) | ChimeSDKMeetings | [chime-sdk-meetings](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-meetings/index.html) |
| [messaging-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) | ChimeSDKMessaging | [chime-sdk-messaging](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-messaging/index.html) |
| [voice-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html) | ChimeSDKVoice | [chime-sdk-voice](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-voice/index.html) |

## Migration help for each service
<a name="help-per-service"></a>

All customers should consider using the dedicated Amazon Chime SDK endpoints for access to the latest Amazon Chime SDK features, APIs, and AWS Regions. If you use the shared endpoint with the `Chime` namespace, the following migration guides can help understand the technical differences before migrating.
+ [Migrating to the Amazon Chime SDKIdentity namespace](identity-namespace-migration.md)
+ [Migrating to the Amazon Chime SDKMediaPipelines namespace](migrate-pipelines.md)
+ [Migrating to the Amazon Chime SDKMeetings namespace](meeting-namespace-migration.md)
+ [Migrating to the Amazon Chime SDKMessaging namespace](messaging-namespace-migration.md)
+ [Migrating to the Amazon Chime SDKVoice namespace](voice-namespace-migration.md)

## API mapping
<a name="name-end-map"></a>

The following table lists the APIs in the `Chime` namespace, and their corresponding dedicated namespaces and APIs. Some of the dedicated APIs differ from the `Chime` APIs, and the table indicates those instances.

- **[AssociatePhoneNumbersWithVoiceConnector](https://docs.aws.amazon.com/chime/latest/APIReference/API_AssociatePhoneNumbersWithVoiceConnector.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [AssociatePhoneNumbersWithVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnector.html)

- ** [AssociatePhoneNumbersWithVoiceConnectorGroup](https://docs.aws.amazon.com/chime/latest/APIReference/API_AssociatePhoneNumbersWithVoiceConnectorGroup.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [AssociatePhoneNumbersWithVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnectorGroup.html)

- ** [BatchCreateAttendee](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchCreateAttendee.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [BatchCreateAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchCreateAttendee.html)

- ** [BatchCreateChannelMembership](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchCreateChannelMembership.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [BatchCreateChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembership.html)

- ** [CreateAppInstance](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAppInstance.html) **
  - **Dedicated namespace:**  identity-chime
  - **Dedicated namespace API:** [CreateAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstance.html)

- ** [CreateAppInstanceAdmin](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAppInstanceAdmin.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [CreateAppInstanceAdmin](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceAdmin.html)

- **[CreateAppInstanceUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAppInstanceUser.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [CreateAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceUser.html)

- **[CreateAttendee](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAttendee.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [CreateAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html)

- **[CreateChannel](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannel.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [CreateChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html)

- ** [CreateChannelBan](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannelBan.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [CreateChannelBan](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelBan.html)

- ** [CreateChannelMembership](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannelMembership.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [CreateChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelMembership.html)

- ** [CreateChannelModerator](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannelModerator.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [CreateChannelModerator](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelModerator.html)

- ** [CreateMediaCapturePipeline](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMediaCapturePipeline.html) **
  - **Dedicated namespace:** media-pipelines-chime
  - **Dedicated namespace API:** [CreateMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html)

- ** [CreateMeeting](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeeting.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [CreateMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html)

- ** [CreateMeetingWithAttendees](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeetingWithAttendees.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [CreateMeetingWithAttendees](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeetingWithAttendees.html)

- ** [CreateMeetingDialOut](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeetingDialOut.html)**\*** **
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- ** [CreateProxySession](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateProxySession.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [CreateProxySession](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateProxySession.html)

- ** [CreateSipMediaApplication](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateSipMediaApplication.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [CreateSipMediaApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplication.html)

- ** [CreateSipMediaApplicationCall](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateSipMediaApplicationCall.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [CreateSipMediaApplicationCall](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplicationCall.html)

- ** [CreateSipRule](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateSipRule.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [CreateSipRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipRule.html)

- ** [CreateVoiceConnector](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateVoiceConnector.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [CreateVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnector.html)

- ** [CreateVoiceConnectorGroup](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateVoiceConnectorGroup.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [CreateVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnectorGroup.html)

- ** [DeleteAppInstance](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstance.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [DeleteAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstance.html)

- ** [DeleteAppInstanceAdmin](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstanceAdmin.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [DeleteAppInstanceAdmin](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceAdmin.html)

- ** [DeleteAppInstanceStreamingConfigurations](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstanceStreamingConfigurations.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DeleteAppInstanceStreamingConfigurations](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteAppInstanceStreamingConfigurations.html)

- ** [DeleteAppInstanceUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstanceUser.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [DeleteAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceUser.html)

- ** [DeleteAttendee](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAttendee.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [DeleteAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteAttendee.html)

- ** [DeleteChannel](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannel.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DeleteChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannel.html)

- ** [DeleteChannelBan](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelBan.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DeleteChannelBan](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelBan.html)

- ** [DeleteChannelMembership](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelMembership.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DeleteChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMembership.html)

- ** [DeleteChannelMessage](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelMessage.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DeleteChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMessage.html)

- ** [DeleteChannelModerator](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelModerator.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DeleteChannelModerator](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelModerator.html)

- ** [DeleteMediaCapturePipeline](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteMediaCapturePipeline.html) **
  - **Dedicated namespace:**  media-pipelines-chime
  - **Dedicated namespace API:** [DeleteMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html)

- ** [DeleteMeeting](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteMeeting.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [DeleteMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteMeeting.html)

- ** [DeleteProxySession](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteProxySession.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteProxySession](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteProxySession.html)

- ** [DeleteSipMediaApplication](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteSipMediaApplication.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteSipMediaApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipMediaApplication.html)

- ** [DeleteSipRule](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteSipRule.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteSipRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipRule.html)

- ** [DeleteVoiceConnector](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnector.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnector.html)

- ** [DeleteVoiceConnectorEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorEmergencyCallingConfiguration.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteVoiceConnectorEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorEmergencyCallingConfiguration.html)

- ** [DeleteVoiceConnectorGroup](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorGroup.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorGroup.html)

- ** [DeleteVoiceConnectorOrigination](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorOrigination.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteVoiceConnectorOrigination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorOrigination.html)

- ** [DeleteVoiceConnectorProxy](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorProxy.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteVoiceConnectorProxy](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorProxy.html)

- ** [DeleteVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorStreamingConfiguration.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorStreamingConfiguration.html)

- ** [DeleteVoiceConnectorTermination](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorTermination.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteVoiceConnectorTermination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTermination.html)

- ** [DeleteVoiceConnectorTerminationCredentials](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorTerminationCredentials.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DeleteVoiceConnectorTerminationCredentials](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTerminationCredentials.html)

- ** [DescribeAppInstance](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeAppInstance.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [DescribeAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstance.html)

- **[DescribeAppInstanceAdmin](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeAppInstanceAdmin.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [DescribeAppInstanceAdmin](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceAdmin.html)

- **[DescribeAppInstanceUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeAppInstanceUser.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [DescribeAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceUser.html)

- **[DescribeChannel](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannel.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DescribeChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannel.html)

- **[DescribeChannelBan](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelBan.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DescribeChannelBan](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelBan.html)

- **[DescribeChannelMembership](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelMembership.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DescribeChannelMembership](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembership.html)

- **[DescribeChannelMembershipForAppInstanceUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelMembershipForAppInstanceUser.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DescribeChannelMembershipForAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembershipForAppInstanceUser.html)

- **[DescribeChannelModeratedByAppInstanceUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelModeratedByAppInstanceUser.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DescribeChannelModeratedByAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModeratedByAppInstanceUser.html)

- **[DescribeChannelModerator](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelModerator.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [DescribeChannelModerator](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModerator.html)

- **[DisassociatePhoneNumbersFromVoiceConnector](https://docs.aws.amazon.com/chime/latest/APIReference/API_DisassociatePhoneNumbersFromVoiceConnector.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DisassociatePhoneNumbersFromVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnector.html)

- **[DisassociatePhoneNumbersFromVoiceConnectorGroup](https://docs.aws.amazon.com/chime/latest/APIReference/API_DisassociatePhoneNumbersFromVoiceConnectorGroup.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [DisassociatePhoneNumbersFromVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnectorGroup.html)

- **[GetAppInstanceRetentionSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAppInstanceRetentionSettings.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [GetAppInstanceRetentionSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_GetAppInstanceRetentionSettings.html)

- **[GetAppInstanceStreamingConfigurations](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAppInstanceStreamingConfigurations.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [GetMessagingStreamingConfigurations](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingStreamingConfigurations.html)

- **[GetAttendee](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAttendee.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [GetAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetAttendee.html)

- ** [GetChannelMessage](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetChannelMessage.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [GetChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessage.html)

- ** [GetMediaCapturePipeline](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetMediaCapturePipeline.html) **
  - **Dedicated namespace:** media-pipelines-chime
  - **Dedicated namespace API:** [GetMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaCapturePipeline.html)

- ** [GetMeeting](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetMeeting.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [GetMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html)

- ** [GetMessagingSessionEndpoint](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetMessagingSessionEndpoint.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [GetMessagingSessionEndpoint](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingSessionEndpoint.html)

- **[GetProxySession](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetProxySession.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetProxySession](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetProxySession.html)

- **[GetSipMediaApplication](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetSipMediaApplication.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetSipMediaApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplication.html)

- **[GetSipMediaApplicationLoggingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetSipMediaApplicationLoggingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetSipMediaApplicationLoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplicationLoggingConfiguration.html)

- ** [GetSipRule](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetSipRule.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetSipRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipRule.html)

- ** [GetVoiceConnector](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnector.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnector.html)

- ** [GetVoiceConnectorEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorEmergencyCallingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetVoiceConnectorEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration.html)

- **[GetVoiceConnectorGroup](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorGroup.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorGroup.html)

- **[GetVoiceConnectorLoggingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorLoggingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetVoiceConnectorLoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorLoggingConfiguration.html)

- **[GetVoiceConnectorOrigination](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorOrigination.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetVoiceConnectorOrigination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorOrigination.html)

- **[GetVoiceConnectorProxy](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorProxy.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetVoiceConnectorProxy](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorProxy.html)

- **[GetVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorStreamingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorStreamingConfiguration.html)

- **[GetVoiceConnectorTermination](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorTermination.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetVoiceConnectorTermination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTermination.html)

- **[GetVoiceConnectorTerminationHealth](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorTerminationHealth.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [GetVoiceConnectorTerminationHealth](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTerminationHealth.html)

- **[ListAppInstanceAdmins](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAppInstanceAdmins.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [ListAppInstanceAdmins](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceAdmins.html)

- **[ListAppInstances](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAppInstances.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [ListAppInstances](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstances.html)

- **[ListAppInstanceUsers](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAppInstanceUsers.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [ListAppInstanceUsers](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceUsers.html)

- **[ListAttendees](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAttendees.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [ListAttendees](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListAttendees.html)

- **[ListAttendeeTags](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAttendeeTags.html)**\*****
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- **[ListChannelBans](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelBans.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [ListChannelBans](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelBans.html)

- **[ListChannelMemberships](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelMemberships.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [ListChannelMemberships](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMemberships.html)

- **[ListChannelMembershipsForAppInstanceUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelMembershipsForAppInstanceUser.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [ListChannelMembershipsForAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html)

- ** [ListChannelMessages](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelMessages.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [ListChannelMessages](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMessages.html)

- ** [ListChannelModerators](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelModerators.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [ListChannelModerators](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelModerators.html)

- ** [ListChannels](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannels.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [ListChannels](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannels.html)

- ** [ListChannelsModeratedByAppInstanceUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelsModeratedByAppInstanceUser.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [ListChannelsModeratedByAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsModeratedByAppInstanceUser.html)

- **[ListMediaCapturePipelines](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListMediaCapturePipelines.html)**
  - **Dedicated namespace:** media-pipelines-chime
  - **Dedicated namespace API:** [ListMediaCapturePipelines](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaCapturePipelines.html)

- **[ListMeetings](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListMeetings.html)**\*****
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- ** [ListMeetingTags](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListMeetingTags.html)**\+****
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [ListTagsForResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html)

- **[ListProxySessions](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListProxySessions.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [ListProxySessions](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListProxySessions.html)

- **[ListSipMediaApplications](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListSipMediaApplications.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [ListSipMediaApplications](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipMediaApplications.html)

- ** [ListSipRules](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListSipRules.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [ListSipRules](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipRules.html)

- **[ListTagsForResource](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListTagsForResource.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [ListTagsForResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListTagsForResource.html)

- **[ListVoiceConnectorGroups](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListVoiceConnectorGroups.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [ListVoiceConnectorGroups](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorGroups.html)

- **[ListVoiceConnectors](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListVoiceConnectors.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [ListVoiceConnectors](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectors.html)

- **[ListVoiceConnectorTerminationCredentials](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListVoiceConnectorTerminationCredentials.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [ListVoiceConnectorTerminationCredentials](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorTerminationCredentials.html)

- **[PutAppInstanceRetentionSettings](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutAppInstanceRetentionSettings.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [PutAppInstanceRetentionSettings](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_PutAppInstanceRetentionSettings.html)

- **[PutAppInstanceStreamingConfigurations](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutAppInstanceStreamingConfigurations.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [PutMessagingStreamingConfigurations](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutMessagingStreamingConfigurations.html)

- **[PutSipMediaApplicationLoggingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutSipMediaApplicationLoggingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [PutSipMediaApplicationLoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutSipMediaApplicationLoggingConfiguration.html)

- **[PutVoiceConnectorEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorEmergencyCallingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [PutVoiceConnectorEmergencyCallingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorEmergencyCallingConfiguration.html)

- **[PutVoiceConnectorLoggingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorLoggingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [PutVoiceConnectorLoggingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorLoggingConfiguration.html)

- **[PutVoiceConnectorOrigination](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorOrigination.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [PutVoiceConnectorOrigination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorOrigination.html)

- **[PutVoiceConnectorProxy](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorProxy.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [PutVoiceConnectorProxy](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorProxy.html)

- **[PutVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorStreamingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [PutVoiceConnectorStreamingConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorStreamingConfiguration.html)

- ** [PutVoiceConnectorTermination](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorTermination.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [PutVoiceConnectorTermination](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTermination.html)

- **[PutVoiceConnectorTerminationCredentials](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorTerminationCredentials.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [PutVoiceConnectorTerminationCredentials](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTerminationCredentials.html)

- **[RedactChannelMessage](https://docs.aws.amazon.com/chime/latest/APIReference/API_RedactChannelMessage.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [RedactChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_RedactChannelMessage.html)

- **[SendChannelMessage](https://docs.aws.amazon.com/chime/latest/APIReference/API_messaging-chime_SendChannelMessage.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [SendChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html)

- **[StartMeetingTranscription](https://docs.aws.amazon.com/chime/latest/APIReference/API_StartMeetingTranscription.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [StartMeetingTranscription](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StartMeetingTranscription.html)

- **[StopMeetingTranscription](https://docs.aws.amazon.com/chime/latest/APIReference/API_StopMeetingTranscription.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [StopMeetingTranscription](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StopMeetingTranscription.html)

- **[TagAttendee](https://docs.aws.amazon.com/chime/latest/APIReference/API_TagAttendee.html)**\*****
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- ** [TagMeeting](https://docs.aws.amazon.com/chime/latest/APIReference/API_TagMeeting.html)**\+****
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html)

- **[TagResource](https://docs.aws.amazon.com/chime/latest/APIReference/API_TagResource.html)**
  - **Dedicated namespace:** identity-chime / **Dedicated namespace API:** [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_TagResource.html)
  - **Dedicated namespace:** media-pipelines-chime / **Dedicated namespace API:** [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_TagResource.html)
  - **Dedicated namespace:** meetings-chime / **Dedicated namespace API:** [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meetings-chime_TagResource.html)
  - **Dedicated namespace:** messaging-chime / **Dedicated namespace API:** [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_TagResource.html)
  - **Dedicated namespace:** voice-chime / **Dedicated namespace API:** [TagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_TagResource.html)

- **[UntagAttendee](https://docs.aws.amazon.com/chime/latest/APIReference/API_UntagAttendee.html)**\*****
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- **[UntagMeeting](https://docs.aws.amazon.com/chime/latest/APIReference/API_UntagMeeting.html)**\+****
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [UntagResource](https://docs.aws.amazon.com/chime/latest/APIReference/API_meeting-chime_UntagResource.html)

- **[UntagResource](https://docs.aws.amazon.com/chime/latest/APIReference/API_UntagResource.html)**
  - **Dedicated namespace:** identity-chime  / **Dedicated namespace API:** [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UntagResource.html)
  - **Dedicated namespace:** media-pipelines-chime / **Dedicated namespace API:** [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UntagResource.html)
  - **Dedicated namespace:** meetings-chime / **Dedicated namespace API:** [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meetings-chime_UntagResource.html)
  - **Dedicated namespace:** messaging-chime / **Dedicated namespace API:** [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UntagResource.html)
  - **Dedicated namespace:** voice-chime / **Dedicated namespace API:** [UntagResource](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UntagResource.html)

- **[UpdateAppInstance](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateAppInstance.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [UpdateAppInstance](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstance.html)

- **[UpdateAppInstanceUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateAppInstanceUser.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [UpdateAppInstanceUser](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstanceUser.html)

- **[UpdateChannel](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateChannel.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [UpdateChannel](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannel.html)

- **[UpdateChannelMessage](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateChannelMessage.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [UpdateChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelMessage.html)

- **[UpdateChannelReadMarker](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateChannelReadMarker.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [UpdateChannelReadMarker](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelReadMarker.html)

- ** [UpdateProxySession](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateProxySession.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [UpdateProxySession](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateProxySession.html)

- ** [UpdateSipMediaApplication](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateSipMediaApplication.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [UpdateSipMediaApplication](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplication.html)

- ** [UpdateSipMediaApplicationCall](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateSipMediaApplicationCall.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [UpdateSipMediaApplicationCall](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplicationCall.html)

- ** [UpdateSipRule](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateSipRule.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [UpdateSipRule](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipRule.html)

- ** [UpdateVoiceConnector](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateVoiceConnector.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [UpdateVoiceConnector](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnector.html)

- ** [UpdateVoiceConnectorGroup](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateVoiceConnectorGroup.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [UpdateVoiceConnectorGroup](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnectorGroup.html)

- ** [ValidateE911Address](https://docs.aws.amazon.com/chime/latest/APIReference/API_ValidateE911Address.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [ValidateE911Address](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ValidateE911Address.html)

**\+** API has been superseded by an API with another name.

**\* **API is no longer available.
