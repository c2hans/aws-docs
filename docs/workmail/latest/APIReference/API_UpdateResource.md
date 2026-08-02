---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_UpdateResource.html
---

# UpdateResource
<a name="API_UpdateResource"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Updates data for the resource. To have the latest information, it must be preceded by a [DescribeResource](API_DescribeResource.md) call. The dataset in the request should be the one expected when performing another `DescribeResource` call.

## Request Syntax
<a name="API_UpdateResource_RequestSyntax"></a>

```
{
   "BookingOptions": {
      "AutoAcceptRequests": {{boolean}},
      "AutoDeclineConflictingRequests": {{boolean}},
      "AutoDeclineRecurringRequests": {{boolean}}
   },
   "Description": "{{string}}",
   "HiddenFromGlobalAddressList": {{boolean}},
   "Name": "{{string}}",
   "OrganizationId": "{{string}}",
   "ResourceId": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BookingOptions](#API_UpdateResource_RequestSyntax) **   <a name="workmail-UpdateResource-request-BookingOptions"></a>
The resource's booking options to be updated.
Type: [BookingOptions](API_BookingOptions.md) object
Required: No

 ** [Description](#API_UpdateResource_RequestSyntax) **   <a name="workmail-UpdateResource-request-Description"></a>
Updates the resource description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [HiddenFromGlobalAddressList](#API_UpdateResource_RequestSyntax) **   <a name="workmail-UpdateResource-request-HiddenFromGlobalAddressList"></a>
If enabled, the resource is hidden from the global address list.
Type: Boolean
Required: No

 ** [Name](#API_UpdateResource_RequestSyntax) **   <a name="workmail-UpdateResource-request-Name"></a>
The name of the resource to be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\w\-.]+(@[a-zA-Z0-9.\-]+\.[a-zA-Z0-9-]{2,})?`
Required: No

 ** [OrganizationId](#API_UpdateResource_RequestSyntax) **   <a name="workmail-UpdateResource-request-OrganizationId"></a>
The identifier associated with the organization for which the resource is updated.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [ResourceId](#API_UpdateResource_RequestSyntax) **   <a name="workmail-UpdateResource-request-ResourceId"></a>
The identifier of the resource to be updated.
The identifier can accept *ResourceId*, *Resourcename*, or *email*. The following identity formats are available:
+ Resource ID: r-0123456789a0123456789b0123456789
+ Email address: resource@domain.tld
+ Resource name: resource
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

 ** [Type](#API_UpdateResource_RequestSyntax) **   <a name="workmail-UpdateResource-request-Type"></a>
Updates the resource type.
Type: String
Valid Values: `ROOM | EQUIPMENT`
Required: No

## Response Elements
<a name="API_UpdateResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectoryUnavailableException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The directory is unavailable. It might be located in another Region or deleted.
HTTP Status Code: 400

 ** EmailAddressInUseException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The email address that you're trying to assign is already created for a different user, group, or resource.
HTTP Status Code: 400

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
HTTP Status Code: 400

 ** EntityStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
You are performing an operation on a user, group, or resource that isn't in the expected state, such as trying to delete an active user.
HTTP Status Code: 400

 ** InvalidConfigurationException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The configuration for a resource isn't valid. A resource must either be able to auto-respond to requests or have at least one delegate associated that can do so on its behalf.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** MailDomainNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The domain specified is not found in your organization.
HTTP Status Code: 400

 ** MailDomainStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
After a domain has been added to the organization, it must be verified. The domain is not yet verified.
HTTP Status Code: 400

 ** NameAvailabilityException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The user, group, or resource name isn't unique in WorkMail.
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
<a name="API_UpdateResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/UpdateResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/UpdateResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/UpdateResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/UpdateResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/UpdateResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/UpdateResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/UpdateResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/UpdateResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/UpdateResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/UpdateResource)
