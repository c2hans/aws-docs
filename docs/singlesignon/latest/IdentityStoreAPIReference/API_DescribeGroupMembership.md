---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroupMembership.html
---

# DescribeGroupMembership
<a name="API_DescribeGroupMembership"></a>

Retrieves membership metadata and attributes from `MembershipId` in an identity store.

**Note**
If you have access to a member account, you can use this API operation from the member account. For more information, see [Limiting access to the identity store from member accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts) in the * AWS IAM Identity Center User Guide*.

## Request Syntax
<a name="API_DescribeGroupMembership_RequestSyntax"></a>

```
{
   "IdentityStoreId": "{{string}}",
   "MembershipId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGroupMembership_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityStoreId](#API_DescribeGroupMembership_RequestSyntax) **   <a name="singlesignon-DescribeGroupMembership-request-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [MembershipId](#API_DescribeGroupMembership_RequestSyntax) **   <a name="singlesignon-DescribeGroupMembership-request-MembershipId"></a>
The identifier for a `GroupMembership` in an identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeGroupMembership_ResponseSyntax"></a>

```
{
   "CreatedAt": number,
   "CreatedBy": "string",
   "GroupId": "string",
   "IdentityStoreId": "string",
   "MemberId": { ... },
   "MembershipId": "string",
   "UpdatedAt": number,
   "UpdatedBy": "string"
}
```

## Response Elements
<a name="API_DescribeGroupMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_DescribeGroupMembership_ResponseSyntax) **   <a name="singlesignon-DescribeGroupMembership-response-CreatedAt"></a>
The date and time the group membership was created.
Type: Timestamp

 ** [CreatedBy](#API_DescribeGroupMembership_ResponseSyntax) **   <a name="singlesignon-DescribeGroupMembership-response-CreatedBy"></a>
The identifier of the user or system that created the group membership.
Type: String

 ** [GroupId](#API_DescribeGroupMembership_ResponseSyntax) **   <a name="singlesignon-DescribeGroupMembership-response-GroupId"></a>
The identifier for a group in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [IdentityStoreId](#API_DescribeGroupMembership_ResponseSyntax) **   <a name="singlesignon-DescribeGroupMembership-response-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [MemberId](#API_DescribeGroupMembership_ResponseSyntax) **   <a name="singlesignon-DescribeGroupMembership-response-MemberId"></a>
An object containing the identifier of a group member.
Type: [MemberId](API_MemberId.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [MembershipId](#API_DescribeGroupMembership_ResponseSyntax) **   <a name="singlesignon-DescribeGroupMembership-response-MembershipId"></a>
The identifier for a `GroupMembership` in an identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [UpdatedAt](#API_DescribeGroupMembership_ResponseSyntax) **   <a name="singlesignon-DescribeGroupMembership-response-UpdatedAt"></a>
The date and time the group membership was last updated.
Type: Timestamp

 ** [UpdatedBy](#API_DescribeGroupMembership_ResponseSyntax) **   <a name="singlesignon-DescribeGroupMembership-response-UpdatedBy"></a>
The identifier of the user or system that last updated the group membership.
Type: String

## Errors
<a name="API_DescribeGroupMembership_Errors"></a>

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
<a name="API_DescribeGroupMembership_Examples"></a>

### Example
<a name="API_DescribeGroupMembership_Example_1"></a>

This example retrieves the member ID for the user and group ID for the group for the specified membership.

#### Sample Request
<a name="API_DescribeGroupMembership_Example_1_Request"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "MembershipId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
}
```

#### Sample Response
<a name="API_DescribeGroupMembership_Example_1_Response"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "MembershipId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
    "GroupId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "MemberId": {
        "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
      }
}
```

## See Also
<a name="API_DescribeGroupMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/identitystore-2020-06-15/DescribeGroupMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/identitystore-2020-06-15/DescribeGroupMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/DescribeGroupMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/identitystore-2020-06-15/DescribeGroupMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/DescribeGroupMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/identitystore-2020-06-15/DescribeGroupMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/identitystore-2020-06-15/DescribeGroupMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/identitystore-2020-06-15/DescribeGroupMembership)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/identitystore-2020-06-15/DescribeGroupMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/DescribeGroupMembership)
