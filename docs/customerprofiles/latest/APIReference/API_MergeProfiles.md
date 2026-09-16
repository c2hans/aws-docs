---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_MergeProfiles.html
---

# MergeProfiles
<a name="API_connect-customer-profiles_MergeProfiles"></a>

Runs an AWS Lambda job that does the following:

1. All the profileKeys in the `ProfileToBeMerged` will be moved to the main profile.

1. All the objects in the `ProfileToBeMerged` will be moved to the main profile.

1. All the `ProfileToBeMerged` will be deleted at the end.

1. All the profileKeys in the `ProfileIdsToBeMerged` will be moved to the main profile.

1. Standard fields are merged as follows:

   1. Fields are always "union"-ed if there are no conflicts in standard fields or attributeKeys.

   1. When there are conflicting fields:

      1. If no `SourceProfileIds` entry is specified, the main Profile value is always taken.

      1. If a `SourceProfileIds` entry is specified, the specified profileId is always taken, even if it is a NULL value.

You can use MergeProfiles together with [GetMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html), which returns potentially matching profiles, or use it with the results of another matching system. After profiles have been merged, they cannot be separated (unmerged).

## Request Syntax
<a name="API_connect-customer-profiles_MergeProfiles_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/profiles/objects/merge HTTP/1.1
Content-type: application/json

{
   "FieldSourceProfileIds": {
      "AccountNumber": "{{string}}",
      "AdditionalInformation": "{{string}}",
      "Address": "{{string}}",
      "Attributes": {
         "{{string}}" : "{{string}}"
      },
      "BillingAddress": "{{string}}",
      "BirthDate": "{{string}}",
      "BusinessEmailAddress": "{{string}}",
      "BusinessName": "{{string}}",
      "BusinessPhoneNumber": "{{string}}",
      "EmailAddress": "{{string}}",
      "EngagementPreferences": "{{string}}",
      "FirstName": "{{string}}",
      "Gender": "{{string}}",
      "HomePhoneNumber": "{{string}}",
      "LastName": "{{string}}",
      "MailingAddress": "{{string}}",
      "MiddleName": "{{string}}",
      "MobilePhoneNumber": "{{string}}",
      "PartyType": "{{string}}",
      "PersonalEmailAddress": "{{string}}",
      "PhoneNumber": "{{string}}",
      "ProfileType": "{{string}}",
      "ShippingAddress": "{{string}}"
   },
   "MainProfileId": "{{string}}",
   "ProfileIdsToBeMerged": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_MergeProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_MergeProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_MergeProfiles-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_MergeProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FieldSourceProfileIds](#API_connect-customer-profiles_MergeProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_MergeProfiles-request-FieldSourceProfileIds"></a>
The identifiers of the fields in the profile that has the information you want to apply to the merge. For example, say you want to merge EmailAddress from Profile1 into MainProfile. This would be the identifier of the EmailAddress field in Profile1.
Type: [FieldSourceProfileIds](API_connect-customer-profiles_FieldSourceProfileIds.md) object
Required: No

 ** [MainProfileId](#API_connect-customer-profiles_MergeProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_MergeProfiles-request-MainProfileId"></a>
The identifier of the profile to be taken.
Type: String
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** [ProfileIdsToBeMerged](#API_connect-customer-profiles_MergeProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_MergeProfiles-request-ProfileIdsToBeMerged"></a>
The identifier of the profile to be merged into MainProfileId.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_MergeProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Message": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_MergeProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Message](#API_connect-customer-profiles_MergeProfiles_ResponseSyntax) **   <a name="connect-connect-customer-profiles_MergeProfiles-response-Message"></a>
A message that indicates the merge request is complete.
Type: String

## Errors
<a name="API_connect-customer-profiles_MergeProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## Examples
<a name="API_connect-customer-profiles_MergeProfiles_Examples"></a>

### Example 1
<a name="API_connect-customer-profiles_MergeProfiles_Example_1"></a>

Fields are always "union"-ed if there are no conflicts in standard fields or attributeKeys.

```
MainProfile: {
    "FirstName": "Jane"
}

ProfileToBeMerged1: {
    "LastName": "Doe"
}

ProfileToBeMerged2: {
    "MiddleName": "None"
}

mergeOf(MainProfile, [ProfileToBeMerged1, ProfileToBeMerged2] // Yields a MainProfile that looks like the following:
    MainProfile: {
       "FirstName": "Jane",
       "LastName": "Doe",
       "MiddleName": "None"
   }
```

### Example 2
<a name="API_connect-customer-profiles_MergeProfiles_Example_2"></a>

When there are conflicting fields, if no SourceProfileIds entry is specified, the main Profile value is always taken.

```
MainProfile: {
    "FirstName": "Jane"
}

ProfileToBeMerged1: {
    "LastName": "Doe"
}

ProfileToBeMerged2: {
    "FirstName": "Jorge" // Note that this has conflict with MainProfile
}

mergeOf(MainProfile, [ProfileToBeMerged1, ProfileToBeMerged2] // Yields a MainProfile that looks like the following:
    MainProfile: {
       "FirstName": "Jane", // "Jane" stays as that is what MainProfile is
       "LastName": "Doe"
   }
```

### Example 3
<a name="API_connect-customer-profiles_MergeProfiles_Example_3"></a>

When there are conflicting fields, if a SourceProfileIds entry is specified, the specified profileId is always taken, even if it is a NULL value.

```
MainProfile: {
    "FirstName": "Jane"
}

ProfileToBeMerged1: {
    "LastName": "Doe"
}

ProfileToBeMerged2: {
    "FirstName": "Jorge" // Note that this has conflict with MainProfile
}

SourceProfileIds: {
    "FirstName": "secondaryProfile2"
}

mergeOf(MainProfile, [ProfileToBeMerged1, ProfileToBeMerged2] // Yields a MainProfile that looks like the following:
    MainProfile: {
       "FirstName": "Jorge", // "Jorge" gets picked because SourceProfileIds is specified
       "LastName": "Doe"
}
```

## See Also
<a name="API_connect-customer-profiles_MergeProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/MergeProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/MergeProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/MergeProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/MergeProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/MergeProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/MergeProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/MergeProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/MergeProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/MergeProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/MergeProfiles)
