---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListConfigurations.html
---

# ListConfigurations
<a name="API_ListConfigurations"></a>

Returns configurations deployed by Quick Setup in the requesting AWS account and AWS Region.

## Request Syntax
<a name="API_ListConfigurations_RequestSyntax"></a>

```
POST /listConfigurations HTTP/1.1
Content-type: application/json

{
   "ConfigurationDefinitionId": "{{string}}",
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "ManagerArn": "{{string}}",
   "MaxItems": {{number}},
   "StartingToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationDefinitionId](#API_ListConfigurations_RequestSyntax) **   <a name="quicksetup-ListConfigurations-request-ConfigurationDefinitionId"></a>
The ID of the configuration definition.
Type: String
Pattern: `[a-z0-9-]{1,20}`
Required: No

 ** [Filters](#API_ListConfigurations_RequestSyntax) **   <a name="quicksetup-ListConfigurations-request-Filters"></a>
Filters the results returned by the request.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [ManagerArn](#API_ListConfigurations_RequestSyntax) **   <a name="quicksetup-ListConfigurations-request-ManagerArn"></a>
The ARN of the configuration manager.
Type: String
Pattern: `arn:aws:ssm-quicksetup:([^:]+):(\d{12}):configuration-manager/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}`
Required: No

 ** [MaxItems](#API_ListConfigurations_RequestSyntax) **   <a name="quicksetup-ListConfigurations-request-MaxItems"></a>
Specifies the maximum number of configurations that are returned by the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [StartingToken](#API_ListConfigurations_RequestSyntax) **   <a name="quicksetup-ListConfigurations-request-StartingToken"></a>
The token to use when requesting a specific set of items from a list.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[A-Za-z0-9+=@_|\/\s-]*`
Required: No

## Response Syntax
<a name="API_ListConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationsList": [
      {
         "Account": "string",
         "ConfigurationDefinitionId": "string",
         "CreatedAt": "string",
         "FirstClassParameters": {
            "string" : "string"
         },
         "Id": "string",
         "ManagerArn": "string",
         "Region": "string",
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
         ],
         "Type": "string",
         "TypeVersion": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationsList](#API_ListConfigurations_ResponseSyntax) **   <a name="quicksetup-ListConfigurations-response-ConfigurationsList"></a>
An array of configurations.
Type: Array of [ConfigurationSummary](API_ConfigurationSummary.md) objects

 ** [NextToken](#API_ListConfigurations_ResponseSyntax) **   <a name="quicksetup-ListConfigurations-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_ListConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requester has insufficient permissions to perform the operation.
HTTP Status Code: 403

 ** InternalServerException **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found. Check the ID or name and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request or operation exceeds the maximum allowed request rate per AWS account and AWS Region.
HTTP Status Code: 429

 ** ValidationException **
The request is invalid. Verify the values provided for the request parameters are accurate.
HTTP Status Code: 400

## See Also
<a name="API_ListConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-quicksetup-2018-05-10/ListConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-quicksetup-2018-05-10/ListConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/ListConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-quicksetup-2018-05-10/ListConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/ListConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-quicksetup-2018-05-10/ListConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-quicksetup-2018-05-10/ListConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-quicksetup-2018-05-10/ListConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-quicksetup-2018-05-10/ListConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/ListConfigurations)
