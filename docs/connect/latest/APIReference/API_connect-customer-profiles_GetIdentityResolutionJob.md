---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetIdentityResolutionJob.html
---

# GetIdentityResolutionJob
<a name="API_connect-customer-profiles_GetIdentityResolutionJob"></a>

Returns information about an Identity Resolution Job in a specific domain.

Identity Resolution Jobs are set up using the Amazon Connect admin console. For more information, see [Use Identity Resolution to consolidate similar profiles](https://docs.aws.amazon.com/connect/latest/adminguide/use-identity-resolution.html).

## Request Syntax
<a name="API_connect-customer-profiles_GetIdentityResolutionJob_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/identity-resolution-jobs/{{JobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetIdentityResolutionJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetIdentityResolutionJob_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [JobId](#API_connect-customer-profiles_GetIdentityResolutionJob_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-request-uri-JobId"></a>
The unique identifier of the Identity Resolution Job.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetIdentityResolutionJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AutoMerging": {
      "ConflictResolution": {
         "ConflictResolvingModel": "string",
         "SourceName": "string"
      },
      "Consolidation": {
         "MatchingAttributesList": [
            [ "string" ]
         ]
      },
      "Enabled": boolean,
      "MinAllowedConfidenceScoreForMerging": number
   },
   "DomainName": "string",
   "ExportingLocation": {
      "S3Exporting": {
         "S3BucketName": "string",
         "S3KeyName": "string"
      }
   },
   "JobEndTime": number,
   "JobExpirationTime": number,
   "JobId": "string",
   "JobStartTime": number,
   "JobStats": {
      "NumberOfMatchesFound": number,
      "NumberOfMergesDone": number,
      "NumberOfProfilesReviewed": number
   },
   "LastUpdatedAt": number,
   "Message": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetIdentityResolutionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoMerging](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-AutoMerging"></a>
Configuration settings for how to perform the auto-merging of profiles.
Type: [AutoMerging](API_connect-customer-profiles_AutoMerging.md) object

 ** [DomainName](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [ExportingLocation](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-ExportingLocation"></a>
The S3 location where the Identity Resolution Job writes result files.
Type: [ExportingLocation](API_connect-customer-profiles_ExportingLocation.md) object

 ** [JobEndTime](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-JobEndTime"></a>
The timestamp of when the Identity Resolution Job was completed.
Type: Timestamp

 ** [JobExpirationTime](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-JobExpirationTime"></a>
The timestamp of when the Identity Resolution Job will expire.
Type: Timestamp

 ** [JobId](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-JobId"></a>
The unique identifier of the Identity Resolution Job.
Type: String
Pattern: `[a-f0-9]{32}`

 ** [JobStartTime](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-JobStartTime"></a>
The timestamp of when the Identity Resolution Job was started or will be started.
Type: Timestamp

 ** [JobStats](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-JobStats"></a>
Statistics about the Identity Resolution Job.
Type: [JobStats](API_connect-customer-profiles_JobStats.md) object

 ** [LastUpdatedAt](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-LastUpdatedAt"></a>
The timestamp of when the Identity Resolution Job was most recently edited.
Type: Timestamp

 ** [Message](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-Message"></a>
The error messages that are generated when the Identity Resolution Job runs.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `.*`

 ** [Status](#API_connect-customer-profiles_GetIdentityResolutionJob_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetIdentityResolutionJob-response-Status"></a>
The status of the Identity Resolution Job.
+  `PENDING`: The Identity Resolution Job is scheduled but has not started yet. If you turn off the Identity Resolution feature in your domain, jobs in the `PENDING` state are deleted.
+  `PREPROCESSING`: The Identity Resolution Job is loading your data.
+  `FIND_MATCHING`: The Identity Resolution Job is using the machine learning model to identify profiles that belong to the same matching group.
+  `MERGING`: The Identity Resolution Job is merging duplicate profiles.
+  `COMPLETED`: The Identity Resolution Job completed successfully.
+  `PARTIAL_SUCCESS`: There's a system error and not all of the data is merged. The Identity Resolution Job writes a message indicating the source of the problem.
+  `FAILED`: The Identity Resolution Job did not merge any data. It writes a message indicating the source of the problem.
Type: String
Valid Values: `PENDING | PREPROCESSING | FIND_MATCHING | MERGING | COMPLETED | PARTIAL_SUCCESS | FAILED`

## Errors
<a name="API_connect-customer-profiles_GetIdentityResolutionJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_GetIdentityResolutionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetIdentityResolutionJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetIdentityResolutionJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetIdentityResolutionJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetIdentityResolutionJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetIdentityResolutionJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetIdentityResolutionJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetIdentityResolutionJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetIdentityResolutionJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetIdentityResolutionJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetIdentityResolutionJob)
