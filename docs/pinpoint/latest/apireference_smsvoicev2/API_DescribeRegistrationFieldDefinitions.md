---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DescribeRegistrationFieldDefinitions.html
---

# DescribeRegistrationFieldDefinitions
<a name="API_DescribeRegistrationFieldDefinitions"></a>

Retrieves the specified registration type field definitions. You can use DescribeRegistrationFieldDefinitions to view the requirements for creating, filling out, and submitting each registration type.

## Request Syntax
<a name="API_DescribeRegistrationFieldDefinitions_RequestSyntax"></a>

```
{
   "FieldPaths": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RegistrationType": "{{string}}",
   "SectionPath": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRegistrationFieldDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FieldPaths](#API_DescribeRegistrationFieldDefinitions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldDefinitions-request-FieldPaths"></a>
An array of paths to the registration form field.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_\.]+`
Required: No

 ** [MaxResults](#API_DescribeRegistrationFieldDefinitions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldDefinitions-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeRegistrationFieldDefinitions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldDefinitions-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [RegistrationType](#API_DescribeRegistrationFieldDefinitions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldDefinitions-request-RegistrationType"></a>
The type of registration form. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](API_DescribeRegistrationTypeDefinitions.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** [SectionPath](#API_DescribeRegistrationFieldDefinitions_RequestSyntax) **   <a name="pinpoint-DescribeRegistrationFieldDefinitions-request-SectionPath"></a>
The path to the section of the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9_]+`
Required: No

## Response Syntax
<a name="API_DescribeRegistrationFieldDefinitions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RegistrationFieldDefinitions": [
      {
         "ConditionalBehavior": {
            "DefaultBehavior": "string",
            "Rules": [
               {
                  "ConditionalValidation": {
                     "AllowedValues": [ "string" ],
                     "MaxLength": number,
                     "MinLength": number,
                     "Pattern": "string"
                  },
                  "Conditions": [
                     {
                        "DependsOnFieldPath": "string",
                        "Operator": "string",
                        "Values": [ "string" ]
                     }
                  ],
                  "RuleBehavior": "string"
               }
            ]
         },
         "DisplayHints": {
            "DocumentationLink": "string",
            "DocumentationTitle": "string",
            "ExampleTextValue": "string",
            "LongDescription": "string",
            "SelectOptionDescriptions": [
               {
                  "Description": "string",
                  "Option": "string",
                  "Title": "string"
               }
            ],
            "ShortDescription": "string",
            "TextValidationDescription": "string",
            "Title": "string"
         },
         "FieldPath": "string",
         "FieldRequirement": "string",
         "FieldType": "string",
         "SectionPath": "string",
         "SelectValidation": {
            "MaxChoices": number,
            "MinChoices": number,
            "Options": [ "string" ]
         },
         "TextValidation": {
            "MaxLength": number,
            "MinLength": number,
            "Pattern": "string"
         }
      }
   ],
   "RegistrationType": "string"
}
```

## Response Elements
<a name="API_DescribeRegistrationFieldDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRegistrationFieldDefinitions_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationFieldDefinitions-response-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [RegistrationFieldDefinitions](#API_DescribeRegistrationFieldDefinitions_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationFieldDefinitions-response-RegistrationFieldDefinitions"></a>
An array of RegistrationFieldDefinitions objects that contain the details for the requested fields.
Type: Array of [RegistrationFieldDefinition](API_RegistrationFieldDefinition.md) objects

 ** [RegistrationType](#API_DescribeRegistrationFieldDefinitions_ResponseSyntax) **   <a name="pinpoint-DescribeRegistrationFieldDefinitions-response-RegistrationType"></a>
The type of registration form. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](API_DescribeRegistrationTypeDefinitions.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`

## Errors
<a name="API_DescribeRegistrationFieldDefinitions_Errors"></a>

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
<a name="API_DescribeRegistrationFieldDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DescribeRegistrationFieldDefinitions)
