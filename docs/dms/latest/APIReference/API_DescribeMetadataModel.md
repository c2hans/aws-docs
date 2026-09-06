---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModel.html
---

# DescribeMetadataModel
<a name="API_DescribeMetadataModel"></a>

Gets detailed information about the specified metadata model, including its definition and corresponding converted objects in the target database if applicable.

 **Required permissions:** `dms:DescribeMetadataModel`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_DescribeMetadataModel_RequestSyntax"></a>

```
{
   "MigrationProjectIdentifier": "{{string}}",
   "Origin": "{{string}}",
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMetadataModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MigrationProjectIdentifier](#API_DescribeMetadataModel_RequestSyntax) **   <a name="DMS-DescribeMetadataModel-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [Origin](#API_DescribeMetadataModel_RequestSyntax) **   <a name="DMS-DescribeMetadataModel-request-Origin"></a>
Specifies whether to retrieve metadata from the source or target tree. Valid values: SOURCE \| TARGET
Type: String
Valid Values: `SOURCE | TARGET`
Required: Yes

 ** [SelectionRules](#API_DescribeMetadataModel_RequestSyntax) **   <a name="DMS-DescribeMetadataModel-request-SelectionRules"></a>
A JSON string that identifies the metadata model to retrieve. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts source or target selection rules depending on the `Origin` parameter. The `server-name` in the object locator must match the corresponding data provider.
+ Supports only `explicit` rule actions.
+ Exactly one rule is allowed.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeMetadataModel_ResponseSyntax"></a>

```
{
   "Definition": "string",
   "MetadataModelName": "string",
   "MetadataModelType": "string",
   "TargetMetadataModels": [
      {
         "MetadataModelName": "string",
         "SelectionRules": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMetadataModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Definition](#API_DescribeMetadataModel_ResponseSyntax) **   <a name="DMS-DescribeMetadataModel-response-Definition"></a>
The SQL text of the metadata model. This field might not be populated for some metadata models.
Type: String

 ** [MetadataModelName](#API_DescribeMetadataModel_ResponseSyntax) **   <a name="DMS-DescribeMetadataModel-response-MetadataModelName"></a>
The name of the metadata model.
Type: String

 ** [MetadataModelType](#API_DescribeMetadataModel_ResponseSyntax) **   <a name="DMS-DescribeMetadataModel-response-MetadataModelType"></a>
The type of the metadata model.
Type: String

 ** [TargetMetadataModels](#API_DescribeMetadataModel_ResponseSyntax) **   <a name="DMS-DescribeMetadataModel-response-TargetMetadataModels"></a>
A list of counterpart metadata models in the target. This field is populated only when Origin is SOURCE and after the object has been converted by DMS Schema Conversion.
Type: Array of [MetadataModelReference](API_MetadataModelReference.md) objects

## Errors
<a name="API_DescribeMetadataModel_Errors"></a>

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
<a name="API_DescribeMetadataModel_Examples"></a>

### Retrieve a source table metadata model
<a name="API_DescribeMetadataModel_Example_1"></a>

The following example retrieves detailed information about the `ExampleTable` table in the `ExampleSchema` schema from the source metadata tree, including its SQL definition and references to the corresponding converted metadata models in the target database.

#### Sample Request
<a name="API_DescribeMetadataModel_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.DescribeMetadataModel
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\", \"table-name\": \"ExampleTable\"}, \"rule-action\": \"explicit\"}]}",
    "Origin": "SOURCE"
}
```

#### Sample Response
<a name="API_DescribeMetadataModel_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "MetadataModelName": "ExampleTable",
    "MetadataModelType": "table",
    "TargetMetadataModels": [
        {
            "MetadataModelName": "exampletable",
            "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-target-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"exampleschema\", \"table-name\": \"exampletable\"}, \"rule-action\": \"explicit\"}]}"
        }
    ],
    "Definition": "CREATE TABLE ExampleTable (ExampleColumn INTEGER NOT NULL);"
}
```

## See Also
<a name="API_DescribeMetadataModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeMetadataModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeMetadataModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeMetadataModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeMetadataModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeMetadataModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeMetadataModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeMetadataModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeMetadataModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeMetadataModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeMetadataModel)
