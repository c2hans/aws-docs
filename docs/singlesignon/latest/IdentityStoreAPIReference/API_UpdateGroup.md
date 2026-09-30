---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateGroup.html
---

# UpdateGroup
<a name="API_UpdateGroup"></a>

Updates the specified group metadata and attributes in the specified identity store.

## Request Syntax
<a name="API_UpdateGroup_RequestSyntax"></a>

```
{
   "GroupId": "{{string}}",
   "IdentityStoreId": "{{string}}",
   "Operations": [
      {
         "AttributePath": "{{string}}",
         "AttributeValue": {{JSON value}}
      }
   ],
   "Revision": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GroupId](#API_UpdateGroup_RequestSyntax) **   <a name="singlesignon-UpdateGroup-request-GroupId"></a>
The identifier for a group in the identity store.
You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID `a1b2c3d4-5678-90ab-cdef-EXAMPLE22222` or group ARN `arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(arn:aws[a-z-]*:identitystore:::(user|group|membership)/)?([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** [IdentityStoreId](#API_UpdateGroup_RequestSyntax) **   <a name="singlesignon-UpdateGroup-request-IdentityStoreId"></a>
The globally unique identifier for the identity store.
You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID `d-1234567890` or identity store ARN `arn:aws:identitystore::111122223333:identitystore/d-1234567890`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 93.
Pattern: `(arn:aws[a-z-]*:identitystore::\d{12}:identitystore/)?(d-[0-9a-f]{10}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: Yes

 ** [Operations](#API_UpdateGroup_RequestSyntax) **   <a name="singlesignon-UpdateGroup-request-Operations"></a>
A list of `AttributeOperation` objects to apply to the requested group. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see [Group](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html).
Type: Array of [AttributeOperation](API_AttributeOperation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [Revision](#API_UpdateGroup_RequestSyntax) **   <a name="singlesignon-UpdateGroup-request-Revision"></a>
The expected current revision of the group. When you provide this value, the update is applied only if it matches the current revision of the group in the identity store, which prevents you from overwriting concurrent changes. If the value doesn't match, the operation fails with a `ConflictException`. If you don't provide this value, the update is applied unconditionally.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9]+`
Required: No

## Response Syntax
<a name="API_UpdateGroup_ResponseSyntax"></a>

```
{
   "GroupArn": "string",
   "GroupId": "string",
   "IdentityStoreId": "string",
   "Revision": "string"
}
```

## Response Elements
<a name="API_UpdateGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GroupArn](#API_UpdateGroup_ResponseSyntax) **   <a name="singlesignon-UpdateGroup-response-GroupArn"></a>
The Amazon Resource Name (ARN) of the group in the identity store. For example, `arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 100.
Pattern: `arn:aws[a-z-]*:identitystore:::(user|group|membership)/([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [GroupId](#API_UpdateGroup_ResponseSyntax) **   <a name="singlesignon-UpdateGroup-response-GroupId"></a>
The identifier for a group in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(arn:aws[a-z-]*:identitystore:::(user|group|membership)/)?([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`

 ** [IdentityStoreId](#API_UpdateGroup_ResponseSyntax) **   <a name="singlesignon-UpdateGroup-response-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 93.
Pattern: `(arn:aws[a-z-]*:identitystore::\d{12}:identitystore/)?(d-[0-9a-f]{10}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`

 ** [Revision](#API_UpdateGroup_ResponseSyntax) **   <a name="singlesignon-UpdateGroup-response-Revision"></a>
The revision of the group after the requested update is applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9]+`

## Errors
<a name="API_UpdateGroup_Errors"></a>

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
Indicates the reason for the conflict error. `UNIQUENESS_CONSTRAINT_VIOLATION` indicates that the request would violate an existing uniqueness constraint, such as a user name or other unique attribute that is already in use. `CONCURRENT_MODIFICATION` indicates that the resource was modified by another request during this operation.
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
An enum object indicating the type of resource in the identity store service. Valid values include USER, GROUP, GROUP\_MEMBERSHIP, RESOURCE\_POLICY, and IDENTITY\_STORE.
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
<a name="API_UpdateGroup_Examples"></a>

### Example 1
<a name="API_UpdateGroup_Example_1"></a>

This example updates the display name of the specified group to "Engineers" and passes the current `Revision` so that your update is applied only if the group hasn't changed since you last read it (optimistic locking). The response returns the new `Revision`.

#### Sample Request
<a name="API_UpdateGroup_Example_1_Request"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "GroupId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "Revision": "1699564800000",
    "Operations": [
        {
            "AttributePath": "displayName",
            "AttributeValue": "Engineers"
        }
    ]
}
```

#### Sample Response
<a name="API_UpdateGroup_Example_1_Response"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "GroupId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "GroupArn": "arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "Revision": "1699651200000"
}
```

### Example 2
<a name="API_UpdateGroup_Example_2"></a>

This example updates the description of the specified group to "Contains all engineers." If you omit `Revision`, your update is applied unconditionally.

#### Sample Request
<a name="API_UpdateGroup_Example_2_Request"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "GroupId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "Operations": [
        {
            "AttributePath": "description",
            "AttributeValue": "Contains all engineers"
        }
    ]
}
```

#### Sample Response
<a name="API_UpdateGroup_Example_2_Response"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "GroupId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "GroupArn": "arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "Revision": "1699651200000"
}
```

### Example 3
<a name="API_UpdateGroup_Example_3"></a>

This example removes the description from the specified group.

#### Sample Request
<a name="API_UpdateGroup_Example_3_Request"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "GroupId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "Operations": [
        {
            "AttributePath": "description"
        }
    ]
}
```

#### Sample Response
<a name="API_UpdateGroup_Example_3_Response"></a>

```
{
    "IdentityStoreId": "d-1234567890",
    "GroupId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "GroupArn": "arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "Revision": "1699651200000"
}
```

## See Also
<a name="API_UpdateGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/identitystore-2020-06-15/UpdateGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/identitystore-2020-06-15/UpdateGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/UpdateGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/identitystore-2020-06-15/UpdateGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/UpdateGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/identitystore-2020-06-15/UpdateGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/identitystore-2020-06-15/UpdateGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/identitystore-2020-06-15/UpdateGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/identitystore-2020-06-15/UpdateGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/UpdateGroup)
