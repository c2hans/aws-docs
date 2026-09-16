---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateTheme.html
---

# CreateTheme
<a name="API_CreateTheme"></a>

Creates a theme to apply to the components in an Amplify app.

## Request Syntax
<a name="API_CreateTheme_RequestSyntax"></a>

```
POST /app/{{appId}}/environment/{{environmentName}}/themes?clientToken={{clientToken}} HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "overrides": [
      {
         "key": "{{string}}",
         "value": {
            "children": [
               "ThemeValues"
            ],
            "value": "{{string}}"
         }
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "values": [
      {
         "key": "{{string}}",
         "value": {
            "children": [
               "ThemeValues"
            ],
            "value": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateTheme_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_CreateTheme_RequestSyntax) **   <a name="amplifyuibuilder-CreateTheme-request-uri-appId"></a>
The unique ID of the Amplify app associated with the theme.
Required: Yes

 ** [clientToken](#API_CreateTheme_RequestSyntax) **   <a name="amplifyuibuilder-CreateTheme-request-uri-clientToken"></a>
The unique client token.

 ** [environmentName](#API_CreateTheme_RequestSyntax) **   <a name="amplifyuibuilder-CreateTheme-request-uri-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Required: Yes

## Request Body
<a name="API_CreateTheme_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreateTheme_RequestSyntax) **   <a name="amplifyuibuilder-CreateTheme-request-name"></a>
The name of the theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [overrides](#API_CreateTheme_RequestSyntax) **   <a name="amplifyuibuilder-CreateTheme-request-overrides"></a>
Describes the properties that can be overriden to customize an instance of the theme.
Type: Array of [ThemeValues](API_ThemeValues.md) objects
Required: No

 ** [tags](#API_CreateTheme_RequestSyntax) **   <a name="amplifyuibuilder-CreateTheme-request-tags"></a>
One or more key-value pairs to use when tagging the theme data.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [values](#API_CreateTheme_RequestSyntax) **   <a name="amplifyuibuilder-CreateTheme-request-values"></a>
A list of key-value pairs that deﬁnes the properties of the theme.
Type: Array of [ThemeValues](API_ThemeValues.md) objects
Required: Yes

## Response Syntax
<a name="API_CreateTheme_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appId": "string",
   "createdAt": "string",
   "environmentName": "string",
   "id": "string",
   "modifiedAt": "string",
   "name": "string",
   "overrides": [
      {
         "key": "string",
         "value": {
            "children": [
               "ThemeValues"
            ],
            "value": "string"
         }
      }
   ],
   "tags": {
      "string" : "string"
   },
   "values": [
      {
         "key": "string",
         "value": {
            "children": [
               "ThemeValues"
            ],
            "value": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_CreateTheme_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appId](#API_CreateTheme_ResponseSyntax) **   <a name="amplifyuibuilder-CreateTheme-response-appId"></a>
The unique ID for the Amplify app associated with the theme.
Type: String

 ** [createdAt](#API_CreateTheme_ResponseSyntax) **   <a name="amplifyuibuilder-CreateTheme-response-createdAt"></a>
The time that the theme was created.
Type: Timestamp

 ** [environmentName](#API_CreateTheme_ResponseSyntax) **   <a name="amplifyuibuilder-CreateTheme-response-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Type: String

 ** [id](#API_CreateTheme_ResponseSyntax) **   <a name="amplifyuibuilder-CreateTheme-response-id"></a>
The ID for the theme.
Type: String

 ** [modifiedAt](#API_CreateTheme_ResponseSyntax) **   <a name="amplifyuibuilder-CreateTheme-response-modifiedAt"></a>
The time that the theme was modified.
Type: Timestamp

 ** [name](#API_CreateTheme_ResponseSyntax) **   <a name="amplifyuibuilder-CreateTheme-response-name"></a>
The name of the theme.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [overrides](#API_CreateTheme_ResponseSyntax) **   <a name="amplifyuibuilder-CreateTheme-response-overrides"></a>
Describes the properties that can be overriden to customize a theme.
Type: Array of [ThemeValues](API_ThemeValues.md) objects

 ** [tags](#API_CreateTheme_ResponseSyntax) **   <a name="amplifyuibuilder-CreateTheme-response-tags"></a>
One or more key-value pairs to use when tagging the theme.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [values](#API_CreateTheme_ResponseSyntax) **   <a name="amplifyuibuilder-CreateTheme-response-values"></a>
A list of key-value pairs that defines the properties of the theme.
Type: Array of [ThemeValues](API_ThemeValues.md) objects

## Errors
<a name="API_CreateTheme_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Please retry your request.
HTTP Status Code: 500

 ** InvalidParameterException **
An invalid or out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource specified in the request conflicts with an existing resource.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
HTTP Status Code: 402

## See Also
<a name="API_CreateTheme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplifyuibuilder-2021-08-11/CreateTheme)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplifyuibuilder-2021-08-11/CreateTheme)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CreateTheme)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplifyuibuilder-2021-08-11/CreateTheme)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CreateTheme)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplifyuibuilder-2021-08-11/CreateTheme)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplifyuibuilder-2021-08-11/CreateTheme)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplifyuibuilder-2021-08-11/CreateTheme)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/amplifyuibuilder-2021-08-11/CreateTheme)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CreateTheme)
