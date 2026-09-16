---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListManagedWorkgroups.html
---

# ListManagedWorkgroups
<a name="API_ListManagedWorkgroups"></a>

Returns information about a list of specified managed workgroups in your account.

## Request Syntax
<a name="API_ListManagedWorkgroups_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListManagedWorkgroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListManagedWorkgroups_RequestSyntax) **   <a name="redshiftserverless-ListManagedWorkgroups-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListManagedWorkgroups_RequestSyntax) **   <a name="redshiftserverless-ListManagedWorkgroups-request-nextToken"></a>
If your initial ListManagedWorkgroups operation returns a nextToken, you can include the returned nextToken in following ListManagedWorkgroups operations, which returns results in the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: No

 ** [sourceArn](#API_ListManagedWorkgroups_RequestSyntax) **   <a name="redshiftserverless-ListManagedWorkgroups-request-sourceArn"></a>
The Amazon Resource Name (ARN) for the managed workgroup in the AWS Glue Data Catalog.
Type: String
Pattern: `arn:aws[a-z-]*:glue:[a-z0-9-]+:\d+:(database|catalog)[a-z0-9-:]*(?:/[A-Za-z0-9-_]{1,255})*`
Required: No

## Response Syntax
<a name="API_ListManagedWorkgroups_ResponseSyntax"></a>

```
{
   "managedWorkgroups": [
      {
         "creationDate": "string",
         "managedWorkgroupId": "string",
         "managedWorkgroupName": "string",
         "sourceArn": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedWorkgroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [managedWorkgroups](#API_ListManagedWorkgroups_ResponseSyntax) **   <a name="redshiftserverless-ListManagedWorkgroups-response-managedWorkgroups"></a>
The returned array of managed workgroups.
Type: Array of [ManagedWorkgroupListItem](API_ManagedWorkgroupListItem.md) objects

 ** [nextToken](#API_ListManagedWorkgroups_ResponseSyntax) **   <a name="redshiftserverless-ListManagedWorkgroups-response-nextToken"></a>
If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

## Errors
<a name="API_ListManagedWorkgroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## See Also
<a name="API_ListManagedWorkgroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListManagedWorkgroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListManagedWorkgroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListManagedWorkgroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListManagedWorkgroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListManagedWorkgroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListManagedWorkgroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListManagedWorkgroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListManagedWorkgroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListManagedWorkgroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListManagedWorkgroups)
