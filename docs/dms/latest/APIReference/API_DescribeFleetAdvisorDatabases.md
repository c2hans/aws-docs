---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorDatabases.html
---

# DescribeFleetAdvisorDatabases
<a name="API_DescribeFleetAdvisorDatabases"></a>

**Important**
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

Returns a list of Fleet Advisor databases in your account.

## Request Syntax
<a name="API_DescribeFleetAdvisorDatabases_RequestSyntax"></a>

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
<a name="API_DescribeFleetAdvisorDatabases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeFleetAdvisorDatabases_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorDatabases-request-Filters"></a>
 If you specify any of the following filters, the output includes information for only those databases that meet the filter criteria:
+  `database-id` – The ID of the database.
+  `database-name` – The name of the database.
+  `database-engine` – The name of the database engine.
+  `server-ip-address` – The IP address of the database server.
+  `database-ip-address` – The IP address of the database.
+  `collector-name` – The name of the associated Fleet Advisor collector.
An example is: `describe-fleet-advisor-databases --filter Name="database-id",Values="45"`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxRecords](#API_DescribeFleetAdvisorDatabases_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorDatabases-request-MaxRecords"></a>
Sets the maximum number of records returned in the response.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeFleetAdvisorDatabases_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorDatabases-request-NextToken"></a>
If `NextToken` is returned by a previous response, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeFleetAdvisorDatabases_ResponseSyntax"></a>

```
{
   "Databases": [
      {
         "Collectors": [
            {
               "CollectorName": "string",
               "CollectorReferencedId": "string"
            }
         ],
         "DatabaseId": "string",
         "DatabaseName": "string",
         "IpAddress": "string",
         "NumberOfSchemas": number,
         "Server": {
            "IpAddress": "string",
            "ServerId": "string",
            "ServerName": "string"
         },
         "SoftwareDetails": {
            "Engine": "string",
            "EngineEdition": "string",
            "EngineVersion": "string",
            "OsArchitecture": number,
            "ServicePack": "string",
            "SupportLevel": "string",
            "Tooltip": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFleetAdvisorDatabases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Databases](#API_DescribeFleetAdvisorDatabases_ResponseSyntax) **   <a name="DMS-DescribeFleetAdvisorDatabases-response-Databases"></a>
Provides descriptions of the Fleet Advisor collector databases, including the database's collector, ID, and name.
Type: Array of [DatabaseResponse](API_DatabaseResponse.md) objects

 ** [NextToken](#API_DescribeFleetAdvisorDatabases_ResponseSyntax) **   <a name="DMS-DescribeFleetAdvisorDatabases-response-NextToken"></a>
If `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

## Errors
<a name="API_DescribeFleetAdvisorDatabases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribeFleetAdvisorDatabases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeFleetAdvisorDatabases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeFleetAdvisorDatabases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeFleetAdvisorDatabases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeFleetAdvisorDatabases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeFleetAdvisorDatabases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeFleetAdvisorDatabases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeFleetAdvisorDatabases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeFleetAdvisorDatabases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeFleetAdvisorDatabases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeFleetAdvisorDatabases)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
