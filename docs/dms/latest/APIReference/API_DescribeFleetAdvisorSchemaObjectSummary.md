---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeFleetAdvisorSchemaObjectSummary.html
---

# DescribeFleetAdvisorSchemaObjectSummary
<a name="API_DescribeFleetAdvisorSchemaObjectSummary"></a>

**Important**
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

Provides descriptions of the schemas discovered by your Fleet Advisor collectors.

## Request Syntax
<a name="API_DescribeFleetAdvisorSchemaObjectSummary_RequestSyntax"></a>

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
<a name="API_DescribeFleetAdvisorSchemaObjectSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeFleetAdvisorSchemaObjectSummary_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemaObjectSummary-request-Filters"></a>
 If you specify any of the following filters, the output includes information for only those schema objects that meet the filter criteria:
+  `schema-id` – The ID of the schema, for example `d4610ac5-e323-4ad9-bc50-eaf7249dfe9d`.
Example: `describe-fleet-advisor-schema-object-summary --filter Name="schema-id",Values="50"`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxRecords](#API_DescribeFleetAdvisorSchemaObjectSummary_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemaObjectSummary-request-MaxRecords"></a>
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).
Sets the maximum number of records returned in the response.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeFleetAdvisorSchemaObjectSummary_RequestSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemaObjectSummary-request-NextToken"></a>
If `NextToken` is returned by a previous response, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeFleetAdvisorSchemaObjectSummary_ResponseSyntax"></a>

```
{
   "FleetAdvisorSchemaObjects": [
      {
         "CodeLineCount": number,
         "CodeSize": number,
         "NumberOfObjects": number,
         "ObjectType": "string",
         "SchemaId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFleetAdvisorSchemaObjectSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetAdvisorSchemaObjects](#API_DescribeFleetAdvisorSchemaObjectSummary_ResponseSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemaObjectSummary-response-FleetAdvisorSchemaObjects"></a>
A collection of `FleetAdvisorSchemaObjectResponse` objects.
Type: Array of [FleetAdvisorSchemaObjectResponse](API_FleetAdvisorSchemaObjectResponse.md) objects

 ** [NextToken](#API_DescribeFleetAdvisorSchemaObjectSummary_ResponseSyntax) **   <a name="DMS-DescribeFleetAdvisorSchemaObjectSummary-response-NextToken"></a>
If `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String

## Errors
<a name="API_DescribeFleetAdvisorSchemaObjectSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribeFleetAdvisorSchemaObjectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeFleetAdvisorSchemaObjectSummary)
