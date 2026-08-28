---
source_url: https://docs.aws.amazon.com/accounts/latest/APIReference/API_EnableRegion.html
---

# EnableRegion
<a name="API_EnableRegion"></a>

Enables (opts-in) a particular Region for an account.

## Request Syntax
<a name="API_EnableRegion_RequestSyntax"></a>

```
POST /enableRegion HTTP/1.1
Content-type: application/json

{
   "AccountId": "{{string}}",
   "RegionName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_EnableRegion_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_EnableRegion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_EnableRegion_RequestSyntax) **   <a name="accounts-EnableRegion-request-AccountId"></a>
Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.
The management account can't specify its own `AccountId`. It must call the operation in standalone context by not including the `AccountId` parameter.
To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.
Type: String
Pattern: `\d{12}`
Required: No

 ** [RegionName](#API_EnableRegion_RequestSyntax) **   <a name="accounts-EnableRegion-request-RegionName"></a>
Specifies the Region-code for a given Region name (for example, `af-south-1`). When you enable a Region, AWS performs actions to prepare your account in that Region, such as distributing your IAM resources to the Region. This process takes a few minutes for most accounts, but it can take several hours. You cannot use the Region until this process is complete. Furthermore, you cannot disable the Region until the enabling process is fully completed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

## Response Syntax
<a name="API_EnableRegion_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_EnableRegion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableRegion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The operation failed because the calling identity doesn't have the minimum required permissions.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of a conflict in the current status of the resource. For example, this happens if you try to enable a Region that is currently being disabled (in a status of DISABLING) or if you try to change an account’s root user email to an email address which is already in use.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 409

 ** InternalServerException **
The operation failed because of an error internal to AWS. Try your operation again later.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 500

 ** TooManyRequestsException **
The operation failed because it was called too frequently and exceeded a throttle limit.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 429

 ** ValidationException **
The operation failed because one of the input parameters was invalid.
 ** fieldList **
The field where the invalid entry was detected.
 ** message **
The message that informs you about what was invalid about the request.
 ** reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_EnableRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/EnableRegion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/EnableRegion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/EnableRegion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/EnableRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/EnableRegion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/EnableRegion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/EnableRegion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/EnableRegion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/EnableRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/EnableRegion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Account Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query accounts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
