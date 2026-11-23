---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiatePointInTimeRecovery.html
---

# InitiatePointInTimeRecovery

Initiates a point-in-time recovery of a user pool to a time in the past that you specify. This operation is the first step of a recovery and doesn't change your user pool data. Amazon Cognito pauses write operations in the user pool and generates a recovery preview, which might not be available immediately. The preview shows the number of entities that the recovery creates, updates, and deletes. To check the status of the recovery and review the preview, make a [DescribePointInTimeRecovery](API_DescribePointInTimeRecovery.md) request. When the status is `PREVIEW_GENERATED`, apply the recovery with a [StartPointInTimeRecovery](API_StartPointInTimeRecovery.md) request or discard it with a [CancelPointInTimeRecovery](API_CancelPointInTimeRecovery.md) request. The time that it takes to generate the recovery preview doesn't depend on the size of your user pool.

**Important**
Point-in-time recovery is a disaster recovery feature. Use it to recover from accidental or unauthorized changes that affect your user data, for example the deletion or corruption of many users. Don't use point-in-time recovery to remove users that were created recently or to revert changes to individual users. To delete or update individual users, use operations like [AdminDeleteUser](API_AdminDeleteUser.md) and [AdminUpdateUserAttributes](API_AdminUpdateUserAttributes.md).

While a recovery is in progress, Amazon Cognito blocks operations that write to the user pool, for example user sign-up, user creation, and attribute updates. Sign-in and read operations continue to work, with the following exceptions:
+ Users who must set a new password, set up MFA, or respond to a TOTP MFA challenge can't complete sign-in. Sign-in with the `NEW_PASSWORD_REQUIRED`, `MFA_SETUP`, and `SOFTWARE_TOKEN_MFA` challenges fails until the recovery ends.
+ Federated users can sign in only if they have previously signed in to the user pool and their attributes from the external identity provider haven't changed.
+ You can't create or start user import jobs. Start your import jobs after the recovery ends.

If you don't start or cancel the recovery within 24 hours after you initiate it, the recovery preview expires. Amazon Cognito then resumes write operations and doesn't change your user pool data. The 24-hour period includes the time that Amazon Cognito takes to generate the recovery preview.

A point-in-time recovery restores user data, including user profiles and attributes, group memberships, passwords, MFA settings, and passkeys. It doesn't restore user pool configuration, for example app clients, the attribute schema, encryption settings, or multi-Region replication settings. Users who changed their password after the recovery point keep their current password.

The following requirements and limits apply to point-in-time recovery:
+ Your user pool must be on the Essentials or Plus [feature plan](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html). With the Essentials feature plan, you can recover your user pool to a point in time up to 1 day in the past. With the Plus feature plan, you can recover up to 14 days in the past. Your user pool must have been on the required feature plan at the recovery point. For example, to recover to a point in time 14 days ago, your user pool must have been on the Plus feature plan for the past 14 days.
+ The recovery point must be at least 15 minutes in the past and can't be earlier than the creation time of the user pool.
+ A user pool can have only one active recovery at a time.
+ An AWS account can have up to five active recoveries at a time across all of its user pools. An organization in AWS Organizations can have up to ten active recoveries at a time across all of its accounts.
+ You can complete one recovery of a user pool in a 24-hour period.
+ You can create up to three recovery previews of a user pool, ten recovery previews in an AWS account, and 15 recovery previews in an organization in AWS Organizations in a 24-hour period. You can create up to ten recovery previews of a user pool in a 30-day period.
+ You can't initiate a recovery while a user import job is in progress in your user pool. Wait for the import job to complete, or stop it with a [StopUserImportJob](API_StopUserImportJob.md) request, and then initiate the recovery.
+ In a user pool with multi-Region replication, you can initiate a recovery only in the primary AWS Region, and only after replication is complete.
+ If your user pool uses a customer managed key in AWS KMS for encryption, the key must remain enabled and accessible to Amazon Cognito for the duration of the recovery.
+ Some user pools don't support point-in-time recovery, for example some older user pools and user pools that contain user data with characters or formats that point-in-time recovery doesn't support. If your user pool doesn't support it, Amazon Cognito returns an error when you initiate a recovery. To get help with this limitation, contact AWS Support.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_InitiatePointInTimeRecovery_RequestSyntax"></a>

```
{
   "RestoreTimestamp": {{number}},
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_InitiatePointInTimeRecovery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RestoreTimestamp](#API_InitiatePointInTimeRecovery_RequestSyntax) **   <a name="CognitoUserPools-InitiatePointInTimeRecovery-request-RestoreTimestamp"></a>
The point in time that you want to recover your user pool to. Amazon Cognito reverts changes to user data that occurred after this time. The recovery point must be at least 15 minutes in the past and within the recovery period of your user pool feature plan: up to 1 day in the past with the Essentials feature plan, or up to 14 days in the past with the Plus feature plan.
Type: Timestamp
Required: Yes

 ** [UserPoolId](#API_InitiatePointInTimeRecovery_RequestSyntax) **   <a name="CognitoUserPools-InitiatePointInTimeRecovery-request-UserPoolId"></a>
The ID of the user pool that you want to recover.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_InitiatePointInTimeRecovery_ResponseSyntax"></a>

```
{
   "Restoration": {
      "RestoreId": "string",
      "RestorePreview": [
         {
            "CreateCount": number,
            "DeleteCount": number,
            "Entity": "string",
            "UpdateCount": number
         }
      ],
      "RestoreStatus": "string",
      "RestoreTimestamp": number,
      "TriggerTimestamp": number
   }
}
```

## Response Elements
<a name="API_InitiatePointInTimeRecovery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Restoration](#API_InitiatePointInTimeRecovery_ResponseSyntax) **   <a name="CognitoUserPools-InitiatePointInTimeRecovery-response-Restoration"></a>
The details of the recovery that you initiated. Includes the recovery ID that you can use in later requests to describe, start, or cancel the recovery.
Type: [RestorationType](API_RestorationType.md) object

## Errors
<a name="API_InitiatePointInTimeRecovery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
This exception is thrown if two or more modifications are happening concurrently.
 ** message **
The message provided when the concurrent exception is thrown.
HTTP Status Code: 400

 ** FeatureUnavailableInTierException **
This exception is thrown when a feature that you attempted to use or configure isn't included in your user pool's current feature plan. This can occur when:
+ You configure a feature that your feature plan doesn't support.
+ You make a request that uses a feature that requires a higher feature plan.
To resolve this issue, upgrade your user pool to a feature plan that includes the feature.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** LimitExceededException **
This exception is thrown when a user exceeds the limit for a requested AWS resource.
 ** message **
The message returned when Amazon Cognito throws a limit exceeded exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_InitiatePointInTimeRecovery_Examples"></a>

### Example
<a name="API_InitiatePointInTimeRecovery_Example_1"></a>

The following example request initiates a point-in-time recovery of a user pool on the Plus feature plan to its state on October 7, 2026 at 12:00 UTC, about 27 hours before the request. Amazon Cognito pauses write operations in the user pool. The status of the recovery is `PREVIEW_GENERATING` until the recovery preview is available.

#### Sample Request
<a name="API_InitiatePointInTimeRecovery_Example_1_Request"></a>

```HTTP
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.InitiatePointInTimeRecovery
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "RestoreTimestamp": 1791374400,
    "UserPoolId": "us-east-1_EXAMPLE"
}
```

#### Sample Response
<a name="API_InitiatePointInTimeRecovery_Example_1_Response"></a>

```HTTP
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
    "Restoration": {
        "RestoreId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "RestoreStatus": "PREVIEW_GENERATING",
        "RestoreTimestamp": 1791374400,
        "TriggerTimestamp": 1791473400
    }
}
```

## See Also
<a name="API_InitiatePointInTimeRecovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/InitiatePointInTimeRecovery)
