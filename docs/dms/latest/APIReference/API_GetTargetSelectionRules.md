---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_GetTargetSelectionRules.html
---

# GetTargetSelectionRules
<a name="API_GetTargetSelectionRules"></a>

Converts source selection rules into their target counterparts for schema conversion operations.

 **Required permissions:** `dms:GetTargetSelectionRules`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_GetTargetSelectionRules_RequestSyntax"></a>

```
{
   "MigrationProjectIdentifier": "{{string}}",
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTargetSelectionRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MigrationProjectIdentifier](#API_GetTargetSelectionRules_RequestSyntax) **   <a name="DMS-GetTargetSelectionRules-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [SelectionRules](#API_GetTargetSelectionRules_RequestSyntax) **   <a name="DMS-GetTargetSelectionRules-request-SelectionRules"></a>
A JSON string that contains the source selection rules to convert into their target counterparts. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts only source selection rules, where `server-name` in the object locator matches the source data provider.
+ Supports only `explicit` rule actions.
+ Does not support `category-name` in the object locator.
+ Up to 10 rules are allowed.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetTargetSelectionRules_ResponseSyntax"></a>

```
{
   "TargetSelectionRules": "string"
}
```

## Response Elements
<a name="API_GetTargetSelectionRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TargetSelectionRules](#API_GetTargetSelectionRules_ResponseSyntax) **   <a name="DMS-GetTargetSelectionRules-response-TargetSelectionRules"></a>
The JSON string representing the counterpart selection rules in the target.
Type: String

## Errors
<a name="API_GetTargetSelectionRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_GetTargetSelectionRules_Examples"></a>

### Convert source selection rules to target selection rules
<a name="API_GetTargetSelectionRules_Example_1"></a>

The following example converts source selection rules that select the `ExampleTable` table in the `ExampleSchema` schema into target selection rules that reference its converted counterpart.

#### Sample Request
<a name="API_GetTargetSelectionRules_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.GetTargetSelectionRules
{
   "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
   "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"database-name\": \"ExampleDatabase\", \"schema-name\": \"ExampleSchema\", \"table-name\": \"ExampleTable\"}, \"rule-action\": \"explicit\"}]}"
}
```

#### Sample Response
<a name="API_GetTargetSelectionRules_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "TargetSelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-target-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"exampledatabase_exampleschema\", \"table-name\": \"exampletable\"}, \"rule-action\": \"explicit\"}]}"
}
```

## See Also
<a name="API_GetTargetSelectionRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/GetTargetSelectionRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/GetTargetSelectionRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/GetTargetSelectionRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/GetTargetSelectionRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/GetTargetSelectionRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/GetTargetSelectionRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/GetTargetSelectionRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/GetTargetSelectionRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/GetTargetSelectionRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/GetTargetSelectionRules)
