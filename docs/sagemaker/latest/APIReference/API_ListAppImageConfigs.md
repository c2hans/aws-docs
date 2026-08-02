---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAppImageConfigs.html
---

# ListAppImageConfigs
<a name="API_ListAppImageConfigs"></a>

Lists the AppImageConfigs in your account and their properties. The list can be filtered by creation time or modified time, and whether the AppImageConfig name contains a specified string.

## Request Syntax
<a name="API_ListAppImageConfigs_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "ModifiedTimeAfter": {{number}},
   "ModifiedTimeBefore": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAppImageConfigs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListAppImageConfigs_RequestSyntax) **   <a name="sagemaker-ListAppImageConfigs-request-CreationTimeAfter"></a>
A filter that returns only AppImageConfigs created on or after the specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListAppImageConfigs_RequestSyntax) **   <a name="sagemaker-ListAppImageConfigs-request-CreationTimeBefore"></a>
A filter that returns only AppImageConfigs created on or before the specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListAppImageConfigs_RequestSyntax) **   <a name="sagemaker-ListAppImageConfigs-request-MaxResults"></a>
The total number of items to return in the response. If the total number of items available is more than the value specified, a `NextToken` is provided in the response. To resume pagination, provide the `NextToken` value in the as part of a subsequent call. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [ModifiedTimeAfter](#API_ListAppImageConfigs_RequestSyntax) **   <a name="sagemaker-ListAppImageConfigs-request-ModifiedTimeAfter"></a>
A filter that returns only AppImageConfigs modified on or after the specified time.
Type: Timestamp
Required: No

 ** [ModifiedTimeBefore](#API_ListAppImageConfigs_RequestSyntax) **   <a name="sagemaker-ListAppImageConfigs-request-ModifiedTimeBefore"></a>
A filter that returns only AppImageConfigs modified on or before the specified time.
Type: Timestamp
Required: No

 ** [NameContains](#API_ListAppImageConfigs_RequestSyntax) **   <a name="sagemaker-ListAppImageConfigs-request-NameContains"></a>
A filter that returns only AppImageConfigs whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [NextToken](#API_ListAppImageConfigs_RequestSyntax) **   <a name="sagemaker-ListAppImageConfigs-request-NextToken"></a>
If the previous call to `ListImages` didn't return the full set of AppImageConfigs, the call returns a token for getting the next set of AppImageConfigs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListAppImageConfigs_RequestSyntax) **   <a name="sagemaker-ListAppImageConfigs-request-SortBy"></a>
The property used to sort results. The default value is `CreationTime`.
Type: String
Valid Values: `CreationTime | LastModifiedTime | Name`
Required: No

 ** [SortOrder](#API_ListAppImageConfigs_RequestSyntax) **   <a name="sagemaker-ListAppImageConfigs-request-SortOrder"></a>
The sort order. The default value is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListAppImageConfigs_ResponseSyntax"></a>

```
{
   "AppImageConfigs": [
      {
         "AppImageConfigArn": "string",
         "AppImageConfigName": "string",
         "CodeEditorAppImageConfig": {
            "ContainerConfig": {
               "ContainerArguments": [ "string" ],
               "ContainerEntrypoint": [ "string" ],
               "ContainerEnvironmentVariables": {
                  "string" : "string"
               }
            },
            "FileSystemConfig": {
               "DefaultGid": number,
               "DefaultUid": number,
               "MountPath": "string"
            }
         },
         "CreationTime": number,
         "JupyterLabAppImageConfig": {
            "ContainerConfig": {
               "ContainerArguments": [ "string" ],
               "ContainerEntrypoint": [ "string" ],
               "ContainerEnvironmentVariables": {
                  "string" : "string"
               }
            },
            "FileSystemConfig": {
               "DefaultGid": number,
               "DefaultUid": number,
               "MountPath": "string"
            }
         },
         "KernelGatewayImageConfig": {
            "FileSystemConfig": {
               "DefaultGid": number,
               "DefaultUid": number,
               "MountPath": "string"
            },
            "KernelSpecs": [
               {
                  "DisplayName": "string",
                  "Name": "string"
               }
            ]
         },
         "LastModifiedTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAppImageConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppImageConfigs](#API_ListAppImageConfigs_ResponseSyntax) **   <a name="sagemaker-ListAppImageConfigs-response-AppImageConfigs"></a>
A list of AppImageConfigs and their properties.
Type: Array of [AppImageConfigDetails](API_AppImageConfigDetails.md) objects

 ** [NextToken](#API_ListAppImageConfigs_ResponseSyntax) **   <a name="sagemaker-ListAppImageConfigs-response-NextToken"></a>
A token for getting the next set of AppImageConfigs, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListAppImageConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListAppImageConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListAppImageConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListAppImageConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListAppImageConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListAppImageConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListAppImageConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListAppImageConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListAppImageConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListAppImageConfigs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListAppImageConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListAppImageConfigs)
