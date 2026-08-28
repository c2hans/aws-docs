---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeResource.html
---

# DescribeResource
<a name="API_DescribeResource"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Returns the data available for the resource.

## Request Syntax
<a name="API_DescribeResource_RequestSyntax"></a>

```
{
   "OrganizationId": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationId](#API_DescribeResource_RequestSyntax) **   <a name="workmail-DescribeResource-request-OrganizationId"></a>
The identifier associated with the organization for which the resource is described.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [ResourceId](#API_DescribeResource_RequestSyntax) **   <a name="workmail-DescribeResource-request-ResourceId"></a>
The identifier of the resource to be described.
The identifier can accept *ResourceId*, *Resourcename*, or *email*. The following identity formats are available:
+ Resource ID: r-0123456789a0123456789b0123456789
+ Email address: resource@domain.tld
+ Resource name: resource
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeResource_ResponseSyntax"></a>

```
{
   "BookingOptions": {
      "AutoAcceptRequests": boolean,
      "AutoDeclineConflictingRequests": boolean,
      "AutoDeclineRecurringRequests": boolean
   },
   "Description": "string",
   "DisabledDate": number,
   "Email": "string",
   "EnabledDate": number,
   "HiddenFromGlobalAddressList": boolean,
   "Name": "string",
   "ResourceId": "string",
   "State": "string",
   "Type": "string"
}
```

## Response Elements
<a name="API_DescribeResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BookingOptions](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-BookingOptions"></a>
The booking options for the described resource.
Type: [BookingOptions](API_BookingOptions.md) object

 ** [Description](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-Description"></a>
Description of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [DisabledDate](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-DisabledDate"></a>
The date and time when a resource was disabled from WorkMail, in UNIX epoch time format.
Type: Timestamp

 ** [Email](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-Email"></a>
The email of the described resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z-]{2,}`

 ** [EnabledDate](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-EnabledDate"></a>
The date and time when a resource was enabled for WorkMail, in UNIX epoch time format.
Type: Timestamp

 ** [HiddenFromGlobalAddressList](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-HiddenFromGlobalAddressList"></a>
If enabled, the resource is hidden from the global address list.
Type: Boolean

 ** [Name](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-Name"></a>
The name of the described resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\w\-.]+(@[a-zA-Z0-9.\-]+\.[a-zA-Z0-9-]{2,})?`

 ** [ResourceId](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-ResourceId"></a>
The identifier of the described resource.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^r-[0-9a-f]{32}$`

 ** [State](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-State"></a>
The state of the resource: enabled (registered to WorkMail), disabled (deregistered or never registered to WorkMail), or deleted.
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`

 ** [Type](#API_DescribeResource_ResponseSyntax) **   <a name="workmail-DescribeResource-response-Type"></a>
The type of the described resource.
Type: String
Valid Values: `ROOM | EQUIPMENT`

## Errors
<a name="API_DescribeResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
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
<a name="API_DescribeResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/DescribeResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/DescribeResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/DescribeResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/DescribeResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/DescribeResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/DescribeResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/DescribeResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/DescribeResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/DescribeResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/DescribeResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
