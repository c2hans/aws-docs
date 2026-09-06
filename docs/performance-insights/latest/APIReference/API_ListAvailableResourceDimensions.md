---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListAvailableResourceDimensions.html
---

# ListAvailableResourceDimensions
<a name="API_ListAvailableResourceDimensions"></a>

Retrieve the dimensions that can be queried for each specified metric type on a specified DB instance.

## Request Syntax
<a name="API_ListAvailableResourceDimensions_RequestSyntax"></a>

```
{
   "AuthorizedActions": [ "{{string}}" ],
   "Identifier": "{{string}}",
   "MaxResults": {{number}},
   "Metrics": [ "{{string}}" ],
   "NextToken": "{{string}}",
   "ServiceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAvailableResourceDimensions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Identifier](#API_ListAvailableResourceDimensions_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceDimensions-request-Identifier"></a>
An immutable identifier for a data source that is unique within an AWS Region. Performance Insights gathers metrics from this data source. To use an Amazon RDS DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VWZ`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [Metrics](#API_ListAvailableResourceDimensions_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceDimensions-request-Metrics"></a>
The types of metrics for which to retrieve dimensions. Valid values include `db.load`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-_\.:/*)( ]+$`
Required: Yes

 ** [ServiceType](#API_ListAvailableResourceDimensions_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceDimensions-request-ServiceType"></a>
The AWS service for which Performance Insights returns metrics.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [AuthorizedActions](#API_ListAvailableResourceDimensions_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceDimensions-request-AuthorizedActions"></a>
The actions to discover the dimensions you are authorized to access. If you specify multiple actions, then the response will contain the dimensions common for all the actions.
When you don't specify this request parameter or provide an empty list, the response contains all the available dimensions for the target database engine whether or not you are authorized to access them.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `DescribeDimensionKeys | GetDimensionKeyDetails | GetResourceMetrics`
Required: No

 ** [MaxResults](#API_ListAvailableResourceDimensions_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceDimensions-request-MaxResults"></a>
The maximum number of items to return in the response. If more items exist than the specified `MaxRecords` value, a pagination token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No

 ** [NextToken](#API_ListAvailableResourceDimensions_RequestSyntax) **   <a name="performanceinsights-ListAvailableResourceDimensions-request-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`
Required: No

## Response Syntax
<a name="API_ListAvailableResourceDimensions_ResponseSyntax"></a>

```
{
   "MetricDimensions": [
      {
         "Groups": [
            {
               "Dimensions": [
                  {
                     "Identifier": "string"
                  }
               ],
               "Group": "string"
            }
         ],
         "Metric": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAvailableResourceDimensions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetricDimensions](#API_ListAvailableResourceDimensions_ResponseSyntax) **   <a name="performanceinsights-ListAvailableResourceDimensions-response-MetricDimensions"></a>
The dimension information returned for requested metric types.
Type: Array of [MetricDimensionGroups](API_MetricDimensionGroups.md) objects

 ** [NextToken](#API_ListAvailableResourceDimensions_ResponseSyntax) **   <a name="performanceinsights-ListAvailableResourceDimensions-response-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`

## Errors
<a name="API_ListAvailableResourceDimensions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
The request failed due to an unknown error.
HTTP Status Code: 500

 ** InvalidArgumentException **
One of the arguments provided is invalid for this request.
HTTP Status Code: 400

 ** NotAuthorizedException **
The user is not authorized to perform this request.
HTTP Status Code: 400

## Examples
<a name="API_ListAvailableResourceDimensions_Examples"></a>

### Retrieving dimensions for the metric type db.load
<a name="API_ListAvailableResourceDimensions_Example_1"></a>

The following example retrieves the dimensions for the metric type `db.load`.

#### Sample Request
<a name="API_ListAvailableResourceDimensions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.DescribeDimensionKeys
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "ServiceType": "RDS",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "Metrics": ["db.load"]
}
```

#### Sample Response
<a name="API_ListAvailableResourceDimensions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive

{
    "MetricDimensions": [
        {
            "Metric": "db.load",
            "Groups": [
                {
                    "Group": "db.user",
                    "Dimensions": [
                        {
                            "Identifier": "db.user.id"
                        },
                        {
                            "Identifier": "db.user.name"
                        }
                    ]
                },
                {
                    "Group": "db.sql_tokenized",
                    "Dimensions": [
                        {
                            "Identifier": "db.sql_tokenized.id"
                        },
                        {
                            "Identifier": "db.sql_tokenized.db_id"
                        },
                        {
                            "Identifier": "db.sql_tokenized.statement"
                        }
                    ]
                },
                ...
            ]
        }
    ]
}
```

## See Also
<a name="API_ListAvailableResourceDimensions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/ListAvailableResourceDimensions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/ListAvailableResourceDimensions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/ListAvailableResourceDimensions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/ListAvailableResourceDimensions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/ListAvailableResourceDimensions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/ListAvailableResourceDimensions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/ListAvailableResourceDimensions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/ListAvailableResourceDimensions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/ListAvailableResourceDimensions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/ListAvailableResourceDimensions)
