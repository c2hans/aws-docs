---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelChildren.html
---

# DescribeMetadataModelChildren
<a name="API_DescribeMetadataModelChildren"></a>

Gets a list of child metadata models for the specified metadata model in the database hierarchy.

 **Required permissions:** `dms:DescribeMetadataModelChildren`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_DescribeMetadataModelChildren_RequestSyntax"></a>

```
{
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "MigrationProjectIdentifier": "{{string}}",
   "Origin": "{{string}}",
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMetadataModelChildren_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_DescribeMetadataModelChildren_RequestSyntax) **   <a name="DMS-DescribeMetadataModelChildren-request-Marker"></a>
Specifies the unique pagination token that indicates where the next page should start. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeMetadataModelChildren_RequestSyntax) **   <a name="DMS-DescribeMetadataModelChildren-request-MaxRecords"></a>
The maximum number of metadata model children to include in the response. If more items exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [MigrationProjectIdentifier](#API_DescribeMetadataModelChildren_RequestSyntax) **   <a name="DMS-DescribeMetadataModelChildren-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [Origin](#API_DescribeMetadataModelChildren_RequestSyntax) **   <a name="DMS-DescribeMetadataModelChildren-request-Origin"></a>
Specifies whether to retrieve metadata from the source or target tree. Valid values: SOURCE \| TARGET
Type: String
Valid Values: `SOURCE | TARGET`
Required: Yes

 ** [SelectionRules](#API_DescribeMetadataModelChildren_RequestSyntax) **   <a name="DMS-DescribeMetadataModelChildren-request-SelectionRules"></a>
A JSON string that identifies the metadata model whose children to retrieve. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts source or target selection rules depending on the `Origin` parameter. The `server-name` in the object locator must match the corresponding data provider.
+ Supports only `explicit` rule actions.
+ Exactly one rule is allowed.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeMetadataModelChildren_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "MetadataModelChildren": [
      {
         "MetadataModelName": "string",
         "SelectionRules": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMetadataModelChildren_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeMetadataModelChildren_ResponseSyntax) **   <a name="DMS-DescribeMetadataModelChildren-response-Marker"></a>
Specifies the unique pagination token that makes it possible to display the next page of metadata model children. If a marker is returned, there are more metadata model children available.
Type: String

 ** [MetadataModelChildren](#API_DescribeMetadataModelChildren_ResponseSyntax) **   <a name="DMS-DescribeMetadataModelChildren-response-MetadataModelChildren"></a>
A list of child metadata models.
Type: Array of [MetadataModelReference](API_MetadataModelReference.md) objects

## Errors
<a name="API_DescribeMetadataModelChildren_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeMetadataModelChildren_Examples"></a>

### Retrieve children of a schema
<a name="API_DescribeMetadataModelChildren_Example_1"></a>

The following example retrieves the child metadata models of the `ExampleSchema` schema from the source metadata tree. The response includes a list of object categories within the schema, each with its own selection rule that you can use in subsequent calls to navigate deeper into the hierarchy.

#### Sample Request
<a name="API_DescribeMetadataModelChildren_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.DescribeMetadataModelChildren
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\"}, \"rule-action\": \"explicit\"}]}",
    "Origin": "SOURCE"
}
```

#### Sample Response
<a name="API_DescribeMetadataModelChildren_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "MetadataModelChildren": [
        {
            "MetadataModelName": "Tables",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\", \"category-name\": \"Tables\"}, \"rule-action\": \"explicit\"}]}"
        },
        {
            "MetadataModelName": "Views",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"2\", \"rule-name\": \"2\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\", \"category-name\": \"Views\"}, \"rule-action\": \"explicit\"}]}"
        },
        {
            "MetadataModelName": "Functions",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"3\", \"rule-name\": \"3\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\", \"category-name\": \"Functions\"}, \"rule-action\": \"explicit\"}]}"
        },
        {
            "MetadataModelName": "Sequences",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"4\", \"rule-name\": \"4\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\", \"category-name\": \"Sequences\"}, \"rule-action\": \"explicit\"}]}"
        }
    ]
}
```

## See Also
<a name="API_DescribeMetadataModelChildren_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeMetadataModelChildren)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeMetadataModelChildren)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeMetadataModelChildren)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeMetadataModelChildren)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeMetadataModelChildren)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeMetadataModelChildren)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeMetadataModelChildren)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeMetadataModelChildren)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeMetadataModelChildren)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeMetadataModelChildren)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
