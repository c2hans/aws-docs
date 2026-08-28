---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateDomain.html
---

# CreateDomain
<a name="API_CreateDomain"></a>

 Creates a domain. CodeArtifact *domains* make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different AWS accounts. An asset is stored only once in a domain, even if it's in multiple repositories.

Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second pre-production domain to test changes to the production domain configuration.

## Request Syntax
<a name="API_CreateDomain_RequestSyntax"></a>

```
POST /v1/domain?domain={{domain}} HTTP/1.1
Content-type: application/json

{
   "encryptionKey": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domain](#API_CreateDomain_RequestSyntax) **   <a name="codeartifact-CreateDomain-request-uri-domain"></a>
 The name of the domain to create. All domain names in an AWS Region that are in the same AWS account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: Yes

## Request Body
<a name="API_CreateDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [encryptionKey](#API_CreateDomain_RequestSyntax) **   <a name="codeartifact-CreateDomain-request-encryptionKey"></a>
 The encryption key for the domain. This is used to encrypt content stored in a domain. An encryption key can be a key ID, a key Amazon Resource Name (ARN), a key alias, or a key alias ARN. To specify an `encryptionKey`, your IAM role must have `kms:DescribeKey` and `kms:CreateGrant` permissions on the encryption key that is used. For more information, see [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestSyntax) in the * AWS Key Management Service API Reference* and [AWS Key Management Service API Permissions Reference](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) in the * AWS Key Management Service Developer Guide*.
 CodeArtifact supports only symmetric CMKs. Do not associate an asymmetric CMK with your domain. For more information, see [Using symmetric and asymmetric keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** [tags](#API_CreateDomain_RequestSyntax) **   <a name="codeartifact-CreateDomain-request-tags"></a>
One or more tag key-value pairs for the domain.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domain": {
      "arn": "string",
      "assetSizeBytes": number,
      "createdTime": number,
      "encryptionKey": "string",
      "name": "string",
      "owner": "string",
      "repositoryCount": number,
      "s3BucketArn": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_CreateDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domain](#API_CreateDomain_ResponseSyntax) **   <a name="codeartifact-CreateDomain-response-domain"></a>
 Contains information about the created domain after processing the request.
Type: [DomainDescription](API_DomainDescription.md) object

## Errors
<a name="API_CreateDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The operation did not succeed because of an unauthorized access attempt.
HTTP Status Code: 403

 ** ConflictException **
 The operation did not succeed because prerequisites are not met.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 409

 ** InternalServerException **
 The operation did not succeed because of an error that occurred inside AWS CodeArtifact.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The operation did not succeed because the resource requested is not found in the service.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
 The operation did not succeed because it would have exceeded a service limit for your account.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
HTTP Status Code: 402

 ** ThrottlingException **
 The operation did not succeed because too many requests are sent to the service.
 ** retryAfterSeconds **
 The time period, in seconds, to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
 The operation did not succeed because a parameter in the request was sent with an invalid value.
 ** reason **

HTTP Status Code: 400

## See Also
<a name="API_CreateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/CreateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/CreateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/CreateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/CreateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/CreateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/CreateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/CreateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/CreateDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/CreateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/CreateDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
