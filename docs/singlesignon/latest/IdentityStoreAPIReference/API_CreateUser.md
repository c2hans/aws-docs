---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateUser.html
---

# CreateUser
<a name="API_CreateUser"></a>

Creates a user within the specified identity store.

## Request Syntax
<a name="API_CreateUser_RequestSyntax"></a>

```
{
   "Addresses": [
      {
         "Country": "{{string}}",
         "Formatted": "{{string}}",
         "Locality": "{{string}}",
         "PostalCode": "{{string}}",
         "Primary": {{boolean}},
         "Region": "{{string}}",
         "StreetAddress": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "Birthdate": "{{string}}",
   "DisplayName": "{{string}}",
   "Emails": [
      {
         "Primary": {{boolean}},
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Extensions": {
      "{{string}}" : {{JSON value}}
   },
   "IdentityStoreId": "{{string}}",
   "Locale": "{{string}}",
   "Name": {
      "FamilyName": "{{string}}",
      "Formatted": "{{string}}",
      "GivenName": "{{string}}",
      "HonorificPrefix": "{{string}}",
      "HonorificSuffix": "{{string}}",
      "MiddleName": "{{string}}"
   },
   "NickName": "{{string}}",
   "PhoneNumbers": [
      {
         "Primary": {{boolean}},
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Photos": [
      {
         "Display": "{{string}}",
         "Primary": {{boolean}},
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "PreferredLanguage": "{{string}}",
   "ProfileUrl": "{{string}}",
   "Roles": [
      {
         "Primary": {{boolean}},
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Timezone": "{{string}}",
   "Title": "{{string}}",
   "UserName": "{{string}}",
   "UserType": "{{string}}",
   "Website": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Addresses](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Addresses"></a>
A list of `Address` objects containing addresses associated with the user.
Type: Array of [Address](API_Address.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [Birthdate](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Birthdate"></a>
The user's birthdate in YYYY-MM-DD format. This field supports standard date format for storing personal information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** [DisplayName](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-DisplayName"></a>
A string containing the name of the user. This value is typically formatted for display when the user is referenced. For example, "John Doe." When used in IAM Identity Center, this parameter is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** [Emails](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Emails"></a>
A list of `Email` objects containing email addresses associated with the user.
Type: Array of [Email](API_Email.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [Extensions](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Extensions"></a>
A map with additional attribute extensions for the user. Each map key corresponds to an extension name, while map values represent extension data in `Document` type (not supported by Java V1, Go V1 and older versions of the AWS CLI). `aws:identitystore:enterprise` is the only supported extension name.
Type: String to JSON value map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `aws:identitystore:[a-z]{1,20}`
Required: No

 ** [IdentityStoreId](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [Locale](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Locale"></a>
A string containing the geographical region or location of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** [Name](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Name"></a>
An object containing the name of the user. When used in IAM Identity Center, this parameter is required.
Type: [Name](API_Name.md) object
Required: No

 ** [NickName](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-NickName"></a>
A string containing an alternate name for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** [PhoneNumbers](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-PhoneNumbers"></a>
A list of `PhoneNumber` objects containing phone numbers associated with the user.
Type: Array of [PhoneNumber](API_PhoneNumber.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [Photos](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Photos"></a>
A list of photos associated with the user. You can add up to 3 photos per user. Each photo can include a value, type, display name, and primary designation.
Type: Array of [Photo](API_Photo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

 ** [PreferredLanguage](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-PreferredLanguage"></a>
A string containing the preferred language of the user. For example, "American English" or "en-us."
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** [ProfileUrl](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-ProfileUrl"></a>
A string containing a URL that might be associated with the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** [Roles](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Roles"></a>
A list of `Role` objects containing roles associated with the user.
Type: Array of [Role](API_Role.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [Timezone](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Timezone"></a>
A string containing the time zone of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** [Title](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Title"></a>
A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** [UserName](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-UserName"></a>
A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store. `Administrator` and `AWSAdministrators` are reserved names and can't be used for users or groups.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** [UserType](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-UserType"></a>
A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** [Website](#API_CreateUser_RequestSyntax) **   <a name="singlesignon-CreateUser-request-Website"></a>
The user's personal website or blog URL. This field allows users to provide a link to their personal or professional website.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

## Response Syntax
<a name="API_CreateUser_ResponseSyntax"></a>

```
{
   "IdentityStoreId": "string",
   "UserId": "string"
}
```

## Response Elements
<a name="API_CreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityStoreId](#API_CreateUser_ResponseSyntax) **   <a name="singlesignon-CreateUser-response-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [UserId](#API_CreateUser_ResponseSyntax) **   <a name="singlesignon-CreateUser-response-UserId"></a>
The identifier of the newly created user in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

## Errors
<a name="API_CreateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
Indicates the reason for an access denial when returned by KMS while accessing a Customer Managed KMS key. For non-KMS access-denied errors, this field is not included.
 ** RequestId **
The identifier for each request. This value is a globally unique ID that is generated by the identity store service for each sent request, and is then returned inside the exception if the request fails.
HTTP Status Code: 400

 ** ConflictException **
This request cannot be completed for one of the following reasons:
+ Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.
+ The requested resource was being concurrently modified by another request.
 ** Reason **
Indicates the reason for a conflict error when the service is unable to access a Customer Managed KMS key. For non-KMS permission errors, this field is not included.
 ** RequestId **
The identifier for each request. This value is a globally unique ID that is generated by the identity store service for each sent request, and is then returned inside the exception if the request fails.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
 ** RequestId **
The identifier for each request. This value is a globally unique ID that is generated by the identity store service for each sent request, and is then returned inside the exception if the request fails.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying the next request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates that a requested resource is not found.
 ** Reason **
Indicates the reason for a resource not found error when the service is unable to access a Customer Managed KMS key. For non-KMS permission errors, this field is not included.
 ** RequestId **
The identifier for each request. This value is a globally unique ID that is generated by the identity store service for each sent request, and is then returned inside the exception if the request fails.
 ** ResourceId **
The identifier for a resource in the identity store that can be used as `UserId` or `GroupId`. The format for `ResourceId` is either `UUID` or `1234567890-UUID`, where `UUID` is a randomly generated value for each resource when it is created and `1234567890` represents the ` IdentityStoreId` string value. In the case that the identity store is migrated from a legacy SSO identity store, the `ResourceId` for that identity store will be in the format of `UUID`. Otherwise, it will be in the `1234567890-UUID` format.
 ** ResourceType **
An enum object indicating the type of resource in the identity store service. Valid values include USER, GROUP, and IDENTITY\_STORE.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request would cause the number of users or groups in the identity store to exceed the maximum allowed.
 ** RequestId **
The identifier for each request. This value is a globally unique ID that is generated by the identity store service for each sent request, and is then returned inside the exception if the request fails.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
Indicates the reason for the throttling error when the service is unable to access a Customer Managed KMS key. For non-KMS permission errors, this field is not included.
 ** RequestId **
The identifier for each request. This value is a globally unique ID that is generated by the identity store service for each sent request, and is then returned inside the exception if the request fails.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying the next request.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
Indicates the reason for the validation error when the service is unable to access a Customer Managed KMS key. For non-KMS permission errors, this field is not included.
 ** RequestId **
The identifier for each request. This value is a globally unique ID that is generated by the identity store service for each sent request, and is then returned inside the exception if the request fails.
HTTP Status Code: 400

## Examples
<a name="API_CreateUser_Examples"></a>

### Example
<a name="API_CreateUser_Example_1"></a>

This example creates a new user in the specified identity store.

#### Sample Request
<a name="API_CreateUser_Example_1_Request"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "UserName": "johndoe",
    "Name": {
        "Formatted": "John Steve Doe",
        "FamilyName": "Doe",
        "GivenName": "John",
        "MiddleName": "Steve",
        "HonorificPrefix": "Mr",
        "HonorificSuffix": "Jr"
    },
    "DisplayName": "John Doe",
    "NickName": "Johny",
    "ProfileUrl": "www.amazondomains.com",
    "Emails": [
        {
            "Value": "johndoe@example.com",
            "Type": "work",
            "Primary": true
        }
    ],
    "Addresses": [
        {
            "StreetAddress": "100 Universal City Plaza",
            "Locality": "Any Town",
            "Region": "WA",
            "PostalCode": "12345",
            "Country": "USA",
            "Formatted": "100 Universal City Plaza Any Town USA",
            "Type": "home",
            "Primary": true
        }
    ],
    "PhoneNumbers": [
        {
            "Value": "832-555-0100",
            "Type": "work",
            "Primary": true
        }
    ],
    "UserType": "temp",
    "Title": "Contractor",
    "PreferredLanguage": "en-us",
    "Locale": "NA",
    "Timezone": "pdt",
    "Extensions": {
        "aws:identitystore:enterprise": {
            "employeeNumber": "701984",
            "costCenter": "4130",
            "organization": "Universal Studios",
            "division": "Theme Park",
            "department": "Tour Operations",
            "manager": {
                "value": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444"
            }
        }
    }
}
```

#### Sample Response
<a name="API_CreateUser_Example_1_Response"></a>

```
{
    "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "IdentityStoreId": "d-1234567890"
}
```

## See Also
<a name="API_CreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/identitystore-2020-06-15/CreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/identitystore-2020-06-15/CreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/CreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/identitystore-2020-06-15/CreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/CreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/identitystore-2020-06-15/CreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/identitystore-2020-06-15/CreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/identitystore-2020-06-15/CreateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/identitystore-2020-06-15/CreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/CreateUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Identity Store. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
