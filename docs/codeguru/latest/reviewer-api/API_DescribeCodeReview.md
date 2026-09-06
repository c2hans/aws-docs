---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeCodeReview.html
---

# DescribeCodeReview
<a name="API_DescribeCodeReview"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Returns the metadata associated with the code review along with its status.

## Request Syntax
<a name="API_DescribeCodeReview_RequestSyntax"></a>

```
GET /codereviews/{{CodeReviewArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeCodeReview_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CodeReviewArn](#API_DescribeCodeReview_RequestSyntax) **   <a name="reviewer-DescribeCodeReview-request-uri-CodeReviewArn"></a>
The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:([a-z-]+|[a-z-]+:[\w-]+:[a-z-]+):[\w-]+$`
Required: Yes

## Request Body
<a name="API_DescribeCodeReview_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeCodeReview_ResponseSyntax"></a>

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
<a name="API_DescribeCodeReview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CodeReview](#API_DescribeCodeReview_ResponseSyntax) **   <a name="reviewer-DescribeCodeReview-response-CodeReview"></a>
Information about the code review.
Type: [CodeReview](API_CodeReview.md) object

## Errors
<a name="API_DescribeCodeReview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_DescribeCodeReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/DescribeCodeReview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/DescribeCodeReview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/DescribeCodeReview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/DescribeCodeReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/DescribeCodeReview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/DescribeCodeReview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/DescribeCodeReview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/DescribeCodeReview)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/DescribeCodeReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/DescribeCodeReview)
