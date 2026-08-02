---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetWorkgroup.html
---

# GetWorkgroup
<a name="API_GetWorkgroup"></a>

Returns information about a specific workgroup.

## Request Syntax
<a name="API_GetWorkgroup_RequestSyntax"></a>

```
{
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetWorkgroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [workgroupName](#API_GetWorkgroup_RequestSyntax) **   <a name="redshiftserverless-GetWorkgroup-request-workgroupName"></a>
The name of the workgroup to return information for.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetWorkgroup_ResponseSyntax"></a>

```
{
   "workgroup": {
      "baseCapacity": number,
      "configParameters": [
         {
            "parameterKey": "string",
            "parameterValue": "string"
         }
      ],
      "creationDate": "string",
      "crossAccountVpcs": [ "string" ],
      "customDomainCertificateArn": "string",
      "customDomainCertificateExpiryTime": "string",
      "customDomainName": "string",
      "endpoint": {
         "address": "string",
         "port": number,
         "vpcEndpoints": [
            {
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
            }
         ]
      },
      "enhancedVpcRouting": boolean,
      "extraComputeForAutomaticOptimization": boolean,
      "ipAddressType": "string",
      "maxCapacity": number,
      "namespaceName": "string",
      "patchVersion": "string",
      "pendingTrackName": "string",
      "port": number,
      "pricePerformanceTarget": {
         "level": number,
         "status": "string"
      },
      "publiclyAccessible": boolean,
      "securityGroupIds": [ "string" ],
      "status": "string",
      "subnetIds": [ "string" ],
      "trackName": "string",
      "workgroupArn": "string",
      "workgroupId": "string",
      "workgroupName": "string",
      "workgroupVersion": "string"
   }
}
```

## Response Elements
<a name="API_GetWorkgroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workgroup](#API_GetWorkgroup_ResponseSyntax) **   <a name="redshiftserverless-GetWorkgroup-response-workgroup"></a>
The returned workgroup object.
Type: [Workgroup](API_Workgroup.md) object

## Errors
<a name="API_GetWorkgroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## Examples
<a name="API_GetWorkgroup_Examples"></a>

### Example
<a name="API_GetWorkgroup_Example_1"></a>

This example illustrates one usage of GetWorkgroup.

#### Sample Request
<a name="API_GetWorkgroup_Example_1_Request"></a>

```
aws redshift-serverless get-workgroup
--workgroup-name test-wg
--region us-east-1
```

#### Sample Response
<a name="API_GetWorkgroup_Example_1_Response"></a>

```
{
  "workgroup": {
    "workgroupId": "875083e4-50b5-4ad7-bd8b-b01beb74d912",
    "workgroupArn": "arn:aws:redshift-serverless:us-east-1:012345678901:workgroup/875083e4-50b5-4ad7-bd8b-b01beb74d912",
    "workgroupName": "test-wg",
    "namespaceName": "test-ns",
    "baseCapacity": 32,
    "enhancedVpcRouting": false,
    ...
    "ipAddressType": "ipv4",
    "trackName": "current",
    "pendingTrackName": "trailing"
  }
}
```

## See Also
<a name="API_GetWorkgroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/GetWorkgroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/GetWorkgroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/GetWorkgroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/GetWorkgroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/GetWorkgroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/GetWorkgroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/GetWorkgroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/GetWorkgroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/GetWorkgroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/GetWorkgroup)
