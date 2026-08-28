---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelPackages.html
---

# ListModelPackages
<a name="API_ListModelPackages"></a>

Lists the model packages that have been created.

## Request Syntax
<a name="API_ListModelPackages_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "ModelApprovalStatus": "{{string}}",
   "ModelPackageGroupName": "{{string}}",
   "ModelPackageType": "{{string}}",
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListModelPackages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-CreationTimeAfter"></a>
A filter that returns only model packages created after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-CreationTimeBefore"></a>
A filter that returns only model packages created before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-MaxResults"></a>
The maximum number of model packages to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [ModelApprovalStatus](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-ModelApprovalStatus"></a>
A filter that returns only the model packages with the specified approval status.
Type: String
Valid Values: `Approved | Rejected | PendingManualApproval`
Required: No

 ** [ModelPackageGroupName](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-ModelPackageGroupName"></a>
A filter that returns only model versions that belong to the specified model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*\/)?([a-zA-Z0-9]([a-zA-Z0-9-]){0,62})(?<!-)`
Required: No

 ** [ModelPackageType](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-ModelPackageType"></a>
A filter that returns only the model packages of the specified type. This can be one of the following values.
+  `UNVERSIONED` - List only unversioined models. This is the default value if no `ModelPackageType` is specified.
+  `VERSIONED` - List only versioned models.
+  `BOTH` - List both versioned and unversioned models.
Type: String
Valid Values: `Versioned | Unversioned | Both`
Required: No

 ** [NameContains](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-NameContains"></a>
A string in the model package name. This filter returns only model packages whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-NextToken"></a>
If the response to a previous `ListModelPackages` request was truncated, the response includes a `NextToken`. To retrieve the next set of model packages, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-SortBy"></a>
The parameter by which to sort the results. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListModelPackages_RequestSyntax) **   <a name="sagemaker-ListModelPackages-request-SortOrder"></a>
The sort order for the results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListModelPackages_ResponseSyntax"></a>

```
{
   "ModelPackageSummaryList": [
      {
         "CreationTime": number,
         "ModelApprovalStatus": "string",
         "ModelLifeCycle": {
            "Stage": "string",
            "StageDescription": "string",
            "StageStatus": "string"
         },
         "ModelPackageArn": "string",
         "ModelPackageDescription": "string",
         "ModelPackageGroupName": "string",
         "ModelPackageName": "string",
         "ModelPackageRegistrationType": "string",
         "ModelPackageStatus": "string",
         "ModelPackageVersion": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListModelPackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelPackageSummaryList](#API_ListModelPackages_ResponseSyntax) **   <a name="sagemaker-ListModelPackages-response-ModelPackageSummaryList"></a>
An array of `ModelPackageSummary` objects, each of which lists a model package.
Type: Array of [ModelPackageSummary](API_ModelPackageSummary.md) objects

 ** [NextToken](#API_ListModelPackages_ResponseSyntax) **   <a name="sagemaker-ListModelPackages-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of model packages, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListModelPackages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListModelPackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListModelPackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListModelPackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListModelPackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListModelPackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListModelPackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListModelPackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListModelPackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListModelPackages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListModelPackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListModelPackages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
