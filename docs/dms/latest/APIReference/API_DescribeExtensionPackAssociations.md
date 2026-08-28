---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeExtensionPackAssociations.html
---

# DescribeExtensionPackAssociations
<a name="API_DescribeExtensionPackAssociations"></a>

Returns a paginated list of extension pack installation requests for a migration project, initiated by [StartExtensionPackAssociation](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartExtensionPackAssociation.html).

 **Required permissions:** `dms:ListExtensionPacks`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_DescribeExtensionPackAssociations_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "MigrationProjectIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeExtensionPackAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeExtensionPackAssociations_RequestSyntax) **   <a name="DMS-DescribeExtensionPackAssociations-request-Filters"></a>
The filters to apply to the extension pack installation requests.
The following filter names are supported:
+  `request-id` – The request identifier.
+  `status` – The request status. Valid values: `RECEIVED`, `IN_PROGRESS`, `SUCCESS`, `FAILED`.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeExtensionPackAssociations_RequestSyntax) **   <a name="DMS-DescribeExtensionPackAssociations-request-Marker"></a>
Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
If `Marker` is returned by a previous response, there are more results available. The value of `Marker` is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeExtensionPackAssociations_RequestSyntax) **   <a name="DMS-DescribeExtensionPackAssociations-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, AWS DMS includes a pagination token in the response so that you can retrieve the remaining results.
Type: Integer
Required: No

 ** [MigrationProjectIdentifier](#API_DescribeExtensionPackAssociations_RequestSyntax) **   <a name="DMS-DescribeExtensionPackAssociations-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_DescribeExtensionPackAssociations_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "Requests": [
      {
         "Error": { ... },
         "ExportSqlDetails": {
            "ObjectURL": "string",
            "S3ObjectKey": "string"
         },
         "MigrationProjectArn": "string",
         "Progress": {
            "ProcessedObject": {
               "EndpointType": "string",
               "Name": "string",
               "Type": "string"
            },
            "ProgressPercent": number,
            "ProgressStep": "string",
            "TotalObjects": number
         },
         "RequestIdentifier": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeExtensionPackAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeExtensionPackAssociations_ResponseSyntax) **   <a name="DMS-DescribeExtensionPackAssociations-response-Marker"></a>
Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
If `Marker` is returned by a previous response, there are more results available. The value of `Marker` is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.
Type: String

 ** [Requests](#API_DescribeExtensionPackAssociations_ResponseSyntax) **   <a name="DMS-DescribeExtensionPackAssociations-response-Requests"></a>
A paginated list of extension pack installation requests.
 AWS DMS never populates the `ExportSqlDetails` field for this operation.
Type: Array of [SchemaConversionRequest](API_SchemaConversionRequest.md) objects

## Errors
<a name="API_DescribeExtensionPackAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeExtensionPackAssociations_Examples"></a>

### Retrieve extension pack installation requests
<a name="API_DescribeExtensionPackAssociations_Example_1"></a>

The following example retrieves extension pack installation requests identified by their request IDs.

#### Sample Request
<a name="API_DescribeExtensionPackAssociations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.DescribeExtensionPackAssociations
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "Filters": [
        {
            "Name": "request-id",
            "Values": ["a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"]
        }
    ]
}
```

#### Sample Response
<a name="API_DescribeExtensionPackAssociations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "Requests": [
        {
            "Status": "SUCCESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
        },
        {
            "Status": "IN_PROGRESS",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Progress": {
                "ProgressPercent": 50.0,
                "ProgressStep": "IN_PROGRESS"
            }
        },
        {
            "Status": "FAILED",
            "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "MigrationProjectArn": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
            "Error": {
                "defaultErrorDetails": {
                    "Message": "The database user in your target secret does not have sufficient privileges. Grant the required privileges and try again."
                }
            }
        }
    ]
}
```

## See Also
<a name="API_DescribeExtensionPackAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeExtensionPackAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeExtensionPackAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeExtensionPackAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeExtensionPackAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeExtensionPackAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeExtensionPackAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeExtensionPackAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeExtensionPackAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeExtensionPackAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeExtensionPackAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
