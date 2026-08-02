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
| [identity-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Identity.html) | ChimeSDKIdentity | [https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-identity/index.html](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-identity/index.html) |
| [media-pipelines-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Media_Pipelines.html) | ChimeSDKMediaPipelines | [https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-media-pipelines/index.html](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-media-pipelines/index.html) |
| [meetings-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Meetings.html) | ChimeSDKMeetings | [https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-meetings/index.html](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-meetings/index.html) |
| [messaging-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Messaging.html) | ChimeSDKMessaging | [https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-messaging/index.html](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-messaging/index.html) |
| [voice-chime](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html) | ChimeSDKVoice | [https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-voice/index.html](https://docs.aws.amazon.com/cli/latest/reference/chime-sdk-voice/index.html) |

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

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_AssociatePhoneNumbersWithVoiceConnector.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_AssociatePhoneNumbersWithVoiceConnector.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnector.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnector.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_AssociatePhoneNumbersWithVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_AssociatePhoneNumbersWithVoiceConnectorGroup.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnectorGroup.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchCreateAttendee.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchCreateAttendee.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchCreateAttendee.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchCreateAttendee.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchCreateChannelMembership.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchCreateChannelMembership.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembership.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembership.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAppInstance.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAppInstance.html) **
  - **Dedicated namespace:**  identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstance.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstance.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAppInstanceAdmin.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAppInstanceAdmin.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceAdmin.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceAdmin.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAppInstanceUser.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAppInstanceUser.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceUser.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateAppInstanceUser.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAttendee.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAttendee.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannel.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannel.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannelBan.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannelBan.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelBan.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelBan.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannelMembership.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannelMembership.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelMembership.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelMembership.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannelModerator.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateChannelModerator.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelModerator.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelModerator.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMediaCapturePipeline.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMediaCapturePipeline.html) **
  - **Dedicated namespace:** media-pipelines-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeeting.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeeting.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeetingWithAttendees.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeetingWithAttendees.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeetingWithAttendees.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeetingWithAttendees.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeetingDialOut.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateMeetingDialOut.html)**\*** **
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateProxySession.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateProxySession.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateProxySession.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateProxySession.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateSipMediaApplication.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateSipMediaApplication.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplication.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplication.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateSipMediaApplicationCall.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateSipMediaApplicationCall.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplicationCall.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplicationCall.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateSipRule.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateSipRule.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipRule.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipRule.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateVoiceConnector.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateVoiceConnector.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnector.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnector.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateVoiceConnectorGroup.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnectorGroup.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstance.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstance.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstance.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstance.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstanceAdmin.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstanceAdmin.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceAdmin.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceAdmin.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstanceStreamingConfigurations.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstanceStreamingConfigurations.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteAppInstanceStreamingConfigurations.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteAppInstanceStreamingConfigurations.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstanceUser.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAppInstanceUser.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceUser.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceUser.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAttendee.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteAttendee.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteAttendee.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteAttendee.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannel.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannel.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannel.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannel.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelBan.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelBan.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelBan.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelBan.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelMembership.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelMembership.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMembership.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMembership.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelMessage.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelMessage.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMessage.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMessage.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelModerator.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteChannelModerator.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelModerator.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelModerator.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteMediaCapturePipeline.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteMediaCapturePipeline.html) **
  - **Dedicated namespace:**  media-pipelines-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteMeeting.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteMeeting.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteMeeting.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteMeeting.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteProxySession.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteProxySession.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteProxySession.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteProxySession.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteSipMediaApplication.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteSipMediaApplication.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipMediaApplication.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipMediaApplication.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteSipRule.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteSipRule.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipRule.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipRule.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnector.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnector.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnector.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnector.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorEmergencyCallingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorEmergencyCallingConfiguration.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorEmergencyCallingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorEmergencyCallingConfiguration.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorGroup.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorGroup.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorOrigination.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorOrigination.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorOrigination.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorOrigination.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorProxy.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorProxy.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorProxy.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorProxy.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorStreamingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorStreamingConfiguration.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorStreamingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorStreamingConfiguration.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorTermination.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorTermination.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTermination.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTermination.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorTerminationCredentials.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DeleteVoiceConnectorTerminationCredentials.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTerminationCredentials.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTerminationCredentials.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeAppInstance.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeAppInstance.html) **
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstance.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstance.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeAppInstanceAdmin.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeAppInstanceAdmin.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceAdmin.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceAdmin.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeAppInstanceUser.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeAppInstanceUser.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceUser.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceUser.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannel.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannel.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannel.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannel.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelBan.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelBan.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelBan.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelBan.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelMembership.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelMembership.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembership.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembership.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelMembershipForAppInstanceUser.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelMembershipForAppInstanceUser.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembershipForAppInstanceUser.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembershipForAppInstanceUser.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelModeratedByAppInstanceUser.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelModeratedByAppInstanceUser.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModeratedByAppInstanceUser.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModeratedByAppInstanceUser.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelModerator.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DescribeChannelModerator.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModerator.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModerator.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DisassociatePhoneNumbersFromVoiceConnector.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DisassociatePhoneNumbersFromVoiceConnector.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnector.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnector.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_DisassociatePhoneNumbersFromVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_DisassociatePhoneNumbersFromVoiceConnectorGroup.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnectorGroup.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAppInstanceRetentionSettings.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAppInstanceRetentionSettings.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_GetAppInstanceRetentionSettings.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_GetAppInstanceRetentionSettings.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAppInstanceStreamingConfigurations.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAppInstanceStreamingConfigurations.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingStreamingConfigurations.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingStreamingConfigurations.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAttendee.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetAttendee.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetAttendee.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetAttendee.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_GetChannelMessage.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetChannelMessage.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessage.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessage.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_GetMediaCapturePipeline.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetMediaCapturePipeline.html) **
  - **Dedicated namespace:** media-pipelines-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaCapturePipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaCapturePipeline.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_GetMeeting.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetMeeting.html) **
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_GetMessagingSessionEndpoint.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetMessagingSessionEndpoint.html) **
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingSessionEndpoint.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingSessionEndpoint.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetProxySession.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetProxySession.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetProxySession.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetProxySession.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetSipMediaApplication.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetSipMediaApplication.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplication.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplication.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetSipMediaApplicationLoggingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetSipMediaApplicationLoggingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplicationLoggingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplicationLoggingConfiguration.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_GetSipRule.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetSipRule.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipRule.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipRule.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnector.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnector.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnector.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnector.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorEmergencyCallingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorEmergencyCallingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorGroup.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorGroup.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorLoggingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorLoggingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorLoggingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorLoggingConfiguration.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorOrigination.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorOrigination.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorOrigination.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorOrigination.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorProxy.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorProxy.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorProxy.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorProxy.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorStreamingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorStreamingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorStreamingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorStreamingConfiguration.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorTermination.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorTermination.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTermination.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTermination.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorTerminationHealth.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_GetVoiceConnectorTerminationHealth.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTerminationHealth.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTerminationHealth.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAppInstanceAdmins.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAppInstanceAdmins.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceAdmins.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceAdmins.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAppInstances.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAppInstances.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstances.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstances.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAppInstanceUsers.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAppInstanceUsers.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceUsers.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceUsers.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAttendees.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAttendees.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListAttendees.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListAttendees.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAttendeeTags.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListAttendeeTags.html)**\*****
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelBans.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelBans.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelBans.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelBans.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelMemberships.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelMemberships.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMemberships.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMemberships.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelMembershipsForAppInstanceUser.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelMembershipsForAppInstanceUser.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelMessages.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelMessages.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMessages.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMessages.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelModerators.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelModerators.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelModerators.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelModerators.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannels.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannels.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannels.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannels.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelsModeratedByAppInstanceUser.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListChannelsModeratedByAppInstanceUser.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsModeratedByAppInstanceUser.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsModeratedByAppInstanceUser.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListMediaCapturePipelines.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListMediaCapturePipelines.html)**
  - **Dedicated namespace:** media-pipelines-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaCapturePipelines.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaCapturePipelines.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListMeetings.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListMeetings.html)**\*****
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_ListMeetingTags.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListMeetingTags.html)**\+****
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListProxySessions.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListProxySessions.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListProxySessions.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListProxySessions.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListSipMediaApplications.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListSipMediaApplications.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipMediaApplications.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipMediaApplications.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_ListSipRules.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListSipRules.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipRules.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipRules.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListTagsForResource.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListTagsForResource.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListTagsForResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListTagsForResource.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListVoiceConnectorGroups.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListVoiceConnectorGroups.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorGroups.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorGroups.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListVoiceConnectors.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListVoiceConnectors.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectors.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectors.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_ListVoiceConnectorTerminationCredentials.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ListVoiceConnectorTerminationCredentials.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorTerminationCredentials.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorTerminationCredentials.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_PutAppInstanceRetentionSettings.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutAppInstanceRetentionSettings.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_PutAppInstanceRetentionSettings.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_PutAppInstanceRetentionSettings.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_PutAppInstanceStreamingConfigurations.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutAppInstanceStreamingConfigurations.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutMessagingStreamingConfigurations.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutMessagingStreamingConfigurations.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_PutSipMediaApplicationLoggingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutSipMediaApplicationLoggingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutSipMediaApplicationLoggingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutSipMediaApplicationLoggingConfiguration.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorEmergencyCallingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorEmergencyCallingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorEmergencyCallingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorEmergencyCallingConfiguration.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorLoggingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorLoggingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorLoggingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorLoggingConfiguration.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorOrigination.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorOrigination.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorOrigination.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorOrigination.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorProxy.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorProxy.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorProxy.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorProxy.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorStreamingConfiguration.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorStreamingConfiguration.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorStreamingConfiguration.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorStreamingConfiguration.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorTermination.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorTermination.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTermination.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTermination.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorTerminationCredentials.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_PutVoiceConnectorTerminationCredentials.html)**
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTerminationCredentials.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTerminationCredentials.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_RedactChannelMessage.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_RedactChannelMessage.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_RedactChannelMessage.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_RedactChannelMessage.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_messaging-chime_SendChannelMessage.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_messaging-chime_SendChannelMessage.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_StartMeetingTranscription.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_StartMeetingTranscription.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StartMeetingTranscription.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StartMeetingTranscription.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_StopMeetingTranscription.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_StopMeetingTranscription.html)**
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StopMeetingTranscription.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StopMeetingTranscription.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_TagAttendee.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_TagAttendee.html)**\*****
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_TagMeeting.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_TagMeeting.html)**\+****
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_TagResource.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_TagResource.html)**
  - **Dedicated namespace:** identity-chime / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_TagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_TagResource.html)
  - **Dedicated namespace:** media-pipelines-chime / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_TagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_TagResource.html)
  - **Dedicated namespace:** meetings-chime / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meetings-chime_TagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meetings-chime_TagResource.html)
  - **Dedicated namespace:** messaging-chime / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_TagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_TagResource.html)
  - **Dedicated namespace:** voice-chime / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_TagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_TagResource.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_UntagAttendee.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UntagAttendee.html)**\*****
  - **Dedicated namespace:** n/a
  - **Dedicated namespace API:**

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_UntagMeeting.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UntagMeeting.html)**\+****
  - **Dedicated namespace:** meetings-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime/latest/APIReference/API_meeting-chime_UntagResource.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_meeting-chime_UntagResource.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_UntagResource.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UntagResource.html)**
  - **Dedicated namespace:** identity-chime  / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UntagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UntagResource.html)
  - **Dedicated namespace:** media-pipelines-chime / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UntagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UntagResource.html)
  - **Dedicated namespace:** meetings-chime / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meetings-chime_UntagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meetings-chime_UntagResource.html)
  - **Dedicated namespace:** messaging-chime / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UntagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UntagResource.html)
  - **Dedicated namespace:** voice-chime / **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UntagResource.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UntagResource.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateAppInstance.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateAppInstance.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstance.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstance.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateAppInstanceUser.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateAppInstanceUser.html)**
  - **Dedicated namespace:** identity-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstanceUser.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_UpdateAppInstanceUser.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateChannel.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateChannel.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannel.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannel.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateChannelMessage.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateChannelMessage.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelMessage.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelMessage.html)

- **[https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateChannelReadMarker.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateChannelReadMarker.html)**
  - **Dedicated namespace:** messaging-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelReadMarker.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelReadMarker.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateProxySession.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateProxySession.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateProxySession.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateProxySession.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateSipMediaApplication.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateSipMediaApplication.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplication.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplication.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateSipMediaApplicationCall.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateSipMediaApplicationCall.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplicationCall.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplicationCall.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateSipRule.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateSipRule.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipRule.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipRule.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateVoiceConnector.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateVoiceConnector.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnector.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnector.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateVoiceConnectorGroup.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnectorGroup.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnectorGroup.html)

- ** [https://docs.aws.amazon.com/chime/latest/APIReference/API_ValidateE911Address.html](https://docs.aws.amazon.com/chime/latest/APIReference/API_ValidateE911Address.html) **
  - **Dedicated namespace:** voice-chime
  - **Dedicated namespace API:** [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ValidateE911Address.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ValidateE911Address.html)

**\+** API has been superseded by an API with another name.

**\* **API is no longer available.
