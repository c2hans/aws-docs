---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorSchemas.html
---

# DescribeFleetAdvisorSchemas
<a name="API_DescribeFleetAdvisorSchemas"></a>

**Important**
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

Returns a list of schemas detected by Fleet Advisor Collectors in your account.

## Request Syntax
<a name="API_DescribeFleetAdvisorSchemas_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxRecords": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetAdvisorSchemas_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeFleetAdvisorSchemas_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemas-request-Filters"></a>
 If you specify any of the following filters, the output includes information for only those schemas that meet the filter criteria:
+  `complexity` – The schema's complexity, for example `Simple`.
+  `database-id` – The ID of the schema's database.
+  `database-ip-address` – The IP address of the schema's database.
+  `database-name` – The name of the schema's database.
+  `database-engine` – The name of the schema database's engine.
+  `original-schema-name` – The name of the schema's database's main schema.
+  `schema-id` – The ID of the schema, for example `15`.
+  `schema-name` – The name of the schema.
+  `server-ip-address` – The IP address of the schema database's server.
An example is: `describe-fleet-advisor-schemas --filter Name="schema-id",Values="50"`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxRecords](#API_DescribeFleetAdvisorSchemas_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemas-request-MaxRecords"></a>
Sets the maximum number of records returned in the response.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeFleetAdvisorSchemas_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemas-request-NextToken"></a>
If `NextToken` is returned by a previous response, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeFleetAdvisorSchemas_ResponseSyntax"></a>

```
{
   "FleetAdvisorSchemas": [
      {
         "CodeLineCount": number,
         "CodeSize": number,
         "Complexity": "string",
         "DatabaseInstance": {
            "DatabaseEngine": "string",
            "DatabaseId": "string",
            "DatabaseIpAddress": "string",
            "DatabaseName": "string"
         },
         "OriginalSchema": {
            "DatabaseId": "string",
            "DatabaseIpAddress": "string",
            "DatabaseName": "string",
            "SchemaId": "string",
            "SchemaName": "string"
         },
         "SchemaId": "string",
         "SchemaName": "string",
         "Server": {
            "IpAddress": "string",
            "ServerId": "string",
            "ServerName": "string"
         },
         "Similarity": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFleetAdvisorSchemas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetAdvisorSchemas](#API_DescribeFleetAdvisorSchemas_ResponseSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemas-response-FleetAdvisorSchemas"></a>
A collection of `SchemaResponse` objects.
Type: Array of [SchemaResponse](API_SchemaResponse.md) objects

 ** [NextToken](#API_DescribeFleetAdvisorSchemas_ResponseSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemas-response-NextToken"></a>
If `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

## Errors
<a name="API_DescribeFleetAdvisorSchemas_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribeFleetAdvisorSchemas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeFleetAdvisorSchemas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeFleetAdvisorSchemas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeFleetAdvisorSchemas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeFleetAdvisorSchemas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeFleetAdvisorSchemas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeFleetAdvisorSchemas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeFleetAdvisorSchemas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeFleetAdvisorSchemas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeFleetAdvisorSchemas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeFleetAdvisorSchemas)
