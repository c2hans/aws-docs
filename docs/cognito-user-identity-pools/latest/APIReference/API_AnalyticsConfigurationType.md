---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AnalyticsConfigurationType.html
---

# AnalyticsConfigurationType
<a name="API_AnalyticsConfigurationType"></a>

The settings for Amazon Pinpoint analytics configuration. With an analytics configuration, your application can collect user-activity metrics for user notifications with a Amazon Pinpoint campaign.

Amazon Pinpoint isn't available in all AWS Regions. For a list of available Regions, see [Amazon Cognito and Amazon Pinpoint Region availability](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html#cognito-user-pools-find-region-mappings).

This data type is a request parameter of [CreateUserPoolClient](API_CreateUserPoolClient.md) and [UpdateUserPoolClient](API_UpdateUserPoolClient.md), and a response parameter of [DescribeUserPoolClient](API_DescribeUserPoolClient.md).

## Contents
<a name="API_AnalyticsConfigurationType_Contents"></a>

 ** ApplicationArn **   <a name="CognitoUserPools-Type-AnalyticsConfigurationType-ApplicationArn"></a>
The Amazon Resource Name (ARN) of an Amazon Pinpoint project that you want to connect to your user pool app client. Amazon Cognito publishes events to the Amazon Pinpoint project that `ApplicationArn` declares. You can also configure your application to pass an endpoint ID in the `AnalyticsMetadata` parameter of sign-in operations. The endpoint ID is information about the destination for push notifications
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** ApplicationId **   <a name="CognitoUserPools-Type-AnalyticsConfigurationType-ApplicationId"></a>
Your Amazon Pinpoint project ID.
Type: String
Pattern: `^[0-9a-fA-F]+$`
Required: No

 ** ExternalId **   <a name="CognitoUserPools-Type-AnalyticsConfigurationType-ExternalId"></a>
The [external ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) of the role that Amazon Cognito assumes to send analytics data to Amazon Pinpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** RoleArn **   <a name="CognitoUserPools-Type-AnalyticsConfigurationType-RoleArn"></a>
The ARN of an AWS Identity and Access Management role that has the permissions required for Amazon Cognito to publish events to Amazon Pinpoint analytics.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** UserDataShared **   <a name="CognitoUserPools-Type-AnalyticsConfigurationType-UserDataShared"></a>
If `UserDataShared` is `true`, Amazon Cognito includes user data in the events that it publishes to Amazon Pinpoint analytics.
Type: Boolean
Required: No

## See Also
<a name="API_AnalyticsConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AnalyticsConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AnalyticsConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AnalyticsConfigurationType)
