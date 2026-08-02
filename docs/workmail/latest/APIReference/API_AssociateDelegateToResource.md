---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_AssociateDelegateToResource.html
---

# AssociateDelegateToResource
<a name="API_AssociateDelegateToResource"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Adds a member (user or group) to the resource's set of delegates.

## Request Syntax
<a name="API_AssociateDelegateToResource_RequestSyntax"></a>

```
{
   "EntityId": "{{string}}",
   "OrganizationId": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateDelegateToResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EntityId](#API_AssociateDelegateToResource_RequestSyntax) **   <a name="workmail-AssociateDelegateToResource-request-EntityId"></a>
The member (user or group) to associate to the resource.
The entity ID can accept *UserId or GroupID*, *Username or Groupname*, or *email*.
+ Entity: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234
+ Email address: entity@domain.tld
+ Entity: entity
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

 ** [OrganizationId](#API_AssociateDelegateToResource_RequestSyntax) **   <a name="workmail-AssociateDelegateToResource-request-OrganizationId"></a>
The organization under which the resource exists.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [ResourceId](#API_AssociateDelegateToResource_RequestSyntax) **   <a name="workmail-AssociateDelegateToResource-request-ResourceId"></a>
The resource for which members (users or groups) are associated.
The identifier can accept *ResourceId*, *Resourcename*, or *email*. The following identity formats are available:
+ Resource ID: r-0123456789a0123456789b0123456789
+ Email address: resource@domain.tld
+ Resource name: resource
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

## Response Elements
<a name="API_AssociateDelegateToResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateDelegateToResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
HTTP Status Code: 400

 ** EntityStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You are performing an operation on a user, group, or resource that isn't in the expected state, such as trying to delete an active user.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

 ** UnsupportedOperationException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You can't perform a write operation against a read-only directory.
HTTP Status Code: 400

## See Also
<a name="API_AssociateDelegateToResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/AssociateDelegateToResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/AssociateDelegateToResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/AssociateDelegateToResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/AssociateDelegateToResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/AssociateDelegateToResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/AssociateDelegateToResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/AssociateDelegateToResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/AssociateDelegateToResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/AssociateDelegateToResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/AssociateDelegateToResource)
