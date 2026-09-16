---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListConfigurationManagers.html
---

# ListConfigurationManagers
<a name="API_ListConfigurationManagers"></a>

Returns Quick Setup configuration managers that were created using the `CreateConfigurationManager` API action.

## Request Syntax
<a name="API_ListConfigurationManagers_RequestSyntax"></a>

```
POST /listConfigurationManagers HTTP/1.1
Content-type: application/json

{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxItems": {{number}},
   "StartingToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConfigurationManagers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConfigurationManagers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListConfigurationManagers_RequestSyntax) **   <a name="quicksetup-ListConfigurationManagers-request-Filters"></a>
Filters the results returned by the request.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxItems](#API_ListConfigurationManagers_RequestSyntax) **   <a name="quicksetup-ListConfigurationManagers-request-MaxItems"></a>
Specifies the maximum number of configuration managers that are returned by the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [StartingToken](#API_ListConfigurationManagers_RequestSyntax) **   <a name="quicksetup-ListConfigurationManagers-request-StartingToken"></a>
The token to use when requesting a specific set of items from a list.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[A-Za-z0-9+=@_\/\s-]*`
Required: No

## Response Syntax
<a name="API_ListConfigurationManagers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationManagersList": [
      {
         "ConfigurationDefinitionSummaries": [
            {
               "FirstClassParameters": {
                  "string" : "string"
               },
               "Id": "string",
               "Type": "string",
               "TypeVersion": "string"
            }
         ],
         "Description": "string",
         "ManagerArn": "string",
         "Name": "string",
         "StatusSummaries": [
            {
               "LastUpdatedAt": "string",
               "Status": "string",
               "StatusDetails": {
                  "string" : "string"
               },
               "StatusMessage": "string",
               "StatusType": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConfigurationManagers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationManagersList](#API_ListConfigurationManagers_ResponseSyntax) **   <a name="quicksetup-ListConfigurationManagers-response-ConfigurationManagersList"></a>
The configuration managers returned by the request.
Type: Array of [ConfigurationManagerSummary](API_ConfigurationManagerSummary.md) objects

 ** [NextToken](#API_ListConfigurationManagers_ResponseSyntax) **   <a name="quicksetup-ListConfigurationManagers-response-NextToken"></a>
The token to use when requesting the next set of configuration managers. If there are no additional operations to return, the string is empty.
Type: String

## Errors
<a name="API_ListConfigurationManagers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requester has insufficient permissions to perform the operation.
HTTP Status Code: 403

 ** ConflictException **
Another request is being processed. Wait a few minutes and try again.
HTTP Status Code: 409

 ** InternalServerException **
An error occurred on the server side.
HTTP Status Code: 500

 ** ThrottlingException **
The request or operation exceeds the maximum allowed request rate per AWS account and AWS Region.
HTTP Status Code: 429

 ** ValidationException **
The request is invalid. Verify the values provided for the request parameters are accurate.
HTTP Status Code: 400

## See Also
<a name="API_ListConfigurationManagers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/ListConfigurationManagers)
