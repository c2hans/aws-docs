---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AnalyticsMetadataType.html
---

# AnalyticsMetadataType
<a name="API_AnalyticsMetadataType"></a>

Information that your application adds to authentication requests. Applies an endpoint ID to the analytics data that your user pool sends to Amazon Pinpoint.

An endpoint ID uniquely identifies a mobile device, email address or phone number that can receive messages from Amazon Pinpoint analytics. For more information about AWS Regions that can contain Amazon Pinpoint resources for use with Amazon Cognito user pools, see [Using Amazon Pinpoint analytics with Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html).

This data type is a request parameter of authentication operations like [InitiateAuth](API_InitiateAuth.md), [AdminInitiateAuth](API_AdminInitiateAuth.md), [RespondToAuthChallenge](API_RespondToAuthChallenge.md), and [AdminRespondToAuthChallenge](API_AdminRespondToAuthChallenge.md).

## Contents
<a name="API_AnalyticsMetadataType_Contents"></a>

 ** AnalyticsEndpointId **   <a name="CognitoUserPools-Type-AnalyticsMetadataType-AnalyticsEndpointId"></a>
The endpoint ID. Information that you want to pass to Amazon Pinpoint about where to send notifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_AnalyticsMetadataType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AnalyticsMetadataType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AnalyticsMetadataType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AnalyticsMetadataType)
