---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_GetEnvironment.html
---

# GetEnvironment
<a name="API_GetEnvironment"></a>

Returns a description of the specified environment.

## Request Syntax
<a name="API_GetEnvironment_RequestSyntax"></a>

```
{
   "environmentId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEnvironment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [environmentId](#API_GetEnvironment_RequestSyntax) **   <a name="evs-GetEnvironment-request-environmentId"></a>
A unique ID for the environment.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

## Response Syntax
<a name="API_GetEnvironment_ResponseSyntax"></a>

```
{
   "environment": {
      "checks": [
         {
            "id": "string",
            "impairedSince": number,
            "result": "string",
            "type": "string"
         }
      ],
      "connectivityInfo": {
         "privateRouteServerPeerings": [ "string" ]
      },
      "createdAt": number,
      "credentials": [
         {
            "secretArn": "string"
         }
      ],
      "environmentArn": "string",
      "environmentId": "string",
      "environmentName": "string",
      "environmentState": "string",
      "environmentStatus": "string",
      "kmsKeyId": "string",
      "licenseInfo": [
         {
            "solutionKey": "string",
            "vsanKey": "string"
         }
      ],
      "modifiedAt": number,
      "serviceAccessSecurityGroups": {
         "securityGroups": [ "string" ]
      },
      "serviceAccessSubnetId": "string",
      "siteId": "string",
      "stateDetails": "string",
      "termsAccepted": boolean,
      "vcfHostnames": {
         "cloudBuilder": "string",
         "nsx": "string",
         "nsxEdge1": "string",
         "nsxEdge2": "string",
         "nsxManager1": "string",
         "nsxManager2": "string",
         "nsxManager3": "string",
         "sddcManager": "string",
         "vCenter": "string"
      },
      "vcfVersion": "string",
      "vpcId": "string"
   }
}
```

## Response Elements
<a name="API_GetEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environment](#API_GetEnvironment_ResponseSyntax) **   <a name="evs-GetEnvironment-response-environment"></a>
A description of the requested environment.
Type: [Environment](API_Environment.md) object

## Errors
<a name="API_GetEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a `state` of `DELETED`.
 ** message **
Describes the error encountered.
 ** resourceId **
The ID of the resource that could not be found.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.
 ** fieldList **
A list of fields that didn't validate.
 ** message **
Describes the error encountered.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/GetEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/GetEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/GetEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/GetEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/GetEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/GetEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/GetEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/GetEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/GetEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/GetEnvironment)
