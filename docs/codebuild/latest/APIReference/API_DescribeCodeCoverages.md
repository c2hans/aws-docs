---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeCodeCoverages.html
---

# DescribeCodeCoverages
<a name="API_DescribeCodeCoverages"></a>

Retrieves one or more code coverage reports.

## Request Syntax
<a name="API_DescribeCodeCoverages_RequestSyntax"></a>

```
{
   "maxLineCoveragePercentage": {{number}},
   "maxResults": {{number}},
   "minLineCoveragePercentage": {{number}},
   "nextToken": "{{string}}",
   "reportArn": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCodeCoverages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [reportArn](#API_DescribeCodeCoverages_RequestSyntax) **   <a name="CodeBuild-DescribeCodeCoverages-request-reportArn"></a>
 The ARN of the report for which test cases are returned.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [maxLineCoveragePercentage](#API_DescribeCodeCoverages_RequestSyntax) **   <a name="CodeBuild-DescribeCodeCoverages-request-maxLineCoveragePercentage"></a>
The maximum line coverage percentage to report.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [maxResults](#API_DescribeCodeCoverages_RequestSyntax) **   <a name="CodeBuild-DescribeCodeCoverages-request-maxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [minLineCoveragePercentage](#API_DescribeCodeCoverages_RequestSyntax) **   <a name="CodeBuild-DescribeCodeCoverages-request-minLineCoveragePercentage"></a>
The minimum line coverage percentage to report.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeCodeCoverages_RequestSyntax) **   <a name="CodeBuild-DescribeCodeCoverages-request-nextToken"></a>
The `nextToken` value returned from a previous call to `DescribeCodeCoverages`. This specifies the next item to return. To return the beginning of the list, exclude this parameter.
Type: String
Required: No

 ** [sortBy](#API_DescribeCodeCoverages_RequestSyntax) **   <a name="CodeBuild-DescribeCodeCoverages-request-sortBy"></a>
Specifies how the results are sorted. Possible values are:
FILE\_PATH
The results are sorted by file path.
LINE\_COVERAGE\_PERCENTAGE
The results are sorted by the percentage of lines that are covered.
Type: String
Valid Values: `LINE_COVERAGE_PERCENTAGE | FILE_PATH`
Required: No

 ** [sortOrder](#API_DescribeCodeCoverages_RequestSyntax) **   <a name="CodeBuild-DescribeCodeCoverages-request-sortOrder"></a>
Specifies if the results are sorted in ascending or descending order.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_DescribeCodeCoverages_ResponseSyntax"></a>

```
{
   "codeCoverages": [
      {
         "branchCoveragePercentage": number,
         "branchesCovered": number,
         "branchesMissed": number,
         "expired": number,
         "filePath": "string",
         "id": "string",
         "lineCoveragePercentage": number,
         "linesCovered": number,
         "linesMissed": number,
         "reportARN": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeCodeCoverages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeCoverages](#API_DescribeCodeCoverages_ResponseSyntax) **   <a name="CodeBuild-DescribeCodeCoverages-response-codeCoverages"></a>
An array of `CodeCoverage` objects that contain the results.
Type: Array of [CodeCoverage](API_CodeCoverage.md) objects

 ** [nextToken](#API_DescribeCodeCoverages_ResponseSyntax) **   <a name="CodeBuild-DescribeCodeCoverages-response-nextToken"></a>
If there are more items to return, this contains a token that is passed to a subsequent call to `DescribeCodeCoverages` to retrieve the next set of items.
Type: String

## Errors
<a name="API_DescribeCodeCoverages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeCodeCoverages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/DescribeCodeCoverages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/DescribeCodeCoverages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/DescribeCodeCoverages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/DescribeCodeCoverages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/DescribeCodeCoverages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/DescribeCodeCoverages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/DescribeCodeCoverages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/DescribeCodeCoverages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/DescribeCodeCoverages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/DescribeCodeCoverages)
