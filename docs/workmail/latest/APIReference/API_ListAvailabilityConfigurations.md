---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListAvailabilityConfigurations.html
---

# ListAvailabilityConfigurations
<a name="API_ListAvailabilityConfigurations"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

List all the `AvailabilityConfiguration`'s for the given WorkMail organization.

## Request Syntax
<a name="API_ListAvailabilityConfigurations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAvailabilityConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListAvailabilityConfigurations_RequestSyntax) **   <a name="workmail-ListAvailabilityConfigurations-request-MaxResults"></a>
The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAvailabilityConfigurations_RequestSyntax) **   <a name="workmail-ListAvailabilityConfigurations-request-NextToken"></a>
The token to use to retrieve the next page of results. The first call does not require a token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`
Required: No

 ** [OrganizationId](#API_ListAvailabilityConfigurations_RequestSyntax) **   <a name="workmail-ListAvailabilityConfigurations-request-OrganizationId"></a>
The WorkMail organization for which the `AvailabilityConfiguration`'s will be listed.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_ListAvailabilityConfigurations_ResponseSyntax"></a>

```
{
   "AvailabilityConfigurations": [
      {
         "DateCreated": number,
         "DateModified": number,
         "DomainName": "string",
         "EwsProvider": {
            "EwsEndpoint": "string",
            "EwsUsername": "string"
         },
         "LambdaProvider": {
            "LambdaArn": "string"
         },
         "ProviderType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAvailabilityConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailabilityConfigurations](#API_ListAvailabilityConfigurations_ResponseSyntax) **   <a name="workmail-ListAvailabilityConfigurations-response-AvailabilityConfigurations"></a>
The list of `AvailabilityConfiguration`'s that exist for the specified WorkMail organization.
Type: Array of [AvailabilityConfiguration](API_AvailabilityConfiguration.md) objects

 ** [NextToken](#API_ListAvailabilityConfigurations_ResponseSyntax) **   <a name="workmail-ListAvailabilityConfigurations-response-NextToken"></a>
The token to use to retrieve the next page of results. The value is `null` when there are no further results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*|[a-zA-Z0-9/+=]{1,1024}`

## Errors
<a name="API_ListAvailabilityConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_ListAvailabilityConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/ListAvailabilityConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/ListAvailabilityConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ListAvailabilityConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/ListAvailabilityConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ListAvailabilityConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/ListAvailabilityConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/ListAvailabilityConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/ListAvailabilityConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/ListAvailabilityConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ListAvailabilityConfigurations)
