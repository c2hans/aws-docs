---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AuthEventType.html
---

# AuthEventType
<a name="API_AuthEventType"></a>

One authentication event that Amazon Cognito logged in a user pool with threat protection active. Contains user and device metadata and a risk assessment from your user pool.

This data type is a response parameter of [AdminListUserAuthEvents](API_AdminListUserAuthEvents.md).

## Contents
<a name="API_AuthEventType_Contents"></a>

 ** ChallengeResponses **   <a name="CognitoUserPools-Type-AuthEventType-ChallengeResponses"></a>
A list of the challenges that the user was requested to answer, for example `Password`, and the result, for example `Success`.
Type: Array of [ChallengeResponseType](API_ChallengeResponseType.md) objects
Required: No

 ** CreationDate **   <a name="CognitoUserPools-Type-AuthEventType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** EventContextData **   <a name="CognitoUserPools-Type-AuthEventType-EventContextData"></a>
The user context data captured at the time of an event request. This value provides additional information about the client from which event the request is received.
Type: [EventContextDataType](API_EventContextDataType.md) object
Required: No

 ** EventFeedback **   <a name="CognitoUserPools-Type-AuthEventType-EventFeedback"></a>
The `UpdateAuthEventFeedback` or `AdminUpdateAuthEventFeedback` feedback that you or your user provided in response to the event. A value of `Valid` indicates that you disagreed with the level of risk that your user pool assigned, and evaluated a session to be valid, or likely safe. A value of `Invalid` indicates that you agreed with the user pool risk level and evaluated a session to be invalid, or likely malicious.
Type: [EventFeedbackType](API_EventFeedbackType.md) object
Required: No

 ** EventId **   <a name="CognitoUserPools-Type-AuthEventType-EventId"></a>
The event ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** EventResponse **   <a name="CognitoUserPools-Type-AuthEventType-EventResponse"></a>
The event response.
Type: String
Valid Values: `Pass | Fail | InProgress`
Required: No

 ** EventRisk **   <a name="CognitoUserPools-Type-AuthEventType-EventRisk"></a>
The threat evaluation from your user pool about an event. Contains information about whether your user pool detected compromised credentials, whether the event triggered an automated response, and the level of risk.
Type: [EventRiskType](API_EventRiskType.md) object
Required: No

 ** EventType **   <a name="CognitoUserPools-Type-AuthEventType-EventType"></a>
The type of authentication event.
Type: String
Valid Values: `SignIn | SignUp | ForgotPassword | PasswordChange | ResendCode`
Required: No

## See Also
<a name="API_AuthEventType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AuthEventType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AuthEventType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AuthEventType)
