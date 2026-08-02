---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListEndpointAccess.html
---

# ListEndpointAccess
<a name="API_ListEndpointAccess"></a>

Returns an array of `EndpointAccess` objects and relevant information.

## Request Syntax
<a name="API_ListEndpointAccess_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "ownerAccount": "{{string}}",
   "vpcId": "{{string}}",
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEndpointAccess_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-ListEndpointAccess-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to display the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-ListEndpointAccess-request-nextToken"></a>
If your initial `ListEndpointAccess` operation returns a `nextToken`, you can include the returned `nextToken` in following `ListEndpointAccess` operations, which returns results in the next page.
Type: String
Required: No

 ** [ownerAccount](#API_ListEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-ListEndpointAccess-request-ownerAccount"></a>
The owner AWS account for the Amazon Redshift Serverless workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `.*(\d{12}).*`
Required: No

 ** [vpcId](#API_ListEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-ListEndpointAccess-request-vpcId"></a>
The unique identifier of the virtual private cloud with access to Amazon Redshift Serverless.
Type: String
Required: No

 ** [workgroupName](#API_ListEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-ListEndpointAccess-request-workgroupName"></a>
The name of the workgroup associated with the VPC endpoint to return.
Type: String
Required: No

## Response Syntax
<a name="API_ListEndpointAccess_ResponseSyntax"></a>

```
{
   "endpoints": [
      {
         "address": "string",
         "endpointArn": "string",
         "endpointCreateTime": "string",
         "endpointName": "string",
         "endpointStatus": "string",
         "port": number,
         "subnetIds": [ "string" ],
         "vpcEndpoint": {
            "networkInterfaces": [
               {
                  "availabilityZone": "string",
                  "ipv6Address": "string",
                  "networkInterfaceId": "string",
                  "privateIpAddress": "string",
                  "subnetId": "string"
               }
            ],
            "vpcEndpointId": "string",
            "vpcId": "string"
         },
         "vpcSecurityGroups": [
            {
               "status": "string",
               "vpcSecurityGroupId": "string"
            }
         ],
         "workgroupName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEndpointAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoints](#API_ListEndpointAccess_ResponseSyntax) **   <a name="redshiftserverless-ListEndpointAccess-response-endpoints"></a>
The returned VPC endpoints.
Type: Array of [EndpointAccess](API_EndpointAccess.md) objects

 ** [nextToken](#API_ListEndpointAccess_ResponseSyntax) **   <a name="redshiftserverless-ListEndpointAccess-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListEndpointAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListEndpointAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListEndpointAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListEndpointAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListEndpointAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListEndpointAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListEndpointAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListEndpointAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListEndpointAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListEndpointAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListEndpointAccess)
