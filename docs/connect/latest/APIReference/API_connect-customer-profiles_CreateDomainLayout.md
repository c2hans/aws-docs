---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_CreateDomainLayout.html
---

# CreateDomainLayout
<a name="API_connect-customer-profiles_CreateDomainLayout"></a>

Creates the layout to view data for a specific domain. This API can only be invoked from the Amazon Connect admin website.

## Request Syntax
<a name="API_connect-customer-profiles_CreateDomainLayout_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/layouts/{{LayoutDefinitionName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "IsDefault": {{boolean}},
   "Layout": "{{string}}",
   "LayoutType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateDomainLayout_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateDomainLayout_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [LayoutDefinitionName](#API_connect-customer-profiles_CreateDomainLayout_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-request-uri-LayoutDefinitionName"></a>
The unique name of the layout.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateDomainLayout_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_connect-customer-profiles_CreateDomainLayout_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-request-Description"></a>
The description of the layout
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** [DisplayName](#API_connect-customer-profiles_CreateDomainLayout_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-request-DisplayName"></a>
The display name of the layout
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`
Required: Yes

 ** [IsDefault](#API_connect-customer-profiles_CreateDomainLayout_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-request-IsDefault"></a>
If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.
Type: Boolean
Required: No

 ** [Layout](#API_connect-customer-profiles_CreateDomainLayout_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-request-Layout"></a>
A customizable layout that can be used to view data under a Customer Profiles domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000000.
Required: Yes

 ** [LayoutType](#API_connect-customer-profiles_CreateDomainLayout_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-request-LayoutType"></a>
The type of layout that can be used to view data under a Customer Profiles domain.
Type: String
Valid Values: `PROFILE_EXPLORER`
Required: Yes

 ** [Tags](#API_connect-customer-profiles_CreateDomainLayout_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "Description": "string",
   "DisplayName": "string",
   "IsDefault": boolean,
   "LastUpdatedAt": number,
   "Layout": "string",
   "LayoutDefinitionName": "string",
   "LayoutType": "string",
   "Tags": {
      "string" : "string"
   },
   "Version": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateDomainLayout_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-CreatedAt"></a>
The timestamp of when the layout was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-Description"></a>
The description of the layout
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [DisplayName](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-DisplayName"></a>
The display name of the layout
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`

 ** [IsDefault](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-IsDefault"></a>
If set to true for a layout, this layout will be used by default to view data. If set to false, then the layout will not be used by default, but it can be used to view data by explicitly selecting it in the console.
Type: Boolean

 ** [LastUpdatedAt](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-LastUpdatedAt"></a>
The timestamp of when the layout was most recently updated.
Type: Timestamp

 ** [Layout](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-Layout"></a>
A customizable layout that can be used to view data under Customer Profiles domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000000.

 ** [LayoutDefinitionName](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-LayoutDefinitionName"></a>
The unique name of the layout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [LayoutType](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-LayoutType"></a>
The type of layout that can be used to view data under customer profiles domain.
Type: String
Valid Values: `PROFILE_EXPLORER`

 ** [Tags](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

 ** [Version](#API_connect-customer-profiles_CreateDomainLayout_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateDomainLayout-response-Version"></a>
The version used to create layout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_connect-customer-profiles_CreateDomainLayout_Errors"></a>

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
<a name="API_connect-customer-profiles_CreateDomainLayout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateDomainLayout)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateDomainLayout)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateDomainLayout)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateDomainLayout)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateDomainLayout)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateDomainLayout)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateDomainLayout)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateDomainLayout)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateDomainLayout)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateDomainLayout)
