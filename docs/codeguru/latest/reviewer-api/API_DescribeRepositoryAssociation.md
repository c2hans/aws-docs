---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeRepositoryAssociation.html
---

# DescribeRepositoryAssociation
<a name="API_DescribeRepositoryAssociation"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Returns a [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) object that contains information about the requested repository association.

## Request Syntax
<a name="API_DescribeRepositoryAssociation_RequestSyntax"></a>

```
GET /associations/{{AssociationArn}}?showDeletedRepository={{ShowDeletedRepository}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeRepositoryAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociationArn](#API_DescribeRepositoryAssociation_RequestSyntax) **   <a name="reviewer-DescribeRepositoryAssociation-request-uri-AssociationArn"></a>
The Amazon Resource Name (ARN) of the [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) object. You can retrieve this ARN by calling [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html).
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:association:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [ShowDeletedRepository](#API_DescribeRepositoryAssociation_RequestSyntax) **   <a name="reviewer-DescribeRepositoryAssociation-request-uri-ShowDeletedRepository"></a>
Specifies whether to include information about deleted repositories in the response.

## Request Body
<a name="API_DescribeRepositoryAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeRepositoryAssociation_ResponseSyntax"></a>

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
<a name="API_DescribeRepositoryAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RepositoryAssociation](#API_DescribeRepositoryAssociation_ResponseSyntax) **   <a name="reviewer-DescribeRepositoryAssociation-response-RepositoryAssociation"></a>
Information about the repository association.
Type: [RepositoryAssociation](API_RepositoryAssociation.md) object

 ** [Tags](#API_DescribeRepositoryAssociation_ResponseSyntax) **   <a name="reviewer-DescribeRepositoryAssociation-response-Tags"></a>
An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:
+ A *tag key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag keys are case sensitive.
+ An optional field known as a *tag value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_DescribeRepositoryAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
The resource specified in the request was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRepositoryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)
