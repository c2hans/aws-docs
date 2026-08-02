---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateSiteRackPhysicalProperties.html
---

# UpdateSiteRackPhysicalProperties
<a name="API_UpdateSiteRackPhysicalProperties"></a>

Update the physical and logistical details for a rack at a site. For more information about hardware requirements for racks, see [Network readiness checklist](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#checklist) in the AWS Outposts User Guide.

To update a rack at a site with an order of `IN_PROGRESS`, you must wait for the order to complete or cancel the order.

## Request Syntax
<a name="API_UpdateSiteRackPhysicalProperties_RequestSyntax"></a>

```
PATCH /sites/{{SiteId}}/rackPhysicalProperties HTTP/1.1
Content-type: application/json

{
   "FiberOpticCableType": "{{string}}",
   "MaximumSupportedWeightLbs": "{{string}}",
   "OpticalStandard": "{{string}}",
   "PowerConnector": "{{string}}",
   "PowerDrawKva": "{{string}}",
   "PowerFeedDrop": "{{string}}",
   "PowerPhase": "{{string}}",
   "UplinkCount": "{{string}}",
   "UplinkGbps": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSiteRackPhysicalProperties_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SiteId](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-uri-SiteId"></a>
 The ID or the Amazon Resource Name (ARN) of the site.
Despite the parameter name, you can make the request with an ARN. The parameter name is `SiteId` for backward compatibility.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`
Required: Yes

## Request Body
<a name="API_UpdateSiteRackPhysicalProperties_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FiberOpticCableType](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-FiberOpticCableType"></a>
The type of fiber that you will use to attach the Outpost to your network.
Type: String
Valid Values: `SINGLE_MODE | MULTI_MODE`
Required: No

 ** [MaximumSupportedWeightLbs](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-MaximumSupportedWeightLbs"></a>
The maximum rack weight that this site can support. `NO_LIMIT` is over 2000lbs.
Type: String
Valid Values: `NO_LIMIT | MAX_1400_LBS | MAX_1600_LBS | MAX_1800_LBS | MAX_2000_LBS`
Required: No

 ** [OpticalStandard](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-OpticalStandard"></a>
The type of optical standard that you will use to attach the Outpost to your network. This field is dependent on uplink speed, fiber type, and distance to the upstream device. For more information about networking requirements for racks, see [Network](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#facility-networking) in the AWS Outposts User Guide.
+  `OPTIC_10GBASE_SR`: 10GBASE-SR
+  `OPTIC_10GBASE_IR`: 10GBASE-IR
+  `OPTIC_10GBASE_LR`: 10GBASE-LR
+  `OPTIC_40GBASE_SR`: 40GBASE-SR
+  `OPTIC_40GBASE_ESR`: 40GBASE-ESR
+  `OPTIC_40GBASE_IR4_LR4L`: 40GBASE-IR (LR4L)
+  `OPTIC_40GBASE_LR4`: 40GBASE-LR4
+  `OPTIC_100GBASE_SR4`: 100GBASE-SR4
+  `OPTIC_100GBASE_CWDM4`: 100GBASE-CWDM4
+  `OPTIC_100GBASE_LR4`: 100GBASE-LR4
+  `OPTIC_100G_PSM4_MSA`: 100G PSM4 MSA
+  `OPTIC_1000BASE_LX`: 1000Base-LX
+  `OPTIC_1000BASE_SX` : 1000Base-SX
Type: String
Valid Values: `OPTIC_10GBASE_SR | OPTIC_10GBASE_IR | OPTIC_10GBASE_LR | OPTIC_40GBASE_SR | OPTIC_40GBASE_ESR | OPTIC_40GBASE_IR4_LR4L | OPTIC_40GBASE_LR4 | OPTIC_100GBASE_SR4 | OPTIC_100GBASE_CWDM4 | OPTIC_100GBASE_LR4 | OPTIC_100G_PSM4_MSA | OPTIC_1000BASE_LX | OPTIC_1000BASE_SX`
Required: No

 ** [PowerConnector](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-PowerConnector"></a>
The power connector that AWS should plan to provide for connections to the hardware. Note the correlation between `PowerPhase` and `PowerConnector`.
+ Single-phase AC feed
  +  **L6-30P** – (common in US); 30A; single phase
  +  **IEC309 (blue)** – P\+N\+E, 6hr; 32 A; single phase
+ Three-phase AC feed
  +  **AH530P7W (red)** – 3P\+N\+E, 7hr; 30A; three phase
  +  **AH532P6W (red)** – 3P\+N\+E, 6hr; 32A; three phase
  +  **CS8365C** – (common in US); 3P\+E, 50A; three phase
Type: String
Valid Values: `L6_30P | IEC309 | AH530P7W | AH532P6W | CS8365C`
Required: No

 ** [PowerDrawKva](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-PowerDrawKva"></a>
The power draw, in kVA, available at the hardware placement position for the rack.
Type: String
Valid Values: `POWER_5_KVA | POWER_10_KVA | POWER_15_KVA | POWER_30_KVA`
Required: No

 ** [PowerFeedDrop](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-PowerFeedDrop"></a>
Indicates whether the power feed comes above or below the rack.
Type: String
Valid Values: `ABOVE_RACK | BELOW_RACK`
Required: No

 ** [PowerPhase](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-PowerPhase"></a>
The power option that you can provide for hardware.
+ Single-phase AC feed: 200 V to 277 V, 50 Hz or 60 Hz
+ Three-phase AC feed: 346 V to 480 V, 50 Hz or 60 Hz
Type: String
Valid Values: `SINGLE_PHASE | THREE_PHASE`
Required: No

 ** [UplinkCount](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-UplinkCount"></a>
Racks come with two Outpost network devices. Depending on the supported uplink speed at the site, the Outpost network devices provide a variable number of uplinks. Specify the number of uplinks for each Outpost network device that you intend to use to connect the rack to your network. Note the correlation between `UplinkGbps` and `UplinkCount`.
+ 1Gbps - Uplinks available: 1, 2, 4, 6, 8
+ 10Gbps - Uplinks available: 1, 2, 4, 8, 12, 16
+ 40 and 100 Gbps- Uplinks available: 1, 2, 4
Type: String
Valid Values: `UPLINK_COUNT_1 | UPLINK_COUNT_2 | UPLINK_COUNT_3 | UPLINK_COUNT_4 | UPLINK_COUNT_5 | UPLINK_COUNT_6 | UPLINK_COUNT_7 | UPLINK_COUNT_8 | UPLINK_COUNT_12 | UPLINK_COUNT_16`
Required: No

 ** [UplinkGbps](#API_UpdateSiteRackPhysicalProperties_RequestSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-request-UplinkGbps"></a>
The uplink speed the rack should support for the connection to the Region.
Type: String
Valid Values: `UPLINK_1G | UPLINK_10G | UPLINK_40G | UPLINK_100G`
Required: No

## Response Syntax
<a name="API_UpdateSiteRackPhysicalProperties_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Site": {
      "AccountId": "string",
      "Description": "string",
      "Name": "string",
      "Notes": "string",
      "OperatingAddressCity": "string",
      "OperatingAddressCountryCode": "string",
      "OperatingAddressStateOrRegion": "string",
      "RackPhysicalProperties": {
         "FiberOpticCableType": "string",
         "MaximumSupportedWeightLbs": "string",
         "OpticalStandard": "string",
         "PowerConnector": "string",
         "PowerDrawKva": "string",
         "PowerFeedDrop": "string",
         "PowerPhase": "string",
         "UplinkCount": "string",
         "UplinkGbps": "string"
      },
      "SiteArn": "string",
      "SiteId": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateSiteRackPhysicalProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Site](#API_UpdateSiteRackPhysicalProperties_ResponseSyntax) **   <a name="outposts-UpdateSiteRackPhysicalProperties-response-Site"></a>
Information about a site.
Type: [Site](API_Site.md) object

## Errors
<a name="API_UpdateSiteRackPhysicalProperties_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource causing the conflict.
 ** ResourceType **
The type of the resource causing the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSiteRackPhysicalProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/UpdateSiteRackPhysicalProperties)
