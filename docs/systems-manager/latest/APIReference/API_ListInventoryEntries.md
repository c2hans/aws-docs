---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListInventoryEntries.html
---

# ListInventoryEntries
<a name="API_ListInventoryEntries"></a>

A list of inventory items returned by the request.

## Request Syntax
<a name="API_ListInventoryEntries_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TypeName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListInventoryEntries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListInventoryEntries_RequestSyntax) **   <a name="systemsmanager-ListInventoryEntries-request-Filters"></a>
One or more filters. Use a filter to return a more specific list of results.
Type: Array of [InventoryFilter](API_InventoryFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [InstanceId](#API_ListInventoryEntries_RequestSyntax) **   <a name="systemsmanager-ListInventoryEntries-request-InstanceId"></a>
The managed node ID for which you want inventory information.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** [MaxResults](#API_ListInventoryEntries_RequestSyntax) **   <a name="systemsmanager-ListInventoryEntries-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListInventoryEntries_RequestSyntax) **   <a name="systemsmanager-ListInventoryEntries-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [TypeName](#API_ListInventoryEntries_RequestSyntax) **   <a name="systemsmanager-ListInventoryEntries-request-TypeName"></a>
The type of inventory item for which you want information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`
Required: Yes

## Response Syntax
<a name="API_ListInventoryEntries_ResponseSyntax"></a>

```
{
   "CaptureTime": "string",
   "Entries": [
      {
         "string" : "string"
      }
   ],
   "InstanceId": "string",
   "NextToken": "string",
   "SchemaVersion": "string",
   "TypeName": "string"
}
```

## Response Elements
<a name="API_ListInventoryEntries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CaptureTime](#API_ListInventoryEntries_ResponseSyntax) **   <a name="systemsmanager-ListInventoryEntries-response-CaptureTime"></a>
The time that inventory information was collected for the managed nodes.
Type: String
Pattern: `^(20)[0-9][0-9]-(0[1-9]|1[012])-([12][0-9]|3[01]|0[1-9])(T)(2[0-3]|[0-1][0-9])(:[0-5][0-9])(:[0-5][0-9])(Z)$`

 ** [Entries](#API_ListInventoryEntries_ResponseSyntax) **   <a name="systemsmanager-ListInventoryEntries-response-Entries"></a>
A list of inventory items on the managed nodes.
Type: Array of string to string maps
Array Members: Minimum number of 0 items. Maximum number of 10000 items.
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [InstanceId](#API_ListInventoryEntries_ResponseSyntax) **   <a name="systemsmanager-ListInventoryEntries-response-InstanceId"></a>
The managed node ID targeted by the request to query inventory information.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`

 ** [NextToken](#API_ListInventoryEntries_ResponseSyntax) **   <a name="systemsmanager-ListInventoryEntries-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [SchemaVersion](#API_ListInventoryEntries_ResponseSyntax) **   <a name="systemsmanager-ListInventoryEntries-response-SchemaVersion"></a>
The inventory schema version used by the managed nodes.
Type: String
Pattern: `^([0-9]{1,6})(\.[0-9]{1,6})$`

 ** [TypeName](#API_ListInventoryEntries_ResponseSyntax) **   <a name="systemsmanager-ListInventoryEntries-response-TypeName"></a>
The type of inventory item returned by the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`

## Errors
<a name="API_ListInventoryEntries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilter **
The filter name isn't valid. Verify that you entered the correct name and try again.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

 ** InvalidTypeNameException **
The parameter type name isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_ListInventoryEntries_Examples"></a>

### Example
<a name="API_ListInventoryEntries_Example_1"></a>

This example illustrates one usage of ListInventoryEntries.

#### Sample Request
<a name="API_ListInventoryEntries_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListInventoryEntries
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240330T154930Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240330/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 68

{
    "InstanceId": "i-04bf6ad63bEXAMPLE",
    "TypeName": "AWS:Application"
}
```

#### Sample Response
<a name="API_ListInventoryEntries_Example_1_Response"></a>

```
{
    "CaptureTime": "2020-03-30T15:45:32Z",
    "Entries": [
        {
            "Architecture": "i386",
            "InstalledTime": "2020-01-15T00:00:00Z",
            "Name": "AWS Tools for Windows",
            "PackageId": "{2088D019-97CC-4349-BA45-9777568EAE94}",
            "Publisher": "Amazon Web Services Developer Relations",
            "Version": "3.15.925"
        },
        {
            "Architecture": "i386",
            "Name": "Amazon SSM Agent",
            "PackageId": "{2a4673c2-68c6-4a4c-9be6-c3b1be96fdff}",
            "Publisher": "Amazon Web Services",
            "Version": "2.3.930.0"
        },
        {
            "Architecture": "x86_64",
            "InstalledTime": "2018-10-14T00:00:00Z",
            "Name": "aws-cfn-bootstrap",
            "PackageId": "{34CD0CCF-195B-4BC5-B409-D44EB9A129C8}",
            "Publisher": "Amazon Web Services",
            "Version": "1.4.31"
        },
        {
            "Architecture": "x86_64",
            "InstalledTime": "2020-03-10T00:00:00Z",
            "Name": "PowerShell 7-x64",
            "PackageId": "{B324E508-9AAE-446A-BC4C-BB446E8C2A18}",
            "Publisher": "Microsoft Corporation",
            "Version": "7.0.0.0"
        },
        {
            "Architecture": "x86_64",
            "InstalledTime": "2019-09-06T00:00:00Z",
            "Name": "AWS PV Drivers",
            "PackageId": "{C1F68A8D-F235-4886-87B0-150107C07EDA}",
            "Publisher": "Amazon Web Services",
            "Version": "8.3.2"
        }
    ],
    "InstanceId": "i-04bf6ad63bEXAMPLE",
    "SchemaVersion": "1.1",
    "TypeName": "AWS:Application"
}
```

## See Also
<a name="API_ListInventoryEntries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListInventoryEntries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListInventoryEntries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListInventoryEntries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListInventoryEntries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListInventoryEntries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListInventoryEntries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListInventoryEntries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListInventoryEntries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListInventoryEntries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListInventoryEntries)
