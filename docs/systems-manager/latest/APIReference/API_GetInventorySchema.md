---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetInventorySchema.html
---

# GetInventorySchema
<a name="API_GetInventorySchema"></a>

Return a list of inventory type names for the account, or return a list of attribute names for a specific Inventory item type.

## Request Syntax
<a name="API_GetInventorySchema_RequestSyntax"></a>

```
{
   "Aggregator": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SubType": {{boolean}},
   "TypeName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetInventorySchema_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Aggregator](#API_GetInventorySchema_RequestSyntax) **   <a name="systemsmanager-GetInventorySchema-request-Aggregator"></a>
Returns inventory schemas that support aggregation. For example, this call returns the `AWS:InstanceInformation` type, because it supports aggregation based on the `PlatformName`, `PlatformType`, and `PlatformVersion` attributes.
Type: Boolean
Required: No

 ** [MaxResults](#API_GetInventorySchema_RequestSyntax) **   <a name="systemsmanager-GetInventorySchema-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 200.
Required: No

 ** [NextToken](#API_GetInventorySchema_RequestSyntax) **   <a name="systemsmanager-GetInventorySchema-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [SubType](#API_GetInventorySchema_RequestSyntax) **   <a name="systemsmanager-GetInventorySchema-request-SubType"></a>
Returns the sub-type schema for a specified inventory type.
Type: Boolean
Required: No

 ** [TypeName](#API_GetInventorySchema_RequestSyntax) **   <a name="systemsmanager-GetInventorySchema-request-TypeName"></a>
The type of inventory item to return.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_GetInventorySchema_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Schemas": [
      {
         "Attributes": [
            {
               "DataType": "string",
               "Name": "string"
            }
         ],
         "DisplayName": "string",
         "TypeName": "string",
         "Version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetInventorySchema_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetInventorySchema_ResponseSyntax) **   <a name="systemsmanager-GetInventorySchema-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [Schemas](#API_GetInventorySchema_ResponseSyntax) **   <a name="systemsmanager-GetInventorySchema-response-Schemas"></a>
Inventory schemas returned by the request.
Type: Array of [InventoryItemSchema](API_InventoryItemSchema.md) objects

## Errors
<a name="API_GetInventorySchema_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

 ** InvalidTypeNameException **
The parameter type name isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_GetInventorySchema_Examples"></a>

### Example
<a name="API_GetInventorySchema_Example_1"></a>

This example illustrates one usage of GetInventorySchema.

#### Sample Request
<a name="API_GetInventorySchema_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetInventorySchema
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240330T150040Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240330/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2
```

#### Sample Response
<a name="API_GetInventorySchema_Example_1_Response"></a>

```
{
   "Schemas":[
      {
         "Attributes":[
            {
               "DataType":"STRING",
               "Name":"Name"
            },
            {
               "DataType":"STRING",
               "Name":"ApplicationType"
            },
            {
               "DataType":"STRING",
               "Name":"Publisher"
            },
            {
               "DataType":"STRING",
               "Name":"Version"
            },
            {
               "DataType":"STRING",
               "Name":"InstalledTime"
            },
            {
               "DataType":"STRING",
               "Name":"Architecture"
            },
            {
               "DataType":"STRING",
               "Name":"URL"
            }
         ],
         "TypeName":"AWS:AWSComponent",
         "Version":"1.0"
      },--truncated--
      {
         "Attributes":[
            {
               "DataType":"STRING",
               "Name":"Name"
            },
            {
               "DataType":"STRING",
               "Name":"DisplayName"
            },
            {
               "DataType":"STRING",
               "Name":"ServiceType"
            },
            {
               "DataType":"STRING",
               "Name":"Status"
            },
            {
               "DataType":"STRING",
               "Name":"DependentServices"
            },
            {
               "DataType":"STRING",
               "Name":"ServicesDependedOn"
            },
            {
               "DataType":"STRING",
               "Name":"StartType"
            }
         ],
         "TypeName":"AWS:Service",
         "Version":"1.0"
      }--truncated--
   ]
}
```

## See Also
<a name="API_GetInventorySchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetInventorySchema)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetInventorySchema)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetInventorySchema)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetInventorySchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetInventorySchema)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetInventorySchema)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetInventorySchema)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetInventorySchema)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetInventorySchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetInventorySchema)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
