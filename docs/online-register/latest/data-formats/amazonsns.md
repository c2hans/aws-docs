---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonsns.html
---

# Data retrieval APIs for Amazon SNS
<a name="amazonsns"></a>

Amazon SNS provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="sns-CheckIfPhoneNumberIsOptedOut"></a>[https://docs.aws.amazon.com/sns/latest/api/API_CheckIfPhoneNumberIsOptedOut.html](https://docs.aws.amazon.com/sns/latest/api/API_CheckIfPhoneNumberIsOptedOut.html) | Accept a phone number and indicate whether the phone holder has opted out of receiving SMS messages from your account | Read |
| <a name="sns-GetDataProtectionPolicy"></a>[https://docs.aws.amazon.com/sns/latest/api/API_GetDataProtectionPolicy.html](https://docs.aws.amazon.com/sns/latest/api/API_GetDataProtectionPolicy.html) | Return the data protection policy of the topic | Read |
| <a name="sns-GetEndpointAttributes"></a>[https://docs.aws.amazon.com/sns/latest/api/API_GetEndpointAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetEndpointAttributes.html) | Retrieve the endpoint attributes for a device on one of the supported push notification services, such as GCM and APNS | Read |
| <a name="sns-GetPlatformApplicationAttributes"></a>[https://docs.aws.amazon.com/sns/latest/api/API_GetPlatformApplicationAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetPlatformApplicationAttributes.html) | Retrieve the attributes of the platform application object for the supported push notification services, such as APNS and GCM | Read |
| <a name="sns-GetSMSAttributes"></a>[https://docs.aws.amazon.com/sns/latest/api/API_GetSMSAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetSMSAttributes.html) | Return the settings for sending SMS messages from your account | Read |
| <a name="sns-GetSMSSandboxAccountStatus"></a>[https://docs.aws.amazon.com/sns/latest/api/API_GetSMSSandboxAccountStatus.html](https://docs.aws.amazon.com/sns/latest/api/API_GetSMSSandboxAccountStatus.html) | Retrieve the sandbox status for the calling account in the target region | Read |
| <a name="sns-GetSubscriptionAttributes"></a>[https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html) | Return all of the properties of a subscription | Read |
| <a name="sns-GetTopicAttributes"></a>[https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html](https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html) | Return all of the properties of a topic | Read |
| <a name="sns-ListEndpointsByPlatformApplication"></a>[https://docs.aws.amazon.com/sns/latest/api/API_ListEndpointsByPlatformApplication.html](https://docs.aws.amazon.com/sns/latest/api/API_ListEndpointsByPlatformApplication.html) | List the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM and APNS | List |
| <a name="sns-ListOriginationNumbers"></a>[https://docs.aws.amazon.com/sns/latest/api/API_ListOriginationNumbers.html](https://docs.aws.amazon.com/sns/latest/api/API_ListOriginationNumbers.html) | List all origination numbers, and their metadata | List |
| <a name="sns-ListPhoneNumbersOptedOut"></a>[https://docs.aws.amazon.com/sns/latest/api/API_ListPhoneNumbersOptedOut.html](https://docs.aws.amazon.com/sns/latest/api/API_ListPhoneNumbersOptedOut.html) | Return a list of phone numbers that are opted out, meaning you cannot send SMS messages to them | Read |
| <a name="sns-ListPlatformApplications"></a>[https://docs.aws.amazon.com/sns/latest/api/API_ListPlatformApplications.html](https://docs.aws.amazon.com/sns/latest/api/API_ListPlatformApplications.html) | List the platform application objects for the supported push notification services, such as APNS and GCM | List |
| <a name="sns-ListSMSSandboxPhoneNumbers"></a>[https://docs.aws.amazon.com/sns/latest/api/API_ListSMSSandboxPhoneNumbers.html](https://docs.aws.amazon.com/sns/latest/api/API_ListSMSSandboxPhoneNumbers.html) | List the calling account's current pending and verified destination phone numbers | List |
| <a name="sns-ListSubscriptions"></a>[https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html) | Return a list of the requester's subscriptions | List |
| <a name="sns-ListSubscriptionsByTopic"></a>[https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html) | Return a list of the subscriptions to a specific topic | List |
| <a name="sns-ListTagsForResource"></a>[https://docs.aws.amazon.com/sns/latest/api/API_ListTagsForResource.html](https://docs.aws.amazon.com/sns/latest/api/API_ListTagsForResource.html) | List all tags added to the specified Amazon SNS topic | Read |
| <a name="sns-ListTopics"></a>[https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) | Return a list of the requester's topics | List |
