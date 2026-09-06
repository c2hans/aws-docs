---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParametersByPath.html
---

# GetParametersByPath
<a name="API_GetParametersByPath"></a>

Retrieve information about one or more parameters under a specified level in a hierarchy.

Request results are returned on a best-effort basis. If you specify `MaxResults` in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of `MaxResults`. If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a `NextToken`. You can specify the `NextToken` in a subsequent call to get the next set of results.

Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a `ValidationException` error.

## Request Syntax
<a name="API_GetParametersByPath_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ParameterFilters": [
      {
         "Key": "{{string}}",
         "Option": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Path": "{{string}}",
   "Recursive": {{boolean}},
   "WithDecryption": {{boolean}}
}
```

## Request Parameters
<a name="API_GetParametersByPath_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetParametersByPath_RequestSyntax) **   <a name="systemsmanager-GetParametersByPath-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [NextToken](#API_GetParametersByPath_RequestSyntax) **   <a name="systemsmanager-GetParametersByPath-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

 ** [ParameterFilters](#API_GetParametersByPath_RequestSyntax) **   <a name="systemsmanager-GetParametersByPath-request-ParameterFilters"></a>
Filters to limit the request results.
The following `Key` values are supported for `GetParametersByPath`: `Type`, `KeyId`, and `Label`.
The following `Key` values aren't supported for `GetParametersByPath`: `tag`, `DataType`, `Name`, `Path`, and `Tier`.
Type: Array of [ParameterStringFilter](API_ParameterStringFilter.md) objects
Required: No

 ** [Path](#API_GetParametersByPath_RequestSyntax) **   <a name="systemsmanager-GetParametersByPath-request-Path"></a>
The hierarchy for the parameter. Hierarchies start with a forward slash (/). The hierarchy is the parameter name except the last part of the parameter. For the API call to succeed, the last part of the parameter name can't be in the path. A parameter name hierarchy can have a maximum of 15 levels. Here is an example of a hierarchy: `/Finance/Prod/IAD/WinServ2016/license33 `
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [Recursive](#API_GetParametersByPath_RequestSyntax) **   <a name="systemsmanager-GetParametersByPath-request-Recursive"></a>
Retrieve all parameters within a hierarchy.
If a user has access to a path, then the user can access all levels of that path. For example, if a user has permission to access path `/a`, then the user can also access `/a/b`. Even if a user has explicitly been denied access in IAM for parameter `/a/b`, they can still call the GetParametersByPath API operation recursively for `/a` and view `/a/b`.
Type: Boolean
Required: No

 ** [WithDecryption](#API_GetParametersByPath_RequestSyntax) **   <a name="systemsmanager-GetParametersByPath-request-WithDecryption"></a>
Retrieve all parameters in a hierarchy with their value decrypted.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetParametersByPath_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Parameters": [
      {
         "ARN": "string",
         "DataType": "string",
         "LastModifiedDate": number,
         "Name": "string",
         "Selector": "string",
         "SourceResult": "string",
         "Type": "string",
         "Value": "string",
         "Version": number
      }
   ]
}
```

## Response Elements
<a name="API_GetParametersByPath_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetParametersByPath_ResponseSyntax) **   <a name="systemsmanager-GetParametersByPath-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

 ** [Parameters](#API_GetParametersByPath_ResponseSyntax) **   <a name="systemsmanager-GetParametersByPath-response-Parameters"></a>
A list of parameters found in the specified hierarchy.
Type: Array of [Parameter](API_Parameter.md) objects

## Errors
<a name="API_GetParametersByPath_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilterKey **
The specified key isn't valid.
HTTP Status Code: 400

 ** InvalidFilterOption **
The specified filter option isn't valid. Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
 ** message **
The specified filter option isn't valid. Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.
HTTP Status Code: 400

 ** InvalidFilterValue **
The filter value isn't valid. Verify the value and try again.
HTTP Status Code: 400

 ** InvalidKeyId **
The query key ID isn't valid.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_GetParametersByPath_Examples"></a>

### Example
<a name="API_GetParametersByPath_Example_1"></a>

This example illustrates one usage of GetParametersByPath.

#### Sample Request
<a name="API_GetParametersByPath_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 46
X-Amz-Target: AmazonSSM.GetParametersByPath
X-Amz-Date: 20240316T004724Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240316/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Path": "/Branch312/Dev/",
    "Recursive": true
}
```

#### Sample Response
<a name="API_GetParametersByPath_Example_1_Response"></a>

```
{
    "Parameters": [
        {
            "Name": "/Branch312/Dev/Engineer1",
            "Type": "String",
            "Value": "Saanvi Sarkar",
            "Version": 1
        },
        {
            "Name": "/Branch312/Dev/Engineer2",
            "Type": "String",
            "Value": "Zhang Wei",
            "Version": 1
        },
        {
            "Name": "/Branch312/Dev/Engineer3",
            "Type": "String",
            "Value": "Alejandro Rosalez",
            "Version": 1
        },
        {
            "Name": "/Branch312/Dev/Intern",
            "Type": "String",
            "Value": "Nikhil Jayashankar",
            "Version": 1
        },
        {
            "Name": "/Branch312/Dev/TeamLead",
            "Type": "String",
            "Value": "Jane Roe",
            "Version": 1
        }
    ]
}
```

## See Also
<a name="API_GetParametersByPath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetParametersByPath)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetParametersByPath)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetParametersByPath)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetParametersByPath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetParametersByPath)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetParametersByPath)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetParametersByPath)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetParametersByPath)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetParametersByPath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetParametersByPath)
