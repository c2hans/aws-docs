---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrialComponents.html
---

# ListTrialComponents
<a name="API_ListTrialComponents"></a>

Lists the trial components in your account. You can sort the list by trial component name or creation time. You can filter the list to show only components that were created in a specific time range. You can also filter on one of the following:
+  `ExperimentName`
+  `SourceArn`
+  `TrialName`

## Request Syntax
<a name="API_ListTrialComponents_RequestSyntax"></a>

```
{
   "ExperimentName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "SourceArn": "{{string}}",
   "TrialName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTrialComponents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExperimentName](#API_ListTrialComponents_RequestSyntax) **   <a name="sagemaker-ListTrialComponents-request-ExperimentName"></a>
A filter that returns only components that are part of the specified experiment. If you specify `ExperimentName`, you can't filter by `SourceArn` or `TrialName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** [MaxResults](#API_ListTrialComponents_RequestSyntax) **   <a name="sagemaker-ListTrialComponents-request-MaxResults"></a>
The maximum number of components to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListTrialComponents_RequestSyntax) **   <a name="sagemaker-ListTrialComponents-request-NextToken"></a>
If the previous call to `ListTrialComponents` didn't return the full set of components, the call returns a token for getting the next set of components.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListTrialComponents_RequestSyntax) **   <a name="sagemaker-ListTrialComponents-request-SortBy"></a>
The property used to sort results. The default value is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListTrialComponents_RequestSyntax) **   <a name="sagemaker-ListTrialComponents-request-SortOrder"></a>
The sort order. The default value is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [SourceArn](#API_ListTrialComponents_RequestSyntax) **   <a name="sagemaker-ListTrialComponents-request-SourceArn"></a>
A filter that returns only components that have the specified source Amazon Resource Name (ARN). If you specify `SourceArn`, you can't filter by `ExperimentName` or `TrialName`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [TrialName](#API_ListTrialComponents_RequestSyntax) **   <a name="sagemaker-ListTrialComponents-request-TrialName"></a>
A filter that returns only components that are part of the specified trial. If you specify `TrialName`, you can't filter by `ExperimentName` or `SourceArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

## Response Syntax
<a name="API_ListTrialComponents_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TrialComponentSummaries": [
      {
         "CreatedBy": {
            "DomainId": "string",
            "IamIdentity": {
               "Arn": "string",
               "PrincipalId": "string",
               "SourceIdentity": "string"
            },
            "UserProfileArn": "string",
            "UserProfileName": "string"
         },
         "DisplayName": "string",
         "LastModifiedBy": {
            "DomainId": "string",
            "IamIdentity": {
               "Arn": "string",
               "PrincipalId": "string",
               "SourceIdentity": "string"
            },
            "UserProfileArn": "string",
            "UserProfileName": "string"
         },
         "Status": {
            "Message": "string",
            "PrimaryStatus": "string"
         },
         "TrialComponentArn": "string",
         "TrialComponentName": "string",
         "TrialComponentSource": {
            "SourceArn": "string",
            "SourceType": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListTrialComponents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTrialComponents_ResponseSyntax) **   <a name="sagemaker-ListTrialComponents-response-NextToken"></a>
A token for getting the next set of components, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [TrialComponentSummaries](#API_ListTrialComponents_ResponseSyntax) **   <a name="sagemaker-ListTrialComponents-response-TrialComponentSummaries"></a>
A list of the summaries of your trial components.
Type: Array of [TrialComponentSummary](API_TrialComponentSummary.md) objects

## Errors
<a name="API_ListTrialComponents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListTrialComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListTrialComponents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListTrialComponents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListTrialComponents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListTrialComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListTrialComponents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListTrialComponents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListTrialComponents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListTrialComponents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListTrialComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListTrialComponents)
