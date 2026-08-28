---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListOpsMetadata.html
---

# ListOpsMetadata
<a name="API_ListOpsMetadata"></a>

 AWS Systems Manager calls this API operation when displaying all Application Manager OpsMetadata objects or blobs.

## Request Syntax
<a name="API_ListOpsMetadata_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListOpsMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListOpsMetadata_RequestSyntax) **   <a name="systemsmanager-ListOpsMetadata-request-Filters"></a>
One or more filters to limit the number of OpsMetadata objects returned by the call.
Type: Array of [OpsMetadataFilter](API_OpsMetadataFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [MaxResults](#API_ListOpsMetadata_RequestSyntax) **   <a name="systemsmanager-ListOpsMetadata-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListOpsMetadata_RequestSyntax) **   <a name="systemsmanager-ListOpsMetadata-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListOpsMetadata_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OpsMetadataList": [
      {
         "CreationDate": number,
         "LastModifiedDate": number,
         "LastModifiedUser": "string",
         "OpsMetadataArn": "string",
         "ResourceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOpsMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOpsMetadata_ResponseSyntax) **   <a name="systemsmanager-ListOpsMetadata-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

 ** [OpsMetadataList](#API_ListOpsMetadata_ResponseSyntax) **   <a name="systemsmanager-ListOpsMetadata-response-OpsMetadataList"></a>
Returns a list of OpsMetadata objects.
Type: Array of [OpsMetadata](API_OpsMetadata.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_ListOpsMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsMetadataInvalidArgumentException **
One of the arguments passed is invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListOpsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListOpsMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListOpsMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListOpsMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListOpsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListOpsMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListOpsMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListOpsMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListOpsMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListOpsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListOpsMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
