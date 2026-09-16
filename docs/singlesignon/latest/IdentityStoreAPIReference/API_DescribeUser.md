---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html
---

# DescribeUser
<a name="API_DescribeUser"></a>

Retrieves the user metadata and attributes from the `UserId` in an identity store.

**Note**
If you have access to a member account, you can use this API operation from the member account. For more information, see [Limiting access to the identity store from member accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts) in the * AWS IAM Identity Center User Guide*.

## Request Syntax
<a name="API_DescribeUser_RequestSyntax"></a>

```
{
   "Extensions": [ "{{string}}" ],
   "IdentityStoreId": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Extensions](#API_DescribeUser_RequestSyntax) **   <a name="singlesignon-DescribeUser-request-Extensions"></a>
A collection of extension names indicating what extensions the service should retrieve alongside other user attributes. `aws:identitystore:enterprise` is the only supported extension name.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `aws:identitystore:[a-z]{1,20}`
Required: No

 ** [IdentityStoreId](#API_DescribeUser_RequestSyntax) **   <a name="singlesignon-DescribeUser-request-IdentityStoreId"></a>
The globally unique identifier for the identity store, such as `d-1234567890`. In this example, `d-` is a fixed prefix, and `1234567890` is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [UserId](#API_DescribeUser_RequestSyntax) **   <a name="singlesignon-DescribeUser-request-UserId"></a>
The identifier for a user in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeUser_ResponseSyntax"></a>

```
{
   "Addresses": [
      {
         "Country": "string",
         "Formatted": "string",
         "Locality": "string",
         "PostalCode": "string",
         "Primary": boolean,
         "Region": "string",
         "StreetAddress": "string",
         "Type": "string"
      }
   ],
   "Birthdate": "string",
   "CreatedAt": number,
   "CreatedBy": "string",
   "DisplayName": "string",
   "Emails": [
      {
         "Primary": boolean,
         "Type": "string",
         "Value": "string"
      }
   ],
   "Extensions": {
      "string" : JSON value
   },
   "ExternalIds": [
      {
         "Id": "string",
         "Issuer": "string"
      }
   ],
   "IdentityStoreId": "string",
   "Locale": "string",
   "Name": {
      "FamilyName": "string",
      "Formatted": "string",
      "GivenName": "string",
      "HonorificPrefix": "string",
      "HonorificSuffix": "string",
      "MiddleName": "string"
   },
   "NickName": "string",
   "PhoneNumbers": [
      {
         "Primary": boolean,
         "Type": "string",
         "Value": "string"
      }
   ],
   "Photos": [
      {
         "Display": "string",
         "Primary": boolean,
         "Type": "string",
         "Value": "string"
      }
   ],
   "PreferredLanguage": "string",
   "ProfileUrl": "string",
   "Roles": [
      {
         "Primary": boolean,
         "Type": "string",
         "Value": "string"
      }
   ],
   "Timezone": "string",
   "Title": "string",
   "UpdatedAt": number,
   "UpdatedBy": "string",
   "UserId": "string",
   "UserName": "string",
   "UserStatus": "string",
   "UserType": "string",
   "Website": "string"
}
```

## Response Elements
<a name="API_DescribeUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Addresses](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Addresses"></a>
The physical address of the user.
Type: Array of [Address](API_Address.md) objects
Array Members: Fixed number of 1 item.

 ** [Birthdate](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Birthdate"></a>
The user's birthdate in YYYY-MM-DD format. This field returns the stored birthdate information for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

 ** [CreatedAt](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-CreatedAt"></a>
The date and time the user was created.
Type: Timestamp

 ** [CreatedBy](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-CreatedBy"></a>
The identifier of the user or system that created the user.
Type: String

 ** [DisplayName](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-DisplayName"></a>
The display name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

 ** [Emails](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Emails"></a>
The email address of the user.
Type: Array of [Email](API_Email.md) objects
Array Members: Fixed number of 1 item.

 ** [Extensions](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Extensions"></a>
A map of explicitly requested attribute extensions associated with the user. Not populated if the user has no requested extensions.
Type: String to JSON value map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `aws:identitystore:[a-z]{1,20}`

 ** [ExternalIds](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-ExternalIds"></a>
A list of `ExternalId` objects that contains the identifiers issued to this resource by an external identity provider.
Type: Array of [ExternalId](API_ExternalId.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [IdentityStoreId](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [Locale](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Locale"></a>
A string containing the geographical region or location of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

 ** [Name](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Name"></a>
The name of the user.
Type: [Name](API_Name.md) object

 ** [NickName](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-NickName"></a>
An alternative descriptive name for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

 ** [PhoneNumbers](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-PhoneNumbers"></a>
A list of `PhoneNumber` objects associated with a user.
Type: Array of [PhoneNumber](API_PhoneNumber.md) objects
Array Members: Fixed number of 1 item.

 ** [Photos](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Photos"></a>
A list of photos associated with the user. Returns up to 3 photos with their associated metadata including type, display name, and primary designation.
Type: Array of [Photo](API_Photo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.

 ** [PreferredLanguage](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-PreferredLanguage"></a>
The preferred language of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

 ** [ProfileUrl](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-ProfileUrl"></a>
A URL link for the user's profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

 ** [Roles](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Roles"></a>
The roles of the user.
Type: Array of [Role](API_Role.md) objects
Array Members: Fixed number of 1 item.

 ** [Timezone](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Timezone"></a>
The time zone for a user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

 ** [Title](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Title"></a>
A string containing the title of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

 ** [UpdatedAt](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-UpdatedAt"></a>
The date and time the user was last updated.
Type: Timestamp

 ** [UpdatedBy](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-UpdatedBy"></a>
The identifier of the user or system that last updated the user.
Type: String

 ** [UserId](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-UserId"></a>
The identifier for a user in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [UserName](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-UserName"></a>
A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`

 ** [UserStatus](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-UserStatus"></a>
The current status of the user account.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [UserType](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-UserType"></a>
A string indicating the type of user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

 ** [Website](#API_DescribeUser_ResponseSyntax) **   <a name="singlesignon-DescribeUser-response-Website"></a>
The user's personal website or blog URL. Returns the stored website information for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`

## Errors
<a name="API_DescribeUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
Indicates the reason for an access denial when returned by KMS while accessing a Customer Managed KMS key. For non-KMS access-denied errors, this field is not included.
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
<a name="API_DescribeUser_Examples"></a>

### Example 1
<a name="API_DescribeUser_Example_1"></a>

This example retrieves only the core information about a user called John Doe.

#### Sample Request
<a name="API_DescribeUser_Example_1_Request"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "UserId": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p"
}
```

#### Sample Response
<a name="API_DescribeUser_Example_1_Response"></a>

```
 {
    "UserName": "johndoe",
    "UserId": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p",
    "Name": {
        "Formatted": "John Doe",
        "FamilyName": "Doe",
        "GivenName": "John",
    },
    "DisplayName": "John Doe",
    "Emails": [
        {
            "Value": "johndoe@example.com",
            "Type": "work",
            "Primary": true
        }
    ],
    "Addresses": [
        {
            "StreetAddress": "123 Main St",
            "Locality": "Any Town",
            "Region": "ST",
            "PostalCode": "12345",
            "Country": "USA",
            "Formatted": "123 Main St, Anytown, ST 12345, USA",
            "Type": "home"
        }
    ],
    "PhoneNumbers": [
        {
            "Value": "+1 (832) 555-0100",
            "Type": "work",
            "Primary": true
        }
    ],
    "IdentityStoreId": "d-1234567890"
}
```

### Example 2
<a name="API_DescribeUser_Example_2"></a>

This example retrieves both core and enterprise information about a user called John Doe.

#### Sample Request
<a name="API_DescribeUser_Example_2_Request"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "UserId": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p",
    "Extensions": ["aws:identitystore:enterprise"]
}
```

#### Sample Response
<a name="API_DescribeUser_Example_2_Response"></a>

```
 {
    "UserName": "johndoe",
    "UserId": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p",
    "Name": {
        "Formatted": "John Doe",
        "FamilyName": "Doe",
        "GivenName": "John",
    },
    "DisplayName": "John Doe",
    "Emails": [
        {
            "Value": "johndoe@example.com",
            "Type": "work",
            "Primary": true
        }
    ],
    "Addresses": [
        {
            "StreetAddress": "123 Main St",
            "Locality": "Any Town",
            "Region": "ST",
            "PostalCode": "12345",
            "Country": "USA",
            "Formatted": "123 Main St, Anytown, ST 12345, USA",
            "Type": "home"
        }
    ],
    "PhoneNumbers": [
        {
            "Value": "+1 (832) 555-0100",
            "Type": "work",
            "Primary": true
        }
    ],
    "IdentityStoreId": "d-1234567890",
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

## See Also
<a name="API_DescribeUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/identitystore-2020-06-15/DescribeUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/identitystore-2020-06-15/DescribeUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/DescribeUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/identitystore-2020-06-15/DescribeUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/DescribeUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/identitystore-2020-06-15/DescribeUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/identitystore-2020-06-15/DescribeUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/identitystore-2020-06-15/DescribeUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/identitystore-2020-06-15/DescribeUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/DescribeUser)
