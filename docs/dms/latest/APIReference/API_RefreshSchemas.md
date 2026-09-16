---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RefreshSchemas.html
---

# RefreshSchemas
<a name="API_RefreshSchemas"></a>

Populates the schema for the specified endpoint. This is an asynchronous operation and can take several minutes. You can check the status of this operation by calling the DescribeRefreshSchemasStatus operation.

## Request Syntax
<a name="API_RefreshSchemas_RequestSyntax"></a>

```
{
   "EndpointArn": "{{string}}",
   "ReplicationInstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_RefreshSchemas_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointArn](#API_RefreshSchemas_RequestSyntax) **   <a name="DMS-RefreshSchemas-request-EndpointArn"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
Type: String
Required: Yes

 ** [ReplicationInstanceArn](#API_RefreshSchemas_RequestSyntax) **   <a name="DMS-RefreshSchemas-request-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the replication instance.
Type: String
Required: Yes

## Response Syntax
<a name="API_RefreshSchemas_ResponseSyntax"></a>

```
{
   "RefreshSchemasStatus": {
      "EndpointArn": "string",
      "LastFailureMessage": "string",
      "LastRefreshDate": number,
      "ReplicationInstanceArn": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_RefreshSchemas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RefreshSchemasStatus](#API_RefreshSchemas_ResponseSyntax) **   <a name="DMS-RefreshSchemas-response-RefreshSchemasStatus"></a>
The status of the refreshed schema.
Type: [RefreshSchemasStatus](API_RefreshSchemasStatus.md) object

## Errors
<a name="API_RefreshSchemas_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
 AWS DMS cannot access the KMS key.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_RefreshSchemas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/RefreshSchemas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/RefreshSchemas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RefreshSchemas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/RefreshSchemas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RefreshSchemas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/RefreshSchemas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/RefreshSchemas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/RefreshSchemas)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/RefreshSchemas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RefreshSchemas)
