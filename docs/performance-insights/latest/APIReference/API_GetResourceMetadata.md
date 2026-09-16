---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetResourceMetadata.html
---

# GetResourceMetadata
<a name="API_GetResourceMetadata"></a>

Retrieve the metadata for different features. For example, the metadata might indicate that a feature is turned on or off on a specific DB instance.

## Request Syntax
<a name="API_GetResourceMetadata_RequestSyntax"></a>

```
{
   "Identifier": "{{string}}",
   "ServiceType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourceMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Identifier](#API_GetResourceMetadata_RequestSyntax) **   <a name="performanceinsights-GetResourceMetadata-request-Identifier"></a>
An immutable identifier for a data source that is unique for an AWS Region. Performance Insights gathers metrics from this data source. To use a DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [ServiceType](#API_GetResourceMetadata_RequestSyntax) **   <a name="performanceinsights-GetResourceMetadata-request-ServiceType"></a>
The AWS service for which Performance Insights returns metrics.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

## Response Syntax
<a name="API_GetResourceMetadata_ResponseSyntax"></a>

```
{
   "Features": {
      "string" : {
         "Status": "string"
      }
   },
   "Identifier": "string"
}
```

## Response Elements
<a name="API_GetResourceMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Features](#API_GetResourceMetadata_ResponseSyntax) **   <a name="performanceinsights-GetResourceMetadata-response-Features"></a>
The metadata for different features. For example, the metadata might indicate that a feature is turned on or off on a specific DB instance.
Type: String to [FeatureMetadata](API_FeatureMetadata.md) object map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*\S.*`

 ** [Identifier](#API_GetResourceMetadata_ResponseSyntax) **   <a name="performanceinsights-GetResourceMetadata-response-Identifier"></a>
An immutable identifier for a data source that is unique for an AWS Region. Performance Insights gathers metrics from this data source. To use a DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`

## Errors
<a name="API_GetResourceMetadata_Errors"></a>

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
<a name="API_GetResourceMetadata_Examples"></a>

### Retrieve metadata for different features
<a name="API_GetResourceMetadata_Example_1"></a>

The following example requests all metadata for the database with the ID `db-ABC1DEFGHIJKL2MNOPQRSTUV3W`. The response shows that SQL digest statistics are enabled.

#### Sample Request
<a name="API_GetResourceMetadata_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetResourceMetadata
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "ServiceType": "RDS",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W"
}
```

#### Sample Response
<a name="API_GetResourceMetadata_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive

{
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "Features":{
        "SQL_DIGEST_STATISTICS":{
            "Status": "ENABLED"
        }
    }
}
```

## See Also
<a name="API_GetResourceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/GetResourceMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/GetResourceMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/GetResourceMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/GetResourceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/GetResourceMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/GetResourceMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/GetResourceMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/GetResourceMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/GetResourceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/GetResourceMetadata)
