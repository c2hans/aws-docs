---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListAttachedFilesConfigurations.html
---

# ListAttachedFilesConfigurations
<a name="API_ListAttachedFilesConfigurations"></a>

Provides summary information about the attached files configurations for the specified Connect Customer instance.

This API returns effective configurations (custom overrides or defaults) for each attachment scope. If no custom configuration exists for a scope, the default configuration values are returned.

## Request Syntax
<a name="API_ListAttachedFilesConfigurations_RequestSyntax"></a>

```
GET /attached-files-configurations/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAttachedFilesConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListAttachedFilesConfigurations_RequestSyntax) **   <a name="connect-ListAttachedFilesConfigurations-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListAttachedFilesConfigurations_RequestSyntax) **   <a name="connect-ListAttachedFilesConfigurations-request-uri-MaxResults"></a>
The maximum number of results to return per page. The default MaxResult size is 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListAttachedFilesConfigurations_RequestSyntax) **   <a name="connect-ListAttachedFilesConfigurations-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListAttachedFilesConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAttachedFilesConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttachedFilesConfigurations": [
      {
         "AttachmentScope": "string",
         "ExtensionConfiguration": {
            "AllowedExtensions": [
               {
                  "Extension": "string"
               }
            ]
         },
         "InstanceId": "string",
         "MaximumSizeLimitInBytes": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAttachedFilesConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachedFilesConfigurations](#API_ListAttachedFilesConfigurations_ResponseSyntax) **   <a name="connect-ListAttachedFilesConfigurations-response-AttachedFilesConfigurations"></a>
Information about the attached files configurations.
Type: Array of [AttachedFilesConfigurationSummary](API_AttachedFilesConfigurationSummary.md) objects

 ** [NextToken](#API_ListAttachedFilesConfigurations_ResponseSyntax) **   <a name="connect-ListAttachedFilesConfigurations-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListAttachedFilesConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListAttachedFilesConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListAttachedFilesConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListAttachedFilesConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListAttachedFilesConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListAttachedFilesConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListAttachedFilesConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListAttachedFilesConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListAttachedFilesConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListAttachedFilesConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListAttachedFilesConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListAttachedFilesConfigurations)
