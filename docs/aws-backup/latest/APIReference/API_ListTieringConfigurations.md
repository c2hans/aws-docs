---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListTieringConfigurations.html
---

# ListTieringConfigurations
<a name="API_ListTieringConfigurations"></a>

Returns a list of tiering configurations.

## Request Syntax
<a name="API_ListTieringConfigurations_RequestSyntax"></a>

```
GET /tiering-configurations/?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTieringConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListTieringConfigurations_RequestSyntax) **   <a name="Backup-ListTieringConfigurations-request-uri-MaxResults"></a>
The maximum number of items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListTieringConfigurations_RequestSyntax) **   <a name="Backup-ListTieringConfigurations-request-uri-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

## Request Body
<a name="API_ListTieringConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTieringConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TieringConfigurations": [
      {
         "BackupVaultName": "string",
         "CreationTime": number,
         "LastUpdatedTime": number,
         "TieringConfigurationArn": "string",
         "TieringConfigurationName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTieringConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTieringConfigurations_ResponseSyntax) **   <a name="Backup-ListTieringConfigurations-response-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

 ** [TieringConfigurations](#API_ListTieringConfigurations_ResponseSyntax) **   <a name="Backup-ListTieringConfigurations-response-TieringConfigurations"></a>
An array of tiering configurations returned by the `ListTieringConfigurations` call.
Type: Array of [TieringConfigurationsListMember](API_TieringConfigurationsListMember.md) objects

## Errors
<a name="API_ListTieringConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_ListTieringConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListTieringConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListTieringConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListTieringConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListTieringConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListTieringConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListTieringConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListTieringConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListTieringConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListTieringConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListTieringConfigurations)
