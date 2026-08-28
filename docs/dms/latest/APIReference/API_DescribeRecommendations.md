---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeRecommendations.html
---

# DescribeRecommendations
<a name="API_DescribeRecommendations"></a>

**Important**
 End of support notice: On May 20, 2026, AWS will end support for AWS DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the AWS DMS Fleet Advisor; console or AWS DMS Fleet Advisor; resources. For more information, see [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html).

Returns a paginated list of target engine recommendations for your source databases.

## Request Syntax
<a name="API_DescribeRecommendations_RequestSyntax"></a>

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
<a name="API_DescribeRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeRecommendations_RequestSyntax) **   <a name="DMS-DescribeRecommendations-request-Filters"></a>
Filters applied to the target engine recommendations described in the form of key-value pairs.
Valid filter names: `database-id` \| `engine-name`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxRecords](#API_DescribeRecommendations_RequestSyntax) **   <a name="DMS-DescribeRecommendations-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, Fleet Advisor includes a pagination token in the response so that you can retrieve the remaining results.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeRecommendations_RequestSyntax) **   <a name="DMS-DescribeRecommendations-request-NextToken"></a>
Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
If `NextToken` is returned by a previous response, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeRecommendations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Recommendations": [
      {
         "CreatedDate": "string",
         "Data": {
            "RdsEngine": {
               "RequirementsToTarget": {
                  "DeploymentOption": "string",
                  "EngineEdition": "string",
                  "EngineVersion": "string",
                  "InstanceMemory": number,
                  "InstanceVcpu": number,
                  "StorageIops": number,
                  "StorageSize": number
               },
               "TargetConfiguration": {
                  "DeploymentOption": "string",
                  "EngineEdition": "string",
                  "EngineVersion": "string",
                  "InstanceMemory": number,
                  "InstanceType": "string",
                  "InstanceVcpu": number,
                  "StorageIops": number,
                  "StorageSize": number,
                  "StorageType": "string"
               }
            }
         },
         "DatabaseId": "string",
         "EngineName": "string",
         "Preferred": boolean,
         "Settings": {
            "InstanceSizingType": "string",
            "WorkloadType": "string"
         },
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeRecommendations_ResponseSyntax) **   <a name="DMS-DescribeRecommendations-response-NextToken"></a>
The unique pagination token returned for you to pass to a subsequent request. Fleet Advisor returns this token when the number of records in the response is greater than the `MaxRecords` value. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.
Type: String

 ** [Recommendations](#API_DescribeRecommendations_ResponseSyntax) **   <a name="DMS-DescribeRecommendations-response-Recommendations"></a>
The list of recommendations of target engines that Fleet Advisor created for the source database.
Type: Array of [Recommendation](API_Recommendation.md) objects

## Errors
<a name="API_DescribeRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribeRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
