---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_AssociateRepository.html
---

# AssociateRepository
<a name="API_AssociateRepository"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Use to associate an AWS CodeCommit repository or a repository managed by AWS CodeStar Connections with Amazon CodeGuru Reviewer. When you associate a repository, CodeGuru Reviewer reviews source code changes in the repository's pull requests and provides automatic recommendations. You can view recommendations using the CodeGuru Reviewer console. For more information, see [Recommendations in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/recommendations.html) in the *Amazon CodeGuru Reviewer User Guide.*

If you associate a CodeCommit or S3 repository, it must be in the same AWS Region and AWS account where its CodeGuru Reviewer code reviews are configured.

Bitbucket and GitHub Enterprise Server repositories are managed by AWS CodeStar Connections to connect to CodeGuru Reviewer. For more information, see [Associate a repository](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-associate-repository.html) in the *Amazon CodeGuru Reviewer User Guide.*

**Note**
You cannot use the CodeGuru Reviewer SDK or the AWS CLI to associate a GitHub repository with Amazon CodeGuru Reviewer. To associate a GitHub repository, use the console. For more information, see [Getting started with CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/getting-started-with-guru.html) in the *CodeGuru Reviewer User Guide.*

## Request Syntax
<a name="API_AssociateRepository_RequestSyntax"></a>

```
POST /associations HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "KMSKeyDetails": {
      "EncryptionOption": "{{string}}",
      "KMSKeyId": "{{string}}"
   },
   "Repository": {
      "Bitbucket": {
         "ConnectionArn": "{{string}}",
         "Name": "{{string}}",
         "Owner": "{{string}}"
      },
      "CodeCommit": {
         "Name": "{{string}}"
      },
      "GitHub": {
         "AccessToken": "{{string}}",
         "Name": "{{string}}",
         "Owner": "{{string}}"
      },
      "GitHubEnterpriseServer": {
         "ConnectionArn": "{{string}}",
         "Name": "{{string}}",
         "Owner": "{{string}}"
      },
      "S3Bucket": {
         "BucketName": "{{string}}",
         "Name": "{{string}}"
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_AssociateRepository_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateRepository_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_AssociateRepository_RequestSyntax) **   <a name="reviewer-AssociateRepository-request-ClientRequestToken"></a>
Amazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate repository associations if there are failures and retries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\w-]+$`
Required: No

 ** [KMSKeyDetails](#API_AssociateRepository_RequestSyntax) **   <a name="reviewer-AssociateRepository-request-KMSKeyDetails"></a>
A `KMSKeyDetails` object that contains:
+ The encryption option for this repository association. It is either owned by AWS Key Management Service (KMS) (`AWS_OWNED_CMK`) or customer managed (`CUSTOMER_MANAGED_CMK`).
+ The ID of the AWS KMS key that is associated with this repository association.
Type: [KMSKeyDetails](API_KMSKeyDetails.md) object
Required: No

 ** [Repository](#API_AssociateRepository_RequestSyntax) **   <a name="reviewer-AssociateRepository-request-Repository"></a>
The repository to associate.
Type: [Repository](API_Repository.md) object
Required: Yes

 ** [Tags](#API_AssociateRepository_RequestSyntax) **   <a name="reviewer-AssociateRepository-request-Tags"></a>
An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:
+ A *tag key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag keys are case sensitive.
+ An optional field known as a *tag value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_AssociateRepository_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RepositoryAssociation": {
      "AssociationArn": "string",
      "AssociationId": "string",
      "ConnectionArn": "string",
      "CreatedTimeStamp": number,
      "KMSKeyDetails": {
         "EncryptionOption": "string",
         "KMSKeyId": "string"
      },
      "LastUpdatedTimeStamp": number,
      "Name": "string",
      "Owner": "string",
      "ProviderType": "string",
      "S3RepositoryDetails": {
         "BucketName": "string",
         "CodeArtifacts": {
            "BuildArtifactsObjectKey": "string",
            "SourceCodeArtifactsObjectKey": "string"
         }
      },
      "State": "string",
      "StateReason": "string"
   },
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_AssociateRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RepositoryAssociation](#API_AssociateRepository_ResponseSyntax) **   <a name="reviewer-AssociateRepository-response-RepositoryAssociation"></a>
Information about the repository association.
Type: [RepositoryAssociation](API_RepositoryAssociation.md) object

 ** [Tags](#API_AssociateRepository_ResponseSyntax) **   <a name="reviewer-AssociateRepository-response-Tags"></a>
An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:
+ A *tag key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag keys are case sensitive.
+ An optional field known as a *tag value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_AssociateRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** FeatureNoLongerAvailableException **

HTTP Status Code: 410

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_AssociateRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/AssociateRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/AssociateRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/AssociateRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/AssociateRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/AssociateRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/AssociateRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/AssociateRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/AssociateRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/AssociateRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/AssociateRepository)
