---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds metadata tags to the Amazon RDS Performance Insights resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "ServiceType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ResourceARN](#API_TagResource_RequestSyntax) **   <a name="performanceinsights-TagResource-request-ResourceARN"></a>
The Amazon RDS Performance Insights resource that the tags are added to. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see [ Constructing an RDS Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.*:pi:.*$`
Required: Yes

 ** [ServiceType](#API_TagResource_RequestSyntax) **   <a name="performanceinsights-TagResource-request-ServiceType"></a>
The AWS service for which Performance Insights returns metrics. Valid value is `RDS`.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="performanceinsights-TagResource-request-Tags"></a>
The metadata assigned to an Amazon RDS resource consisting of a key-value pair.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

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
<a name="API_TagResource_Examples"></a>

### Add tag to an analysis report
<a name="API_TagResource_Example_1"></a>

The following example adds a tag to the report `report-01234567890abcdef`.

#### Sample Request
<a name="API_TagResource_Example_1_Request"></a>

```
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.TagResource
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "ServiceType": "RDS",
    "ResourceARN": "arn:aws:pi:us-west-2:123456789012:perf-reports/rds/db-ABC1DEFGHIJKL2MNOPQRSTUV3W/report-01234567890abcdef",
    "Tags": [{
        "Key": "MyKey",
        "Value": "MyValue"
    }]
}
```

#### Sample Response
<a name="API_TagResource_Example_1_Response"></a>

```
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
```

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/TagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
