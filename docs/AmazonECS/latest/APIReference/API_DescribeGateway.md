---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeGateway.html
---

# DescribeGateway
<a name="API_DescribeGateway"></a>

Describes a gateway, including its configuration, status, and the type-specific infrastructure settings that it uses.

## Request Syntax
<a name="API_DescribeGateway_RequestSyntax"></a>

```
{
   "gateway": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [gateway](#API_DescribeGateway_RequestSyntax) **   <a name="ECS-DescribeGateway-request-gateway"></a>
The name or Amazon Resource Name (ARN) of the gateway to describe.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeGateway_ResponseSyntax"></a>

```
{
   "gateway": {
      "accessType": "string",
      "configuration": { ... },
      "createdAt": number,
      "deletionProtection": boolean,
      "failures": [
         {
            "arn": "string",
            "errors": [
               {
                  "code": "string",
                  "message": "string",
                  "operation": "string"
               }
            ]
         }
      ],
      "gatewayArn": "string",
      "infrastructureRoleArn": "string",
      "name": "string",
      "propagateTags": "string",
      "status": "string",
      "statusReason": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_DescribeGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gateway](#API_DescribeGateway_ResponseSyntax) **   <a name="ECS-DescribeGateway-response-gateway"></a>
The details of the gateway.
Type: [Gateway](API_Gateway.md) object

## Errors
<a name="API_DescribeGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** GatewayNotFoundException **
The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeGateway)
