---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/operations.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Operations
<a name="operations"></a>

The Amazon Pinpoint REST API includes the following operations.
+ [CreateApp](apps.md#CreateApp)

  Creates an application.
+ [CreateCampaign](apps-application-id-campaigns.md#CreateCampaign)

  Creates a new campaign for an application or updates the settings of an existing campaign for an application.
+ [CreateEmailTemplate](templates-template-name-email.md#CreateEmailTemplate)

  Creates a message template for messages that are sent through the email channel.
+ [CreateExportJob](apps-application-id-jobs-export.md#CreateExportJob)

  Creates an export job for an application.
+ [CreateImportJob](apps-application-id-jobs-import.md#CreateImportJob)

  Creates an import job for an application.
+ [CreateInAppTemplate](templates-template-name-inapp.md#CreateInAppTemplate)

  Creates a new in-app message template.
+ [CreateJourney](apps-application-id-journeys.md#CreateJourney)

  Creates a journey for an application.
+ [CreatePushTemplate](templates-template-name-push.md#CreatePushTemplate)

  Creates a message template for messages that are sent through a push notification channel.
+ [CreateRecommenderConfiguration](recommenders.md#CreateRecommenderConfiguration)

  Creates an Amazon Pinpoint configuration for a recommender model.
+ [CreateSegment](apps-application-id-segments.md#CreateSegment)

  Creates a new segment.
+ [CreateSmsTemplate](templates-template-name-sms.md#CreateSmsTemplate)

  Creates a message template for messages that are sent through the SMS channel.
+ [CreateVoiceTemplate](templates-template-name-voice.md#CreateVoiceTemplate)

  Creates a message template for messages that are sent through the voice channel.
+ [DeleteAdmChannel](apps-application-id-channels-adm.md#DeleteAdmChannel)

  Disables the ADM channel for an application and deletes any existing settings for the channel.
+ [DeleteApnsChannel](apps-application-id-channels-apns.md#DeleteApnsChannel)

  Disables the APNs channel for an application and deletes any existing settings for the channel.
+ [DeleteApnsSandboxChannel](apps-application-id-channels-apns_sandbox.md#DeleteApnsSandboxChannel)

  Disables the APNs sandbox channel for an application and deletes any existing settings for the channel.
+ [DeleteApnsVoipChannel](apps-application-id-channels-apns_voip.md#DeleteApnsVoipChannel)

  Disables the APNs VoIP channel for an application and deletes any existing settings for the channel.
+ [DeleteApnsVoipSandboxChannel](apps-application-id-channels-apns_voip_sandbox.md#DeleteApnsVoipSandboxChannel)

  Disables the APNs VoIP sandbox channel for an application and deletes any existing settings for the channel.
+ [DeleteApp](apps-application-id.md#DeleteApp)

  Deletes an application.
+ [DeleteBaiduChannel](apps-application-id-channels-baidu.md#DeleteBaiduChannel)

  Disables the Baidu channel for an application and deletes any existing settings for the channel.
+ [DeleteCampaign](apps-application-id-campaigns-campaign-id.md#DeleteCampaign)

  Deletes a campaign from an application.
+ [DeleteEmailChannel](apps-application-id-channels-email.md#DeleteEmailChannel)

  Disables the email channel for an application and deletes any existing settings for the channel.
+ [DeleteEmailTemplate](templates-template-name-email.md#DeleteEmailTemplate)

  Deletes a message template for messages that were sent through the email channel.
+ [DeleteEndpoint](apps-application-id-endpoints-endpoint-id.md#DeleteEndpoint)

  Deletes an endpoint from an application.
+ [DeleteEventStream](apps-application-id-eventstream.md#DeleteEventStream)

  Deletes the event stream for an application.
+ [DeleteGcmChannel](apps-application-id-channels-gcm.md#DeleteGcmChannel)

  Disables the GCM channel for an application and deletes any existing settings for the channel.
+ [DeleteInAppTemplate](templates-template-name-inapp.md#DeleteInAppTemplate)

  Deletes an existing in-app message template.
+ [DeleteJourney](apps-application-id-journeys-journey-id.md#DeleteJourney)

  Deletes a journey from an application.
+ [DeletePushTemplate](templates-template-name-push.md#DeletePushTemplate)

  Deletes a message template for messages that were sent through a push notification channel.
+ [DeleteRecommenderConfiguration](recommenders-recommender-id.md#DeleteRecommenderConfiguration)

  Deletes an Amazon Pinpoint configuration for a recommender model.
+ [DeleteSegment](apps-application-id-segments-segment-id.md#DeleteSegment)

  Deletes a segment from an application.
+ [DeleteSmsChannel](apps-application-id-channels-sms.md#DeleteSmsChannel)

  Disables the SMS channel for an application and deletes any existing settings for the channel.
+ [DeleteSmsTemplate](templates-template-name-sms.md#DeleteSmsTemplate)

  Deletes a message template for messages that were sent through the SMS channel.
+ [DeleteUserEndpoints](apps-application-id-users-user-id.md#DeleteUserEndpoints)

  Deletes all the endpoints that are associated with a specific user ID.
+ [DeleteVoiceChannel](apps-application-id-channels-voice.md#DeleteVoiceChannel)

  Disables the voice channel for an application and deletes any existing settings for the channel.
+ [DeleteVoiceTemplate](templates-template-name-voice.md#DeleteVoiceTemplate)

  Deletes a message template for messages that were sent through the voice channel.
+ [GetAdmChannel](apps-application-id-channels-adm.md#GetAdmChannel)

  Retrieves information about the status and settings of the ADM channel for an application.
+ [GetApnsChannel](apps-application-id-channels-apns.md#GetApnsChannel)

  Retrieves information about the status and settings of the APNs channel for an application.
+ [GetApnsSandboxChannel](apps-application-id-channels-apns_sandbox.md#GetApnsSandboxChannel)

  Retrieves information about the status and settings of the APNs sandbox channel for an application.
+ [GetApnsVoipChannel](apps-application-id-channels-apns_voip.md#GetApnsVoipChannel)

  Retrieves information about the status and settings of the APNs VoIP channel for an application.
+ [GetApnsVoipSandboxChannel](apps-application-id-channels-apns_voip_sandbox.md#GetApnsVoipSandboxChannel)

  Retrieves information about the status and settings of the APNs VoIP sandbox channel for an application.
+ [GetApp](apps-application-id.md#GetApp)

  Retrieves information about an application.
+ [GetApplicationDateRangeKpi](apps-application-id-kpis-daterange-kpi-name.md#GetApplicationDateRangeKpi)

  Retrieves (queries) pre-aggregated data for a standard metric that applies to an application.
+ [GetApplicationSettings](apps-application-id-settings.md#GetApplicationSettings)

  Retrieves information about the settings for an application.
+ [GetApps](apps.md#GetApps)

  Retrieves information about all the applications that are associated with your Amazon Pinpoint account.
+ [GetBaiduChannel](apps-application-id-channels-baidu.md#GetBaiduChannel)

  Retrieves information about the status and settings of the Baidu channel for an application.
+ [GetCampaign](apps-application-id-campaigns-campaign-id.md#GetCampaign)

  Retrieves information about the status, configuration, and other settings for a campaign.
+ [GetCampaignActivities](apps-application-id-campaigns-campaign-id-activities.md#GetCampaignActivities)

  Retrieves information about all the activities for a campaign.
+ [GetCampaignDateRangeKpi](apps-application-id-campaigns-campaign-id-kpis-daterange-kpi-name.md#GetCampaignDateRangeKpi)

  Retrieves (queries) pre-aggregated data for a standard metric that applies to a campaign.
+ [GetCampaigns](apps-application-id-campaigns.md#GetCampaigns)

  Retrieves information about the status, configuration, and other settings for all the campaigns that are associated with an application.
+ [GetCampaignVersion](apps-application-id-campaigns-campaign-id-versions-version.md#GetCampaignVersion)

  Retrieves information about the status, configuration, and other settings for a specific version of a campaign.
+ [GetCampaignVersions](apps-application-id-campaigns-campaign-id-versions.md#GetCampaignVersions)

  Retrieves information about the status, configuration, and other settings for all versions of a campaign.
+ [GetChannels](apps-application-id-channels.md#GetChannels)

  Retrieves information about the history and status of each channel for an application.
+ [GetEmailChannel](apps-application-id-channels-email.md#GetEmailChannel)

  Retrieves information about the status and settings of the email channel for an application.
+ [GetEmailTemplate](templates-template-name-email.md#GetEmailTemplate)

  Retrieves the content and settings of a message template for messages that are sent through the email channel.
+ [GetEndpoint](apps-application-id-endpoints-endpoint-id.md#GetEndpoint)

  Retrieves information about the settings and attributes of a specific endpoint for an application.
+ [GetEventStream](apps-application-id-eventstream.md#GetEventStream)

  Retrieves information about the event stream settings for an application.
+ [GetExportJob](apps-application-id-jobs-export-job-id.md#GetExportJob)

  Retrieves information about the status and settings of a specific export job for an application.
+ [GetExportJobs](apps-application-id-jobs-export.md#GetExportJobs)

  Retrieves information about the status and settings of all the export jobs for an application.
+ [GetGcmChannel](apps-application-id-channels-gcm.md#GetGcmChannel)

  Retrieves information about the status and settings of the GCM channel for an application.
+ [GetImportJob](apps-application-id-jobs-import-job-id.md#GetImportJob)

  Retrieves information about the status and settings of a specific import job for an application.
+ [GetImportJobs](apps-application-id-jobs-import.md#GetImportJobs)

  Retrieves information about the status and settings of all the import jobs for an application.
+ [GetInAppMessages](apps-application-id-endpoints-endpoint-id-inappmessages.md#GetInAppMessages)

  Retrieves information about the in-app messages that have been sent to the requested endpoint.
+ [GetInAppTemplate](templates-template-name-inapp.md#GetInAppTemplate)

  Retrieves the content and configuration of an in-app message template.
+ [GetJourney](apps-application-id-journeys-journey-id.md#GetJourney)

  Retrieves information about the status, configuration, and other settings for a journey.
+ [GetJourneyDateRangeKpi](apps-application-id-journeys-journey-id-kpis-daterange-kpi-name.md#GetJourneyDateRangeKpi)

  Retrieves (queries) pre-aggregated data for a standard engagement metric that applies to a journey.
+ [GetJourneyExecutionActivityMetrics](apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics.md#GetJourneyExecutionActivityMetrics)

  Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey activity.
+ [GetJourneyExecutionMetrics](apps-application-id-journeys-journey-id-execution-metrics.md#GetJourneyExecutionMetrics)

  Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey.
+ [GetJourneyRunExecutionActivityMetrics](apps-application-id-journeys-journey-id-runs-run-id-activities-journey-activity-id-execution-metrics.md#GetJourneyRunExecutionActivityMetrics)

  Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey activity.
+ [GetJourneyRunExecutionMetrics](apps-application-id-journeys-journey-id-runs-run-id-execution-metrics.md#GetJourneyRunExecutionMetrics)

  Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey.
+ [GetJourneyRuns](apps-application-id-journeys-journey-id-runs.md#GetJourneyRuns)

  Provides information about the runs of a journey.
+ [GetPushTemplate](templates-template-name-push.md#GetPushTemplate)

  Retrieves the content and settings of a message template for messages that are sent through a push notification channel.
+ [GetRecommenderConfiguration](recommenders-recommender-id.md#GetRecommenderConfiguration)

  Retrieves information about an Amazon Pinpoint configuration for a recommender model.
+ [GetRecommenderConfigurations](recommenders.md#GetRecommenderConfigurations)

  Retrieves information about all the recommender model configurations that are associated with your Amazon Pinpoint account.
+ [GetSegment](apps-application-id-segments-segment-id.md#GetSegment)

  Retrieves information about the configuration, dimension, and other settings for a specific segment that's associated with an application.
+ [GetSegmentExportJobs](apps-application-id-segments-segment-id-jobs-export.md#GetSegmentExportJobs)

  Retrieves information about the status and settings of the export jobs for a segment.
+ [GetSegmentImportJobs](apps-application-id-segments-segment-id-jobs-import.md#GetSegmentImportJobs)

  Retrieves information about the status and settings of the import jobs for a segment.
+ [GetSegments](apps-application-id-segments.md#GetSegments)

  Retrieves information about the configuration, dimension, and other settings for all the segments that are associated with an application.
+ [GetSegmentVersion](apps-application-id-segments-segment-id-versions-version.md#GetSegmentVersion)

  Retrieves information about the configuration, dimension, and other settings for a specific version of a segment that's associated with an application.
+ [GetSegmentVersions](apps-application-id-segments-segment-id-versions.md#GetSegmentVersions)

  Retrieves information about the configuration, dimension, and other settings for all the versions of a specific segment that's associated with an application.
+ [GetSmsChannel](apps-application-id-channels-sms.md#GetSmsChannel)

  Retrieves information about the status and settings of the SMS channel for an application.
+ [GetSmsTemplate](templates-template-name-sms.md#GetSmsTemplate)

  Retrieves the content and settings of a message template for messages that are sent through the SMS channel.
+ [GetUserEndpoints](apps-application-id-users-user-id.md#GetUserEndpoints)

  Retrieves information about all the endpoints that are associated with a specific user ID.
+ [GetVoiceChannel](apps-application-id-channels-voice.md#GetVoiceChannel)

  Retrieves information about the status and settings of the voice channel for an application.
+ [GetVoiceTemplate](templates-template-name-voice.md#GetVoiceTemplate)

  Retrieves the content and settings of a message template for messages that are sent through the voice channel.
+ [ListJourneys](apps-application-id-journeys.md#ListJourneys)

  Retrieves information about the status, configuration, and other settings for all the journeys that are associated with an application.
+ [ListTagsForResource](tags-resource-arn.md#ListTagsForResource)

  Retrieves all the tags (keys and values) that are associated with an application, campaign, message template, or segment.
+ [ListTemplates](templates.md#ListTemplates)

  Retrieves information about all the message templates that are associated with your Amazon Pinpoint account.
+ [ListTemplateVersions](templates-template-name-template-type-versions.md#ListTemplateVersions)

  Retrieves information about all the versions of a specific message template.
+ [PhoneNumberValidate](phone-number-validate.md#PhoneNumberValidate)

  Retrieves information about a phone number.
+ [PutEvents](apps-application-id-events.md#PutEvents)

  Creates a new event to record for endpoints, or creates or updates endpoint data that existing events are associated with.
+ [PutEventStream](apps-application-id-eventstream.md#PutEventStream)

  Creates a new event stream for an application or updates the settings of an existing event stream for an application.
+ [RemoveAttributes](apps-application-id-attributes-attribute-type.md#RemoveAttributes)

  Removes one or more custom attributes, of the same attribute type, from the application. Existing endpoints still have the attributes but Amazon Pinpoint will stop capturing new or changed values for these attributes.
+ [SendMessages](apps-application-id-messages.md#SendMessages)

  Creates and sends a direct message.
+ [SendOTPMessage](apps-application-id-otp.md#SendOTPMessage)

  Use this operation to send an OTP code to a user of your application. When you use this API, Amazon Pinpoint generates a random code and sends it to your user.
+ [SendUsersMessages](apps-application-id-users-messages.md#SendUsersMessages)

  Creates and sends a message to a list of users.
+ [TagResource](tags-resource-arn.md#TagResource)

  Adds one or more tags (keys and values) to an application, campaign, message template, or segment.
+ [UntagResource](tags-resource-arn.md#UntagResource)

  Removes one or more tags (keys and values) from an application, campaign, message template, or segment.
+ [UpdateAdmChannel](apps-application-id-channels-adm.md#UpdateAdmChannel)

  Enables the ADM channel for an application or updates the status and settings of the ADM channel for an application.
+ [UpdateApnsChannel](apps-application-id-channels-apns.md#UpdateApnsChannel)

  Enables the APNs channel for an application or updates the status and settings of the APNs channel for an application.
+ [UpdateApnsSandboxChannel](apps-application-id-channels-apns_sandbox.md#UpdateApnsSandboxChannel)

  Enables the APNs sandbox channel for an application or updates the status and settings of the APNs sandbox channel for an application.
+ [UpdateApnsVoipChannel](apps-application-id-channels-apns_voip.md#UpdateApnsVoipChannel)

  Enables the APNs VoIP channel for an application or updates the status and settings of the APNs VoIP channel for an application.
+ [UpdateApnsVoipSandboxChannel](apps-application-id-channels-apns_voip_sandbox.md#UpdateApnsVoipSandboxChannel)

  Enables the APNs VoIP sandbox channel for an application or updates the status and settings of the APNs VoIP sandbox channel for an application.
+ [UpdateApplicationSettings](apps-application-id-settings.md#UpdateApplicationSettings)

  Updates the settings for an application.
+ [UpdateBaiduChannel](apps-application-id-channels-baidu.md#UpdateBaiduChannel)

  Enables the Baidu channel for an application or updates the status and settings of the Baidu channel for an application.
+ [UpdateCampaign](apps-application-id-campaigns-campaign-id.md#UpdateCampaign)

  Updates the configuration and other settings for a campaign.
+ [UpdateEmailChannel](apps-application-id-channels-email.md#UpdateEmailChannel)

  Enables the email channel for an application or updates the status and settings of the email channel for an application.
+ [UpdateEmailTemplate](templates-template-name-email.md#UpdateEmailTemplate)

  Updates an existing message template for messages that are sent through the email channel.
+ [UpdateEndpoint](apps-application-id-endpoints-endpoint-id.md#UpdateEndpoint)

  Creates a new endpoint for an application or updates the settings and attributes of an existing endpoint for an application. You can also use this operation to define custom attributes for an endpoint. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.
+ [UpdateEndpointsBatch](apps-application-id-endpoints.md#UpdateEndpointsBatch)

  Creates a new batch of endpoints for an application or updates the settings and attributes of a batch of existing endpoints for an application. You can also use this operation to define custom attributes for a batch of endpoints. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.
+ [UpdateGcmChannel](apps-application-id-channels-gcm.md#UpdateGcmChannel)

  Enables the GCM channel for an application or updates the status and settings of the GCM channel for an application.
+ [UpdateInAppTemplate](templates-template-name-inapp.md#UpdateInAppTemplate)

  Updates an existing in-app message template.
+ [UpdateJourney](apps-application-id-journeys-journey-id.md#UpdateJourney)

  Updates the configuration and other settings for a journey.
+ [UpdateJourneyState](apps-application-id-journeys-journey-id-state.md#UpdateJourneyState)

  Cancels (stops) an active journey.
+ [UpdatePushTemplate](templates-template-name-push.md#UpdatePushTemplate)

  Updates an existing message template for messages that are sent through a push notification channel.
+ [UpdateRecommenderConfiguration](recommenders-recommender-id.md#UpdateRecommenderConfiguration)

  Updates an Amazon Pinpoint configuration for a recommender model.
+ [UpdateSegment](apps-application-id-segments-segment-id.md#UpdateSegment)

  Updates the configuration, dimension, and other settings for an existing segment.
+ [UpdateSmsChannel](apps-application-id-channels-sms.md#UpdateSmsChannel)

  Enables the SMS channel for an application or updates the status and settings of the SMS channel for an application.
+ [UpdateSmsTemplate](templates-template-name-sms.md#UpdateSmsTemplate)

  Updates an existing message template for messages that are sent through the SMS channel.
+ [UpdateTemplateActiveVersion](templates-template-name-template-type-active-version.md#UpdateTemplateActiveVersion)

  Changes the status of a specific version of a message template to *active*.
+ [UpdateVoiceChannel](apps-application-id-channels-voice.md#UpdateVoiceChannel)

  Enables the voice channel for an application or updates the status and settings of the voice channel for an application.
+ [UpdateVoiceTemplate](templates-template-name-voice.md#UpdateVoiceTemplate)

  Updates an existing message template for messages that are sent through the voice channel.
+ [VerifyOTPMessage](apps-application-id-verify-otp.md#VerifyOTPMessage)

  Verifies a One-Time Password that was generated by the `OTP Message` resource.
