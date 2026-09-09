---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAssociations.html
---

# ListAssociations
<a name="API_ListAssociations"></a>

Lists the associations in your account and their properties.

## Request Syntax
<a name="API_ListAssociations_RequestSyntax"></a>

```
{
   "AssociationType": "{{string}}",
   "DestinationArn": "{{string}}",
   "DestinationType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "SourceArn": "{{string}}",
   "SourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationType](#API_ListAssociations_RequestSyntax) **   <a name="sagemaker-ListAssociations-request-AssociationType"></a>
A filter that returns only associations of the specified type.
Type: String
Valid Values: `ContributedTo | AssociatedWith | DerivedFrom | Produced | SameAs`
Required: No

 ** [DestinationArn](#API_ListAssociations_RequestSyntax) **   <a name="sagemaker-ListAssociations-request-DestinationArn"></a>
A filter that returns only associations with the specified destination Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: No

 ** [DestinationType](#API_ListAssociations_RequestSyntax) **   <a name="sagemaker-ListAssociations-request-DestinationType"></a>
A filter that returns only associations with the specified destination type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [MaxResults](#API_ListAssociations_RequestSyntax) **   <a name="sagemaker-ListAssociations-request-MaxResults"></a>
The maximum number of associations to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAssociations_RequestSyntax) **   <a name="sagemaker-ListAssociations-request-NextToken"></a>
If the previous call to `ListAssociations` didn't return the full set of associations, the call returns a token for getting the next set of associations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListAssociations_RequestSyntax) **   <a name="sagemaker-ListAssociations-request-SortBy"></a>
The property used to sort results. The default value is `CreationTime`.
Type: String
Valid Values: `SourceArn | DestinationArn | SourceType | DestinationType | CreationTime`
Required: No

 ** [SortOrder](#API_ListAssociations_RequestSyntax) **   <a name="sagemaker-ListAssociations-request-SortOrder"></a>
The sort order. The default value is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [SourceArn](#API_ListAssociations_RequestSyntax) **   <a name="sagemaker-ListAssociations-request-SourceArn"></a>
A filter that returns only associations with the specified source ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: No

 ** [SourceType](#API_ListAssociations_RequestSyntax) **   <a name="sagemaker-ListAssociations-request-SourceType"></a>
A filter that returns only associations with the specified source type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_ListAssociations_ResponseSyntax"></a>

```
{
   "AssociationSummaries": [
      {
         "AssociationType": "string",
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
         "DestinationArn": "string",
         "DestinationName": "string",
         "DestinationType": "string",
         "SourceArn": "string",
         "SourceName": "string",
         "SourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationSummaries](#API_ListAssociations_ResponseSyntax) **   <a name="sagemaker-ListAssociations-response-AssociationSummaries"></a>
A list of associations and their properties.
Type: Array of [AssociationSummary](API_AssociationSummary.md) objects

 ** [NextToken](#API_ListAssociations_ResponseSyntax) **   <a name="sagemaker-ListAssociations-response-NextToken"></a>
A token for getting the next set of associations, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListAssociations)
