---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationTypeDefinitions.html
---

# DescribeRegistrationTypeDefinitions
<a name="API_DescribeRegistrationTypeDefinitions"></a>

Retrieves the specified registration type definitions. You can use DescribeRegistrationTypeDefinitions to view the requirements for creating, filling out, and submitting each registration type.

## Request Syntax
<a name="API_DescribeRegistrationTypeDefinitions_RequestSyntax"></a>

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
   "RegistrationTypes": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeRegistrationTypeDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeRegistrationTypeDefinitions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationTypeDefinitions-request-Filters"></a>
An array of RegistrationFilter objects to filter the results.
Type: Array of [RegistrationTypeFilter](API_RegistrationTypeFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_DescribeRegistrationTypeDefinitions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationTypeDefinitions-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRegistrationTypeDefinitions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationTypeDefinitions-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [RegistrationTypes](#API_DescribeRegistrationTypeDefinitions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationTypeDefinitions-request-RegistrationTypes"></a>
The type of registration form. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](#API_DescribeRegistrationTypeDefinitions) action.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`
Required: No

## Response Syntax
<a name="API_DescribeRegistrationTypeDefinitions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RegistrationTypeDefinitions": [
      {
         "DisplayHints": {
            "DocumentationLink": "string",
            "DocumentationTitle": "string",
            "LongDescription": "string",
            "ShortDescription": "string",
            "Title": "string"
         },
         "RegistrationType": "string",
         "SupportedAssociations": [
            {
               "AssociationBehavior": "string",
               "DisassociationBehavior": "string",
               "IsoCountryCode": "string",
               "ResourceType": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRegistrationTypeDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRegistrationTypeDefinitions_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationTypeDefinitions-response-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [RegistrationTypeDefinitions](#API_DescribeRegistrationTypeDefinitions_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationTypeDefinitions-response-RegistrationTypeDefinitions"></a>
The type of registration form. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](#API_DescribeRegistrationTypeDefinitions) action.
Type: Array of [RegistrationTypeDefinition](API_RegistrationTypeDefinition.md) objects

## Errors
<a name="API_DescribeRegistrationTypeDefinitions_Errors"></a>

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
<a name="API_DescribeRegistrationTypeDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationTypeDefinitions)
