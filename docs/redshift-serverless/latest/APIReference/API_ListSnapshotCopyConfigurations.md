---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListSnapshotCopyConfigurations.html
---

# ListSnapshotCopyConfigurations
<a name="API_ListSnapshotCopyConfigurations"></a>

Returns a list of snapshot copy configurations.

## Request Syntax
<a name="API_ListSnapshotCopyConfigurations_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "namespaceName": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSnapshotCopyConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListSnapshotCopyConfigurations_RequestSyntax) **   <a name="redshiftserverless-ListSnapshotCopyConfigurations-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to display the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [namespaceName](#API_ListSnapshotCopyConfigurations_RequestSyntax) **   <a name="redshiftserverless-ListSnapshotCopyConfigurations-request-namespaceName"></a>
The namespace from which to list all snapshot copy configurations.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

 ** [nextToken](#API_ListSnapshotCopyConfigurations_RequestSyntax) **   <a name="redshiftserverless-ListSnapshotCopyConfigurations-request-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListSnapshotCopyConfigurations_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "snapshotCopyConfigurations": [
      {
         "destinationKmsKeyId": "string",
         "destinationRegion": "string",
         "namespaceName": "string",
         "snapshotCopyConfigurationArn": "string",
         "snapshotCopyConfigurationId": "string",
         "snapshotRetentionPeriod": number
      }
   ]
}
```

## Response Elements
<a name="API_ListSnapshotCopyConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSnapshotCopyConfigurations_ResponseSyntax) **   <a name="redshiftserverless-ListSnapshotCopyConfigurations-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [snapshotCopyConfigurations](#API_ListSnapshotCopyConfigurations_ResponseSyntax) **   <a name="redshiftserverless-ListSnapshotCopyConfigurations-response-snapshotCopyConfigurations"></a>
All of the returned snapshot copy configurations.
Type: Array of [SnapshotCopyConfiguration](API_SnapshotCopyConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_ListSnapshotCopyConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** InvalidPaginationException **
The provided pagination token is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListSnapshotCopyConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListSnapshotCopyConfigurations)
