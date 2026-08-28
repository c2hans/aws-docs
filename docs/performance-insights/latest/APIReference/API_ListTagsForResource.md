---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Retrieves all the metadata tags associated with Amazon RDS Performance Insights resource.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "ServiceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ResourceARN](#API_ListTagsForResource_RequestSyntax) **   <a name="performanceinsights-ListTagsForResource-request-ResourceARN"></a>
Lists all the tags for the Amazon RDS Performance Insights resource. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see [ Constructing an RDS Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.*:pi:.*$`
Required: Yes

 ** [ServiceType](#API_ListTagsForResource_RequestSyntax) **   <a name="performanceinsights-ListTagsForResource-request-ServiceType"></a>
List the tags for the AWS service for which Performance Insights returns metrics. Valid value is `RDS`.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="performanceinsights-ListTagsForResource-response-Tags"></a>
The metadata assigned to an Amazon RDS resource consisting of a key-value pair.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

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
<a name="API_ListTagsForResource_Examples"></a>

### List tags for an analysis report
<a name="API_ListTagsForResource_Example_1"></a>

The following example lists all the tags for the report `report-01234567890abcdef`.

#### Sample Request
<a name="API_ListTagsForResource_Example_1_Request"></a>

```
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.ListTagsForResource
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "ServiceType": "RDS",
    "ResourceARN": "arn:aws:pi:us-west-2:123456789012:perf-reports/rds/db-ABC1DEFGHIJKL2MNOPQRSTUV3W/report-01234567890abcdef"
}
```

#### Sample Response
<a name="API_ListTagsForResource_Example_1_Response"></a>

```
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive

{
    "Tags": [
        {
            "Key": "MyKey",
            "Value": "MyValue"
        },
        {
            "Key": "Name",
            "Value": "MyName"
        }
    ]
}
```

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/ListTagsForResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
