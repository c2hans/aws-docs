---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeTrafficDistributionGroup.html
---

# DescribeTrafficDistributionGroup
<a name="API_DescribeTrafficDistributionGroup"></a>

Gets details and status of a traffic distribution group.

## Request Syntax
<a name="API_DescribeTrafficDistributionGroup_RequestSyntax"></a>

```
GET /traffic-distribution-group/{{TrafficDistributionGroupId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTrafficDistributionGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TrafficDistributionGroupId](#API_DescribeTrafficDistributionGroup_RequestSyntax) **   <a name="connect-DescribeTrafficDistributionGroup-request-uri-TrafficDistributionGroupId"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z-]+-[0-9]{1}:[0-9]{1,20}:traffic-distribution-group/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_DescribeTrafficDistributionGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTrafficDistributionGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TrafficDistributionGroup": {
      "Arn": "string",
      "Description": "string",
      "Id": "string",
      "InstanceArn": "string",
      "IsDefault": boolean,
      "Name": "string",
      "Status": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeTrafficDistributionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrafficDistributionGroup](#API_DescribeTrafficDistributionGroup_ResponseSyntax) **   <a name="connect-DescribeTrafficDistributionGroup-response-TrafficDistributionGroup"></a>
Information about the traffic distribution group.
Type: [TrafficDistributionGroup](API_TrafficDistributionGroup.md) object

## Errors
<a name="API_DescribeTrafficDistributionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeTrafficDistributionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeTrafficDistributionGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeTrafficDistributionGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeTrafficDistributionGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeTrafficDistributionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeTrafficDistributionGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeTrafficDistributionGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeTrafficDistributionGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeTrafficDistributionGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeTrafficDistributionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeTrafficDistributionGroup)
