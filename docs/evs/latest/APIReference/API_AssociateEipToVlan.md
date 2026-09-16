---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_AssociateEipToVlan.html
---

# AssociateEipToVlan
<a name="API_AssociateEipToVlan"></a>

Associates an Elastic IP address with a public HCX VLAN. This operation is only allowed for public HCX VLANs at this time.

## Request Syntax
<a name="API_AssociateEipToVlan_RequestSyntax"></a>

```
{
   "allocationId": "{{string}}",
   "clientToken": "{{string}}",
   "environmentId": "{{string}}",
   "vlanName": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateEipToVlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [allocationId](#API_AssociateEipToVlan_RequestSyntax) **   <a name="evs-AssociateEipToVlan-request-allocationId"></a>
The Elastic IP address allocation ID.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 26.
Pattern: `eipalloc-[a-zA-Z0-9_-]+`
Required: Yes

 ** [environmentId](#API_AssociateEipToVlan_RequestSyntax) **   <a name="evs-AssociateEipToVlan-request-environmentId"></a>
A unique ID for the environment containing the VLAN that the Elastic IP address associates with.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [vlanName](#API_AssociateEipToVlan_RequestSyntax) **   <a name="evs-AssociateEipToVlan-request-vlanName"></a>
The name of the VLAN. `hcx` is the only accepted VLAN name at this time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** [clientToken](#API_AssociateEipToVlan_RequestSyntax) **   <a name="evs-AssociateEipToVlan-request-clientToken"></a>
This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.
A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[!-~]+`
Required: No

## Response Syntax
<a name="API_AssociateEipToVlan_ResponseSyntax"></a>

```
{
   "vlan": {
      "availabilityZone": "string",
      "cidr": "string",
      "createdAt": number,
      "eipAssociations": [
         {
            "allocationId": "string",
            "associationId": "string",
            "ipAddress": "string"
         }
      ],
      "functionName": "string",
      "isPublic": boolean,
      "modifiedAt": number,
      "networkAclId": "string",
      "stateDetails": "string",
      "subnetId": "string",
      "vlanId": number,
      "vlanState": "string"
   }
}
```

## Response Elements
<a name="API_AssociateEipToVlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [vlan](#API_AssociateEipToVlan_ResponseSyntax) **   <a name="evs-AssociateEipToVlan-response-vlan"></a>
The VLANs that Amazon EVS creates during environment creation.
Type: [Vlan](API_Vlan.md) object

## Errors
<a name="API_AssociateEipToVlan_Errors"></a>

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

 [ThrottlingException](API_ThrottlingException.md)
The operation could not be performed because the service is throttling requests. This exception is thrown when the service endpoint receives too many concurrent requests.
 ** message **
Describes the error encountered.
 ** retryAfterSeconds **
The seconds to wait to retry.
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
<a name="API_AssociateEipToVlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/AssociateEipToVlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/AssociateEipToVlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/AssociateEipToVlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/AssociateEipToVlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/AssociateEipToVlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/AssociateEipToVlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/AssociateEipToVlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/AssociateEipToVlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/AssociateEipToVlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/AssociateEipToVlan)
