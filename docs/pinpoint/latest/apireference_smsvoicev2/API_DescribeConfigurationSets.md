---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeConfigurationSets.html
---

# DescribeConfigurationSets
<a name="API_DescribeConfigurationSets"></a>

Describes the specified configuration sets or all in your account.

If you specify configuration set names, the output includes information for only the specified configuration sets. If you specify filters, the output includes information for only those configuration sets that meet the filter criteria. If you don't specify configuration set names or filters, the output includes information for all configuration sets.

If you specify a configuration set name that isn't valid, an error is returned.

## Request Syntax
<a name="API_DescribeConfigurationSets_RequestSyntax"></a>

```
{
   "ConfigurationSetNames": [ "{{string}}" ],
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConfigurationSets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetNames](#API_DescribeConfigurationSets_RequestSyntax) **   <a name="pinpoint-DescribeConfigurationSets-request-ConfigurationSetNames"></a>
An array of strings. Each element can be either a ConfigurationSetName or ConfigurationSetArn.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: No

 ** [Filters](#API_DescribeConfigurationSets_RequestSyntax) **   <a name="pinpoint-DescribeConfigurationSets-request-Filters"></a>
An array of filters to apply to the results that are returned.
Type: Array of [ConfigurationSetFilter](API_ConfigurationSetFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribeConfigurationSets_RequestSyntax) **   <a name="pinpoint-DescribeConfigurationSets-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeConfigurationSets_RequestSyntax) **   <a name="pinpoint-DescribeConfigurationSets-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

## Response Syntax
<a name="API_DescribeConfigurationSets_ResponseSyntax"></a>

```
{
   "ConfigurationSets": [
      {
         "ConfigurationSetArn": "string",
         "ConfigurationSetName": "string",
         "CreatedTimestamp": number,
         "DefaultMessageFeedbackEnabled": boolean,
         "DefaultMessageType": "string",
         "DefaultSenderId": "string",
         "EventDestinations": [
            {
               "CloudWatchLogsDestination": {
                  "IamRoleArn": "string",
                  "LogGroupArn": "string"
               },
               "Enabled": boolean,
               "EventDestinationName": "string",
               "KinesisFirehoseDestination": {
                  "DeliveryStreamArn": "string",
                  "IamRoleArn": "string"
               },
               "MatchingEventTypes": [ "string" ],
               "SnsDestination": {
                  "TopicArn": "string"
               }
            }
         ],
         "ProtectConfigurationId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConfigurationSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationSets](#API_DescribeConfigurationSets_ResponseSyntax) **   <a name="pinpoint-DescribeConfigurationSets-response-ConfigurationSets"></a>
An array of ConfigurationSets objects.
Type: Array of [ConfigurationSetInformation](API_ConfigurationSetInformation.md) objects

 ** [NextToken](#API_DescribeConfigurationSets_ResponseSyntax) **   <a name="pinpoint-DescribeConfigurationSets-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

## Errors
<a name="API_DescribeConfigurationSets_Errors"></a>

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
<a name="API_DescribeConfigurationSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeConfigurationSets)
