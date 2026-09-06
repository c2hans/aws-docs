---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationVersions.html
---

# DescribeRegistrationVersions
<a name="API_DescribeRegistrationVersions"></a>

Retrieves the specified registration version.

## Request Syntax
<a name="API_DescribeRegistrationVersions_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RegistrationId": "{{string}}",
   "VersionNumbers": [ {{number}} ]
}
```

## Request Parameters
<a name="API_DescribeRegistrationVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeRegistrationVersions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationVersions-request-Filters"></a>
An array of RegistrationVersionFilter objects to filter the results.
Type: Array of [RegistrationVersionFilter](API_RegistrationVersionFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribeRegistrationVersions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationVersions-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRegistrationVersions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationVersions-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [RegistrationId](#API_DescribeRegistrationVersions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationVersions-request-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [VersionNumbers](#API_DescribeRegistrationVersions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationVersions-request-VersionNumbers"></a>
An array of registration version numbers.
Type: Array of longs
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

## Response Syntax
<a name="API_DescribeRegistrationVersions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RegistrationArn": "string",
   "RegistrationId": "string",
   "RegistrationVersions": [
      {
         "DeniedReasons": [
            {
               "DocumentationLink": "string",
               "DocumentationTitle": "string",
               "LongDescription": "string",
               "Reason": "string",
               "ShortDescription": "string"
            }
         ],
         "Feedback": "string",
         "RegistrationVersionStatus": "string",
         "RegistrationVersionStatusHistory": {
            "ApprovedTimestamp": number,
            "ArchivedTimestamp": number,
            "AwsReviewingTimestamp": number,
            "DeniedTimestamp": number,
            "DiscardedTimestamp": number,
            "DraftTimestamp": number,
            "RequiresAuthenticationTimestamp": number,
            "ReviewingTimestamp": number,
            "RevokedTimestamp": number,
            "SubmittedTimestamp": number
         },
         "VersionNumber": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRegistrationVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRegistrationVersions_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationVersions-response-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [RegistrationArn](#API_DescribeRegistrationVersions_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationVersions-response-RegistrationArn"></a>
The Amazon Resource Name (ARN) for the registration.
Type: String

 ** [RegistrationId](#API_DescribeRegistrationVersions_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationVersions-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [RegistrationVersions](#API_DescribeRegistrationVersions_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationVersions-response-RegistrationVersions"></a>
An array of RegistrationVersions objects.
Type: Array of [RegistrationVersionInformation](API_RegistrationVersionInformation.md) objects

## Errors
<a name="API_DescribeRegistrationVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRegistrationVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationVersions)
