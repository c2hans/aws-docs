---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReviewInternal.html
---

# CreateCodeReviewInternal
<a name="API_CreateCodeReviewInternal"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Creates an internal code review for CodeGuru Reviewer analysis.

## Request Syntax
<a name="API_CreateCodeReviewInternal_RequestSyntax"></a>

```
POST /createCodeReviewInternal HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Name": "{{string}}",
   "RepositoryAssociationArn": "{{string}}",
   "Type": {
      "AnalysisTypes": [ "{{string}}" ],
      "RepositoryAnalysis": {
         "RepositoryHead": {
            "BranchName": "{{string}}"
         },
         "S3BucketRepository": {
            "Details": {
               "BucketName": "{{string}}",
               "CodeArtifacts": {
                  "BuildArtifactsObjectKey": "{{string}}",
                  "SourceCodeArtifactsObjectKey": "{{string}}"
               }
            },
            "Name": "{{string}}"
         },
         "SourceCodeType": {
            "BranchDiff": {
               "DestinationBranchName": "{{string}}",
               "SourceBranchName": "{{string}}"
            },
            "CommitDiff": {
               "DestinationCommit": "{{string}}",
               "MergeBaseCommit": "{{string}}",
               "SourceCommit": "{{string}}"
            },
            "RepositoryHead": {
               "BranchName": "{{string}}"
            },
            "RequestMetadata": {
               "EventInfo": {
                  "Name": "{{string}}",
                  "State": "{{string}}"
               },
               "Requester": "{{string}}",
               "RequestId": "{{string}}",
               "VendorName": "{{string}}"
            },
            "S3BucketRepository": {
               "Details": {
                  "BucketName": "{{string}}",
                  "CodeArtifacts": {
                     "BuildArtifactsObjectKey": "{{string}}",
                     "SourceCodeArtifactsObjectKey": "{{string}}"
                  }
               },
               "Name": "{{string}}"
            }
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateCodeReviewInternal_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCodeReviewInternal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateCodeReviewInternal_RequestSyntax) **   <a name="reviewer-CreateCodeReviewInternal-request-ClientRequestToken"></a>
Amazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate code reviews if there are failures and retries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\w-]+$`
Required: No

 ** [Name](#API_CreateCodeReviewInternal_RequestSyntax) **   <a name="reviewer-CreateCodeReviewInternal-request-Name"></a>
The name of the code review. The name of each code review in your AWS account must be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[a-zA-Z0-9-_]*`
Required: Yes

 ** [RepositoryAssociationArn](#API_CreateCodeReviewInternal_RequestSyntax) **   <a name="reviewer-CreateCodeReviewInternal-request-RepositoryAssociationArn"></a>
The Amazon Resource Name (ARN) of the [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) object. You can retrieve this ARN by calling [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html).
A code review can only be created on an associated repository. This is the ARN of the associated repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:association:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [Type](#API_CreateCodeReviewInternal_RequestSyntax) **   <a name="reviewer-CreateCodeReviewInternal-request-Type"></a>
The type of code review to create. This is specified using a [CodeReviewType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html) object. You can create a code review only of type `RepositoryAnalysis`.
Type: [CodeReviewType](API_CodeReviewType.md) object
Required: Yes

## Response Syntax
<a name="API_CreateCodeReviewInternal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CodeReview": {
      "AnalysisTypes": [ "string" ],
      "AssociationArn": "string",
      "CodeReviewArn": "string",
      "ConfigFileState": "string",
      "CreatedTimeStamp": number,
      "LastUpdatedTimeStamp": number,
      "Metrics": {
         "FindingsCount": number,
         "MeteredLinesOfCodeCount": number,
         "SuppressedLinesOfCodeCount": number
      },
      "Name": "string",
      "Owner": "string",
      "ProviderType": "string",
      "PullRequestId": "string",
      "RepositoryName": "string",
      "SourceCodeType": {
         "BranchDiff": {
            "DestinationBranchName": "string",
            "SourceBranchName": "string"
         },
         "CommitDiff": {
            "DestinationCommit": "string",
            "MergeBaseCommit": "string",
            "SourceCommit": "string"
         },
         "RepositoryHead": {
            "BranchName": "string"
         },
         "RequestMetadata": {
            "EventInfo": {
               "Name": "string",
               "State": "string"
            },
            "Requester": "string",
            "RequestId": "string",
            "VendorName": "string"
         },
         "S3BucketRepository": {
            "Details": {
               "BucketName": "string",
               "CodeArtifacts": {
                  "BuildArtifactsObjectKey": "string",
                  "SourceCodeArtifactsObjectKey": "string"
               }
            },
            "Name": "string"
         }
      },
      "State": "string",
      "StateReason": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_CreateCodeReviewInternal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CodeReview](#API_CreateCodeReviewInternal_ResponseSyntax) **   <a name="reviewer-CreateCodeReviewInternal-response-CodeReview"></a>
Information about a code review. A code review belongs to the associated repository that contains the reviewed code.
Type: [CodeReview](API_CodeReview.md) object

## Errors
<a name="API_CreateCodeReviewInternal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_CreateCodeReviewInternal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/CreateCodeReviewInternal)
