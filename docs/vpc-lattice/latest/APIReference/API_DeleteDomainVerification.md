---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DeleteDomainVerification.html
---

# DeleteDomainVerification
<a name="API_DeleteDomainVerification"></a>

 Deletes the specified domain verification.

## Request Syntax
<a name="API_DeleteDomainVerification_RequestSyntax"></a>

```
DELETE /domainverifications/{{domainVerificationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDomainVerification_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainVerificationIdentifier](#API_DeleteDomainVerification_RequestSyntax) **   <a name="vpclattice-DeleteDomainVerification-request-uri-domainVerificationIdentifier"></a>
 The ID of the domain verification to delete.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `((dv-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:domainverification/dv-[a-fA-F0-9]{17}))`
Required: Yes

## Request Body
<a name="API_DeleteDomainVerification_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDomainVerification_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteDomainVerification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDomainVerification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** resourceId **
The resource ID.
 ** resourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying.
 ** serviceCode **
The service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
 ** fieldList **
The fields that failed validation.
 ** reason **
The reason.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDomainVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/vpc-lattice-2022-11-30/DeleteDomainVerification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/vpc-lattice-2022-11-30/DeleteDomainVerification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/DeleteDomainVerification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/vpc-lattice-2022-11-30/DeleteDomainVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/DeleteDomainVerification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/vpc-lattice-2022-11-30/DeleteDomainVerification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/vpc-lattice-2022-11-30/DeleteDomainVerification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/vpc-lattice-2022-11-30/DeleteDomainVerification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/vpc-lattice-2022-11-30/DeleteDomainVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/DeleteDomainVerification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
