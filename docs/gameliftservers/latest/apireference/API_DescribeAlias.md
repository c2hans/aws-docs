---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeAlias.html
---

# DescribeAlias
<a name="API_DescribeAlias"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves properties for an alias. This operation returns all alias metadata and settings. To get an alias's target fleet ID only, use `ResolveAlias`.

To get alias properties, specify the alias ID. If successful, the requested alias record is returned.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_DescribeAlias_RequestSyntax"></a>

```
{
   "AliasId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAlias_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AliasId](#API_DescribeAlias_RequestSyntax) **   <a name="gameliftservers-DescribeAlias-request-AliasId"></a>
The unique identifier for the fleet alias that you want to retrieve. You can use either the alias ID or ARN value.
Type: String
Pattern: `^alias-\S+|^arn:.*:alias\/alias-\S+`
Required: Yes

## Response Syntax
<a name="API_DescribeAlias_ResponseSyntax"></a>

```
{
   "Alias": {
      "AliasArn": "string",
      "AliasId": "string",
      "CreationTime": number,
      "Description": "string",
      "LastUpdatedTime": number,
      "Name": "string",
      "RoutingStrategy": {
         "FleetId": "string",
         "Message": "string",
         "Type": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Alias](#API_DescribeAlias_ResponseSyntax) **   <a name="gameliftservers-DescribeAlias-response-Alias"></a>
The requested alias resource.
Type: [Alias](API_Alias.md) object

## Errors
<a name="API_DescribeAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeAlias)
