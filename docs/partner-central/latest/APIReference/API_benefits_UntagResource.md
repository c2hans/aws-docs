---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_UntagResource.html
---

# UntagResource
<a name="API_benefits_UntagResource"></a>

Removes specified tags from a resource.

## Request Syntax
<a name="API_benefits_UntagResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}",
   "tagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_benefits_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [resourceArn](#API_benefits_UntagResource_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UntagResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to remove tags from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `arn:[\w+=/,.@-]+:partnercentral:[\w+=/,.@-]*:[0-9]{12}:catalog/([a-zA-Z]+)/[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

 ** [tagKeys](#API_benefits_UntagResource_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_UntagResource-request-tagKeys"></a>
A list of tag keys to remove from the resource.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

## Response Elements
<a name="API_benefits_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_benefits_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Thrown when the caller does not have sufficient permissions to perform the requested operation.
 ** Message **
A message describing the access denial.
HTTP Status Code: 400

 ** ConflictException **
Thrown when the request conflicts with the current state of the resource, such as attempting to modify a resource that has been changed by another process.
 ** Message **
A message describing the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an unexpected error occurs on the server side during request processing.
 ** Message **
A message describing the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when the requested resource cannot be found or does not exist.
 ** Message **
A message describing the resource not found error.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Thrown when the request would exceed the service quotas or limits for the account.
 ** Message **
A message describing the service quota exceeded error.
 ** QuotaCode **
The code identifying the specific quota that would be exceeded.
 ** ResourceId **
The identifier of the resource that would exceed the quota.
 ** ResourceType **
The type of the resource that would exceed the quota.
HTTP Status Code: 400

 ** ThrottlingException **
Thrown when the request rate exceeds the allowed limits and the request is being throttled.
 ** Message **
A message describing the throttling error.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the request contains invalid parameters or fails input validation requirements.
 ** FieldList **
A list of fields that failed validation.
 ** Message **
A message describing the validation error.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_benefits_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/UntagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
