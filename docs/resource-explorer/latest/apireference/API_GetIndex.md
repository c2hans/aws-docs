---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetIndex.html
---

# GetIndex
<a name="API_GetIndex"></a>

Retrieves details about the AWS Resource Explorer index in the AWS Region in which you invoked the operation.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:GetIndex`

   **Resource**: The ARN of the index in the AWS Region in which you call this operation.

 **Related operations**
+ To create an index in a new AWS Region, use [CreateIndex](API_CreateIndex.md).
+ To delete an index and turn off Resource Explorer in an AWS Region, use [DeleteIndex](API_DeleteIndex.md).
+ To retrieve the details for an index and check its state or its type, use [GetIndex](#API_GetIndex).
+ To list all of the indexes in the AWS account, use [ListIndexes](API_ListIndexes.md).
+ To switch an index between being a local index or an aggregator index, use [UpdateIndexType](API_UpdateIndexType.md).

## Request Syntax
<a name="API_GetIndex_RequestSyntax"></a>

```
POST /GetIndex HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIndex_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetIndex_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedAt": "string",
   "LastUpdatedAt": "string",
   "ReplicatingFrom": [ "string" ],
   "ReplicatingTo": [ "string" ],
   "State": "string",
   "Tags": {
      "string" : "string"
   },
   "Type": "string"
}
```

## Response Elements
<a name="API_GetIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetIndex_ResponseSyntax) **   <a name="resourceexplorer-GetIndex-response-Arn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the index.
Type: String

 ** [CreatedAt](#API_GetIndex_ResponseSyntax) **   <a name="resourceexplorer-GetIndex-response-CreatedAt"></a>
The date and time when the index was originally created.
Type: Timestamp

 ** [LastUpdatedAt](#API_GetIndex_ResponseSyntax) **   <a name="resourceexplorer-GetIndex-response-LastUpdatedAt"></a>
The date and time when the index was last updated.
Type: Timestamp

 ** [ReplicatingFrom](#API_GetIndex_ResponseSyntax) **   <a name="resourceexplorer-GetIndex-response-ReplicatingFrom"></a>
This response value is present only if this index is `Type=AGGREGATOR`.
A list of the AWS Regions that replicate their content to the index in this Region.
Type: Array of strings
Pattern: `[a-z-]+-[a-z]+-[0-9]`

 ** [ReplicatingTo](#API_GetIndex_ResponseSyntax) **   <a name="resourceexplorer-GetIndex-response-ReplicatingTo"></a>
This response value is present only if this index is `Type=LOCAL`.
The AWS Region that contains the aggregator index, if one exists. If an aggregator index does exist then the Region in which you called this operation replicates its index information to the Region specified in this response value.
Type: Array of strings
Pattern: `[a-z-]+-[a-z]+-[0-9]`

 ** [State](#API_GetIndex_ResponseSyntax) **   <a name="resourceexplorer-GetIndex-response-State"></a>
The current state of the index in this AWS Region.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | UPDATING`

 ** [Tags](#API_GetIndex_ResponseSyntax) **   <a name="resourceexplorer-GetIndex-response-Tags"></a>
Tag key and value pairs that are attached to the index.
Type: String to string map

 ** [Type](#API_GetIndex_ResponseSyntax) **   <a name="resourceexplorer-GetIndex-response-Type"></a>
The type of the index in this Region. For information about the aggregator index and how it differs from a local index, see [Turning on cross-Region search by creating an aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html).
Type: String
Valid Values: `LOCAL | AGGREGATOR`

## Errors
<a name="API_GetIndex_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## Examples
<a name="API_GetIndex_Examples"></a>

### Example
<a name="API_GetIndex_Example_1"></a>

The following example displays the details for the Resource Explorer index in the specified AWS Region. Because the specified Region contains the aggregator index for the account, it lists the two other Regions in the account that replicate data into this Region's index.

#### Sample Request
<a name="API_GetIndex_Example_1_Request"></a>

```
POST /GetIndex HTTP/1.1
                    Host: resource-explorer-2.us-east-1.amazonaws.com
X-Amz-Date: 20221101T200059Z
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
```

#### Sample Response
<a name="API_GetIndex_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 20:00:59 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111",
    "CreatedAt": "2022-07-12T18:59:10.503000+00:00",
    "LastUpdatedAt": "2022-07-13T18:41:58.799000+00:00",
    "ReplicatingFrom": [
        "ap-south-1",
        "us-west-2"
    ],
    "State": "active",
    "Tags": {},
    "Type": "aggregator"
}
```

## See Also
<a name="API_GetIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/GetIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/GetIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/GetIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/GetIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/GetIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/GetIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/GetIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/GetIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/GetIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/GetIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
